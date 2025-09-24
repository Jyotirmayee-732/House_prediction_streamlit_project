from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def greet():
    return render_template("index.html")

@app.route('/addition')
def addition():
    try:
        # Get input values from query parameters
        a = request.args.get('num1', type=int)
        b = request.args.get('num2', type=int)

        # Check for missing values
        if a is None or b is None:
            return jsonify({"error": "Please provide valid numbers"}), 400

        # Return the correct structure
        return jsonify({
            "result": a + b
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
