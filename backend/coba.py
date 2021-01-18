stem error: 0
INFO:werkzeug:127.0.0.1 - - [17/Jan/2021 23:03:53] "GET /check/123321 HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 233, in _open_connection
    self._cmysql.connect(**cnx_kwargs)
_mysql_connector.MySQLInterfaceError: Lost connection to MySQL server at 'reading initial communication packet', system error: 0    

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1867, in handle_exception      
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1952, in full_dispatch_request 
    rv = self.handle_user_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1821, in handle_user_exception 
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1950, in full_dispatch_request 
    rv = self.dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1936, in dispatch_request      
    return self.view_functions[rule.endpoint](**req.view_args)    
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 92, in 
check
    if not sudahAbsenPagi(nik):
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 57, in 
sudahAbsenPagi
    result = queryToDb(query, value)
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 34, in 
queryToDb
    connection =  mysql.connector.connect(
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\__init__.py", line 270, in connect 
    return CMySQLConnection(*args, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 86, in __init__
    self.connect(**kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\abstracts.py", line 985, in connect    self._open_connection()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 235, in _open_connection
    raise errors.get_mysql_exception(msg=exc.msg, errno=exc.errno,mysql.connector.errors.OperationalError: 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0
INFO:werkzeug:127.0.0.1 - - [17/Jan/2021 23:03:53] "GET /attendance HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 233, in _open_connection
    self._cmysql.connect(**cnx_kwargs)
_mysql_connector.MySQLInterfaceError: Lost connection to MySQL server at 'reading initial communication packet', system error: 0    

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1867, in handle_exception      
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1952, in full_dispatch_request 
    rv = self.handle_user_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1821, in handle_user_exception 
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1950, in full_dispatch_request 
    rv = self.dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1936, in dispatch_request      
    return self.view_functions[rule.endpoint](**req.view_args)    
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 135, in fetchAttendance
    connection =  mysql.connector.connect(
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\__init__.py", line 270, in connect 
    return CMySQLConnection(*args, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 86, in __init__
    self.connect(**kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\abstracts.py", line 985, in connect    self._open_connection()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 235, in _open_connection
    raise errors.get_mysql_exception(msg=exc.msg, errno=exc.errno,mysql.connector.errors.OperationalError: 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0
INFO:werkzeug:127.0.0.1 - - [17/Jan/2021 23:03:54] "GET /check/123321 HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 233, in _open_connection
    self._cmysql.connect(**cnx_kwargs)
_mysql_connector.MySQLInterfaceError: Lost connection to MySQL server at 'reading initial communication packet', system error: 0    

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1867, in handle_exception      
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1952, in full_dispatch_request 
    rv = self.handle_user_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1821, in handle_user_exception 
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1950, in full_dispatch_request 
    rv = self.dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1936, in dispatch_request      
    return self.view_functions[rule.endpoint](**req.view_args)    
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 92, in 
check
    if not sudahAbsenPagi(nik):
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 57, in 
sudahAbsenPagi
    result = queryToDb(query, value)
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 34, in 
queryToDb
    connection =  mysql.connector.connect(
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\__init__.py", line 270, in connect 
    return CMySQLConnection(*args, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 86, in __init__
    self.connect(**kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\abstracts.py", line 985, in connect    self._open_connection()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 235, in _open_connection
    raise errors.get_mysql_exception(msg=exc.msg, errno=exc.errno,mysql.connector.errors.OperationalError: 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0
INFO:werkzeug:127.0.0.1 - - [17/Jan/2021 23:03:54] "GET /check/123321 HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 233, in _open_connection
    self._cmysql.connect(**cnx_kwargs)
_mysql_connector.MySQLInterfaceError: Lost connection to MySQL server at 'reading initial communication packet', system error: 0    

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1867, in handle_exception      
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1952, in full_dispatch_request 
    rv = self.handle_user_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1821, in handle_user_exception 
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1950, in full_dispatch_request 
    rv = self.dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1936, in dispatch_request      
    return self.view_functions[rule.endpoint](**req.view_args)    
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 92, in 
check
    if not sudahAbsenPagi(nik):
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 57, in 
sudahAbsenPagi
    result = queryToDb(query, value)
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 34, in 
queryToDb
    connection =  mysql.connector.connect(
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\__init__.py", line 270, in connect 
    return CMySQLConnection(*args, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 86, in __init__
    self.connect(**kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\abstracts.py", line 985, in connect    self._open_connection()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 235, in _open_connection
    raise errors.get_mysql_exception(msg=exc.msg, errno=exc.errno,mysql.connector.errors.OperationalError: 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0
INFO:werkzeug:127.0.0.1 - - [17/Jan/2021 23:03:55] "GET /attendance HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 233, in _open_connection
    self._cmysql.connect(**cnx_kwargs)
_mysql_connector.MySQLInterfaceError: Lost connection to MySQL server at 'reading initial communication packet', system error: 0    

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1867, in handle_exception      
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1952, in full_dispatch_request 
    rv = self.handle_user_exception(e)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask_cors\extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1821, in handle_user_exception 
    reraise(exc_type, exc_value, tb)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1950, in full_dispatch_request 
    rv = self.dispatch_request()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\flask\app.py", line 1936, in dispatch_request      
    return self.view_functions[rule.endpoint](**req.view_args)    
  File "E:\KULIAH\Semester5\PKB\aars\backend\api.py", line 135, in fetchAttendance
    connection =  mysql.connector.connect(
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\__init__.py", line 270, in connect 
    return CMySQLConnection(*args, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 86, in __init__
    self.connect(**kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\abstracts.py", line 985, in connect    self._open_connection()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\Lib\site-packages\mysql\connector\connection_cext.py", line 235, in _open_connection
    raise errors.get_mysql_exception(msg=exc.msg, errno=exc.errno,mysql.connector.errors.OperationalError: 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0