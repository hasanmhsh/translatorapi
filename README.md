# Translated voice calls and chats final project
This is the backend source code of omac final project by hasan.mohamed to provide required database endpoints restful api for translated voice calls and chat android application
This project is developed using python flask frame work and postgres database.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 


## Getting Started

### Pre-requisites and Local Development 
Developers who will use this project must have Python3 and pip and node installed on their workstations.

#### Backend

First you must install back end dependence , in backend folder type this command in shell
`pip install requirements.txt`

To run the app execute the following command
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

These commands setup the application in development mode and use `__init__.py` 

application is running on `http://127.0.0.1:5000/` by default and is a proxy on the frontend settings. 



First time neglect dropdb command. 

## API Reference

### Getting Started
- Base URL: backend app is running by default on this endpoint, `http://127.0.0.1:5000/`, which is s proxy in the frontend settings. 


### Error Handling
Errors are issued in JSON format as following:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
API will issue three error types at failure:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 

### Endpoints 
#### GET /users
- General:
    - Returns a list of user json objects
- Sample: `curl http://127.0.0.1:5000/users`
``` 
[
    {
        "country": null,
        "email": "hasan.mh.sh@gmail.com",
        "gender": null,
        "id": 15,
        "isactive": false,
        "language": "Arabic",
        "lastactivetimedt": "Tue, 16 Nov 2021 13:16:58 GMT",
        "name": "حسن محمد",
        "phone": ""
    },
    {
        "country": null,
        "email": "wwws.5566@gmail.com",
        "gender": null,
        "id": 16,
        "isactive": false,
        "language": "Arabic",
        "lastactivetimedt": "Sat, 13 Nov 2021 22:50:42 GMT",
        "name": "Hossam Mohamed",
        "phone": ""
    },
    {
        "country": null,
        "email": "abdullah.mohamed2004006@gmail.com",
        "gender": null,
        "id": 18,
        "isactive": false,
        "language": "Arabic",
        "lastactivetimedt": "Sat, 13 Nov 2021 23:40:34 GMT",
        "name": "Abdullah",
        "phone": ""
    },
    {
        "country": null,
        "email": "m.ali.younus2261@gmail.com",
        "gender": null,
        "id": 19,
        "isactive": false,
        "language": "English",
        "lastactivetimedt": "Sun, 14 Nov 2021 21:59:10 GMT",
        "name": "Mohamed Ali Younus",
        "phone": ""
    },
    {
        "country": null,
        "email": "abdulrahman.mohamed201747@gmail.com",
        "gender": null,
        "id": 20,
        "isactive": false,
        "language": "French",
        "lastactivetimedt": "Sun, 14 Nov 2021 11:09:04 GMT",
        "name": "Abdulrahman",
        "phone": ""
    },
    {
        "country": null,
        "email": "boody.6644@yahoo.com",
        "gender": null,
        "id": 21,
        "isactive": false,
        "language": "Arabic",
        "lastactivetimedt": "Sun, 14 Nov 2021 10:46:01 GMT",
        "name": "Boody",
        "phone": ""
    },
    {
        "country": null,
        "email": "boody.664hx4@yahoo.com",
        "gender": null,
        "id": 22,
        "isactive": false,
        "language": "English",
        "lastactivetimedt": "Sun, 14 Nov 2021 13:50:30 GMT",
        "name": "Abdlh.M",
        "phone": ""
    },
    {
        "country": null,
        "email": "hasan_m19@yahoo.com",
        "gender": null,
        "id": 23,
        "isactive": false,
        "language": "English",
        "lastactivetimedt": "Sun, 14 Nov 2021 13:50:35 GMT",
        "name": "Hasan M.Sh",
        "phone": ""
    },
    {
        "country": null,
        "email": "seif56544.455@yahoo.com",
        "gender": null,
        "id": 24,
        "isactive": false,
        "language": "Italian",
        "lastactivetimedt": "Sun, 14 Nov 2021 18:57:54 GMT",
        "name": "Seif m",
        "phone": ""
    },
    {
        "country": null,
        "email": "mostafa45.mb75@gmail.com",
        "gender": null,
        "id": 25,
        "isactive": false,
        "language": "Chinese",
        "lastactivetimedt": "Sun, 14 Nov 2021 16:20:58 GMT",
        "name": "Mostafa",
        "phone": ""
    },
    {
        "country": null,
        "email": "jimmy.jjj13645@gmail.com",
        "gender": null,
        "id": 26,
        "isactive": false,
        "language": "Czech",
        "lastactivetimedt": "Sun, 14 Nov 2021 18:51:25 GMT",
        "name": "Jimmy",
        "phone": ""
    },
    {
        "country": null,
        "email": "karim.ahmed55535@gmail.com",
        "gender": null,
        "id": 27,
        "isactive": false,
        "language": "Russian",
        "lastactivetimedt": "Sun, 14 Nov 2021 20:02:11 GMT",
        "name": "Karim Ahmed",
        "phone": ""
    },
    {
        "country": null,
        "email": "sv464356533@yahoo.com",
        "gender": null,
        "id": 28,
        "isactive": false,
        "language": "Dutch",
        "lastactivetimedt": "Sun, 14 Nov 2021 20:02:29 GMT",
        "name": "Seira Von",
        "phone": ""
    },
    {
        "country": null,
        "email": "ahmedtest67235423@gmail.com",
        "gender": null,
        "id": 31,
        "isactive": false,
        "language": "Arabic",
        "lastactivetimedt": "Mon, 15 Nov 2021 19:24:59 GMT",
        "name": "Ahmed for test",
        "phone": ""
    },
    {
        "country": null,
        "email": "johntest6723546@gmail.com",
        "gender": null,
        "id": 32,
        "isactive": false,
        "language": "English",
        "lastactivetimedt": "Mon, 15 Nov 2021 19:24:23 GMT",
        "name": "John for test",
        "phone": ""
    }
]
```

#### GET /users/ping/overloaded/2
- General:
    - Returns a list of all user objects
    - Results a list of unread messages for user with {id} value. 
- Sample: `curl http://127.0.0.1:5000/users/ping/overloaded/19`

``` 
{
    "id": 19,
    "messages": [
        {
            "id": 613,
            "moshakkaltext": null,
            "receiver_id": 19,
            "sender_id": 15,
            "text": "اهلا بك يا صديقي",
            "timedt": "Mon, 15 Nov 2021 12:30:45 GMT",
            "translatedtext": "Hey, buddy. "
        },
        {
            "id": 633,
            "moshakkaltext": null,
            "receiver_id": 19,
            "sender_id": 15,
            "text": "اهلا بك يا صديقي كيف حالك",
            "timedt": "Tue, 16 Nov 2021 13:16:48 GMT",
            "translatedtext": "Hey, buddy. How you doing? "
        }
    ],
    "success": true,
    "users": [
        {
            "country": null,
            "email": "hasan.mh.sh@gmail.com",
            "gender": null,
            "id": 15,
            "isactive": false,
            "language": "Arabic",
            "lastactivetimedt": "Tue, 16 Nov 2021 13:16:58 GMT",
            "name": "حسن محمد",
            "phone": ""
        },
        {
            "country": null,
            "email": "wwws.5566@gmail.com",
            "gender": null,
            "id": 16,
            "isactive": false,
            "language": "Arabic",
            "lastactivetimedt": "Sat, 13 Nov 2021 22:50:42 GMT",
            "name": "Hossam Mohamed",
            "phone": ""
        },
        {
            "country": null,
            "email": "abdullah.mohamed2004006@gmail.com",
            "gender": null,
            "id": 18,
            "isactive": false,
            "language": "Arabic",
            "lastactivetimedt": "Sat, 13 Nov 2021 23:40:34 GMT",
            "name": "Abdullah",
            "phone": ""
        },
        {
            "country": null,
            "email": "m.ali.younus2261@gmail.com",
            "gender": null,
            "id": 19,
            "isactive": true,
            "language": "English",
            "lastactivetimedt": "Tue, 16 Nov 2021 14:11:27 GMT",
            "name": "Mohamed Ali Younus",
            "phone": ""
        },
        {
            "country": null,
            "email": "abdulrahman.mohamed201747@gmail.com",
            "gender": null,
            "id": 20,
            "isactive": false,
            "language": "French",
            "lastactivetimedt": "Sun, 14 Nov 2021 11:09:04 GMT",
            "name": "Abdulrahman",
            "phone": ""
        },
        {
            "country": null,
            "email": "boody.6644@yahoo.com",
            "gender": null,
            "id": 21,
            "isactive": false,
            "language": "Arabic",
            "lastactivetimedt": "Sun, 14 Nov 2021 10:46:01 GMT",
            "name": "Boody",
            "phone": ""
        },
        {
            "country": null,
            "email": "boody.664hx4@yahoo.com",
            "gender": null,
            "id": 22,
            "isactive": false,
            "language": "English",
            "lastactivetimedt": "Sun, 14 Nov 2021 13:50:30 GMT",
            "name": "Abdlh.M",
            "phone": ""
        },
        {
            "country": null,
            "email": "hasan_m19@yahoo.com",
            "gender": null,
            "id": 23,
            "isactive": false,
            "language": "English",
            "lastactivetimedt": "Sun, 14 Nov 2021 13:50:35 GMT",
            "name": "Hasan M.Sh",
            "phone": ""
        },
        {
            "country": null,
            "email": "seif56544.455@yahoo.com",
            "gender": null,
            "id": 24,
            "isactive": false,
            "language": "Italian",
            "lastactivetimedt": "Sun, 14 Nov 2021 18:57:54 GMT",
            "name": "Seif m",
            "phone": ""
        },
        {
            "country": null,
            "email": "mostafa45.mb75@gmail.com",
            "gender": null,
            "id": 25,
            "isactive": false,
            "language": "Chinese",
            "lastactivetimedt": "Sun, 14 Nov 2021 16:20:58 GMT",
            "name": "Mostafa",
            "phone": ""
        },
        {
            "country": null,
            "email": "jimmy.jjj13645@gmail.com",
            "gender": null,
            "id": 26,
            "isactive": false,
            "language": "Czech",
            "lastactivetimedt": "Sun, 14 Nov 2021 18:51:25 GMT",
            "name": "Jimmy",
            "phone": ""
        },
        {
            "country": null,
            "email": "karim.ahmed55535@gmail.com",
            "gender": null,
            "id": 27,
            "isactive": false,
            "language": "Russian",
            "lastactivetimedt": "Sun, 14 Nov 2021 20:02:11 GMT",
            "name": "Karim Ahmed",
            "phone": ""
        },
        {
            "country": null,
            "email": "sv464356533@yahoo.com",
            "gender": null,
            "id": 28,
            "isactive": false,
            "language": "Dutch",
            "lastactivetimedt": "Sun, 14 Nov 2021 20:02:29 GMT",
            "name": "Seira Von",
            "phone": ""
        },
        {
            "country": null,
            "email": "ahmedtest67235423@gmail.com",
            "gender": null,
            "id": 31,
            "isactive": false,
            "language": "Arabic",
            "lastactivetimedt": "Mon, 15 Nov 2021 19:24:59 GMT",
            "name": "Ahmed for test",
            "phone": ""
        },
        {
            "country": null,
            "email": "johntest6723546@gmail.com",
            "gender": null,
            "id": 32,
            "isactive": false,
            "language": "English",
            "lastactivetimedt": "Mon, 15 Nov 2021 19:24:23 GMT",
            "name": "John for test",
            "phone": ""
        }
    ]
}
```

#### POST /messages
- General:
    - Creates a new message sent from a user of {sender_id} to user of receiver id
- `curl http://127.0.0.1:5000/questions?page=3 -X POST -H "Content-Type: application/json" -d '{"moshakkaltext": null, "receiver_id": 19, "sender_id": 15, "text": "اهلا بك يا صديقي", "translatedtext": "Hey, buddy. "}'`
```
{
   "moshakkaltext": null,
   "receiver_id": 19,
   "sender_id": 15,
   "text": "اهلا بك يا صديقي",
   "translatedtext": "Hey, buddy. "
}
```

#### POST /users/photo/upload/{id}
- General:
    - Upload user avatar image. 
- `curl http://127.0.0.1:5000/users/photo/upload/19 -X POST -H "Content-Type: application/json" -F 'image=@/path/to/pictures/picture.jpg'`
```
{
    "result": "successful"
}

```
#### GET /users/photo/download/{id}
- General:
    - Download user avatar message for user with id = {id}. 
- `curl -X GET http://127.0.0.1:5000/users/photo/download/23`
```
Response is the avatar image file.
```

## Authors
Hasan

## Acknowledgements 
The awesome team at Udacity and all of the instructors, mentors and reviewers
