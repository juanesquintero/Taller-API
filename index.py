from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

fruits = [
    { 'id': 0, 'nombre': 'Manzana', 'imagen': "./imagenes/1.jpg" },
    { 'id': 1, 'nombre': 'Moras', 'imagen': "./imagenes/2.jpg" },
    { 'id': 2, 'nombre': 'Bananos', 'imagen': "./imagenes/3.jpg" },
    { 'id': 3, 'nombre': 'Kiwi', 'imagen': "./imagenes/4.jpg" },
    { 'id': 4, 'nombre': 'Mango', 'imagen': "./imagenes/5.jpg" },
    { 'id': 5, 'nombre': 'Piña', 'imagen': "./imagenes/6.jpg" },
]

#Get
@app.route("/")
def get():
    return "Fruits API"

#Get
@app.route("/fruits")
def allFruits():
    return jsonify({'fruits': fruits})

#Get One
@app.route("/fruits/<int:fruit_id>")
def getFruit(fruit_id):
    i = 0
    for fruit in fruits:
        if fruit['id'] == fruit_id:
            return jsonify(fruits[i])
        i+=1
    return jsonify(fruits)

#Post 
@app.route("/fruits", methods=['POST'])
def postFruit():
    #Agregar elemento a un array
    id = 0
    for fruit in fruits:
        if fruit['id'] > id:
            id = fruit['id']
    request.json['id'] = id+1
    fruits.append(request.json)
    print(str(request.json),"\nAgregado")
    return jsonify(fruits)

#PUT One
@app.route("/fruits/<int:fruit_id>", methods=['PUT'])
def putFruit(fruit_id):
    i=0
    for myFruit in fruits:
        if myFruit['id']== fruit_id:
            print("PUT")
            #print(fruits[i])
            fruits[i]=request.json
            #print(fruits[i])
        i+=1
    return jsonify(fruits)


#Delete One
@app.route("/fruits/<int:fruit_id>", methods=['DELETE'])
def deleteFruit(fruit_id):
    print(fruit_id," Eliminado")
    for myFruit in fruits:
        if myFruit['id']== fruit_id:
            fruits.remove(myFruit)
    return jsonify(fruits)


#Solo es uno
app.run(port=5000,debug=True)

