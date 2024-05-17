from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.mydatabase
todos = db.todos

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_description = request.form['task_description']
        todos.insert_one({
            'task_description': task_description
            
        })
        return redirect(url_for('index'))
    
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.route('/<id>/update', methods=['GET', 'POST'])
def update(id):
    todo = todos.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        new_task_description = request.form['task_description']

        todos.update_one({'_id': ObjectId(id)}, {'$set': {'task_description': new_task_description}})
        return redirect(url_for('index'))
    return render_template('update.html', todo=todo)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
