#!/usr/bin/env python3

from myapp.factory import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)