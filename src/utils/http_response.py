from flask import jsonify

def http_response(message: str, data=None, errors:list = {}, status: int = 200):
    if data is None:
        data = {}

    return jsonify({
        "message": message,
        "data": data,
        "errors": errors,
        "status": status
    }), status
