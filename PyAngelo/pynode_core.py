import sys
import time
import traceback
import javascript
import random
import json
from browser import document, window, alert, timer, worker, bind, html, load
from browser.local_storage import storage

load("howler.js")

# Cursor control and motion
KEY_HOME          = 0xff50
KEY_LEFT          = 37
KEY_UP            = 38
KEY_RIGHT         = 39
KEY_DOWN          = 40
KEY_PAGEUP        = 0xff55
KEY_PAGEDOWN      = 0xff56
KEY_END           = 0xff57
KEY_BEGIN         = 0xff58

# Create a web worker, identified by a script id in this page.
sab_proto = window.SharedArrayBuffer;
sab = sab_proto.new(1);

test_data = window.Array.new(sab);
test_data[0] = 42;



myWorker = worker.Worker("executor")

myWorker.send(sab)

def onmessage(e):
    #alert("Message received from executor:" + str(e.data));
    if e.data[0].lower() == "reveal":
        # successful
        
        graphics_main.commands = e.data[1]
        graphics_main.execute_commands()
        
        # now wait 1 frame before continuing the code execution in the worker thread
        timer.set_timeout(graphics_main.next_frame, 16)
        
myWorker.bind("message", onmessage)

class PyAngeloImage():
    def __init__(self, image):
        self.img = image
        self.height = image.naturalHeight
        self.width = image.naturalWidth

class PyAngelo():
    def __init__(self):
        self.commands = []
        
        # get the canvas element
        self.canvas = document["canvas"]
        self.ctx = self.canvas.getContext('2d')		
        
        self.width = self.canvas.width
        self.height = self.canvas.height
        
        self.timer_id = None
        
        self.resources =  {}
        self.loadingResources = 0
        
        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)]) 

        document.bind("keydown", self._keydown)
        document.bind("keyup", self._keyup)   

        self.soundPlayers = {}        
        
        # clear to cornflower blue (XNA!) by default        
        self.__clear(0.392,0.584,0.929)
        
    def __loadSound(self, filename, streaming = False):
        howl = window.Howl
        sound = howl.new({"src": [filename]})
        self.soundPlayers[filename] = sound
        return filename


    def __playSound(self, sound, loop = False):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].loop = loop
            self.soundPlayers[sound].play()

    def __pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()        
        
    def _keydown(self, ev):
        global test_data
        #alert("key pressed!" + str(ev.which));
        self.keys[ev.which] = True
        test_data[0] = 1
        
                       
        myWorker.send(["keydown", ev.which])	

    def _keyup(self, ev):
        self.keys[ev.which] = False
        
        myWorker.send(["keyup", ev.which])    
        
    def resourceLoaded(self, e):
        self.loadingResources -= 1
        e.target.jmssImg.height = e.target.naturalHeight
        e.target.jmssImg.width = e.target.naturalWidth        
        
    def loadImage(self, file):
    
        if file in self.resources:
            return self.resources[file]       
        
        self.loadingResources += 1
        
        img = html.IMG(src = file)
        #alert("Attempting to draw image");
        img.bind('load', self.resourceLoaded)
        jmssImg = PyAngeloImage(img)
        img.jmssImg = jmssImg
        
        self.resources[file] = jmssImg
        
        return jmssImg


    def __drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, r=1.0, g=1.0, b=1.0, rect=None):        
        
        if (isinstance(image, str)):
            image = self.loadImage(image)
        
        if self.loadingResources > 0:
            return
            
        #alert("Attempting to draw image");
        '''        
        self.ctx.save()
        if opacity is not None:
            self.ctx.globalAlpha = opacity
            self.ctx.drawImage(image.img, x, self._convY(y + image.height) )
            self.ctx.restore()
        else:
            self.ctx.drawImage(image.img, x, self._convY(y + image.height))  
        '''         
        
        self.ctx.save()

        if width is None:
            width = image.width

        if height is None:
            height = image.height

        if opacity is not None:
            if opacity > 1.0:
                opacity = 1.0
            elif opacity < 0.0:
                opacity = 0.0
            self.ctx.globalAlpha = opacity


        if rotation != 0.0:
            # TODO: Buggy!!!
            self.ctx.save()
            self.ctx.translate(x, self._convY(y))
            self.ctx.rotate(- rotation)# - 3.1415926535)# + math.PI / 180)
            self.ctx.drawImage(image.img, -anchorX * width, -anchorY * height, width, height)
            self.ctx.restore()
        else:
            self.ctx.drawImage(image.img, x, self._convY(y + height), width, height)


        self.ctx.restore()           

    def __clear(self, r = 0, g = 0, b = 0, a = 1):
        #alert("Clearing!");
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)    
        
    def __drawLine(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0, width = 1):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.moveTo(x1, self._convY(y1))
        self.ctx.lineTo(x2, self._convY(y2))
        self.ctx.stroke()        
        
    def _convY(self, y):
        return self.height - y

    def _convColor(self, c):
        return (int(c[0] * 255.0), int(c[1] * 255.0), int(c[2] * 255.0), int(c[3] * 255.0))                
       
    def execute_commands(self):       
        while len(self.commands) > 0:
            command = self.commands[0]
            
            if command[0] == "drawLine":
                command[0] = self.__drawLine
            elif command[0] == "clear":
                command[0] = self.__clear
            elif command[0] == "drawImage":                
                command[0] = self.__drawImage
            elif command[0] == "loadSound":                
                command[0] = self.__loadSound                
            elif command[0] == "playSound":                
                command[0] = self.__playSound
            elif command[0] == "pauseSound":                
                command[0] = self.__pauseSound                
            else:
                # not a valid command
                del self.commands[0]
                continue
                
            command[0](**command[1])    
            del self.commands[0]
            
    def next_frame(self):
        myWorker.send(["next"])
        
    def start(self, src):
        global myWorker
        myWorker.terminate()
        myWorker = worker.Worker("executor")
        myWorker.bind("message", onmessage)
        myWorker.send(["run", src])

    def stop(self):
        myWorker.send(["stop"])		
        myWorker.terminate()
        # clear to cornflower blue (XNA!) by default        
        self.__clear(0.392,0.584,0.929)		
    
graphics_main = PyAngelo()    


import pynode_graphlib

class PynodeCoreGlobals():
    GLOBAL_ID = 0
    GLOBAL_USER_ID = 0
    event_queue = []
    event_timer = None
    update_timer = None
    do_events = True
    has_ended = False
    do_update = True
    fix_layout = True
    did_fix_layout = False
    did_update_layout = False
    delay_type = {}
    click_listener_func = {"f": None}
    positioning_counter = None
    error = ""

def enable_events(enable):
    PynodeCoreGlobals.do_events = enable
def enable_update(enable):
    PynodeCoreGlobals.do_update = enable

def next_global_id():
    id_value = PynodeCoreGlobals.GLOBAL_ID
    PynodeCoreGlobals.GLOBAL_ID += 1
    return id_value

def next_user_id():
    id_value = PynodeCoreGlobals.GLOBAL_USER_ID
    PynodeCoreGlobals.GLOBAL_USER_ID += 1
    return id_value

class Event():
    def __init__(self, func, args):
        self.func = func
        self.args = args
    def execute(self):
        self.func(*self.args)
class EventPrint(Event):
    def __init__(self, func, args):
        super().__init__(func, args)
class EventPause():
    def __init__(self, time):
        self.time = time

def add_event(event, source=None):
    if PynodeCoreGlobals.do_events:
        if source is not None:
            if isinstance(source, pynode_graphlib.Node) and not pynode_graphlib.graph.has_node(source): return
            if isinstance(source, pynode_graphlib.Edge) and not pynode_graphlib.graph.has_edge(source): return
        if isinstance(event, Event) and isinstance(event.func, str) and event.func.startswith("js_"):
            event.args = [event.func, json.dumps(event.args)]
            event.func = window["js_run_function"]
        PynodeCoreGlobals.event_queue.append(event)

def get_data(event, source=None):
    if source is not None:
        if isinstance(source, pynode_graphlib.Node) and not pynode_graphlib.graph.has_node(source): return None
        if isinstance(source, pynode_graphlib.Edge) and not pynode_graphlib.graph.has_edge(source): return None
    if isinstance(event, Event) and isinstance(event.func, str) and event.func.startswith("js_"):
        return json.loads(window.js_run_function_with_return(event.func, json.dumps(event.args)))
    return None

def format_string_HTML(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>").replace("\"", "&quot;").replace("'", "&apos;").replace(" ", "&nbsp;")

def do_print(s, color=None):
    if color is not None: window.writeOutput("<p style='display:inline;color:" + color + ";'>" + format_string_HTML(s) + "</p>", True)
    else: window.writeOutput("<p style='display:inline;'>" + format_string_HTML(s) + "</p>", True)

def do_print_formatted(s):
    window.writeOutput(s, True)

class PrintOutput:
    def write(self, data):
        alert(str(data));
        #add_event(EventPrint(do_print, [str(data)]))
        #do_print(data)
    def flush(self):
        pass

class ErrorOutput:
    def write(self, data):
        #alert(str(data));
        #PynodeCoreGlobals.error += "<p style='display:inline;color:red;'>" + format_string_HTML(str(data)) + "</p>"
        document["console"].innerHTML += "<p style='display:inline;color:red;'>" + format_string_HTML(str(data)) + "</p>"
    def flush(self):
        pass

sys.stdout = PrintOutput()
sys.stderr = ErrorOutput()

def end_playing():
    if not PynodeCoreGlobals.has_ended:
        clear_button_run()
        document["runPlay"].style.display = "inherit"
        document["run"].bind("click", button_play)
        do_print("Done\n", color="green")
    PynodeCoreGlobals.has_ended = True

def play_events():
    try:
        try:
            if len(PynodeCoreGlobals.event_queue) > 0:
                event = PynodeCoreGlobals.event_queue[0]
                delay = 5
                if isinstance(event, EventPause):
                    delay = event.time
                else:
                    event.execute()
                del PynodeCoreGlobals.event_queue[0]
                PynodeCoreGlobals.event_timer = timer.set_timeout(play_events, delay)
            else:
                PynodeCoreGlobals.event_timer = timer.set_timeout(play_events, 100)
                end_playing()
        except:
            traceback.print_exc(file=sys.stderr)
            handle_exception(False)
            end_playing()
        sys.exit()
    except:
        pass

def handle_exception(emptyPrint=True):
    try:
        if PynodeCoreGlobals.event_queue is not None and emptyPrint:
            for event in PynodeCoreGlobals.event_queue:
                if isinstance(event, EventPrint):
                    event.execute()
        do_print_formatted(PynodeCoreGlobals.error)
    except:
        pass

def execute_function(func, args):
    try:
        pynode_graphlib._execute_function(func, args)
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        handle_exception(False)

def reset(clear_console=True):
    return
    try:       
        PynodeCoreGlobals.GLOBAL_USER_ID = 0
        if clear_console: window.writeOutput("", False)
        pynode_graphlib.graph._reset()
        window.js_clear()
        if PynodeCoreGlobals.event_timer is not None: timer.clear_timeout(PynodeCoreGlobals.event_timer)
        if PynodeCoreGlobals.update_timer is not None: timer.clear_timeout(PynodeCoreGlobals.update_timer)
        PynodeCoreGlobals.event_queue = [EventPause(100)]
        PynodeCoreGlobals.fix_layout = True
        PynodeCoreGlobals.did_fix_layout = False
        PynodeCoreGlobals.did_update_layout = False
        PynodeCoreGlobals.has_ended = False
        PynodeCoreGlobals.delay_type = {}
        PynodeCoreGlobals.positioning_counter = 0
        PynodeCoreGlobals.error = ""
        PynodeCoreGlobals.click_listener_func = {"f": None}
        window.set_layout_type()
        window.registerClickListener(node_click)
        window.clickListenerFunc = None
    except:
        timer.set_timeout(reset, 20)

def clear_button_run():
    document["runPlay"].style.display = "none"
    document["runPlayLoad"].style.display = "none"
    document["runPause"].style.display = "none"
    document["runResume"].style.display = "none"
    for event in document["run"].events("click"):
        document["run"].unbind("click", event)
    document["run"].bind("click", save_code)

def button_play(event):    
    reset()
    clear_button_run()
    document["runPlayLoad"].style.display = "inherit"
    document["run"].bind("click", button_pause)
    timer.set_timeout(do_play, 20)

def do_play():
    src = window.getCode()
    try:
        success = True
        try:
            # try and run the code in the web worker!!!!
            graphics_main.start(src)
            #myWorker.send(["run", src])
            #pynode_graphlib._exec_code(src)
        except Exception as exc:
            alert("Error!");
            traceback.print_exc(file=sys.stderr)
            handle_exception()
            success = False
        clear_button_run()
        document["runPause"].style.display = "inherit"
        document["run"].bind("click", button_pause)
        if success: 
            #graphics.run()
            play_events()
        else: 
            end_playing()
        sys.exit()
    except:
        pass

def button_pause(event):
    clear_button_run()
    document["runResume"].style.display = "inherit"
    document["run"].bind("click", button_resume)
    if PynodeCoreGlobals.event_timer is not None:
        timer.clear_timeout(PynodeCoreGlobals.event_timer)

def button_resume(event):
    clear_button_run()
    document["runPause"].style.display = "inherit"
    document["run"].bind("click", button_pause)
    PynodeCoreGlobals.event_timer = timer.set_timeout(play_events, 0)

def button_stop(event):
    clear_button_run()
    document["runPlay"].style.display = "inherit"
    document["run"].bind("click", button_play)
    reset(False)

    graphics_main.stop()
    
    if PynodeCoreGlobals.event_timer is not None:
        timer.clear_timeout(PynodeCoreGlobals.event_timer)

def button_restart(event):
    button_play(event)

def node_click(node_id):
    node = None
    if pynode_graphlib.graph is not None and PynodeCoreGlobals.click_listener_func["f"] is not None:
        for n in pynode_graphlib.graph.nodes():
            if n._internal_id == node_id: node = n
        if node is not None:
            execute_function(PynodeCoreGlobals.click_listener_func["f"], [node])

def save_code(event):
    window.saveCode()

def update_instant():
    pass
    try: window.greuler_instance.update({"skipLayout": True})
    except: PynodeCoreGlobals.update_timer = timer.set_timeout(update_instant, 20)

def update_instant_layout():
    try: window.updateLayout()
    except: PynodeCoreGlobals.update_timer = timer.set_timeout(update_instant_layout, 20)

def refresh_layout():
    window.refreshLayout()

def js_update(layout=True):
    pass
    if PynodeCoreGlobals.do_update:
        try:
            if layout:
                PynodeCoreGlobals.update_timer = timer.set_timeout(update_instant_layout, 50)
                window.updateLayout()
            else:
                PynodeCoreGlobals.update_timer = timer.set_timeout(update_instant, 50)
                window.greuler_instance.update({"skipLayout": True})
        except:
            pass

def js_clear():
    pass
    window.greuler_instance.graph.removeEdges(window.greuler_instance.graph.edges)
    window.greuler_instance.graph.removeNodes(window.getGraphNodes())
    js_update(True)

# These functions have been moved over to JavaScript
js_add_node = "js_add_node"
js_remove_node = "js_remove_node"
js_add_edge = "js_add_edge"
js_remove_edge = "js_remove_edge"
js_add_all = "js_add_all"
js_remove_all = "js_remove_all"
js_set_spread = "js_set_spread"
js_node_set_value = "js_node_set_value"
js_node_set_position = "js_node_set_position"
js_node_get_position = "js_node_get_position"
js_node_set_label = "js_node_set_label"
js_node_set_size = "js_node_set_size"
js_node_set_color = "js_node_set_color"
js_node_set_value_style = "js_node_set_value_style"
js_node_set_label_style = "js_node_set_label_style"
js_node_highlight = "js_node_highlight"
js_edge_set_weight = "js_edge_set_weight"
js_edge_set_directed = "js_edge_set_directed"
js_edge_set_width = "js_edge_set_width"
js_edge_set_color = "js_edge_set_color"
js_edge_set_weight_style = "js_edge_set_weight_style"
js_edge_highlight = "js_edge_highlight"
js_edge_traverse = "js_edge_traverse"
