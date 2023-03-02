import packages as pkg
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg



def create_xtiklabels(data,xtick):
  xticklabels = []
  for xtik in range(0,len(xtick)):
      try :
          index = int(str(xtick[xtik]).split("'")[1])
          if data.iloc[index]['Time']:
              xticklabels.append(data.iloc[index]['Time'])
          else:
              xticklabels.append(str(index))
      except :
          xticklabels.append(str(xtick[xtik]).split("'")[1])
  return xticklabels

def savefig(pred,y,perm_pred):  
  stockprice = y[-1]
  y = pkg.pd.Series(y)
  pred = pkg.pd.Series(pred)
  perm_pred = pkg.pd.Series(perm_pred,index=[y.shape[0]])
  print(y.shape,pred.shape)
  datetime = pkg.datetime.fromtimestamp(pkg.time.time(),pkg.ZoneInfo('America/New_York'))
  #indx=today.index[-1]
  #pred = pkg.pd.Series(pred,index=[i for i in range(indx,indx+10)])
  fig = Figure(figsize=(10,5))
  ax = fig.add_subplot(111)
  ax.plot(y.iloc[-10:],c='blue',marker='o')
  ax.plot(pred[y.shape[0]-10:],c='orange',marker='o')
  ax.plot(perm_pred,c='red',marker='o')
  ax.legend(['actual','pred'])
  #ax.set_xticklabels(create_xtiklabels(data,ax.get_xticklabels()))
  #ax.set_xlabel("Time")
  ax.set_ylabel("Price")
  canvas = FigureCanvasAgg(fig)
  canvas.print_figure("static/plot2.png", dpi=120)
  return stockprice,datetime