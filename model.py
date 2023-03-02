import packages as pkg

def LSTM_model(X,y):
  lstm_model = pkg.joblib.load("finalized_model.sav")
  iterations = 0
  predictions = []
  pred = lstm_model.predict(X)
  pred = pred.round(2)
  pred = pred.flatten()
  """while iterations < 10:
    
    pred_data = pkg.np.delete(pred_data,[0,0])
    pred_data = pkg.np.append(pred_data,pred) 
    predictions.append(pred)
    pred_data = pred_data.reshape(1,5,1)
    iterations += 1"""

  for i in range(0,6):
    predic = lstm_model.predict(X)
    pred_new = predic.round(2)
    new = pkg.np.append(X[-1,:4],pred[-1]).reshape(1,5,1)
    X = pkg.np.append(X,new).reshape(X.shape[0]+1,5,1)

  predictions.append(pred_new[-5])

  mse = pkg.mse(y,pred)
  return mse,pred_new.flatten(),predictions
