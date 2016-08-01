# AdmiPaste
A pastebin made in Python and Flask

## Requirements
* Python 2
* Flask
* MySQL-python
* pyyaml

(also available in requirements.txt)

## API Documentation

###`/api/submit` *POST*
* **user** (optional), **paste**, **language** (optional)*

Submits a paste

###`/api/pastes` *GET*

Get newest 20 pastes

###`/api/pastes/<id>` *GET*

Get specific paste