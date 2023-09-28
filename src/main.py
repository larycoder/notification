from application import app

# application routes
import routes

if __name__ == "__main__":
    debug = True
    host = "0.0.0.0"
    port = 8080
    app.run(debug=debug, host=host, port=port)
