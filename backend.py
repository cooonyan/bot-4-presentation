from flask import Flask, abort
import os

app = Flask(__name__)

@app.route('/<int:guild_id>', methods=['GET'])
def serve_log(guild_id):
    file_path = f'cache/{guild_id}.cache'
    if not os.path.exists(file_path):
        abort(404)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return f"""
    <html>
        <body>
            <pre>{content}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
