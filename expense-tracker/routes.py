from flask import Blueprint, request, jsonify
from models import db, Expense

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Expense Tracker API is running!"})

# CREATE
@bp.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = Expense(title=data['title'], amount=data['amount'])
    db.session.add(expense)
    db.session.commit()
    return jsonify(expense.to_dict()), 201

# READ ALL
@bp.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([e.to_dict() for e in expenses])

# READ ONE
@bp.route('/expenses/<int:id>', methods=['GET'])
def get_expense(id):
    expense = Expense.query.get_or_404(id)
    return jsonify(expense.to_dict())

# UPDATE
@bp.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    expense = Expense.query.get_or_404(id)
    data = request.get_json()
    expense.title = data.get('title', expense.title)
    expense.amount = data.get('amount', expense.amount)
    db.session.commit()
    return jsonify(expense.to_dict())

# DELETE
@bp.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

 