from flask import Flask, request

app = Flask(__name__)

# Arithmetic operations
def sudetis(pirmas, antras):
    return pirmas + antras

def atimtis(pirmas, antras):
    return pirmas - antras

def daugyba(pirmas, antras):
    return pirmas * antras

def dalyba(pirmas, antras):
    if antras == 0:  # Avoid division by zero
        return "Dalyba is 0 neimanoma"
    return pirmas / antras

@app.route("/")  # Route 1: Home/Form
def hello_world():
    return '''
            <html>
                <head>
                    <title>Simple Calculator</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 40px; }
                        label { display: block; margin: 20px 0 10px; }
                        input, select { padding: 10px; margin: 5px 0; width: 200px; }
                        input[type="submit"] { width: auto; cursor: pointer; background-color: #4CAF50; color: white; }
                        form { background-color: #f2f2f2; padding: 20px; border-radius: 8px; }
                    </style>
                </head>
                <body>
                    <h2>Skaiciuotuvas</h2>
                    <form action="/skaicius">
                        <label for="test">Skaicius 1:</label>
                        <input type="text" id="test" name="test" value="0">
                        
                        <label for="test2">Skaicius 2:</label>
                        <input type="text" id="test2" name="test2" value="0">
                        
                        <label for="operation">Operacija:</label>
                        <select name="operation" id="operation">
                            <option value="sudetis">Sudetis</option>
                            <option value="atimtis">Atimtis</option>
                            <option value="daugyba">Daugyba</option>
                            <option value="dalyba">Dalyba</option>
                        </select>
                        
                        <br>
                        <input type="submit" value="Skaiciuoti">
                    </form> 
                </body>
            </html>
            '''

@app.route("/skaicius")  # Route 3: Calculation
def skaiciavimo():
    try:
        skaicius1 = float(request.args.get("test", type=str))
        skaicius2 = float(request.args.get("test2", type=str))
    except ValueError:
        return "Iveskite tinkamus duomenis."

    operation = request.args.get("operation")

    if operation == "sudetis":
        rezultatas = sudetis(skaicius1, skaicius2)
    elif operation == "atimtis":
        rezultatas = atimtis(skaicius1, skaicius2)
    elif operation == "daugyba":
        rezultatas = daugyba(skaicius1, skaicius2)
    elif operation == "dalyba":
        rezultatas = dalyba(skaicius1, skaicius2)
    else:
        return "Invalid operation"

    return f"Rezultatas: {rezultatas}"

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
