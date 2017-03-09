# Program              : autolike
# Author               : Ahmedur Rahman Shovon
# Description          : Automatically like any given Facebook URL if the user is logged in.
#                        DO NOT MISUSE IT FOR DISTURBING INDIVIDUALS.                    
# Date                 : 09/03/2017
# Version              : 0.0.3
# Tested OS            : Windows (10)
# Python Version       : Python 3

import pyautogui as pt
import webbrowser
import time
import os

def facebook(url = "https://www.facebook.com/", run_time = 120):
    return_dict = {
        "status":"error",
        "message": "Error message in details.",
        "url": "",
        "like": 0,
        "time": 0
        }
    try:
        pt.moveTo(800,250)
        start = time.time()
        like_image = os.path.join(os.path.dirname(__file__), 'like.png')
        webbrowser.open(url)
        time.sleep(4)
        cnt_like = 0
        elapsed_time = 0
        while True:
            like_pos = pt.locateCenterOnScreen(like_image,grayscale = True)
            if like_pos != None:
                pt.click(like_pos[0], like_pos[1])
                pt.moveTo(800,250)
                cnt_like+=1
            pt.scroll(-400)
            time.sleep(4)    
            end = time.time()
            elapsed_time = end - start
            if elapsed_time > run_time:
                elapsed_time = str(int(elapsed_time))
                return_dict["status"] = "success"
                return_dict["message"] = "Method is called successfully."
                return_dict["like"] = cnt_like
                return_dict["url"] = url
                return_dict["time"] = elapsed_time                
                break
            elapsed_time = str(int(elapsed_time))
            return_dict["status"] = "success"
            return_dict["message"] = "Method is called successfully."
            return_dict["like"] = cnt_like
            return_dict["url"] = url
            return_dict["time"] = elapsed_time                
    except Exception as e:
        return_dict["message"] = str(e)
    return return_dict
