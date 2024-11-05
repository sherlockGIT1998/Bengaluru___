from flask  import Flask,render_template,request

from utils import BengaluruHousePrice

app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('Bengaluru House Price Prediction')
    return render_template('index.html')

@app.route('/predict_price',methods=['POST','GET'])
def get_price_info():
    if request.method == 'GET':
        print('In GET Method...')
        
        # data = request.form
        
        # availability = data['availability']
        # area_type = data['area_type']
        # location = data['location']
        # size = data['size']
        # total_sqft = data['total_sqft']
        # bath = eval(data['bath'])
        # balcony = eval(data['balcony'])
        
        availability = request.args.get('availability')
        area_type = request.args.get('area_type')
        location = request.args.get('location')
        size = request.args.get('size')
        total_sqft = request.args.get('total_sqft')
        bath = eval(request.args.get('bath'))
        balcony = eval(request.args.get('balcony'))
        
        price = BengaluruHousePrice(area_type,availability,location,size,total_sqft,bath,balcony)
        
        predict = price.get_predicted_price()
        
        return render_template('index.html',prediction=round(predict,2))
    
        # return f'Price of Bengaluru House is {round(predict,2)} Lakh/-'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run()