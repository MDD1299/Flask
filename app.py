from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/ml')
def ml():
    return render_template('ml.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    select_ = request.form.get('pos_lvl')
    exp_ = request.form.get('experience')
    # print(select_)
    # print('form val: ', request.form.values())
    int_features = [select_, exp_]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    res = prediction.item()
    return render_template('ml.html', prediction_text='Expected Salary Rate should be $ {}'.format(res) )

#Still need model from data scraping
#model = predict.load(open('C:/Users/itsloudc/webdev/flask_app/model.pkl', 'rb'))
