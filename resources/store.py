import sqlite3
from flask import jsonify 
from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel
    
class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
           return store.json()
        return {'message': 'store was not found'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
           return {"message": "Store with name {} already exists.".format(name)}, 400
        store = StoreModel(name)
        try:
          store.save_to_db()
        except:
           return {"message":"an error occurred when inserting the store."}, 500
        return store.json(), 201
 
    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
           store.delete_from_db()
        return {"message": "store successfully deleted"}
        
    
class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
