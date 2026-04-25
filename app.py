from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <style>
        body {
            background: #0f0f0f;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial;
        }
        .calc {
            background: #1e1e1e;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 20px #00ffcc;
        }
        #display {
            width: 100%;
            height: 50px;
            margin-bottom: 10px;
            font-size: 20px;
            text-align: right;
            padding: 10px;
            background: black;
            color: #00ffcc;
            border: none;
        }
        .btns {
            display: grid;
            grid-template-columns: repeat(4, 60px);
            gap: 10px;
        }
        button {
            padding: 15px;
            font-size: 16px;
            border: none;
            border-radius: 10px;
            background: #333;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background: #00ffcc;
            color: black;
        }
    </style>

    <div class="calc">
        <input id="display" readonly>

        <div class="btns">
            <button onclick="press('7')">7</button>
            <button onclick="press('8')">8</button>
            <button onclick="press('9')">9</button>
            <button onclick="press('/')">/</button>

            <button onclick="press('4')">4</button>
            <button onclick="press('5')">5</button>
            <button onclick="press('6')">6</button>
            <button onclick="press('*')">*</button>

            <button onclick="press('1')">1</button>
            <button onclick="press('2')">2</button>
            <button onclick="press('3')">3</button>
            <button onclick="press('-')">-</button>

            <button onclick="press('0')">0</button>
            <button onclick="press('.')">.</button>
            <button onclick="calculate()">=</button>
            <button onclick="press('+')">+</button>

            <button onclick="clearDisplay()" style="grid-column: span 4; background:red;">C</button>
        </div>
    </div>

    <script>
        function press(val) {
            document.getElementById("display").value += val;
        }

        function clearDisplay() {
            document.getElementById("display").value = "";
        }

        function calculate() {
            let exp = document.getElementById("display").value;

            fetch('/calculate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({exp: exp})
            })
            .then(res => res.text())
            .then(data => {
                document.getElementById("display").value = data;
            });
        }
    </script>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        result = eval(data['exp'])
        return str(result)
    except:
        return "Error"

if __name__ == '__main__':
    app.run(debug=True)
