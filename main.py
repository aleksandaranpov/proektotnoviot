import sqlite3
from flask import Flask, jsonify,request
import pymongo

app=Flask(__name__)
@app.route('/companies', methods = ["GET"])
def company():
    conn = sqlite3.connect("data.db")
    cursor=conn.cursor()
    companies=[]
    cursor.execute("SELECT * FROM companies LIMIT 5")
    for row in cursor.fetchall():
         companyy={
            "id":row[0],
            "name": row[1],
            "country_iso":row[2],
            "city":row[3],
            "nace":row[4],
            "website":row[5] }

         companies.append(companyy)
    cursor.close()
    conn.close()

    return jsonify({"companies":companies})



@app.route('/companies/', methods = ["POST"])
def add_company():
    conn =pymongo.MongoClient()
    db= conn["mydatabase"]
    collections=db["cleaned_companies"]
    data= request.get_json()
    result=collections.instert_one(data)
    if result.inserted_id:
        return jsonify({"success":True}),201
    else:
        return jsonify({"success":False}),400
if __name__ =="__main__":
    app.run()