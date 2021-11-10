from application import init_app

# entrypoint for our app usign the factory pattern
app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
