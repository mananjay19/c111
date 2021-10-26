import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()
#fig = ff.create_distplot([data],['Math_score'],show_hist = False)
#fig.show()
mean = statistics.mean(data)
std  = statistics.stdev(data)
print('population mean',mean)
print('population std',std)
def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
meanlist=[]
for i in range(0,1000):
    setofmeans = randomsetofmean(100)
    meanlist.append(setofmeans)
samplemean=statistics.mean(meanlist)
samplestd=statistics.stdev(meanlist)
print(samplemean,'samplemean')
print(samplestd,'samplestd')
# fig=ff.create_distplot([meanlist],['studentMarks'],show_hist=False)
fsds,fsde=samplemean - samplestd,samplemean + samplestd
ssds,ssde=samplemean - 2*samplestd,samplemean + 2*samplestd
tsds,tsde=samplemean - 3*samplestd,samplemean + 3*samplestd
# print('sdt1',fsds,fsde)
# print('sdt2',ssds,ssde)
# print('sdt3',tsds,tsde)
# fig.add_trace(go.Scatter(x=[samplemean,samplemean],y=[0,0.17],mode='lines',name='mean'))
# fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode='lines',name='fsds'))
# fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode='lines',name='fsde'))
# fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode='lines',name='ssds'))
# fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode='lines',name='ssde'))
# fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode='lines',name='tsds'))
# fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode='lines',name='tsde'))
# fig.show()
df=pd.read_csv('data3.csv')
data=df['Math_score'].tolist()
samplemean1=statistics.mean(data)
samplestd1=statistics.stdev(data)
print('mean of sample 1',samplemean1)
print('std of sample 1',samplestd1)
fig=ff.create_distplot([meanlist],['studentMarks'],show_hist=False)
fig.add_trace(go.Scatter(x=[samplemean1,samplemean1],y=[0,0.17],mode='lines',name='meansample1'))
fig.add_trace(go.Scatter(x=[samplemean,samplemean],y=[0,0.17],mode='lines',name='samplemean'))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode='lines',name='fsde'))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode='lines',name='ssde'))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode='lines',name='tsde'))
fig.show()
zscore=(samplemean1-samplemean)/samplestd
print(zscore)