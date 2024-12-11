from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Run the application
    app.run(host="127.0.0.1", port=5000, debug=True)
