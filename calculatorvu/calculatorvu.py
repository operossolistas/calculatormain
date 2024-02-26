''' 1 susidiegiame Flask
        pip3 install Flask
        pip install Flask
''' 

# 2. Importuojame

from flask import Flask, request
app = Flask(__name__)



skaicius = 0 # apsirasome kintamaji ( Globalus )

def sudetis(pirmas,antras):
        return pirmas+antras




@app.route("/") # Route 1
def hello_world():

    return f"""
                <form action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>
                        
                    <label for="[[__ID__]]">skaicius 2</label><br>   
                        <input type="text" id="[[__ID__]]" name="[[__ID__]]" value="0"><br><br>
                        </br></br>

                    <input type="submit" value="Submit">
                </form> 
            """

@app.route("/labas")  # Route 2
def sakyk_labas():
    global skaicius ## Naudoju globalu kintamaji
    skaicius = skaicius +1 ## kaskart atidare pridedam 1
    return f"Labas {skaicius}"


    '''
        /skaicius?test=100
        /skaicius?test=0  &  test2=0
    '''

@app.route("/skaicius") # Route 3
def skaiciavimo():
    #UZKLAUSA. ARGUMENTAI. METODAS()
    skaicius = request.args.get("test") ### Pasiimam argumenta is URL pvz.: /skaicius?test=100
    skaicius2 = request.args.get("test2") ### Pasiimam argumenta 2 is URL pvz.: /skaicius?test2=100

    suma = sudetis(int(skaicius2),int(skaicius))

    return f"Tavo ivestas skaicius: {suma}"





if __name__ == "__main__":
    app.run()








