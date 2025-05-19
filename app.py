from flask import Flask, request, jsonify



app = Flask('__name__')

albums = []

@app.route("/albums",methods=['POST'])
def create_album():
    
    data = request.get_json()

    new_album = {
        "id" : len(albums) + 1,
        "title": data.get("title"),
        "artist": data.get("artist")
    }

    albums.append(new_album)

    return jsonify(new_album), 201

@app.route("/albums",methods=['GET'])
def get_albums():

    return jsonify(albums), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)