from flask import Flask, request, render_template_string
import math  # Import math module for root and power calculations

app = Flask(__name__)

# Function to solve basic arithmetic including roots
def solve_arithmetic(expression):
    try:
        # Handling square root operations explicitly
        if 'sqrt' in expression:
            expression = expression.replace('sqrt', 'math.sqrt')
        # Handling power operations explicitly
        expression = expression.replace('^', '**')
        # Evaluate the enhanced expression and return the result
        result = eval(expression, {'math': math, '__builtins__': None})
        return result
    except Exception as e:
        raise ValueError(f"Error while solving arithmetic expression: {str(e)}")

# Function to solve algebraic equations of the form ax+b=c
def solve_algebra(equation):
    try:
        equation = equation.replace(" ", "")
        if "x" in equation:
            lhs, rhs = equation.split("=")
            a, b = lhs.split("x")
            if a == '': a = '1'  # Handle case of equation like x+2=5
            if a == '-': a = '-1'  # Handle case of equation like -x+2=5
            a = float(a)
            b = float(b)
            c = float(rhs)
            x = (c - b) / a
            return x
        else:
            raise ValueError("No variable 'x' found in the equation.")
    except Exception as e:
        raise ValueError(f"Error while solving algebraic equation: {str(e)}")

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        input_expression = request.form.get("expression", "")
        try:
            if "x" in input_expression and "=" in input_expression:
                result = solve_algebra(input_expression)
                message = f"Solution: x = {result}"
            else:
                result = solve_arithmetic(input_expression)
                message = f"Result: {result}"
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
            <title>Calculator and Algebra</title>
            <style>
                /* Your existing CSS plus any additional styles */
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Calculator and Algebra</h2>
                <form method="post">
                    <div class="button-container">
                        <!-- Buttons for numbers and symbols -->
                        <button type="button" onclick="appendToInput('1')">1</button>
                        <button type="button" onclick="appendToInput('2')">2</button>
                        <button type="button" onclick="appendToInput('3')">3</button>
                        <button type="button" onclick="appendToInput(' + ')">+</button>
                        <button type="button" onclick="appendToInput(' - ')">-</button>
                        <button type="button" onclick="appendToInput(' * ')">*</button>
                        <button type="button" onclick="appendToInput(' / ')">/</button>
                        <button type="button" onclick="appendToInput('sqrt(')">sqrt(</button>
                        <button type="button" onclick="appendToInput('^')">^</button>
                        <button type="button" onclick="appendToInput('x')">x</button>
                        <!-- Include more buttons as needed -->
                    </div>
                    <input type="text" name="expression" id="expression" placeholder="Enter expression or equation" autofocus/>
                    <button type="submit">Calculate/Solve</button>
                </form>
                <button class="toggle-night">Night Mode</button>
                {% if result %}
                    <p><strong>Result:</strong> {{ result }}</p>
                {% endif %}
            </div>
            <script>
                function appendToInput(value) {
                    document.getElementById('expression').value += value;
                }
            </script>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
