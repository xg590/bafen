* Flask
```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "FrontPage"

app.run() 
```
* mitmproxy load addons.py (it is loaded in real-time, any change to the addons.py will be applied instantly)
``` 
cat << EOF > addons.py
import time, logging
from mitmproxy.script import concurrent
 
@concurrent # This decorator allows all requests run concurrently.
# If the decorator is removed, the first request will block the second,
# which means the second request will takes 10 seconds to be finished.
def request(flow): # The is a Event Hook. 
    # Full hook list @ https://docs.mitmproxy.org/stable/api/events.html
    time.sleep(5)  # Delay the request by 5 second
EOF

mitmproxy --set console_eventlog_verbosity=error --listen-host 0.0.0.0 -s addons.py
```
* Press <kbd>Shift</kbd>+<kbd>E</kbd> to see Event log.
* CURL
```
curl --proxy "http://127.0.0.1:8080" -v 127.0.0.1:5000
```