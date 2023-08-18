from flask import Flask, render_template, request

app = Flask(__name__)

# ... Rotas existentes ...

@app.route('/configure_migration', methods=['GET', 'POST'])
def configure_migration():
    if request.method == 'POST':
        source_email = request.form.get('source_email')
        target_email = request.form.get('target_email')
        # Capturar mais campos e opções do formulário

        # Agora, você pode usar essas informações para gerar o comando imapsync

    return render_template('configure_migration.html')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

