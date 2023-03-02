import flask, requests, pandas, threading, os, logging
app = flask.Flask(__name__)
@app.route("/")
def index():
    return "FrontPage"

play_list = {}
@app.route("/play_list", methods=['POST'])
def play_list():
    req = flask.request
    global play_list
    play_list = {e['vid']:e['title'] for e in req.json['data']['articles']}
    pandas.DataFrame(tuple(play_list.items()), columns=['vid','title']).to_csv('audio/list.csv', index=False)
    return ''

@app.route("/audio_file_url", methods=['POST'])
def audio_file_url():
    req           = flask.request
    Vid           = req.json['Result']['Vid']
    Format        = req.json['Result']['PlayInfoList'][0]['Format']
    filename      = f'audio/{Vid}.{Format}'
    MainPlayUrl   = req.json['Result']['PlayInfoList'][0]['MainPlayUrl']
    BackupPlayUrl = req.json['Result']['PlayInfoList'][0]['BackupPlayUrl']
    if os.path.exists(filename):
        print('Existed', filename, play_list[Vid])
        return ''
    else:
        print('New',     filename, play_list[Vid])
        threading.Thread(target=downloader, args=(filename, MainPlayUrl, BackupPlayUrl),
                         name='thread-1', daemon=True).start()
        return ''

def downloader(filename, MainPlayUrl, BackupPlayUrl):
    #print(filename, MainPlayUrl, BackupPlayUrl)
    resp = requests.get(MainPlayUrl)
    if resp.status_code == 200:
        with open(filename, 'wb') as fw:
            fw.write(resp.content)
        return
    else:
        resp = requests.get(BackupPlayUrl)
        if resp.status_code == 200:
            with open(filename, 'wb') as fw:
                fw.write(resp.content)
            return
        else:
            return

logging.getLogger('werkzeug').disabled = True
app.run(debug=False)