AutoLike
--------
Automatically like any given Facebook URL if the user is logged in.
The facebook(url, run_time) method takes a Facebook URL and run time in seconds.
It will return a dictionary with status, message, url, like and time attribute.
If the status has "success" value then the program is successfully completed.

DO NOT MISUSE IT FOR DISTURBING INDIVIDUALS.

The current version is tested on Windows(10) and Ubuntu(16.04 LTS).

To install (in Ubuntu having both Python2 and Python3 by default)::

    >>> sudo pip3 install autolike

To install (in Windows with which has only Python 3 installed)::

    >>> sudo pip install autolike

To use (with caution), simply do::

    import autolike
	url = "https://www.facebook.com/" #any Facebook URL
	run_time = 200	
    like_result_dict = autolike.facebook(url, run_time)

BEFORE RUNNING THE PROGRAM, YOU NEED TO BE LOGGED IN TO FACEBOOK USING YOUR DEFAULT BROWSER.
	