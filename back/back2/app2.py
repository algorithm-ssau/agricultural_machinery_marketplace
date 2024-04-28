from flask import Flask, render_template, redirect, url_for, request


app2 = Flask(__name__)

#  наша корневая страиницу лендинда 
@app2.route('/')
def home():
    # Загрузка и отображение главной страницы (landing page)
    return render_template('landing.html') 

# страница формы логина в админ панель  
@app2.route('/adm_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # Здесь должна быть логика аутентификации
        # Если аутентификация прошла успешно, перенаправляем на панель админа (admin_panel)
        return redirect(url_for('admin_panel'))
    # Если GET запрос, показываем форму входа
    return render_template('login_adm.html')

# страница админ панели
@app2.route('/admin_panel')
def admin_panel():
    # Загрузка и отображение админ-панели
    return render_template('admin_panel.html')

if __name__ == '__main__':
    app2.run(debug=True)
