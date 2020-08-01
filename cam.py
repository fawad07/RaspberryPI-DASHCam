#!/usr/bin/env python3
import os
from picamera import PiCamera
from time import sleep
import tkinter as tk
from datetime import *

dialog=tk.Tk()       #main Window
cam=PiCamera()
time=str(datetime.now().strftime("%c %A"))

def main():
    dialog.geometry("300x275+5+5")
    btn_frame = tk.Frame(dialog)
    btn_frame.pack(fill=tk.X, side=tk.BOTTOM)

    pic_btn = tk.Button(btn_frame, text="take pic", command=camera_take_pic)
    pic_btn.grid(row=0, column=0, sticky=tk.W + tk.E)
    # pic_btn.pack()

    vid_rec_btn = tk.Button(btn_frame, text="record", command=camera_record)
    vid_rec_btn.grid(row=0, column=1, sticky=tk.W + tk.E)
    # vid_btn.pack()
    stop_vid_rec = tk.Button(btn_frame, text="Stop recording", command=stop_record)
    stop_vid_rec.grid(row=1, column=1, sticky=tk.W + tk.E)

    close_btn = tk.Button(btn_frame, text="Close", command=close_window)
    close_btn.grid(row=0, column=2, sticky=tk.W + tk.E)

    btn_frame.columnconfigure(0, weight=1)
    btn_frame.columnconfigure(1, weight=1)
    btn_frame.columnconfigure(2, weight=1)
    camera_record()
    tk.mainloop();


def camera_take_pic():
    #cam=PiCamera()
    cam.resolution = (1024, 768)
    cam.framerate = 10
    cam.preview_fullscreen=False
    cam.preview_window=(10,40, 300,200)
    cam.start_preview()
    cam.annotate_text = time
    sleep(1)
    cam.capture(time)
    cam.stop_preview()
    cam.close()
    
def camera_record():
    #cam=PiCamera();
    cam.rotation = 90;
    cam.sharpness = 76;
    cam.brightness = 46;
    cam.framerate = 60
    cam.zoom=(0.03,0.03, 0.7, 0.5);
    cam.resolution = (1024, 768);
    cam.start_recording('/home/pi/Desktop/test.h264');
    cam.preview_fullscreen=False
    cam.preview_window=(10,40, 300,200)
    cam.start_preview();
    cam.annotate_text = time
    cam.wait_recording(0.05);
    #cam.stop_recording();
    #cam.close();

def stop_record():
    #cam=PiCamera();
    cam.wait_recording(1);
    os.rename(r'/home/pi/Desktop/test.h264',r'/home/pi/Desktop/'+time+'.h264')
    cam.stop_recording();
    cam.close();

def close_window():
    cam.close();
    dialog.destroy();



#_______________________________________________________________________
if __name__ == "__main__":
    main()

#dialog.geometry("300x275+5+5")
#btn_frame=tk.Frame(dialog)
#btn_frame.pack(fill=tk.X, side=tk.BOTTOM)

#pic_btn=tk.Button(btn_frame, text="take pic", command=camera_take_pic)
#pic_btn.grid(row=0, column=0, sticky=tk.W+tk.E)
#pic_btn.pack()

#vid_rec_btn=tk.Button(btn_frame, text="record", command=camera_record)
#vid_rec_btn.grid(row=0, column=1, sticky=tk.W+tk.E)
#vid_btn.pack()
#stop_vid_rec=tk.Button(btn_frame, text="Stop recording", command=stop_record)
#stop_vid_rec.grid(row=1, column=1, sticky=tk.W+tk.E)

#close_btn=tk.Button(btn_frame, text="Close", command=close_window)
#close_btn.grid(row=0, column=2, sticky=tk.W+tk.E)

#btn_frame.columnconfigure(0, weight=1)
#btn_frame.columnconfigure(1, weight=1)
#btn_frame.columnconfigure(2, weight=1)
#tk.mainloop();
