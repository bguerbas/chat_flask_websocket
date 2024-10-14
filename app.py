from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Timer

app = Flask(__name__)
socketio = SocketIO(app)


# Função que simula um bot respondendo ao usuário
def bot_response():
    return "Olá, sou o ChatBot! Como posso te ajudar?"


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)
    print(f"Mensagem recebida do usuário: {msg}")

    # Simular o bot respondendo com um delay de 2 segundos
    Timer(2.0, lambda: responder_bot()).start()


def responder_bot():
    resposta = bot_response()
    print(f"Bot está enviando a resposta: {resposta}")
    socketio.emit('message', resposta)  # Removido o to='/'


@socketio.on('disconnect')
def handle_disconnect():
    print('Usuário desconectado.')


if __name__ == '__main__':
    socketio.run(app, debug=True, log_output=True)  # Ativado o log_output para mais detalhes
