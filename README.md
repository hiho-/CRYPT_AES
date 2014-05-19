CRYPT_AES
=========

CRYPT_AES is a plugin for [web2py framework](web2py.com).
This will encrypt the database field that you specify.


##PyCrypt

In order to run this plugin, [PyCrypto](https://pypi.python.org/pypi/pycrypto) module is required.

You can install it by using the pypi is PyCript but, compilation environment is required. 
For this reason, those who search for binary files, and is easy to install.

  example: <https://www.google.com/search?q=pycrypto+windows>

After installing the PyCript, and then set up to operate in web2py application.

###PyCrypt on Server

If you can not install the PyCript in such as a shared server, set it in such as copying to "site-packages" folder of web2py. Please consult the web2py for more information.

###PyCrypt on Google App Engine

You do not need to install any PyCrypt on GAE. It is necessary to __app.yaml__ of application, to add the following.

    libraries:
    - name: pycrypto
      version: latest
  

##How to use CRYPT_AES

Download the plugin file and upload it to the application.

For a table field that you want to encrypt, and then write the following in the model.

    from plugin_crypt_aes.crypt_aes import CRYPT_AES
    table = db.define_table('user_control',
        Field('name', 'string', notnull=True, unique=True),
        Field('access_id', 'string', notnull=True),
        Field('password', 'password'),
        format='%(name)s')
    table.access_id.requires=crypt_aes=CRYPT_AES()
    table.password.requires=crypt_aes

As a result, 'access_id' field and 'password' of 'user_control' table are encrypted and written to the database.

It is also possible to specify the encryption key.

    import os
    from plugin_crypt_aes.crypt_aes import CRYPT_AES
    table = db.define_table('user_control',
        Field('name', 'string', notnull=True, unique=True),
        Field('access_id', 'string', notnull=True),
        Field('password', 'password'),
        format='%(name)s')
    keyf = os.path.join(request.folder,'private','access_id.key')
    table.access_id.requires=CRYPT_AES(CRYPT_AES.get_or_create_key(keyf))
    table.password.requires=CRYPT_AES('master-key0123456789012345678901')

If you do not want to use the SQLTABLE and SQLFORM, encryption and decryption is not done automatically. At that time, you can use some methods such as the following.

* Field - validate
* Field - formatter
* Table - validate_and_insert
* Set   - validate_and_update
    
Please see also this article.

  blog : <http://blog1.erp2py.com/2012/05/web2py_28.html> (japanese)
