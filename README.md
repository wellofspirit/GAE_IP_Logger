# IP Logger
A simple GAE based IP Logger application

## Features
- [x] Returns caller's IP
- [x] Stores caller's IP to data store if header matches
- [x] Returns the IP info for given ID of IP
- [x] Systemd configuration file for periodically updating

## Before Deploy
1. Remember to replace ```{PUT_YOUR_KEY_HERE}``` in ```main.py``` and ```logip.service``` by your key.
2. Replace ```{DOMAIN}``` and ```{IP_OWNER}``` by your domain and the id of IP you like.

## Commands
### Deploy
```
$ cd gapp
$ gcloud app deploy -v {VERSION_TEXT}
```
If you do not specify **VERSION_TEXT**, GAE will automatically creates a new version. Which will run another instance for you. This will quickly burn out your daily free quota.
