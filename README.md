# IP Logger
A simple GAE based IP Logger application

## Features
- [x] Returns caller's IP
- [x] Stores caller's IP to data store if header matches
- [x] Returns the IP info for given ID of IP
- [x] Systemd configuration file for periodically updating

## Commands
### Deploy
```
$ cd gapp
$ gcloud app deploy -v {VERSION_TEXT}
```
If you do not specify **VERSION_TEXT**, GAE will automatically creates a new version. Which will run another instance for you. This will quickly burn out your daily free quota.
