from log import add_to_log
from flask import Flask, request
import json
from handle_dialog import handle_dialog

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def main():
    add_to_log("Info", f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(request.json, response)
    add_to_log("Info", f'Response:  {response!r}')
    return json.dumps(response)


if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        add_to_log("Warning", e)
