import sys ,os 
if "--spawn-loader"in sys .argv :
    from PySide6 .QtWidgets import QApplication ,QWidget ,QVBoxLayout ,QFrame ,QLabel ,QGraphicsDropShadowEffect 
    from PySide6 .QtCore import Qt ,QTimer 
    from PySide6 .QtGui import QPixmap ,QColor ,QPainter ,QConicalGradient ,QPen 
    import time ,random 
    class LoadingOverlay (QWidget ):
        def __init__ (self ,start_time =None ):
            super ().__init__ ()
            self .setWindowFlags (Qt .Window |Qt .FramelessWindowHint |Qt .WindowStaysOnTopHint |Qt .Tool )
            self .setAttribute (Qt .WA_TranslucentBackground )
            self .setMinimumSize (650 ,565 )
            self .setMaximumSize (650 ,565 )
            self .start_ts =start_time if start_time else time .time ()
            self ._angle =0 
            self .phrases =["FORCING PALS TO WORK OVERTIME...","CONDENSING EXTRA PALS INTO JUICE...","CRACKING THE PROGRESSIVE WORK WHIP...","PETTING THE CHILLETS FOR LUCK...","IGNORING SANITY DEPLETION...","FEEDING BERRIES TO DEPRESSED LAMBALLS...","CALIBRATING PALBOX COORDINATES...","CLEANING UP AFTER A RAID...","SEARCHING FOR LUCKY PALS...","OPTIMIZING WORKFLOW EFFICIENCY...","REPLACING TIRED PALS WITH FRESHER MODELS...","CONVINCING DEPRESSED PALS THAT THE VIEW IS BETTER FROM THE ASSEMBLY LINE...","RECYCLING UNSATISFACTORY SPECIMENS...","UPDATING WORKER CONTRACTS (NOW WITH 0% BREAK TIME)...","TELLING THE LOVEANDERS TO SETTLE DOWN...","HARVESTING PAL FLUIDS... DON'T ASK HOW...","SHARPENING THE BUTCHER'S CLEAVER FOR 'VALUATION'...","TELLING THE GUMOSS IT'S JUST A HAIRCUT...","UPGRADING THE ELECTRICITY GENERATOR WITH MORE SPARKITS...","REASSURING THE CREW THAT THE PAL FLUID IS JUST BLUE GATORADE..."]
            self .main_layout =QVBoxLayout (self )
            self .main_layout .setContentsMargins (50 ,50 ,50 ,50 )
            self .container =QFrame ()
            self .container .setStyleSheet ("background-color: rgba(5, 7, 12, 252); border-radius: 40px; border: none;")
            self .shadow =QGraphicsDropShadowEffect (self )
            self .shadow .setBlurRadius (40 )
            self .shadow .setXOffset (0 )
            self .shadow .setYOffset (0 )
            self .shadow .setColor (QColor (0 ,0 ,0 ,255 ))
            self .container .setGraphicsEffect (self .shadow )
            inner =QVBoxLayout (self .container )
            inner .setContentsMargins (35 ,40 ,35 ,40 )
            inner .setSpacing (20 )
            self .label =QLabel (random .choice (self .phrases ))
            self .label .setAlignment (Qt .AlignCenter )
            self .label .setWordWrap (True )
            self .label .setMinimumHeight (120 )
            self .label .setStyleSheet ("color: white; font-family: 'Segoe UI'; font-size: 19px; font-weight: 900; letter-spacing: 1px; background: transparent; border: none;")
            self .icon_label =QLabel ()
            self .icon_label .setAlignment (Qt .AlignCenter )
            self .icon_label .setStyleSheet ("background: transparent; border: none;")
            self .timer_label =QLabel ("00:00.00")
            self .timer_label .setAlignment (Qt .AlignCenter )
            self .timer_label .setStyleSheet ("color: #00f2ff; font-family: 'Consolas'; font-size: 38px; font-weight: bold; background: transparent; border: none;")
            inner .addWidget (self .label )
            inner .addWidget (self .icon_label )
            inner .addWidget (self .timer_label )
            self .main_layout .addWidget (self .container )
            self .set_icon ()
            self .anim_timer =QTimer (self )
            self .anim_timer .timeout .connect (self .update_sync )
            self .anim_timer .start (10 )
            self .joke_timer =QTimer (self )
            self .joke_timer .timeout .connect (self .cycle_phrase )
            self .joke_timer .start (3500 )
        def cycle_phrase (self ):
            new_phrase =random .choice (self .phrases )
            while new_phrase ==self .label .text ():
                new_phrase =random .choice (self .phrases )
            self .label .setText (new_phrase )
        def update_sync (self ):
            elapsed =time .time ()-self .start_ts 
            self ._angle =(elapsed *300 )%360 
            self .timer_label .setText (f"{int (elapsed //60 ):02d}:{int (elapsed %60 ):02d}.{int ((elapsed *100 )%100 ):02d}")
            self .update ()
        def paintEvent (self ,event ):
            p =QPainter (self )
            p .setRenderHint (QPainter .Antialiasing )
            rect =self .container .geometry ()
            g =QConicalGradient (rect .center (),-self ._angle )
            stops =[(0.0 ,QColor (255 ,0 ,0 )),(0.17 ,QColor (255 ,255 ,0 )),(0.33 ,QColor (0 ,255 ,0 )),(0.5 ,QColor (0 ,255 ,255 )),(0.67 ,QColor (0 ,0 ,255 )),(0.83 ,QColor (255 ,0 ,255 )),(1.0 ,QColor (255 ,0 ,0 ))]
            for s ,c in stops :g .setColorAt (s ,c )
            pen =QPen (g ,10 )
            p .setPen (pen )
            p .drawRoundedRect (rect .adjusted (2 ,2 ,-2 ,-2 ),40 ,40 )
        def set_icon (self ):
            if getattr (sys ,'frozen',False ):
                base_path =os .path .dirname (sys .executable )
                res_path =os .path .join (base_path ,"resources","Xenolord.webp")
                if not os .path .exists (res_path ):
                    res_path =os .path .join (base_path ,"Assets","resources","Xenolord.webp")
                if not os .path .exists (res_path ):
                    res_path =os .path .join (base_path ,"lib","Assets","resources","Xenolord.webp")
            else :
                base_path =os .path .dirname (os .path .abspath (__file__ ))
                res_path =os .path .join (base_path ,"resources","Xenolord.webp")
                if not os .path .exists (res_path ):
                    res_path =os .path .join (base_path ,"..","resources","Xenolord.webp")
            if os .path .exists (res_path ):
                self .icon_label .setPixmap (QPixmap (res_path ).scaled (180 ,180 ,Qt .KeepAspectRatio ,Qt .SmoothTransformation ))
            else :
                print (f"Warning: Icon file not found at {res_path }")
    app =QApplication (sys .argv )
    st =None 
    try :
        idx =sys .argv .index ("--spawn-loader")
        st =float (sys .argv [idx +1 ])
    except :
        pass 
    overlay =LoadingOverlay (start_time =st )
    overlay .show ()
    overlay .move (QApplication .primaryScreen ().geometry ().center ()-overlay .rect ().center ())
    sys .exit (app .exec ())
from import_libs import *
from PySide6 .QtWidgets import QWidget ,QVBoxLayout ,QFrame ,QLabel ,QApplication ,QMainWindow ,QGraphicsDropShadowEffect 
from PySide6 .QtCore import Qt ,QTimer ,QRectF 
from PySide6 .QtGui import QPixmap ,QColor ,QPainter ,QConicalGradient ,QPen 
from PySide6 .QtCore import qInstallMessageHandler ,QtMsgType 
def qt_suppress_handler (msg_type ,context ,message ):
    if any (err in message for err in ["QProcess: Destroyed","UpdateLayeredWindowIndirect","Unable to set geometry"]):
        return 
    print (message )
qInstallMessageHandler (qt_suppress_handler )
import time ,os ,math ,sys ,threading ,random ,subprocess 
_active_loader_proc =None 
_worker_ref =None 
_result_data ={"status":"idle","data":None }
def run_with_loading (callback ,func ,*args ,**kwargs ):
    global _active_loader_proc ,_worker_ref ,_result_data 
    from PySide6 .QtCore import QTimer 
    _result_data ["status"]="running"
    _result_data ["data"]=None 
    start_time_arg =str (time .time ())
    if getattr (sys ,'frozen',False ):
        args_list =[sys .executable ,"--spawn-loader",start_time_arg ]
    else :
        args_list =[sys .executable ,os .path .abspath (__file__ ),"--spawn-loader",start_time_arg ]
    _active_loader_proc =subprocess .Popen (args_list ,creationflags =subprocess .CREATE_NO_WINDOW if os .name =="nt"else 0 )
    def task_wrapper ():
        try :
            _result_data ["data"]=func (*args ,**kwargs )
        except Exception as e :
            _result_data ["data"]=e 
        _result_data ["status"]="finished"
    _worker_ref =threading .Thread (target =task_wrapper ,daemon =True )
    _worker_ref .start ()
    timer =QTimer ()
    timer .setInterval (100 )
    def monitor ():
        global _active_loader_proc 
        if _result_data ["status"]!="finished":
            return 
        timer .stop ()
        if _active_loader_proc :
            _active_loader_proc .terminate ()
            try :
                _active_loader_proc .wait (timeout =1 )
            except subprocess .TimeoutExpired :
                _active_loader_proc .kill ()
            _active_loader_proc =None 
        res =_result_data ["data"]
        _result_data ["status"]="idle"
        if callback :
            callback (res )
    timer .timeout .connect (monitor )
    timer .start ()
