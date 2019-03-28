#!/usr/bin/python
# -*- coding: utf-8 -*-

class Generator_Tools(object):
	def __init__(self, type_payload, payload_code):
		self.identifier = type_payload
		self.payload = payload_code

	@property
	def main_generate(self):
		try:
			import base64
			code = {
				'author' : 'Mochammad Rizki (ReztDev)',
				'version' : '1.0.0',
				'module' : self.identifier,
				'description' : 'Payload Generator to encrypt code exploit',
				'payload' : base64.b64encode(self.payload)
			}

			execute = ("""
# Author by {author}                                     
# Modules payload: {module}                              
# Version: {versi}                                       
# Description: {descrip}
# => Payload Code = (
		{code}
	);""".format(author=code['author'], module=code['module'], versi=code['version'],
					descrip=code['description'], code=code['payload']))
			return execute
		except IOError:
			pass
