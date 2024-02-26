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
        return "Dalyba iš nulio negalima"
    return pirmas / antras

@app.route("/")  # Route 1: Home/Form
def hello_world():
    return '''
            <form action="/skaicius">
                <label for="test">Skaicius 1:</label><br>
                <input type="text" id="test" name="test" value="0"><br>
                
                <label for="test2">Skaicius 2:</label><br>
                <input type="text" id="test2" name="test2" value="0"><br>
                
                <label for="operation">Operacija:</label><br>
                <select name="operation" id="operation">
                    <option value="sudetis">Sudėtis</option>
                    <option value="atimtis">Atimtis</option>
                    <option value="daugyba">Daugyba</option>
                    <option value="dalyba">Dalyba</option>
                </select><br><br>
                
                <input type="submit" value="Apskaičiuoti">
            </form> 
            '''

@app.route("/labas")  # Route 2: Greeting Counter
def sakyk_labas():
    global skaicius  # Using global variable
    skaicius = skaicius + 1  # Increment global variable by 1 each visit
    return f"Labas {skaicius}"

@app.route("/skaicius")  # Route 3: Calculation
def skaiciavimo():
    skaicius1 = request.args.get("test", 0, type=int)
    skaicius2 = request.args.get("test2", 0, type=int)
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
        return "Neteisinga operacija"

    return f"Operacijos rezultatas: {rezultatas}"

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
