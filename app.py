from flask import Flask, request, jsonify, abort

# The availabe languages 
greetings = {
            'en': 'hello', 
            'es': 'Hola', 
            'ar': 'مرحبا',
            'ru': 'Привет',
            'fi': 'Hei',
            'he': 'שלום',
            'ja': 'こんにちは'
            }

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # Get all the languages 
    @app.route('/greeting')
    def greeting_all():
        return jsonify({
            'greetings':greetings
            })

    # get a specific language 
    @app.route('/greeting/<lang>', methods=['GET'])
    def greeting_one(lang):
        print(lang)
        if(lang not in greetings):
            abort(404)
        return jsonify({'greeting': greetings[lang
        ]})

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success":False,
            "error":404,
            "message":"resource not found"
        }),404

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)