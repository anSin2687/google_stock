import packages as pkg
import data as dt

app = pkg.Flask(__name__,template_folder='template')
# <img src = "static/plot2.png" />
@app.route("/")
def index():
    today_X,today_y,X,y = dt.data_process()
    mse , prediction, perm_prediction = pkg.model.LSTM_model(today_X,today_y)

    price , datetime = pkg.plot.savefig(prediction,today_y,perm_prediction)
    return pkg.render_template("index.html",
                                stockprice = price,
                                Datetime = datetime,
                                Prediction = prediction[-1],
                                mse = mse)

if __name__ == "__main__":
    app.run(host="192.168.29.146",port=5000,debug=True)
