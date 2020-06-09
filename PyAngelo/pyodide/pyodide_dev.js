/**
 * The main bootstrap script for loading pyodide.
 */

var languagePluginLoader = new Promise((resolve, reject) => {
  // This is filled in by the Makefile to be either a local file or the
  // deployed location. TODO: This should be done in a less hacky
  // way.
  var baseURL = self.languagePluginUrl || '';
  baseURL = baseURL.substr(0, baseURL.lastIndexOf('/')) + '/';

  ////////////////////////////////////////////////////////////
  // Package loading
  let loadedPackages = [];
  let loadedModules = [];
  let stdlibModules = [
    "__future__",
    "__main__",
    "_dummy_thread",
    "_thread",
    "abc",
    "aifc",
    "argparse",
    "array",
    "ast",
    "asynchat",
    "asyncio",
    "asyncore",
    "atexit",
    "audioop",
    "base64",
    "bdb",
    "binascii",
    "binhex",
    "bisect",
    "builtins",
    "bz2",
    "cProfile",
    "calendar",
    "cgi",
    "cgitb",
    "chunk",
    "cmath",
    "cmd",
    "code",
    "codecs",
    "codeop",
    "collections",
    "colorsys",
    "compileall",
    "concurrent",
    "configparser",
    "contextlib",
    "contextvars",
    "copy",
    "copyreg",
    "crypt",
    "csv",
    "ctypes",
    "curses",
    "dataclasses",
    "datetime",
    "dbm",
    "decimal",
    "difflib",
    "dis",
    "distutils",
    "doctest",
    "dummy_threading",
    "email",
    "encodings",
    "ensurepip",
    "enum",
    "errno",
    "faulthandler",
    "fcntl",
    "filecmp",
    "fileinput",
    "fnmatch",
    "formatter",
    "fractions",
    "ftplib",
    "functools",
    "gc",
    "getopt",
    "getpass",
    "gettext",
    "glob",
    "grp",
    "gzip",
    "hashlib",
    "heapq",
    "hmac",
    "html",
    "http",
    "imaplib",
    "imghdr",
    "imp",
    "importlib",
    "inspect",
    "io",
    "ipaddress",
    "itertools",
    "json",
    "keyword",
    "lib2to3",
    "linecache",
    "locale",
    "logging",
    "lzma",
    "macpath",
    "mailbox",
    "mailcap",
    "marshal",
    "math",
    "mimetypes",
    "mmap",
    "modulefinder",
    "msilib",
    "msvcrt",
    "multiprocessing",
    "netrc",
    "nis",
    "nntplib",
    "numbers",
    "operator",
    "optparse",
    "os",
    "ossaudiodev",
    "parser",
    "pathlib",
    "pdb",
    "pickle",
    "pickletools",
    "pipes",
    "pkgutil",
    "platform",
    "plistlib",
    "poplib",
    "posix",
    "pprint",
    "profile",
    "pstats",
    "pty",
    "pwd",
    "py_compile",
    "pyclbr",
    "pydoc",
    "queue",
    "quopri",
    "random",
    "re",
    "readline",
    "reprlib",
    "resource",
    "rlcompleter",
    "runpy",
    "sched",
    "secrets",
    "select",
    "selectors",
    "shelve",
    "shlex",
    "shutil",
    "signal",
    "site",
    "smtpd",
    "smtplib",
    "sndhdr",
    "socket",
    "socketserver",
    "spwd",
    "sqlite3",
    "ssl",
    "stat",
    "statistics",
    "string",
    "stringprep",
    "struct",
    "subprocess",
    "sunau",
    "symbol",
    "symtable",
    "sys",
    "sysconfig",
    "syslog",
    "tabnanny",
    "tarfile",
    "telnetlib",
    "tempfile",
    "termios",
    "test",
    "textwrap",
    "threading",
    "time",
    "timeit",
    "tkinter",
    "token",
    "tokenize",
    "trace",
    "traceback",
    "tracemalloc",
    "tty",
    "turtle",
    "turtledemo",
    "types",
    "typing",
    "unicodedata",
    "unittest",
    "urllib",
    "uu",
    "uuid",
    "venv",
    "warnings",
    "wave",
    "weakref",
    "webbrowser",
    "winreg",
    "winsound",
    "wsgiref",
    "xdrlib",
    "xml",
    "xmlrpc",
    "zipapp",
    "zipfile",
    "zipimport",
    "zlib"
  ];
  var packagesToLoad = {};
  var loadPackagePromise = new Promise((resolve) => resolve());

  // Regexp for validating package name and URI
  var package_ident_regexp = '[a-z0-9_][a-z0-9_\-]*';
  var package_uri_regexp =
      new RegExp('^https?://.*?(' + package_ident_regexp + ').js$', 'i');
  var package_name_regexp = new RegExp('^' + package_ident_regexp + '$', 'i');

  let _uri_to_package_name = (package_uri) => {
    // Generate a unique package name from URI
    if (package_name_regexp.test(package_uri)) {
      return package_uri;
    } else if (package_uri_regexp.test(package_uri)) {
      let match = package_uri_regexp.exec(package_uri);
      // Get the regexp group corresponding to the package name
      return match[1];
    }

    return null;
  };

  // clang-format off
  let preloadWasm = () => {
    // On Chrome, we have to instantiate wasm asynchronously. Since that
    // can't be done synchronously within the call to dlopen, we instantiate
    // every .so that comes our way up front, caching it in the
    // `preloadedWasm` dictionary.

    let promise = new Promise((resolve) => resolve());
    let FS = pyodide._module.FS;

    function recurseDir(rootpath) {
      let dirs;
      try {
        dirs = FS.readdir(rootpath);
      } catch {
        return;
      }
      for (let entry of dirs) {
        if (entry.startsWith('.')) {
          continue;
        }
        const path = rootpath + entry;
        if (entry.endsWith('.so')) {
          if (Module['preloadedWasm'][path] === undefined) {
            promise = promise
              .then(() => Module['loadWebAssemblyModule'](
                FS.readFile(path), {loadAsync: true}))
              .then((module) => {
                Module['preloadedWasm'][path] = module;
              });
          }
        } else if (FS.isDir(FS.lookupPath(path).node.mode)) {
          recurseDir(path + '/');
        }
      }
    }

    recurseDir('/');

    return promise;
  };
  // clang-format on

  function loadScript(url, onload, onerror) {
    if (self.document) { // browser
      const script = self.document.createElement('script');
      script.src = url;
      script.onload = (e) => { onload(); };
      script.onerror = (e) => { onerror(); };
      self.document.head.appendChild(script);
    } else if (self.importScripts) { // webworker
      try {
        self.importScripts(url);
        onload();
      } catch {
        onerror();
      }
    }
  }

  // Recursively resolve imports for Python modules being fetched
  let _pythonPath = "";

  let _resolveImports = (imports, prefix) => {
    var promises = [];

    if (typeof prefix === "undefined")
      prefix = "";

    if (!Array.isArray(imports))
      imports = [ imports ];

    for (let name of imports) {
      let pkg = _uri_to_package_name(name);

      // Check for known packages via their alias mapping
      if (self.pyodide._module.packages.import_name_to_package_name[name] !==
          undefined) {
        packagesToLoad[self.pyodide._module.packages
                           .import_name_to_package_name[name]] = undefined;
        continue;
      }

      // Check for directly known packages or packages via URI regexp
      if (self.pyodide._module.packages.dependencies[name] !== undefined ||
          package_uri_regexp.test(name)) {
        packagesToLoad[name] = undefined;
        continue;
      }

      // Check for invalid pkg or disabled remotePath feature
      if (!self.pyodide.remotePath.length || pkg == null) {

        // Only add to packageList if this is not a stdlib module
        if (stdlibModules.indexOf(name) < 0)
          packagesToLoad[name] = undefined;

        continue;
      }

      // Check if this module with the same prefix is in loadedModules,
      // to avoid multiple fetching of the same module from different
      // sub-modules.
      if (loadedModules.indexOf(prefix + pkg) >= 0) {
        continue;
      }

      loadedModules.push(prefix + pkg);

      var remotePath;

      // Fetch modules per entry configured in remotePath
      if (!Array.isArray(self.pyodide.remotePath))
        remotePath = [ self.pyodide.remotePath ]; // Convert into an array
      else
        remotePath = self.pyodide.remotePath.slice();

      function fetchModule() {
        let remoteURL = remotePath.shift();

        // The entry "/" points to pyodide's baseURL
        if (remoteURL === "/")
          remoteURL = baseURL;

        if (remoteURL.slice(-1) !== '/')
          remoteURL = remoteURL += '/';

        // Try to fetch a single .py-file first
        let filename = pkg + ".py";
        let url = remoteURL + (prefix ? prefix + "/" : "") + filename;
        let path =
            self.pyodide._pythonPath + (prefix ? prefix + "/" : "") + filename;

        return new Promise((resolve, reject) => {
          fetch(url, {}).then((response) => {
            if (response.status === 200)
              return response.text().then((code) => {
                console.debug(`fetched ${name} from ${url} successfully, ` +
                              `saving to ${path}`);

                self.pyodide._module.FS.writeFile(path, code);

                let imports = self.pyodide.parsePythonImports(code, prefix);

                if (imports.length)
                  _resolveImports(imports, prefix).then(() => resolve());
                else
                  resolve();
              });

            // Try to fetch directory with pkg/__init__.py afterwards

            let fFilename = "__init__.py";
            let fPrefix = (prefix ? prefix + "/" : "") + pkg;
            let fUrl = remoteURL + fPrefix + "/" + fFilename;
            let fPath = self.pyodide._pythonPath + fPrefix + "/" + fFilename;

            return fetch(fUrl, {}).then((response) => {
              if (response.status === 200)
                return response.text().then((code) => {
                  console.debug(
                      `fetched ${fFilename} from ${fUrl} successfully, ` +
                      `saving to ${fPath}`);

                  self.pyodide._module.FS.mkdir(self.pyodide._pythonPath +
                                                fPrefix);
                  self.pyodide._module.FS.writeFile(fPath, code);

                  let imports = self.pyodide.parsePythonImports(code, fPrefix);

                  if (imports.length) {
                    _resolveImports(imports, fPrefix).then(() => resolve());
                  } else {
                    resolve();
                  }
                });

              // Try another remote path?
              if (remotePath.length) {
                fetchModule().then(() => resolve());
              } else {
                // In case this is a standard module, silently ignore this
                // import.
                if (stdlibModules.indexOf(name) < 0) {
                  packagesToLoad[name] = undefined;
                }

                // Mark this promise as resolved, although no file was
                // fetched. Python will do the rest.
                resolve();

                // reject(`Unable to locate package ${pkg}`)
              }
            });
          });
        });
      }

      promises.push(fetchModule());
    }

    return Promise.all(promises);
  };

  let _loadPackage = (names, messageCallback) => {
    let promise = _resolveImports(names).then(() => {
      // DFS to find all dependencies of the requested packages
      let packages = self.pyodide._module.packages.dependencies;
      let loadedPackages = self.pyodide.loadedPackages;

      let queue = [].concat(Object.keys(packagesToLoad) || []);
      let toLoad = [];

      if (queue.length === 0) {
        // Invalidate Python's import caches also here, in case remotePath
        // feature imported something...
        self.pyodide.runPython('import importlib as _importlib\n' +
                               '_importlib.invalidate_caches()\n');
        resolve();
        return;
      }

      // Clear packagesToLoad for later imports
      packagesToLoad = {};

      while (queue.length) {
        let package_uri = queue.pop();

        const pkg = _uri_to_package_name(package_uri);

        if (pkg == null) {
          console.error(`Invalid package name or URI '${package_uri}'`);
          return;
        } else if (pkg == package_uri) {
          package_uri = 'default channel';
        }

        if (pkg in loadedPackages) {
          if (package_uri != loadedPackages[pkg]) {
            console.error(`URI mismatch, attempting to load package ` +
                          `${pkg} from ${package_uri} while it is already ` +
                          `loaded from ${loadedPackages[pkg]}!`);
            return;
          }
        } else if (pkg in toLoad) {
          if (package_uri != toLoad[pkg]) {
            console.error(`URI mismatch, attempting to load package ` +
                          `${pkg} from ${package_uri} while it is already ` +
                          `being loaded from ${toLoad[pkg]}!`);
            return;
          }
        } else {
          console.log(`Loading ${pkg} from ${package_uri}`);

          toLoad[pkg] = package_uri;

          if (packages.hasOwnProperty(pkg)) {
            packages[pkg].forEach((subpackage) => {
              if (!(subpackage in loadedPackages) && !(subpackage in toLoad)) {
                queue.push(subpackage);
              }
            });
          } else {
            console.error(`Unknown package '${pkg}'`);
          }
        }
      }

      self.pyodide._module.locateFile = (path) => {
        // handle packages loaded from custom URLs
        let pkg = path.replace(/\.data$/, "");
        if (pkg in toLoad) {
          let package_uri = toLoad[pkg];
          if (package_uri !== 'default channel') {
            return package_uri.replace(/\.js$/, ".data");
          };
        };
        return baseURL + path;
      };

      let promise = new Promise((resolve, reject) => {
        if (Object.keys(toLoad).length === 0) {
          resolve('No new packages to load');
          return;
        }

        const packageList = Array.from(Object.keys(toLoad)).join(', ');
        if (messageCallback !== undefined) {
          messageCallback(`Loading ${packageList}`);
        }

        // monitorRunDependencies is called at the beginning and the end of each
        // package being loaded. We know we are done when it has been called
        // exactly "toLoad * 2" times.
        var packageCounter = Object.keys(toLoad).length * 2;

        self.pyodide._module.monitorRunDependencies = () => {
          packageCounter--;
          if (packageCounter === 0) {
            for (let pkg in toLoad) {
              self.pyodide.loadedPackages[pkg] = toLoad[pkg];
            }
            delete self.pyodide._module.monitorRunDependencies;
            self.removeEventListener('error', windowErrorHandler);
            if (!isFirefox) {
              preloadWasm().then(() => {resolve(`Loaded ${packageList}`)});
            } else {
              resolve(`Loaded ${packageList}`);
            }
          }
        };

        // Add a handler for any exceptions that are thrown in the process of
        // loading a package
        var windowErrorHandler = (err) => {
          delete self.pyodide._module.monitorRunDependencies;
          self.removeEventListener('error', windowErrorHandler);
          // Set up a new Promise chain, since this one failed
          loadPackagePromise = new Promise((resolve) => resolve());
          reject(err.message);
        };
        self.addEventListener('error', windowErrorHandler);

        for (let pkg in toLoad) {
          let scriptSrc;
          let package_uri = toLoad[pkg];
          if (package_uri === 'default channel') {
            scriptSrc = `${baseURL}${pkg}.js`;
          } else {
            scriptSrc = `${package_uri}`;
          }

          loadScript(scriptSrc, () => {}, () => {
            // If the package_uri fails to load, call monitorRunDependencies
            // twice (so packageCounter will still hit 0 and finish loading),
            // and remove the package from toLoad so we don't mark it as loaded.
            console.error(`Couldn't load package from URL ${scriptSrc}`)
            let index = toLoad.indexOf(pkg);
            if (index !== -1) {
              toLoad.splice(index, 1);
            }
            for (let i = 0; i < 2; i++) {
              self.pyodide._module.monitorRunDependencies();
            }
          });
        }

        // We have to invalidate Python's import caches, or it won't
        // see the new files. This is done here so it happens in parallel
        // with the fetching over the network.
        self.pyodide.runPython('import importlib as _importlib\n' +
                               '_importlib.invalidate_caches()\n');
      });

      return promise;
    });

    return promise;
  };

  let loadPackage = (names, messageCallback) => {
    /* We want to make sure that only one loadPackage invocation runs at any
     * given time, so this creates a "chain" of promises. */
    loadPackagePromise =
        loadPackagePromise.then(() => _loadPackage(names, messageCallback));
    return loadPackagePromise;
  };

  ////////////////////////////////////////////////////////////
  // Fix Python recursion limit
  function fixRecursionLimit(pyodide) {
    // The Javascript/Wasm call stack may be too small to handle the default
    // Python call stack limit of 1000 frames. This is generally the case on
    // Chrom(ium), but not on Firefox. Here, we determine the Javascript call
    // stack depth available, and then divide by 50 (determined heuristically)
    // to set the maximum Python call stack depth.

    let depth = 0;
    function recurse() {
      depth += 1;
      recurse();
    }
    try {
      recurse();
    } catch (err) {
      ;
    }

    let recursionLimit = depth / 50;
    if (recursionLimit > 1000) {
      recursionLimit = 1000;
    }
    pyodide.runPython(
        `import sys; sys.setrecursionlimit(int(${recursionLimit}))`);
  };

  ////////////////////////////////////////////////////////////
  // Rearrange namespace for public API
  let PUBLIC_API = [
    'globals',
    'loadPackage',
    'loadedPackages',
    'pyimport',
    'repr',
    'runPython',
    'parsePythonImports',
    'runPythonAsync',
    'checkABI',
    'version',
    'remotePath',
  ];

  function makePublicAPI(module, public_api) {
    var namespace = {_module : module};
    for (let name of public_api) {
      namespace[name] = module[name];
    }
    return namespace;
  }

  ////////////////////////////////////////////////////////////
  // Loading Pyodide
  let wasmURL = `${baseURL}pyodide.asm.wasm`;
  let Module = {};
  self.Module = Module;

  Module.noImageDecoding = true;
  Module.noAudioDecoding = true;
  Module.noWasmDecoding = true;
  Module.preloadedWasm = {};
  Module.remotePath = [];

  let isFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;

  let wasm_promise;
  if (WebAssembly.compileStreaming === undefined) {
    wasm_promise = fetch(wasmURL)
                       .then(response => response.arrayBuffer())
                       .then(bytes => WebAssembly.compile(bytes));
  } else {
    wasm_promise = WebAssembly.compileStreaming(fetch(wasmURL));
  }

  Module.instantiateWasm = (info, receiveInstance) => {
    wasm_promise.then(module => WebAssembly.instantiate(module, info))
        .then(instance => receiveInstance(instance));
    return {};
  };

  Module.checkABI = function(ABI_number) {
    if (ABI_number !== parseInt('1')) {
      var ABI_mismatch_exception =
          `ABI numbers differ. Expected 1, got ${ABI_number}`;
      console.error(ABI_mismatch_exception);
      throw ABI_mismatch_exception;
    }
    return true;
  };

  Module.locateFile = (path) => baseURL + path;

  var postRunPromise = new Promise((resolve, reject) => {
    Module.postRun = () => {
      delete self.Module;
      fetch(`${baseURL}packages.json`)
          .then((response) => response.json())
          .then((json) => {
            fixRecursionLimit(self.pyodide);
            self.pyodide.globals =
                self.pyodide.runPython('import sys\nsys.modules["__main__"]');
            self.pyodide = makePublicAPI(self.pyodide, PUBLIC_API);
            self.pyodide._module.packages = json;

            // Obtain PYTHONPATH for remotePath feature
            self.pyodide._pythonPath = pyodide.runPython(`
                import os
                
                def setupPythonPath():
                    pythonpath = os.environ.get("PYTHONPATH", "").split(":")[-1]
                    
                    if pythonpath:
                        os.makedirs(pythonpath)
                        if not pythonpath.endswith("/"):
                          pythonpath += "/"
                    
                    return pythonpath
                    
                setupPythonPath()`);

            resolve();
          });
    };
  });

  var dataLoadPromise = new Promise((resolve, reject) => {
    Module.monitorRunDependencies =
        (n) => {
          if (n === 0) {
            delete Module.monitorRunDependencies;
            resolve();
          }
        }
  });

  Promise.all([ postRunPromise, dataLoadPromise ]).then(() => resolve());

  const data_script_src = `${baseURL}pyodide.asm.data.js`;
  loadScript(data_script_src, () => {
    const scriptSrc = `${baseURL}pyodide.asm.js`;
    loadScript(scriptSrc, () => {
      // The emscripten module needs to be at this location for the core
      // filesystem to install itself. Once that's complete, it will be replaced
      // by the call to `makePublicAPI` with a more limited public API.
      self.pyodide = pyodide(Module);
      self.pyodide.loadedPackages = new Array();
      self.pyodide.loadPackage = loadPackage;
    }, () => {});
  }, () => {});

  ////////////////////////////////////////////////////////////
  // Iodide-specific functionality, that doesn't make sense
  // if not using with Iodide.
  if (self.iodide !== undefined) {
    // Load the custom CSS for Pyodide
    let link = document.createElement('link');
    link.rel = 'stylesheet';
    link.type = 'text/css';
    link.href = `${baseURL}renderedhtml.css`;
    document.getElementsByTagName('head')[0].appendChild(link);

    // Add a custom output handler for Python objects
    self.iodide.addOutputRenderer({
      shouldRender : (val) => {
        return (typeof val === 'function' &&
                pyodide._module.PyProxy.isPyProxy(val));
      },

      render : (val) => {
        let div = document.createElement('div');
        div.className = 'rendered_html';
        var element;
        if (val._repr_html_ !== undefined) {
          let result = val._repr_html_();
          if (typeof result === 'string') {
            div.appendChild(new DOMParser()
                                .parseFromString(result, 'text/html')
                                .body.firstChild);
            element = div;
          } else {
            element = result;
          }
        } else {
          let pre = document.createElement('pre');
          pre.textContent = val.toString();
          div.appendChild(pre);
          element = div;
        }
        return element.outerHTML;
      }
    });
  }
});
languagePluginLoader
