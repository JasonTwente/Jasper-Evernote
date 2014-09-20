import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

import sys
import time
import re

WORDS = ["NOTE"] 

PRIORITY = 1

def writeNote(mic,api):
	note = Types.Note()
	note.title = "Jasper Note"
	
# Jasper listens to the note of the user
	mic.say("What would you like me to write down?")
	NotetobeWrited = mic.activeListen()
	
# The content of an Evernote note is represented using Evernote Markup Language
# (ENML). The full ENML specification can be found in the Evernote API Overview
# at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
	note.content = '<?xml version="1.0" encoding="UTF-8"?>'
	note.content += '<!DOCTYPE en-note SYSTEM ' \
    '"http://xml.evernote.com/pub/enml2.dtd">'
	note.content += '<en-note>Note:<br/>'
	note.content += ' + NotetobeWrited + '
	note.content += '</en-note>'
	
# Finally, send the new note to Evernote using the createNote method
# The new Note object that is returned will contain server-generated
# attributes such as the new note's unique GUID.

	created_note = note_store.createNote(note)
	mic.say("I successfully wrote down your note.")
	
def handle(text, mic, profile):

# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action hollandtester123@live.com

	auth_token = "S=s1:U=8f7e3:E=14fe2136603:C=1488a6238f0:P=1cd:A=en-devtoken:V=2:H=61ef9345d462ebf92ffc5759ec1d0c9e"
	
	if auth_token == "your developer token":
    mic.say("Please, fill in your developer token")
    exit(1)
	
	client = EvernoteClient(token=auth_token, sandbox=True)
	user_store = client.get_user_store()
	user = userStore.getUser()

	if bool(re.search(r'\Note\b', text, re.IGNORECASE)):
		writeNote(mic, api)
		
def isValid(text):
	noteBool = bool(re.search(r'\Note\b', text, re.IGNORECASE))
	
	if noteBool:
		return noteBool
	else:
		return False
	
	
	
