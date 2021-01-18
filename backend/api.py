from flask import Flask, request, jsonify
# from  flask_mysqldb import MySQL
import mysql.connector
from flask_cors import CORS
import random
from datetime import datetime
from werkzeug.utils import secure_filename
from playsound import playsound
from gtts import gTTS
import json
import os 
import shutil
import cv2
import attendance_recording_system as aars
from threading import Thread
import time
import getpass

app = Flask(__name__)
CORS(app)

cwd = os.getcwd()
KNOWN_FACES_DIR = os.path.join(cwd, 'known_faces_attendance')

INTERVAL_ABSEN_IN_MINUTE = 1
# connection =  mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="absensipkb"
# )
def queryToDb(query, value):
    # Initialize DB connection
    connection =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="absensipkb"
)
    cursor = connection.cursor(buffered = True)
    cursor.execute(query, value)
    connection.commit()

    result = None
    try:
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
    except:
        pass
    return result

def sudahAbsenPagi(nik_karyawan):
    query = "SELECT COUNT(1) FROM kehadiran WHERE nik_karyawan=%s AND DATE(timestamp)=DATE(NOW())"
    value = (nik_karyawan, )

    result = queryToDb(query, value)
    sudahAbsen = result >= 1
    # print(sudahAbsen)
    return sudahAbsen

def terakhirTerlihatNMenitLalu(nik_karyawan):
    query = "SELECT (HOUR( NOW() - timestamp) * 60 +MINUTE( NOW() - timestamp)) AS terakhir_absen FROM kehadiran WHERE nik_karyawan=%s AND date(timestamp)=DATE(NOW()) ORDER BY timestamp DESC LIMIT 1"
    value = (nik_karyawan, )
    result = queryToDb(query, value)
    return result > INTERVAL_ABSEN_IN_MINUTE

def absen(nik_karyawan, timestamp):
    try:
        query = "INSERT INTO kehadiran (nik_karyawan, timestamp) VALUES (%s, %s)"
        value = (nik_karyawan, timestamp)
        queryToDb(query, value)
        print(f'{nik_karyawan} berhasil absen pada {timestamp}')
    except:
        print(f'{nik_karyawan} tidak dikenali')

def getNamaKaryawan(nik):
    # dapatkan nama, beri salam 
    query = "SELECT nama FROM karyawan WHERE nik=%s"
    value = (nik, )
    result = queryToDb(query, value) 

    return result

@app.route('/')
def helloworld():
    return 'Hello world'

@app.route('/check/<nik>')
def check(nik):
    ts = datetime.now()
    if not sudahAbsenPagi(nik):
        # belum absen pagi, absen
        print(f"{nik} belum absen hari ini, catat")
        absen(nik, ts)
    else:
        # sudah absen pagi, catat tiap INTERVAL_ABSEN_IN_MINUTE menit
        if terakhirTerlihatNMenitLalu(nik):
            print(f"{nik} terakhir terlihat lebih dari {INTERVAL_ABSEN_IN_MINUTE} menit lalu, catat")
            absen(nik, ts)
    return "hello"

@app.route('/report/<date>')
def getAttendanceRecord(date):
    print(f'getting report of date {date}')
    query = "SELECT karyawan.nik, karyawan.nama, MIN(kehadiran.timestamp), MAX(kehadiran.timestamp) FROM kehadiran, karyawan WHERE kehadiran.nik_karyawan=karyawan.nik AND timestamp >= DATE(%s) AND timestamp < DATE(%s) + INTERVAL 1 DAY GROUP BY karyawan.nik".format(date, date)
    # print(query)
    connection =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="absensipkb"
    )
    value = (date, date)
    cursor = connection.cursor()
    cursor.execute(query, value)
    result = cursor.fetchall()
    final_result = []
    for res in result:
        final_result.append({
            'id_karyawan': res[0],
            'nama': res[1],
            'datang': res[2],
            'pulang': res[3]
        })
    # print(final_result)
    cursor.close()
    connection.close()
    return jsonify(final_result)

@app.route('/attendance')
def fetchAttendance():
    query = "SELECT kar.nik, kar.nama, keh.timestamp, keh.id FROM karyawan AS kar INNER JOIN kehadiran AS keh ON kar.nik=keh.nik_karyawan WHERE kar.active=1 AND TIMESTAMP >= DATE(NOW()) AND TIMESTAMP < DATE(NOW()) + INTERVAL 1 DAY ORDER BY keh.timestamp DESC"
    # Initialize DB connection
    connection =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="absensipkb"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    res = []
    for r in result:
        # ts = datetime.datetime.strptime(r[2], '%Y-%m-%d %H:%M:%S.%f')
        waktu = r[2].strftime("%H:%M:%S")
        res.append({
            'nik': r[0],
            'nama': r[1],
            'timestamp': str(waktu),
            'id': r[3]
        })
    return json.dumps(res)

@app.route('/employee')
def fetchEmployee():
    query = "SELECT * FROM karyawan"
    # Initialize DB connection
    connection =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="absensipkb"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    cursor.close()
    connection.close()
    res = []
    for r in result:
        res.append({
            'nik': r[0],
            'nama': r[1],
            'created_at': str(r[2])[:19],
            'active': int(r[3])
        })
    return json.dumps(res)

@app.route('/add_employee_upload/<nik>/<nama>', methods=['GET', 'POST'])
def add_employee_upload(nik, nama):
    f = request.files['file']
    filename = secure_filename(f.filename)
    cwd = os.getcwd()
    os.mkdir(os.path.join(KNOWN_FACES_DIR, f"{nama}-{nik}"))
    f.save(os.path.join(KNOWN_FACES_DIR, f"{nama}-{nik}", filename))
    # menambahkan nik dan nama ke database
    # print(f"menambahkan karyawan dengan nama {nama} dan nik {nik}")
    ts = datetime.now()
    query = "INSERT INTO karyawan(nik, created_at, nama, active) VALUES(%s, %s, %s, '1')"
    value = (nik, ts, nama)
    queryToDb(query, value)
    return "success" 

@app.route('/add_employee/<nik>/<nama>', methods=['GET', 'POST'])
def add_employee(nik, nama):
    # menambahkan nik dan nama ke database
    # print(f"menambahkan karyawan dengan nama {nama} dan nik {nik}")
    ts = datetime.now()
    query = "INSERT INTO karyawan(nik, created_at, nama, active) VALUES(%s, %s, %s, '1')"
    value = (nik, ts, nama)
    queryToDb(query, value)
    # mengopy gambar ke karyawan folder C:\Users\Lenovo\Downloads
    username = getpass.getuser()
    download_dir = f"C:Users\{username}\Downloads"
    # make dir if not exists yet

    if nik not in os.listdir(KNOWN_FACES_DIR):
        os.mkdir(os.path.join(KNOWN_FACES_DIR, f"{nama}-{nik}"))

    # looking for image in Download dir
    for f in os.listdir(download_dir):
        if nik in f:
            # copy that file
            try:
                shutil.copyfile(os.path.join(download_dir, f), os.path.join(KNOWN_FACES_DIR, f"{nama}-{nik}", f))
            except Exception as e:
                print(e)
            finally:
                # remove 
                print('done')
                # os.remove(os.path.join(download_dir, f))
    return "success" 

@app.route('/turn_on')
def turnOn():
    stream = os.popen('python attendance_recording_system.py')
    output = stream.read()
    return output

@app.route('/download_success/<nik>')
def download_success(nik):
    username = getpass.getuser()
    download_dir = f"C:/Users/{username}/Downloads"
    files = os.listdir(os.path.join(download_dir))
    for f in files:
        if nik in f:
            return jsonify({
                'status': 200,
                'msg': f'{nik} exists'
            })
    return jsonify({
        'status': 404,
        'msg': f'{nik} doesn\'t exist'
    })

@app.route('/remove_employee/<nik>')
def remove_employee(nik):
    try:
        query = "UPDATE karyawan SET active=0 WHERE nik=%s"
        value = (nik,)
        queryToDb(query, value)
    except:
        print("can't set employee to inactive")
    try:
        for folder in os.listdir(KNOWN_FACES_DIR):
            if nik in folder:
                shutil.rmtree(os.path.join(KNOWN_FACES_DIR, folder))
    except:
        print("can't remove folder")
    
    return f'successfully removed {nik}'
 

if __name__=='__main__':
    app.run(debug=True)