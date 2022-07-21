# helpers
Quick helper functions


### jwt_helper.py
This file contains a python class which provides a very simple JSON Web Tokens authentications. Basically it provides a wrapper on top of jwt and allows users to choose `secret` key and `hashing` algorithm for generating the tokens. It has two main methods `encode_payload` and `decode_token` which encodes a payload and decodes the payload respectively.

A main function is also written for the reference for users to let them know how to use this simple class