import os
from flask import Flask, request, abort, jsonify, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_, and_, not_, asc, desc
from flask_cors import CORS
import random
from datetime import datetime, timedelta
import mishkal.tashkeel
from werkzeug import secure_filename

from models import setup_db, MyUser, Message, Avatar,db

import io

QUESTIONS_PER_PAGE = 10



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    
    '''
    @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app, resources={r"/*": {'origins': '*'}})
    

    '''
    @DONE: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response


    @app.route('/shakkelha', methods=['POST'])
    def shakkel():
        body = request.get_json()
        text = body.get('text', 'No text')
        vocalizer = mishkal.tashkeel.TashkeelClass()
        result = vocalizer.tashkeel(text)
        return jsonify(
            {
                "text-result": result
            }
        )


    '''
    DONE: Create user OK
    '''
    @app.route('/users', methods=['POST'])
    def create_user():
        ''' 
        expected_body_for_user = {
            'name' : "name",
            'phone' : "phone",
            'email' : "email",
            'language' : "language",
            'country' : "country"
            "password": "password",
            "gender" : "gender"

        }
        '''
        error = False
        body = request.get_json()
        new_name = body.get('name', None)
        new_phone = body.get('phone', None)
        new_email = body.get('email', None)
        new_language = body.get('language', None)
        new_country = body.get('country', None)
        new_password = body.get('password', None)
        new_gender = body.get('gender', None)
        returned = {}


        try:
            existed_user = MyUser.query.filter(MyUser.email == new_email).one_or_none()
            if existed_user is not None:
                return jsonify({"exist":True,"success":False})
            user=MyUser(
                new_name, 
                new_phone, 
                new_email, 
                new_language, 
                new_country,
                new_password,
                new_gender
                )
            # print("before insert")
            user.insert()
            # print("after insert")
            returned = user.format()
        except Exception as e:
            return str(e)
            error = True

            # Question.rollback()
            # print(sys.exc_info())
        # finally:
        #     Question.close()
        if error:
            abort(422)
        else:
            return jsonify(returned)


    '''
    DONE: Create message OK
    '''
    @app.route('/messages', methods=['POST'])
    def create_message():
        '''
        expected_body_for_message = {
            'id': id,
            'text': text,
            'translatedtext': translatedtext,
            'moshakkaltext': moshakkaltext
            'sender_id' :id,
            'receiver_id' : id
        }
        '''
        error = False
        body = request.get_json()
        text = body.get('text', None)
        translatedtext = body.get('translatedtext', None)
        moshakkaltext = body.get('moshakkaltext', None)
        sender_id = body.get('sender_id', None)
        receiver_id = body.get('receiver_id', None)


        returned = {}
        try:
            sender_obj = MyUser.query.filter(MyUser.id == sender_id).one_or_none()
            receiver_obj = MyUser.query.filter(MyUser.id == receiver_id).one_or_none()
            if sender_obj is None or receiver_obj is None:
                abort(404)
                # return jsonify({
                #     "result" : "not found"
                # })
            msg=Message(
                text, 
                translatedtext, 
                moshakkaltext,
                )
            msg.sender = sender_obj
            msg.receiver = receiver_obj
            msg.insert()
            returned = msg.format()
        except Exception as e:
            return str(e)
            error = True
            # Question.rollback()
            # print(sys.exc_info())
        # finally:
        #     Question.close()
        if error:
            abort(422)
        else:
            return jsonify(returned)

    '''
    DONE: Get mesages OK
    '''
    @app.route('/messages/firstuserid/<int:firstuserid>/seconduserid/<int:seconduserid>')
    def get_usr_msgs(firstuserid, seconduserid):
        #selection = Message.query.filter(or_(and_(Message.sender_id==firstuserid, Message.receiver_id==seconduserid),and_(Message.receiver_id==firstuserid, Message.sender_id==seconduserid))).order_by(desc(Message.timedt)).all()
        
        selection = Message.query.filter(and_(Message.receiver_id==firstuserid, Message.sender_id==seconduserid)).order_by(asc(Message.timedt)).all()

        # firstuser id is the id of the one who request this endpoint so i will return the message for sended to only
        # total_size = len(selection)

        # if total_size==0:
        #     abort(404)
        return single_msg_burst(selection)

    def single_msg_burst(selection, is_jsonified=True):
        msgs = []
        # returned_json = jsonify([msg.format() for msg in selection ])
        for msg in selection:
            msgs.append(msg.format())
            db.session.delete(msg)
        db.session.commit()
        if is_jsonified:
            return jsonify(msgs)
        else:
            return msgs

    '''
    DONE: Get receiver mesages OK
    '''
    @app.route('/messages/receiver/<int:receiver_id>')
    def get_receiver_msgs(receiver_id, is_jsonified=True):
        #selection = Message.query.filter(or_(and_(Message.sender_id==firstuserid, Message.receiver_id==seconduserid),and_(Message.receiver_id==firstuserid, Message.sender_id==seconduserid))).order_by(desc(Message.timedt)).all()
        
        selection = Message.query.filter(Message.receiver_id==receiver_id).order_by(asc(Message.timedt)).all()

        # firstuser id is the id of the one who request this endpoint so i will return the message for sended to only

        # if total_size==0:
        #     abort(404)
        return single_msg_burst(selection, is_jsonified)
        
        
    @app.route('/messages/messages')
    def get_all_msgs():
        selection = Message.query.order_by(desc(Message.timedt)).all()

        # firstuser id is the id of the one who request this endpoint so i will return the message for sended to only
        total_size = len(selection)

        # if total_size==0:
        #     abort(404)
        returned_json = jsonify([msg.format() for msg in selection ])
        
        return returned_json


    '''
    TODO: Get messages by receiver id
    '''

    '''
    TODO: Get messages by user
    '''

    '''
    DONE: Delete message OK
    '''
    @app.route('/messages/<int:id>', methods=['DELETE'])
    def delete_msg(id):
        success = True
        returned = {}
        try:
            msg = Message.query.filter(Message.id == id).one_or_none()
            if msg is not None:
                # abort(404)
                # return jsonify({
                #     "result" : "not found"
                # })
                msg.delete() 
            returned["success"] = True
            returned["deleted"] = id
        except Exception as e:
            return str(e)
            error = True
            # Question.rollback()
        # finally:
            # Question.close()
        if success:
            return jsonify(returned)
        else:
            abort(422)
            
            '''
    DONE: Delete user OK
    '''
    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_usr(id):
        success = True
        returned = {}
        try:
            usr = MyUser.query.filter(MyUser.id == id).one_or_none()
            if usr is None:
                abort(404)
                # return jsonify({
                #     "result" : "not found"
                # })
            usr.delete() 
            try:
                delete_user_photo(id)
            except Exception as e:
                photo_error = True
            returned["success"] = True
            returned["deleted"] = usr.id
        except Exception as e:
            return str(e)
            error = True
            # Question.rollback()
        # finally:
            # Question.close()
        if success:
            return jsonify(returned)
        else:
            abort(422)


    '''
    DONE: Get users OK
    '''
    @app.route('/users')
    def get_users(is_jsonified = True):
        # user last update before 5 sec will be rejected
        delta_sec = int(os.getenv('ACTIVITY_THRESHOLD_SECONDS', 5))
        dttime_threshold = datetime.now() - timedelta(hours=0, minutes=0, seconds=delta_sec)
        selection = MyUser.query.order_by(MyUser.id).all()


        # if total_size==0:
        #     abort(404)
        users = [usr.format_special(dttime_threshold) for usr in selection ]
        if is_jsonified:
            return jsonify(users)
        else:
            return users

    '''
    DONE: Ping to update user last active time OK
    '''
    @app.route('/users/ping/<int:id>')
    def ping_user(id):
        success = True
        returned = {}
        try:
            user = MyUser.query.filter(MyUser.id == id).one_or_none()
            if user is None:
                abort(404)
                # return jsonify({
                #     "result" : "not found"
                # })
            user.update() 
            returned["success"] = True
            returned["id"] = user.id
        except Exception as e:
            return str(e)
            success = False
            # Question.rollback()
        # finally:
            # Question.close()
        if success:
            return jsonify(returned)
        else:
            abort(422)

    '''
     DONE: Ping overloaded return all required information
    '''
    @app.route('/users/ping/overloaded/<int:id>')
    def ping_user_overloaded(id):
        success = True
        returned = {}
        try:
            user = MyUser.query.filter(MyUser.id == id).one_or_none()
            if user is None:
                abort(404)
                # return jsonify({
                #     "result" : "not found"
                # })
            user.update() 
            returned["success"] = True
            returned["id"] = user.id
            is_jsonified = False
            returned['users'] = get_users(is_jsonified)
            returned['messages'] = get_receiver_msgs(id, is_jsonified)
        except Exception as e:
            return str(e)
            success = False
            # Question.rollback()
        # finally:
            # Question.close()
        if success:
            return jsonify(returned)
        else:
            abort(422)
            
    '''
    DONE: Login
    '''
    @app.route('/users/login',  methods=['POST'])
    def login_user():
        success = True
        body = request.get_json()
        email = body.get('email', None)
        password = body.get('password', None)
        returned = {}
        if email is None or password is None:
            return jsonify({"success" : False})
        try:
            user = MyUser.query.filter(and_(MyUser.email == email , MyUser.password == password)).one_or_none()
            if user is None:
                return jsonify({"success" : False})
            else:
                return jsonify({"success" : True , "user" : user.format()})
            user.update() 
            returned["success"] = True
        except Exception as e:
            return str(e)
            success = False
            # Question.rollback()
        # finally:
            # Question.close()
        if success:
            return jsonify(returned)
        else:
            abort(422)

    # @app.route('/users/photo/upload/<int:id>', methods = ['GET', 'POST'])
    # def upload_user_photo(id):
    #     print(id)
    #     filename = str(id)+".png"
    #     f = request.files['file']
    #     full_filename =  os.path.join(app.root_path+'/UPLOAD_FOLDER/', filename)
    #     f.save(full_filename)
    #     return jsonify({
    #             "result" : "successful"
    #     })


    # @app.route('/users/photo/download/<int:id>', methods=['GET', 'POST'])
    # def download_user_photo(id):
    #     filename = str(id)+".png"
    #     uploads = os.path.join(app.root_path+'/UPLOAD_FOLDER')
    #     return send_from_directory(directory=uploads, filename=filename)

    
    # @app.route('/users/photo/delete/<int:id>', methods=['DELETE'])
    # def delete_user_photo(id):
    #     try:
    #         filename = str(id)+".png"
    #         os.remove(os.path.join(app.root_path+'/UPLOAD_FOLDER/' , filename))
    #         return jsonify({
    #             "result" : "successful"
    #         })
    #     except Exception as e:
    #         abort(404)



    @app.route('/users/photo/upload/<int:id>', methods = ['GET', 'POST'])
    def upload_user_photo(id):
        try:
            delete_user_photo(id)
            f = request.files['file']
            avatar = Avatar(id,f.read())
            avatar.insert()
            # with db.engine.connect() as connection:
            #     res = connection.execute(
            #         '''INSERT INTO avatar (id, image) VALUES (%s,%s)''', 
              
            #         (id, f.read() ))

            return jsonify({
                "result" : "successful"
            })
        except Exception as e:
            # return jsonify({
            #     "result" : str(e)
            # })
            abort(422)


    @app.route('/users/photo/download/<int:id>', methods=['GET', 'POST'])
    def download_user_photo(id):
        try:
            avatar = Avatar.query.filter(Avatar.id == id).one_or_none()
            if avatar is None:
                abort(404)
            filename = "temporaryavatar.png"
            full_filename =  os.path.join(app.root_path+'/UPLOAD_FOLDER/', filename)
            f = open(full_filename, "wb")
            f.write(avatar.image)
            f.close()
            uploads = os.path.join(app.root_path+'/UPLOAD_FOLDER')
            return send_from_directory(directory=uploads, filename=filename)
            # return avatar.image
        except Exception as e:
            # return jsonify({
            #     "result" : str(e)
            # })
            abort(404)


    
    @app.route('/users/photo/download/withid/<int:id>', methods=['GET', 'POST'])
    def download_user_photo_json(id):
        try:
            avatar = Avatar.query.filter(Avatar.id == id).one_or_none()
            if avatar is None:
                abort(404)
            filename = "temporaryavatar.png"
            full_filename =  os.path.join(app.root_path+'/UPLOAD_FOLDER/', filename)
            f = open(full_filename, "wb")
            f.write(avatar.image)
            f.close()
            uploads = os.path.join(app.root_path+'/UPLOAD_FOLDER')
            image = send_from_directory(directory=uploads, filename=filename)
            image.headers['id'] = id
            return image
            # return jsonify(
            #     {
            #         "id" : id,
            #         "image" : image
            #     }
            # )
            # return avatar.image
        except Exception as e:
            # return jsonify({
            #     "result" : str(e)
            # })
            abort(404)

    
    @app.route('/users/photo/delete/<int:id>', methods=['DELETE'])
    def delete_user_photo(id):
        try:
            avatar = Avatar.query.filter(Avatar.id == id).one_or_none()
            if avatar is not None:
                avatar.delete()
            # with db.engine.connect() as connection:
            #     res = connection.execute(
            #         '''DELETE FROM avatar WHERE id=%s''', 
            #         (id))
            return jsonify({
                "result" : "successful"
            })
        except Exception as e:
            # return jsonify({
            #     "result" : str(e)
            # })
            abort(404)




    @app.route('/download/tts/key', methods=['GET'])  #Get key
    def download_key():
        try:
            filename = 'key.google'
            full_filename =  os.path.join(app.root_path+'/auth', filename)
            f = open(full_filename, "r")
            key = f.readline()
            f.close()
            return jsonify({'key':key[0:len(key)-1]})
        except Exception as e:
            # return jsonify({
            #     "key" : key
            # })
            abort(404)


    @app.route('/download/asr/clientkey', methods=['GET'])  #Get key
    def download_clientkey():
        try:
            filename = 'clientkey.google'
            dir = os.path.join(app.root_path+'/auth')
            parcel = send_from_directory(directory=dir, filename=filename)
            return parcel
        except Exception as e:
            # return jsonify({
            #     "key" : key
            # })
            abort(404)





    '''
    @DONE: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found",
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable",
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request",
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed",
        }), 405
    
    return app

        
