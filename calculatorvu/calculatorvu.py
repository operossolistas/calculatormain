from flask import Flask, request, render_template_string

app = Flask(__name__)

# Function to solve basic arithmetic
def solve_arithmetic(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError(f"Klaida sprendžiant aritmetinę išraišką: {str(e)}")

# Function to solve algebraic equations of the form ax+b=c
def solve_algebra(equation):
    # Removing whitespaces for simplicity
    equation = equation.replace(" ", "")
    if "x" in equation:
        # Splitting at '=' to separate both sides
        lhs, rhs = equation.split("=")
        # Assuming the equation is in form ax+b=c, find 'a' and 'b'
        a, b = lhs.split("x")
        if a == '': a = '1'  # Handle case of equation like x+2=5
        if a == '-': a = '-1'  # Handle case of equation like -x+2=5
        a = float(a)
        b = float(b)
        c = float(rhs)
        # Solve for x
        x = (c - b) / a
        return x
    else:
        raise ValueError("Lygtyje nerasta kintamojo 'x'.")

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        input_expression = request.form.get("expression", "")
        try:
            # Check if the expression is an algebraic equation or arithmetic
            if "x" in input_expression and "=" in input_expression:
                result = solve_algebra(input_expression)
                message = f"Sprendimas: x = {result}"
            else:
                result = solve_arithmetic(input_expression)
                message = f"Rezultatas: {result}"
        except Exception as e:
            message = str(e)
        return render_template_string(main_page(), result=message)
    else:
        return render_template_string(main_page())

def main_page():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Skaičiuotuvas ir Algebra</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; transition: background-color 0.5s ease; }
                .night { background-color: #333; color: white; }
                input, button, select { padding: 10px; margin: 5px 0; width: calc(100% - 22px); box-sizing: border-box; }
                button { background-color: #4CAF50; color: white; cursor: pointer; }
                .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 400px; margin: auto; transition: background-color 0.5s ease, color 0.5s ease; }
                .night .container { background-color: #424242; }
                h2 { color: #333; }
                .night h2 { color: white; }
                form { margin-bottom: 20px; }
                p { color: #666; }
                .night p { color: #ccc; }
                .gif-container { text-align: center; margin-top: 20px; }
                .toggle-night { margin-top: 20px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Skaičiuotuvas ir Algebra</h2>
                <form method="post">
                    <input type="text" name="expression" placeholder="Įveskite išraišką ar lygtį" autofocus/>
                    <button type="submit">Skaičiuoti/Spręsti</button>
                </form>
                <button class="toggle-night">Nakties režimas</button>
                {% if result %}
                    <p><strong>Rezultatas:</strong> {{ result }}</p>
                {% endif %}
            </div>
            <div class="gif-container">
                <iframe src="https://giphy.com/embed/Za7KwK4AMeFq" width="376" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
            </div>
            <script>
                document.querySelector('.toggle-night').onclick = function() {
                    document.body.classList.toggle('night');
                };
            </script>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
