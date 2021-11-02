from flask import jsonify


def success(params: dict = None, status_code: int = 200):

    if not params:
        params = {}

    response = params.copy()
    response.update({"success": True})
    return response, status_code


def error(params: dict = None, status_code: int = 400):

    if not params:
        params = {}
    response = {"success": False}
    response.update({'errors': params})
    return response, status_code
