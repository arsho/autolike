# Program              : autolike
# Author               : Ahmedur Rahman Shovon
# Description          : Automatically like any given Facebook URL if the user is logged in.
#                        DO NOT MISUSE IT FOR DISTURBING INDIVIDUALS.                    
# Date                 : 03/09/2017
# Update               : 12/31/2023
# Version              : 1.0.4
# Tested OS            : Windows 11, Windows 10, Windows 8.1, Windows 8
# Python Version       : Python 3

import pyautogui as pt
import webbrowser
import time


def give_a_like():
    try:
        pt.press('j')
        pt.press('l')
        pt.press('enter')
        return 1
    except Exception as ex:
        print(f"Error {str(ex)}")
    return 0


def facebook_autolike(url="https://www.facebook.com/", run_time=60):
    return_dict = {
        "status": "error",
        "message": "Error message in details.",
        "url": "",
        "like": 0,
        "time": 0
    }
    try:
        pt.moveTo(800, 250)
        start = time.time()
        webbrowser.open(url)
        time.sleep(2)
        cnt_like = 0
        elapsed_time = 0
        while True:
            cnt_like += give_a_like()
            time.sleep(1)
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


if __name__ == '__main__':
    print(facebook_autolike())
