from flask import Flask, request, jsonify
import pymysql.cursors
import re

app = Flask(__name__)

# MySQL Configuration
mysql_config = {
    'user': 'root',
    'password': 'rootpass',
    'host': 'localhost:3306',
    'database': 'sakila',
    'raise_on_warnings': True
}

# Simple SQL Injection Protection
def is_safe_query(query):
    return not re.search(r'\b(DELETE|ALTER|DROP|INSERT|UPDATE)\b', query, re.IGNORECASE)

@app.route('/query', methods=['POST'])
def query_mysql():
    data = request.json
    query = data.get('query')

    if query and is_safe_query(query):
        try:
            connection = pymysql.connect(**mysql_config)
            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
            connection.close()
            return jsonify(results)
        except Exception as e:
            return str(e), 400

if __name__ == "__main__":
    app.run(debug=True)
