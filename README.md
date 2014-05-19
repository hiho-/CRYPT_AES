CRYPT_AES
=========

CRYPT_AES is a plugin for [web2py framework](web2py.com).
This will encrypt the database field that you specify.


#PyCrypt

In order to run this plugin, [PyCrypto](https://pypi.python.org/pypi/pycrypto) module is required.

You can install it by using the pypi is PyCript but, compilation environment is required. 
For this reason, those who search for binary files, and is easy to install.

  example: <https://www.google.com/search?q=pycrypto+windows>

After installing the PyCript, and then set up to operate in web2py application.

This is a file of PyCrypt that is installed on the python, set it in such as copying to "site-packages" folder of web2py. Please consult the web2py for more information.

##PyCrypt on Google App Engine

You do not need to install any PyCrypt on GAE. It is necessary to __app.yaml__ of application, to add the following.

    libraries:
    - name: pycrypto
      version: latest
  

    
    
    
