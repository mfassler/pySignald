
## Stand-alone server for Signal (encrypted text messaging)

This is a Python Tornado server that implements the bare minimum of the TextSecure API --
just enough to build a small chat service using Signal-Desktop for clients.

### Requires:

 * Python 2.7
 * Python-Tornado
 * protobufs
 * python-crypto
 * socat

### To use:

#### Server

Check out the settings in `config.py`.  Modify if needed.  Start the server:
```sh
python main.py
```


#### Client

Grab a copy of Signal Desktop from here:  https://github.com/WhisperSystems/Signal-Desktop

In Signal-Desktop, modify `js/background.js`. 

Change this:
```
var SERVER_URL = 'https://textsecure-service-staging.whispersystems.org';
```
to
```
var SERVER_URL = 'http://localhost:8123';
```
(or whereever your server is.  No trailing slash.)

Signal Desktop is a Chrome app:
 * Open Chrome. 
 * Go to:  chrome://extensions/
 * Enable "Developer Mode"
 * Load unpacked extension...
 * Navigate to Signal-Desktop and open that directory.

You should now see a blue page with "Welcome to Signal Desktop".  
Go into the JavaScript console:
 * Right-click on the page and go to "inspect"
 * a new window opens.  Click on the "Console" tab.

In the console, type this JavaScript:
```
extension.install('standalone');
```

... a new screen opens, prompting for a phone number and verification code.
(you might see a warning for "HTTP not connected".  That's okay for now.)

Back on your server, as a regular user, run this command:
```sh
socat STDIO UNIX-CONNECT:/tmp/pySignald.sock
```

... This will give you your phone number and verification code.  
Put this phone number and verification code into Signal Desktop, and click "Register"
("Call" and "Send SMS" do nothing.)

It might take a second or two for Signal to respond (it's generating keys), but then you should
be in.

### Multiple users:

Make a new Chrome profile, and a new user on your server, and repeat the steps above.  They
should be able to talk to each other.


License
---------------------

Copyright 2016 Mark Fassler

Licensed under the AGPLv3: https://www.gnu.org/licenses/agpl-3.0.html

