import sqlite3
from flask import Flask, jsonify,request
import pymongo

app=Flask(__name__)
@app.route('/companies/<companies_id>', methods = ["GET"])
def company(companies_id):
    broj=int(companies_id)
    conn = sqlite3.connect("data.db")
    cursor=conn.cursor()
    companies=[]
    cursor.execute("SELECT * FROM companies WHERE id ={}".format(broj))
    for r in cursor.fetchall():
         companyy={
            "id":r[0],
            "name": r[1],
            "country_iso":r[2],
            "city":r[3],
            "nace":r[4],
            "website":r[5] }

         companies.append(companyy)
    cursor.close()
    conn.close()

    return jsonify({"companies":companies})



@app.route('/companies/', methods = ["POST"])
def add_company():
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    db= client["moja_database"]
    lista=db["cleaned_companies"]
    get_data= request.get_json()
    result=lista.insert_one(get_data)
    print(result)
    if result.inserted_id:
        return jsonify({"success":True}),201
    else:
        return jsonify({"success":False}),400
if __name__ =="__main__":
    app.run()
