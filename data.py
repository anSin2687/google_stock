import packages as pkg


def data_process():
    time_stamp = pkg.time.time()
    date_time = pkg.datetime.fromtimestamp(time_stamp,pkg.ZoneInfo('America/New_York'))
    day = date_time.day
    month = date_time.month

    data = pkg.pd.read_csv('GoogleStock.csv')
    data['DateTime'] = data['DateTime'].astype('datetime64')
    data['Month'] = data['DateTime'].dt.month
    data['Date'] = data['DateTime'].dt.day
    data['Time'] = data['DateTime'].dt.time
    
    today = data.loc[(data['Date'] == day) & (data['Month'] == month),['Price']]
    today_X = []
    today_y = pkg.np.array(today[5:]['Price'])
    for i in range(0,today.shape[0]-5):
        today_X.append(pkg.np.array(today.iloc[i:i+5]))
    today_X = pkg.np.array(today_X)
    today_X = today_X.reshape(today_X.shape[0],today_X.shape[1],1)
    

    X = []
    y = pkg.np.array(data[5:]['Price'])
    for i in range(0,data.shape[0]-5):
        X.append(pkg.np.array(data.iloc[i:i+5]['Price']))
    X = pkg.np.array(X)
    X = X.reshape(X.shape[0],X.shape[1],1)


    return today_X,today_y,X,y
 