from application import app

# sql engine
import sql_db as sql

if __name__ == "__main__":
    debug = True
    host = "0.0.0.0"
    port = 8080
    app.run(debug=debug, host=host, port=port)
