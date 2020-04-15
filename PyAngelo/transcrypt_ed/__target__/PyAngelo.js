// Transcrypt'ed from Python, 2020-04-12 10:51:18
var random = {};
var sys = {};
var time = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
import * as __module_time__ from './time.js';
__nest__ (time, '', __module_time__);
import * as __module_sys__ from './sys.js';
__nest__ (sys, '', __module_sys__);
var __name__ = 'PyAngelo';
export var KEY_HOME = 65360;
export var KEY_ENTER = 13;
export var KEY_ESC = 27;
export var KEY_LEFT = 37;
export var KEY_UP = 38;
export var KEY_RIGHT = 39;
export var KEY_DOWN = 40;
export var KEY_W = 87;
export var KEY_A = 65;
export var KEY_S = 83;
export var KEY_D = 68;
export var KEY_Q = 81;
export var KEY_J = 74;
export var KEY_CTRL = 17;
export var KEY_PAGEUP = 65365;
export var KEY_PAGEDOWN = 65366;
export var KEY_END = 65367;
export var KEY_BEGIN = 65368;
export var KEY_V_LEFT = 'v_left';
export var KEY_V_RIGHT = 'v_right';
export var KEY_V_UP = 'v_up';
export var KEY_V_DOWN = 'v_down';
export var KEY_V_FIRE = 'v_fire';
export var CMD_DRAWLINE = 1;
export var CMD_CLEAR = 2;
export var CMD_DRAWIMAGE = 3;
export var CMD_LOADSOUND = 4;
export var CMD_PLAYSOUND = 5;
export var CMD_PAUSESOUND = 6;
export var CMD_DRAWTEXT = 7;
export var CMD_DRAWPIXEL = 8;
export var CMD_DRAWRECT = 9;
export var CMD_DRAWCIRCLE = 10;
export var CMD_REVEAL = 11;
export var CMD_HALT = 12;
export var CMD_PRINT = 13;
export var CMD_INPUT = 14;
export var PyAngeloImage =  __class__ ('PyAngeloImage', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, image, sprite) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'image': var image = __allkwargs0__ [__attrib0__]; break;
						case 'sprite': var sprite = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.img = image;
		self.height = image.naturalHeight;
		self.width = image.naturalWidth;
		self.sprite = sprite;
	});}
});
export var Point =  __class__ ('Point', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, x, y) {
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.x = x;
		self.y = y;
	});}
});
export var Rectangle =  __class__ ('Rectangle', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, x, y, width, height) {
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = 0;
		};
		if (typeof height == 'undefined' || (height != null && height.hasOwnProperty ("__kwargtrans__"))) {;
			var height = 0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
						case 'height': var height = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.x = x;
		self.y = y;
		self.width = width;
		self.height = height;
	});}
});
export var Circle =  __class__ ('Circle', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, x, y, radius) {
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		if (typeof radius == 'undefined' || (radius != null && radius.hasOwnProperty ("__kwargtrans__"))) {;
			var radius = 0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.x = x;
		self.y = y;
		self.radius = radius;
	});}
});
export var Colour =  __class__ ('Colour', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.r = r;
		self.g = g;
		self.b = b;
		self.a = a;
	});}
});
export var Text =  __class__ ('Text', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, text, fontSize, fontName) {
		if (typeof fontSize == 'undefined' || (fontSize != null && fontSize.hasOwnProperty ("__kwargtrans__"))) {;
			var fontSize = 20;
		};
		if (typeof fontName == 'undefined' || (fontName != null && fontName.hasOwnProperty ("__kwargtrans__"))) {;
			var fontName = 'Arial';
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'text': var text = __allkwargs0__ [__attrib0__]; break;
						case 'fontSize': var fontSize = __allkwargs0__ [__attrib0__]; break;
						case 'fontName': var fontName = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.text = text;
		self.fontSize = fontSize;
		self.fontName = fontName;
		self.width = graphics.measureText (text, fontName, fontSize) [0];
		self.height = graphics.measureText (text, fontName, fontSize) [1];
	});}
});
export var Sprite =  __class__ ('Sprite', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, image, x, y, r, g, b) {
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'image': var image = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (image, str)) {
			var image = graphics.loadImage (image, self);
		}
		self.image = image;
		self.r = r;
		self.g = g;
		self.b = b;
		self.width = 0;
		self.height = 0;
		self.py_metatype = 0;
		if (isinstance (image, Circle)) {
			self.x = self.image.x;
			self.y = self.image.y;
			self.radius = self.image.radius;
		}
		else if (isinstance (image, Rectangle)) {
			self.x = self.image.x;
			self.y = self.image.y;
			self.width = self.image.width;
			self.height = self.image.height;
		}
		else if (isinstance (image, Text)) {
			self.x = x;
			self.y = y;
			self.width = self.image.width;
			self.height = self.image.height;
		}
		else {
			self.x = x;
			self.y = y;
		}
	});},
	get getHeight () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (self.image, PyAngeloImage)) {
			return self.image.height;
		}
		else {
			return self.height;
		}
	});},
	get getWidth () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (self.image, PyAngeloImage)) {
			return self.image.width;
		}
		else {
			return self.width;
		}
	});},
	get overlaps () {return __get__ (this, function (self, other) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'other': var other = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (self.image, PyAngeloImage)) {
			var x1 = self.x;
			var y1 = self.y;
			var width1 = self.image.width;
			var height1 = self.image.height;
		}
		else if (isinstance (self.image, Rectangle) || isinstance (self.image, Text)) {
			var x1 = self.x;
			var y1 = self.y;
			var width1 = self.width;
			var height1 = self.height;
		}
		else if (isinstance (self.image, Circle)) {
			var x1 = self.x - self.radius;
			var y1 = self.y - self.radius;
			var width1 = self.radius * 2;
			var height1 = self.radius * 2;
		}
		else {
			var x1 = self.x;
			var y1 = self.y;
			var width1 = self.width;
			var height1 = self.height;
		}
		if (isinstance (other.image, PyAngeloImage)) {
			var x2 = other.x;
			var y2 = other.y;
			var width2 = other.image.width;
			var height2 = other.image.height;
		}
		else if (isinstance (other.image, Rectangle) || isinstance (self.image, Text)) {
			var x2 = other.x;
			var y2 = other.y;
			var width2 = other.width;
			var height2 = other.height;
		}
		else if (isinstance (other.image, Circle)) {
			var x2 = other.x - other.radius;
			var y2 = other.y - other.radius;
			var width2 = other.radius * 2;
			var height2 = other.radius * 2;
		}
		else {
			var x2 = other.x;
			var y2 = other.y;
			var width2 = other.width;
			var height2 = other.height;
		}
		return x1 < x2 + width2 && x1 + width1 > x2 && y1 < y2 + height2 && y1 + height1 > y2;
	});},
	get contains () {return __get__ (this, function (self, point) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'point': var point = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return point.x >= self.x && point.x <= self.x + self.image.width && point.y >= self.y && point.y <= self.y + self.image.height;
	});}
});
export var TextSprite =  __class__ ('TextSprite', [Sprite], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, text, fontSize, fontName, x, y, r, g, b) {
		if (typeof fontSize == 'undefined' || (fontSize != null && fontSize.hasOwnProperty ("__kwargtrans__"))) {;
			var fontSize = 20;
		};
		if (typeof fontName == 'undefined' || (fontName != null && fontName.hasOwnProperty ("__kwargtrans__"))) {;
			var fontName = 'Arial';
		};
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'text': var text = __allkwargs0__ [__attrib0__]; break;
						case 'fontSize': var fontSize = __allkwargs0__ [__attrib0__]; break;
						case 'fontName': var fontName = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var textObject = Text (text, fontSize, fontName);
		Sprite.__init__ (self, textObject, x, y, r, g, b);
	});}
});
export var PyAngelo =  __class__ ('PyAngelo', [object], {
	__module__: __name__,
	STATE_STOP: 1,
	STATE_RUN: 2,
	STATE_HALT: 3,
	STATE_LOAD: 4,
	STATE_INPUT: 5,
	STATE_LOADED: 6,
	get __init__ () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.commands = [];
		self.canvas = document.getElementById ('canvas');
		self.width = self.canvas.getAttribute ('width');
		self.height = self.canvas.getAttribute ('height');
		self.ctx = self.canvas.getContext ('2d');
		self.timer_id = null;
		self.main_loop = null;
		self.stopped = false;
		self.resources = dict ({});
		self.loadingResources = 0;
		self.py_keys = dict ((function () {
			var __accu0__ = [];
			for (var a = 0; a < 255; a++) {
				__accu0__.append (tuple ([a, false]));
			}
			return __accu0__;
		}) ());
		self.py_keys [KEY_V_LEFT] = false;
		self.py_keys [KEY_V_RIGHT] = false;
		self.py_keys [KEY_V_UP] = false;
		self.py_keys [KEY_V_DOWN] = false;
		self.py_keys [KEY_V_FIRE] = false;
		document.onkeydown = self._keydown;
		document.onkeyup = self._keyup;
		document.onmousemove = self._mousemove;
		document.onmousedown = self._mousedown;
		document.onmouseup = self._mouseup;
		document.ontouchstart = self._touchstart;
		document.ontouchmove = self._touchmove;
		document.ontouchend = self._touchend;
		self.mouse_x = 0;
		self.mouse_y = 0;
		self.touches = dict ({});
		self.soundPlayers = dict ({});
		self.state = self.STATE_RUN;
		self.anim_timer = 0;
		self.anim_time = 200;
		self.starting_text = 'Starting up';
		self.loading_text = 'Loading resources';
		self.py_clear (0.392, 0.584, 0.929);
		self.pixel_id = self.ctx.createImageData (1, 1);
		self.pixel_color = self.pixel_id.data;
		self.last_frame_commands = [];
		self.just_halted = false;
		self.input_concluded = false;
		self.input_buffer_index = 0;
		self.loading_filename = '';
		window.requestAnimationFrame (self.py_update);
	});},
	get isKeyPressed () {return __get__ (this, function (self, key) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'key': var key = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return self.py_keys [key];
	});},
	get refresh () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.execute_commands ();
	});},
	get loadSound () {return __get__ (this, function (self, filename, streaming) {
		if (typeof streaming == 'undefined' || (streaming != null && streaming.hasOwnProperty ("__kwargtrans__"))) {;
			var streaming = false;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'filename': var filename = __allkwargs0__ [__attrib0__]; break;
						case 'streaming': var streaming = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var howl = window.Howl;
		var sound = new howl (dict ([['src', [filename]]]));
		self.soundPlayers [filename] = sound;
		return filename;
	});},
	get playSound () {return __get__ (this, function (self, sound, loop) {
		if (typeof loop == 'undefined' || (loop != null && loop.hasOwnProperty ("__kwargtrans__"))) {;
			var loop = false;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sound': var sound = __allkwargs0__ [__attrib0__]; break;
						case 'loop': var loop = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (__in__ (sound, self.soundPlayers)) {
			self.soundPlayers [sound].loop = loop;
			self.soundPlayers [sound].play ();
		}
		else {
			self.loadSound (sound);
			self.soundPlayers [sound].loop = loop;
			self.soundPlayers [sound].play ();
		}
	});},
	get stopAllSounds () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		for (var sound of self.soundPlayers) {
			self.stopSound (sound);
		}
	});},
	get pauseSound () {return __get__ (this, function (self, sound) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sound': var sound = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (__in__ (sound, self.soundPlayers)) {
			self.soundPlayers [sound].pause ();
		}
	});},
	get stopSound () {return __get__ (this, function (self, sound) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sound': var sound = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (__in__ (sound, self.soundPlayers)) {
			self.soundPlayers [sound].stop ();
		}
	});},
	get _keydown () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.py_keys [ev.which] = true;
		if (ev.which == KEY_ESC && self.state == self.STATE_HALT) {
			self.stop ();
		}
		if (self.state == self.STATE_INPUT) {
			if (ev.which != KEY_ENTER && (ev.which < 32 || ev.which > KEY_A + 26)) {
				return ;
			}
			array [(len (array) - 1) - self.input_buffer_index] = ev.which;
			if (ev.which == KEY_ENTER) {
				self.input_concluded = true;
			}
			else {
				var returned_string = '';
				var n = self.input_buffer_index;
				while (n >= 0) {
					var returned_string = chr (array [(len (array) - 1) - n]) + returned_string;
					n -= 1;
				}
				self.input_buffer_index += 1;
				self.drawText (returned_string + '_', 0, 0);
			}
		}
	});},
	get _keyup () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.py_keys [ev.which] = false;
	});},
	get _updateTouchedKeys () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.py_keys [KEY_V_LEFT] = false;
		self.py_keys [KEY_V_RIGHT] = false;
		self.py_keys [KEY_V_UP] = false;
		self.py_keys [KEY_V_DOWN] = false;
		self.py_keys [KEY_V_FIRE] = false;
		for (var touch of self.touches.py_values ()) {
			var x = touch [0];
			var y = touch [1];
			if (x < (-(self.width) * 0.33) * 0.67 && y < self.height * 0.6 && y > self.height * 0.4) {
				self.py_keys [KEY_V_LEFT] = true;
			}
			if (x < 0 && x > (-(self.width) * 0.33) * 0.33 && y < self.height * 0.6 && y > self.height * 0.4) {
				self.py_keys [KEY_V_RIGHT] = true;
			}
			if (y < self.height * 0.4 && y > 0 && x < (-(self.width) * 0.33) * 0.33 && x > (-(self.width) * 0.33) * 0.67) {
				self.py_keys [KEY_V_DOWN] = true;
			}
			if (y < self.height && y > self.height * 0.6 && x < (-(self.width) * 0.33) * 0.33 && x > (-(self.width) * 0.33) * 0.67) {
				self.py_keys [KEY_V_UP] = true;
			}
			if (x > self.width && y < self.height && y > 0) {
				self.py_keys [KEY_V_FIRE] = true;
			}
		}
	});},
	get _touchstart () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		for (var touch of ev.changedTouches) {
			self.mouse_x = touch.clientX;
			self.mouse_y = touch.clientY;
			var boundingRect = self.canvas.getBoundingClientRect ();
			var x = int (self.mouse_x - boundingRect.left);
			var y = int (self.height - (self.mouse_y - boundingRect.top));
			self.touches [touch.identifier] = [x, y];
		}
		self._updateTouchedKeys ();
		return false;
	});},
	get _touchend () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.mouse_x = -(1);
		self.mouse_y = -(1);
		for (var touch of ev.changedTouches) {
			delete self.touches [touch.identifier];
		}
		self._updateTouchedKeys ();
		return false;
	});},
	get _touchmove () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		for (var touch of ev.changedTouches) {
			self.mouse_x = touch.clientX;
			self.mouse_y = touch.clientY;
			var boundingRect = self.canvas.getBoundingClientRect ();
			var x = int (self.mouse_x - boundingRect.left);
			var y = int (self.height - (self.mouse_y - boundingRect.top));
			self.touches [touch.identifier] = [x, y];
		}
		self._updateTouchedKeys ();
		return false;
	});},
	get _mousemove () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.mouse_x = ev.clientX;
		self.mouse_y = ev.clientY;
	});},
	get _mousedown () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.mouse_x = ev.clientX;
		self.mouse_y = ev.clientY;
		var boundingRect = self.canvas.getBoundingClientRect ();
		var x = int (self.mouse_x - boundingRect.left);
		var y = int (self.height - (self.mouse_y - boundingRect.top));
		self.py_keys [KEY_V_LEFT] = false;
		self.py_keys [KEY_V_RIGHT] = false;
		self.py_keys [KEY_V_UP] = false;
		self.py_keys [KEY_V_DOWN] = false;
		self.py_keys [KEY_V_FIRE] = false;
		if (x < (-(self.width) * 0.33) * 0.67 && y < self.height * 0.6 && y > self.height * 0.4) {
			self.py_keys [KEY_V_LEFT] = true;
		}
		if (x < 0 && x > (-(self.width) * 0.33) * 0.33 && y < self.height * 0.6 && y > self.height * 0.4) {
			self.py_keys [KEY_V_RIGHT] = true;
		}
		if (y < self.height * 0.4 && y > 0 && x < (-(self.width) * 0.33) * 0.33 && x > (-(self.width) * 0.33) * 0.67) {
			self.py_keys [KEY_V_DOWN] = true;
		}
		if (y < self.height && y > self.height * 0.6 && x < (-(self.width) * 0.33) * 0.33 && x > (-(self.width) * 0.33) * 0.67) {
			self.py_keys [KEY_V_UP] = true;
		}
		if (x > self.width && y < self.height && y > 0) {
			self.py_keys [KEY_V_FIRE] = true;
		}
	});},
	get _mouseup () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.mouse_x = -(1);
		self.mouse_y = -(1);
		self.py_keys [KEY_V_LEFT] = false;
		self.py_keys [KEY_V_RIGHT] = false;
		self.py_keys [KEY_V_UP] = false;
		self.py_keys [KEY_V_DOWN] = false;
		self.py_keys [KEY_V_FIRE] = false;
	});},
	get getMousePos () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var boundingRect = self.canvas.getBoundingClientRect ();
		return Point (int (self.mouse_x - boundingRect.left), int (self.height - (self.mouse_y - boundingRect.top)));
	});},
	get resourceLoaded () {return __get__ (this, function (self, e) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'e': var e = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		window.console.log ('Successfully loaded file:' + e.target.src);
		e.target.jmssImg.height = e.target.naturalHeight;
		e.target.jmssImg.width = e.target.naturalWidth;
		if (e.target.jmssImg.sprite !== null) {
			e.target.jmssImg.sprite.height = e.target.naturalHeight;
			e.target.jmssImg.sprite.width = e.target.naturalWidth;
			window.console.log ('Setting sprite width and height:', e.target.jmssImg.sprite.height, e.target.jmssImg.sprite.width);
		}
		self.loadingResources -= 1;
	});},
	get loadImage () {return __get__ (this, function (self, file, sprite) {
		if (typeof sprite == 'undefined' || (sprite != null && sprite.hasOwnProperty ("__kwargtrans__"))) {;
			var sprite = null;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'file': var file = __allkwargs0__ [__attrib0__]; break;
						case 'sprite': var sprite = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (__in__ (file, self.resources)) {
			return self.resources [file];
		}
		self.loadingResources += 1;
		window.console.log ('Attempting to load file:' + file);
		var img = document.createElement ('img');
		img.setAttribute ('src', file);
		img.setAttribute ('crossOrigin', 'Anonymous');
		img.addEventListener ('load', self.resourceLoaded, false);
		var jmssImg = PyAngeloImage (img, sprite);
		img.jmssImg = jmssImg;
		self.resources [file] = jmssImg;
		return jmssImg;
	});},
	get drawImage () {return __get__ (this, function (self, image, x, y, width, height, rotation, anchorX, anchorY, opacity, r, g, b, rect) {
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = null;
		};
		if (typeof height == 'undefined' || (height != null && height.hasOwnProperty ("__kwargtrans__"))) {;
			var height = null;
		};
		if (typeof rotation == 'undefined' || (rotation != null && rotation.hasOwnProperty ("__kwargtrans__"))) {;
			var rotation = 0;
		};
		if (typeof anchorX == 'undefined' || (anchorX != null && anchorX.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorX = null;
		};
		if (typeof anchorY == 'undefined' || (anchorY != null && anchorY.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorY = null;
		};
		if (typeof opacity == 'undefined' || (opacity != null && opacity.hasOwnProperty ("__kwargtrans__"))) {;
			var opacity = null;
		};
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof rect == 'undefined' || (rect != null && rect.hasOwnProperty ("__kwargtrans__"))) {;
			var rect = null;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'image': var image = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
						case 'height': var height = __allkwargs0__ [__attrib0__]; break;
						case 'rotation': var rotation = __allkwargs0__ [__attrib0__]; break;
						case 'anchorX': var anchorX = __allkwargs0__ [__attrib0__]; break;
						case 'anchorY': var anchorY = __allkwargs0__ [__attrib0__]; break;
						case 'opacity': var opacity = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'rect': var rect = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (image, str)) {
			var image = self.loadImage (image);
		}
		self.ctx.save ();
		if (width === null) {
			var width = image.width;
		}
		if (height === null) {
			var height = image.height;
		}
		if (opacity !== null) {
			if (opacity > 1.0) {
				var opacity = 1.0;
			}
			else if (opacity < 0.0) {
				var opacity = 0.0;
			}
			self.ctx.globalAlpha = opacity;
		}
		if (rotation != 0.0) {
			self.ctx.save ();
			self.ctx.translate (x, self._convY (y));
			self.ctx.rotate (-(rotation));
			self.ctx.drawImage (image.img, -(anchorX) * width, -(anchorY) * height, width, height);
			self.ctx.restore ();
		}
		else {
			self.ctx.drawImage (image.img, x, self._convY (y + height), width, height);
		}
		self.ctx.restore ();
	});},
	get drawSprite () {return __get__ (this, function (self, sprite, offsetX, offsetY) {
		if (typeof offsetX == 'undefined' || (offsetX != null && offsetX.hasOwnProperty ("__kwargtrans__"))) {;
			var offsetX = 0;
		};
		if (typeof offsetY == 'undefined' || (offsetY != null && offsetY.hasOwnProperty ("__kwargtrans__"))) {;
			var offsetY = 0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sprite': var sprite = __allkwargs0__ [__attrib0__]; break;
						case 'offsetX': var offsetX = __allkwargs0__ [__attrib0__]; break;
						case 'offsetY': var offsetY = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (sprite.image, Rectangle)) {
			self.drawRect (sprite.x - offsetX, sprite.y - offsetY, sprite.width, sprite.height, sprite.r, sprite.g, sprite.b);
		}
		else if (isinstance (sprite.image, Circle)) {
			self.drawCircle (sprite.x - offsetX, sprite.y - offsetY, sprite.radius, sprite.r, sprite.g, sprite.b);
		}
		else if (isinstance (sprite.image, Text)) {
			self.drawText (sprite.image.text, sprite.x - offsetX, sprite.y - offsetY, sprite.image.fontName, sprite.image.fontSize, sprite.r, sprite.g, sprite.b);
		}
		else {
			self.drawImage (sprite.image, sprite.x - offsetX, sprite.y - offsetY);
		}
	});},
	get measureText () {return __get__ (this, function (self, text, fontName, fontSize) {
		if (typeof fontName == 'undefined' || (fontName != null && fontName.hasOwnProperty ("__kwargtrans__"))) {;
			var fontName = 'Arial';
		};
		if (typeof fontSize == 'undefined' || (fontSize != null && fontSize.hasOwnProperty ("__kwargtrans__"))) {;
			var fontSize = 10;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'text': var text = __allkwargs0__ [__attrib0__]; break;
						case 'fontName': var fontName = __allkwargs0__ [__attrib0__]; break;
						case 'fontSize': var fontSize = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.ctx.font = (str (fontSize) + 'pt ') + fontName;
		var textMetrics = self.ctx.measureText (text);
		return tuple ([abs (textMetrics.actualBoundingBoxLeft) + abs (textMetrics.actualBoundingBoxRight), abs (textMetrics.actualBoundingBoxAscent) + abs (textMetrics.actualBoundingBoxDescent)]);
	});},
	get drawText () {return __get__ (this, function (self, text, x, y, fontName, fontSize, r, g, b, a, anchorX, anchorY) {
		if (typeof fontName == 'undefined' || (fontName != null && fontName.hasOwnProperty ("__kwargtrans__"))) {;
			var fontName = 'Arial';
		};
		if (typeof fontSize == 'undefined' || (fontSize != null && fontSize.hasOwnProperty ("__kwargtrans__"))) {;
			var fontSize = 10;
		};
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (typeof anchorX == 'undefined' || (anchorX != null && anchorX.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorX = 'left';
		};
		if (typeof anchorY == 'undefined' || (anchorY != null && anchorY.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorY = 'bottom';
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'text': var text = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'fontName': var fontName = __allkwargs0__ [__attrib0__]; break;
						case 'fontSize': var fontSize = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
						case 'anchorX': var anchorX = __allkwargs0__ [__attrib0__]; break;
						case 'anchorY': var anchorY = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.ctx.fillStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.font = (str (fontSize) + 'pt ') + fontName;
		self.ctx.textBaseline = 'bottom';
		self.ctx.fillText (text, x, self.height - y);
	});},
	get py_clear () {return __get__ (this, function (self, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.ctx.fillStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.fillRect (0, 0, self.width, self.height);
	});},
	get drawLine () {return __get__ (this, function (self, x1, y1, x2, y2, r, g, b, a, width) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = 1;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x1': var x1 = __allkwargs0__ [__attrib0__]; break;
						case 'y1': var y1 = __allkwargs0__ [__attrib0__]; break;
						case 'x2': var x2 = __allkwargs0__ [__attrib0__]; break;
						case 'y2': var y2 = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var r = min (r, 1.0);
		var g = min (g, 1.0);
		var b = min (b, 1.0);
		var a = min (a, 1.0);
		self.ctx.beginPath ();
		self.ctx.lineWidth = width;
		self.ctx.strokeStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.moveTo (x1, self._convY (y1));
		self.ctx.lineTo (x2, self._convY (y2));
		self.ctx.stroke ();
	});},
	get drawCircle () {return __get__ (this, function (self, x, y, radius, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var r = min (r, 1.0);
		var g = min (g, 1.0);
		var b = min (b, 1.0);
		var a = min (a, 1.0);
		self.ctx.fillStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.beginPath ();
		self.ctx.strokeStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.arc (x, self._convY (y), radius, 0, 2 * 3.1415926535, true);
		self.ctx.fill ();
		self.ctx.stroke ();
	});},
	get drawPixel () {return __get__ (this, function (self, x, y, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var r = min (r, 1.0);
		var g = min (g, 1.0);
		var b = min (b, 1.0);
		var a = min (a, 1.0);
		self.pixel_color [0] = int (r * 255.0);
		self.pixel_color [1] = int (g * 255.0);
		self.pixel_color [2] = int (b * 255.0);
		self.pixel_color [3] = int (a * 255.0);
		self.ctx.putImageData (self.pixel_id, x, self._convY (y));
	});},
	get drawRect () {return __get__ (this, function (self, x, y, w, h, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'w': var w = __allkwargs0__ [__attrib0__]; break;
						case 'h': var h = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var r = min (r, 1.0);
		var g = min (g, 1.0);
		var b = min (b, 1.0);
		var a = min (a, 1.0);
		var ctx = self.ctx;
		ctx.fillStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		ctx.beginPath ();
		ctx.moveTo (x, self._convY (y));
		ctx.lineTo (x + w, self._convY (y));
		ctx.lineTo (x + w, self._convY (y + h));
		ctx.lineTo (x, self._convY (y + h));
		ctx.closePath ();
		ctx.fill ();
	});},
	get _convY () {return __get__ (this, function (self, y) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return self.height - y;
	});},
	get _convColor () {return __get__ (this, function (self, c) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'c': var c = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return tuple ([int (c [0] * 255.0), int (c [1] * 255.0), int (c [2] * 255.0), int (c [3] * 255.0)]);
	});},
	get __input () {return __get__ (this, function (self, msg) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'msg': var msg = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.state = self.STATE_INPUT;
		self.input_concluded = false;
		self.input_buffer_index = 0;
	});},
	get loop () {return __get__ (this, function (self, func) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'func': var func = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.main_loop = func;
	});},
	get py_update () {return __get__ (this, function (self, deltaTime) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'deltaTime': var deltaTime = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (self.state == self.STATE_STOP) {
			self.py_clear (0.392, 0.584, 0.929);
			var width = self.measureText ('Ready', __kwargtrans__ ({fontSize: 30})) [0];
			self.drawText ('Ready', 250 - width / 2, 170, __kwargtrans__ ({fontSize: 30}));
		}
		else if (self.state == self.STATE_RUN) {
			if (self.main_loop !== null) {
				try {
					self.main_loop ();
				}
				catch (__except0__) {
					if (isinstance (__except0__, Exception)) {
						var e = __except0__;
						do_print ((('Error: ' + str (e)) + '\n') + traceback.format_exc (), 'red');
						self.stop ();
					}
					else {
						throw __except0__;
					}
				}
			}
		}
		else if (self.state == self.STATE_INPUT) {
			if (self.input_concluded) {
				self.state = self.STATE_RUN;
				self.input_concluded = false;
			}
		}
		else if (self.state == self.STATE_LOAD) {
			self.py_clear (0.192, 0.384, 0.729);
			var text = 'Loading: ' + self.loading_filename;
			var width = self.measureText (text, __kwargtrans__ ({fontSize: 20})) [0];
			self.drawText (text, 250 - width / 2, 170, __kwargtrans__ ({fontSize: 20}));
		}
		else if (self.state == self.STATE_LOADED) {
			self.py_clear (0.192, 0.384, 0.729);
			var text = 'Successfully Loaded:';
			var width = self.measureText (text, __kwargtrans__ ({fontSize: 20})) [0];
			self.drawText (text, 250 - width / 2, 200, __kwargtrans__ ({fontSize: 20}));
			var text = self.loading_filename;
			var width = self.measureText (text, __kwargtrans__ ({fontSize: 20})) [0];
			self.drawText (text, 250 - width / 2, 170, __kwargtrans__ ({fontSize: 20}));
		}
		window.requestAnimationFrame (self.py_update);
	});},
	get start () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (self.state != self.STATE_RUN) {
			self.state = self.STATE_RUN;
		}
	});},
	get stop () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		disable_stop_enable_play ();
		if (self.state != self.STATE_STOP) {
			self.state = self.STATE_STOP;
			self.resources = dict ({});
			self.loadingResources = 0;
			self.stopAllSounds ();
		}
	});},
	get getPixelColour () {return __get__ (this, function (self, x, y) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var pixel = new window.Int8Array (4);
		var imageData = self.ctx.getImageData (x, self._convY (y), 1, 1);
		return Colour (imageData.data [0] / 255.0, imageData.data [1] / 255.0, imageData.data [2] / 255.0, imageData.data [3] / 255.0);
	});},
	get sleep () {return __get__ (this, function (self, milliseconds) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'milliseconds': var milliseconds = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var currTime = window.performance.now ();
		var prevTime = currTime;
		while (currTime - prevTime < milliseconds) {
			var currTime = window.performance.now ();
		}
	});},
	get overlaps () {return __get__ (this, function (self, x1, y1, width1, height1, x2, y2, width2, height2) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x1': var x1 = __allkwargs0__ [__attrib0__]; break;
						case 'y1': var y1 = __allkwargs0__ [__attrib0__]; break;
						case 'width1': var width1 = __allkwargs0__ [__attrib0__]; break;
						case 'height1': var height1 = __allkwargs0__ [__attrib0__]; break;
						case 'x2': var x2 = __allkwargs0__ [__attrib0__]; break;
						case 'y2': var y2 = __allkwargs0__ [__attrib0__]; break;
						case 'width2': var width2 = __allkwargs0__ [__attrib0__]; break;
						case 'height2': var height2 = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return x1 < x2 + width2 && x1 + width1 > x2 && y1 < y2 + height2 && y1 + height1 > y2;
	});}
});
export var graphics = PyAngelo ();

//# sourceMappingURL=PyAngelo.map