import statistics;
import plotly.graph_objects as go;
import plotly.figure_factory as ff;
import pandas as pd;
import random;
data = pd.read_csv("data.csv")
dataList = data["reading_time"].tolist()

populationMean = statistics.mean(dataList)
print("Population Mean:",populationMean)

def random_mean_set(counter):
  dataSet = []
  for i in range(0,counter):
    randomIndex = random.randint(0,len(dataList))
    value = dataList[randomIndex]
    dataSet.append(value)
  randomMean = statistics.mean(dataSet)
  return randomMean

def show_fig(meanList):
  figData = meanList

  fig = ff.create_distplot([figData],["Reading Time"],show_hist = False)

  samplingMean = statistics.mean(meanList)
  sd = statistics.stdev(meanList)
  
  std1_str,std1_end = samplingMean - std,samplingMean + std
  std2_str,std2_end = samplingMean - (2*std),samplingMean + (2*std)
  std3_str,std3_end = samplingMean - (3*std),samplingMean + (3*std)
  
  print("Standard Deviation 1:",std1_str,",",std1_end)
  print("Standard Deviation 2:",std2_str,",",std2_end)
  print("Standard Deviation 3:",std3_str,",",std3_end)

  fig.add_trace(go.Scatter(x = [std1_str,std1_str],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std1_end,std1_end],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std2_str,std2_str],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std2_end,std2_end],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std3_str,std3_str],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std3_end,std3_end],y = [0,0.8]))


  fig.add_trace(go.Scatter(x = [samplingMean,samplingMean],y = [0,0.8]))
  sampleMean = statistics.mean(dataList)
  fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.8]))
  
  zTest = (sampleMean - samplingMean)/std
  print("Z Test:",zTest)

  fig.show()



