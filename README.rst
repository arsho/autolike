AutoLike
========

|Version| |Python| |Size|

Automatically like any given Facebook URL if the user is logged in.
The facebook(url, run_time) method takes a Facebook URL and run time in seconds.
It will return a dictionary with status, message, url, like and time attribute.
If the status has "success" value then the program is successfully completed.

DO NOT MISUSE IT FOR DISTURBING INDIVIDUALS.

The current version is tested on Windows 11, Windows 10, and Windows 8.

Requirement
~~~~~~~~~~~

Login to Facebook using your default browser and turn on the keyboard shortcuts in Facebook:

1. Click your profile picture in the top right of Facebook.
2. Click *Display and accessibility*, then *Keyboard*.
3. Click *On* below Use single-character keyboard shortcuts.

Installation
~~~~~~~~~~~~

``autolike`` only supports Python 3. Install it using pip.

.. code:: bash

    $ pip install autolike

Example
~~~~~~~

To use (with caution), simply do:

.. code:: python

    import autolike
    url = "https://www.facebook.com/" # any Facebook URL
    run_time = 30 # time in seconds
    like_result_dict = autolike.facebook_autolike(url, run_time)
    print(like_result_dict)

Demonstration video: https://youtu.be/OLQNz0mbJg4

Development
~~~~~~~~~~~

You can build the code by yourself in any Windows 8/8.1/10/11 machine that has Python 3 installed.
For development purpose we recommend to use a virtual environment.

.. code:: bash

    $ python -m venv venv --clear
    $ venv\Scripts\activate
    $ pip install -r requirements.txt
    $ python autolike\__init__.py

Contribute
~~~~~~~~~~

Create Github Pull Request https://github.com/arsho/autolike/pulls

If you have suggestion use GitHub issue system or send a message in Facebook https://www.facebook.com/ars.shovon.


.. |Version| image:: https://img.shields.io/pypi/v/autolike.svg?
   :target: http://badge.fury.io/py/autolike
   
.. |Python| image:: https://img.shields.io/pypi/pyversions/autolike.svg?
   :target: https://pypi.python.org/pypi/autolike/1.0.1
      
.. |Size| image:: https://img.shields.io/github/size/arsho/autolike/autolike/__init__.py.svg?
   :target: https://github.com/arsho/autolike/   
   