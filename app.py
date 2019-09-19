from flask import Flask, request
from flask import jsonify
from instasentiments import getPublicProfileCaptions, getPrivateProfileCaptions, getSentiments

#Initializing our application
app = Flask(__name__)


#Route that sends the JSON response to the client
@app.route('/requestjson', methods=['POST','GET'])
def receiveSendJSON():
    if request.method == 'GET': #We want some data to be received by the server, hence we return an error if the method was GET
        return "<h1 style='color:red'> GET requests are not allowed, send some JSON data to this URL. </h1>"
    else:
        data = request.json # JSON received from the client
        if data['type'] == 'Public':
            login_id = data['login_id']
            print(login_id)
            result, profile_pic, full_name = getPublicProfileCaptions(login_id)

            print(full_name)
            if type(result) == str:
                return jsonify({
                    'Type':'Fail',
                    'Value': result
                })
            else:
                sentiments = getSentiments(result)
                if type(sentiments) == str:
                    return jsonify({
                        'Type': 'Fail',
                        'Value': sentiments,
                    })
                else:
                    return jsonify({
                        'Type': 'Success',
                        'Value': sentiments,
                        'Picture': profile_pic,
                        'Name': full_name
                    })

        elif data['type'] == 'Private':
            login_id = data['login_id']
            login_username = data['login_username']
            password = data['password']
            print(login_id)
            result, profile_pic, full_name = getPrivateProfileCaptions(login_id, login_username, password)
            if type(result) == str:
                return jsonify({
                    'Type': 'Fail',
                    'Value': result
                })
            else:
                sentiments = getSentiments(result)
                if type(sentiments) == str:
                    return jsonify({
                        'Type': 'Fail',
                        'Value': sentiments
                    })
                else:
                    return jsonify({
                        'Type': 'Success',
                        'Value': sentiments,
                        'Picture': profile_pic,
                        'Name': full_name
                    })


if __name__ == '__main__':
    app.run(debug=False,threaded=False)
