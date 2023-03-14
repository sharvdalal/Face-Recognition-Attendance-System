
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-c0922-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')


data = {
    "321654":
        {
            "name":"Sharv Dalal",
            "major":"EnTC",
            "starting-year":2020,
            "total_attendance":6,
            "standing": "G",
            "year":3,
            "last_attendance_time": "2022-3-14 00:54:34"
        },
    "852741":
        {
            "name":"Emily Blunt",
            "major":"Economics",
            "starting-year":2010,
            "total_attendance":16,
            "standing": "B",
            "year":3,
            "last_attendance_time": "2022-3-14 00:54:34"
        },
    "963852":
        {
            "name":"Elon Musk",
            "major":"Space Technology",
            "starting-year":2019,
            "total_attendance":10,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-3-14 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

