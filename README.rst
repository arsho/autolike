AutoLike
========

|Build Status| |Version| |Python| |Size| |Codecov|

Automatically like any given Facebook URL if the user is logged in.
The facebook(url, run_time) method takes a Facebook URL and run time in seconds.
It will return a dictionary with status, message, url, like and time attribute.
If the status has "success" value then the program is successfully completed.

DO NOT MISUSE IT FOR DISTURBING INDIVIDUALS.

The current version is tested on Windows(8) and Windows(10). It does not support Linux based OS.

Installation
~~~~~~~~~~~~

We recommend install ``autolike`` through pip install using Python 3.

.. code:: bash

    $ pip install autolike

Example
~~~~~~~

To use (with caution), simply do:

.. code:: python

    import autolike
    url = "https://www.facebook.com/" # any Facebook URL
    run_time = 100 # time in seconds
    like_result_dict = autolike.facebook(url, run_time)
    print(like_result_dict)


BEFORE RUNNING THE PROGRAM, YOU NEED TO BE LOGGED IN TO FACEBOOK USING YOUR DEFAULT BROWSER.
	
Contribute
~~~~~~~~~~

Create Github Pull Request https://github.com/arsho/autolike/pulls

If you have suggestion use GitHub issue system or send a message in Facebook https://www.facebook.com/ars.shovon.

.. |Build Status| image:: https://travis-ci.org/arsho/autolike.svg?branch=master
   :target: https://travis-ci.org/arsho/autolike

.. |Version| image:: https://img.shields.io/pypi/v/autolike.svg?
   :target: http://badge.fury.io/py/autolike
   
.. |Python| image:: https://img.shields.io/pypi/pyversions/autolike.svg?
   :target: https://pypi.python.org/pypi/autolike/0.0.4
      
.. |Size| image:: https://img.shields.io/github/size/arsho/autolike/autolike/__init__.py.svg?
   :target: https://github.com/arsho/autolike/   
   
.. |Codecov| image:: https://codecov.io/github/arsho/autolike/coverage.svg?branch=master
   :target: https://codecov.io/github/arsho/autolike      