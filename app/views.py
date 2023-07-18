from flask import render_template, redirect, request, url_for
from app import app, db
from app.models import Produto

@app.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        produto_titulo = request.form['titulo']
        quantidade = request.form['quantidade']
        produto = Produto(titulo=produto_titulo, quantidade=quantidade)
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:produto_id>', methods=['GET', 'POST'])
def update(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    if request.method == 'POST':
        produto.titulo = request.form['titulo']
        produto.quantidade = request.form['quantidade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', produto=produto)

@app.route('/delete/<int:produto_id>', methods=['POST'])
def delete(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('index'))
