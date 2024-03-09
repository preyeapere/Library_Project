import sqlite3
from flask import Flask, render_template
from flask import Flask, render_template, request, url_for, flash, redirect,abort

# ...
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connect():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ...

@app.route('/new/', methods=('GET', 'POST'))
def new():
    return render_template('create.html')

@app.route('/')
def index():
    conn = get_db_connect()
    collects = conn.execute('SELECT * FROM book').fetchall()
    conn.close()
    return render_template('index.html', collects=collects)

# ...

def get_post(post_id):
    conn = get_db_connect()
    post = conn.execute('SELECT * FROM book WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# ...

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        quantity = request.form['quantity']

        if not title:
            flash('Title is required!')

        elif not author:
            flash('author is required!')
        elif not quantity:
            flash('quantity is required!')

        else:
            conn = get_db_connect()
            conn.execute('UPDATE book SET title = ?, author = ?, quantity = ?'
                         ' WHERE id = ?',
                         (title, author,quantity, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        quantity = request.form['quantity']

        if not title:
            flash('Title is required!')
        elif not author:
            flash('Content is required!')
        else:
            conn = get_db_connect()
            conn.execute('INSERT INTO book (title, author,quantity) VALUES (?, ?, ?)',
                         (title,author,quantity))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


# ...

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connect()
    conn.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


if __name__ == '__main__':
      
       app.run(debug = True,port=5002)
