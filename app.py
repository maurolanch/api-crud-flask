from flask import Flask, request, jsonify



app = Flask('__name__')

albums = []

@app.route("/albums", methods=['POST'])
def create_album():
    
    data = request.get_json()

    new_album = {
        "id" : len(albums) + 1,
        "title": data.get("title"),
        "artist": data.get("artist")
    }

    albums.append(new_album)

    return jsonify(new_album), 201

@app.route("/albums", methods=['GET'])
def get_albums():

    return jsonify(albums), 200

@app.route("/albums/<int:id>", methods=['PUT'])
def update_album(id):
    data = request.get_json()
    for album in albums:
        if album['id'] == id:
            album['title'] = data.get('title', album['title'])
            album['artist'] = data.get('artist', album['artist'])
            return jsonify(album), 200
    return jsonify({'mensaje': 'Álbum no encontrado'}), 404

@app.route("/albums/<int:id>", methods=['DELETE'])
def delete_album(id):
    for album in albums:
        if album['id'] == id:
            albums.remove(album)
            return jsonify({'message': 'Album deleted'}), 200
    return jsonify({'message': 'Album not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)