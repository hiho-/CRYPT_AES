#!/usr/bin/env python
# coding: utf8
from gluon import *
from Crypto.Cipher import AES
import base64
import os

class CRYPT_AES:
    '''
    example:
    
        from crypt_aes import CRYPT_AES
        db.define_table('example',
            Field('access_id', 'string', requires=CRYPT_AES()))
        
    Encode the value on validation to encrypt.
    Decode the encrypted value.
    '''
    block_size = 32
    block_size_list = (16, 24, 32)
    def __init__(self, key=None): 
        self.padding = '{'
        if key is None:
            key = CRYPT_AES.get_or_create_key()
        elif len(key) in self.block_size_list:
            self.block_size = len(key)       
        else:
            raise TypeError, "Key length is not allowed"
        self.cipher = AES.new(key)
    def __call__(self,value):
        value += (self.block_size - len(value) % self.block_size) * self.padding
        return (base64.b64encode(self.cipher.encrypt(value)), None)
    def formatter(self,value):
        try:
            return self.cipher.decrypt(base64.b64decode(value)).\
                                                        rstrip(self.padding)
        except:
            return None
                
    @classmethod
    def get_or_create_key(cls, filename=None, block_size=None):
        if block_size in cls.block_size_list:
            cls.block_size = block_size
        request = current.request
        if not filename:
            filename = os.path.join(request.folder,'private','validator.key')
        if os.path.exists(filename):
            key = base64.b64decode(open(filename,'r').read().strip())
        else:
            key = base64.b64encode(os.urandom(cls.block_size))
            open(filename,'w').write(key)
        return key
