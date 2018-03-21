import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def autoLabelInt(rects, ax):

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,'%d' % height,ha='center', va='bottom')


def autoLabelFloat(rects, ax):

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,'%.2f' % height,ha='center', va='bottom')


def barPlot(x,y,title, ylabel, ax=None):

    if ax is None:
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = 8
        fig_size[1] = 5
        plt.rcParams["figure.figsize"] = fig_size       
        fig, ax = plt.subplots()    
    rect = ax.bar(range(len(y)),y)
    ax.set_xticks(range(len(y)))
    ax.set_xticklabels(x)
    ax.set_ylabel(ylabel)
    
    if all(isinstance(i, int) for i in y):
        autoLabelInt(rect,ax)
    else:
        autoLabelFloat(rect,ax)
    plt.title(title)
    plt.xticks(rotation=20)



def getTopAirportFrom(df):
    
    queryResult = df.groupby('5').size()
    queryResult = queryResult.sort_values(ascending=False)
    queryResult = queryResult[0:10]
    airports = queryResult.index.values
    countSearchs = queryResult.values
    countSearchs = [int(i) for i in countSearchs]
    return airports, countSearchs


def getTopAirportTo(df):
    
    queryResult = df.groupby('6').size()
    queryResult = queryResult.sort_values(ascending=False)
    queryResult = queryResult[0:10]
    airports = queryResult.index.values
    countSearchs = queryResult.values
    countSearchs = [int(i) for i in countSearchs]
    return airports, countSearchs


def filterToFlights(df):
    df = df[df['4']=='Ida']
    return df


def filterFromToFlights(df):
    df = df[df['4']=='Ida/Volta']
    return df


def countTypeOfFlights(df):
    
    df = df.iloc[:,4]
    df.name='Tipo de voo'
    print(df.groupby(df).size())


def topAirportsOnlyToFlights(df):

    df = filterToFlights(df)
    topAirportsFrom, countSearchsFrom = getTopAirportFrom(df)
    topAirportsTo, countSearchsTo = getTopAirportTo(df)

    fig = plt.figure(figsize = (15,5))
    ax1 = fig.add_subplot(1,2,1)
    barPlot(topAirportsFrom, countSearchsFrom,'Origens mais procuradas para voos executivos (Ida)','Número de buscas',ax1)
    ax2 = fig.add_subplot(1,2,2)
    barPlot(topAirportsTo, countSearchsTo,'Destinos mais procurados para voos executivos (Ida)','Número de buscas',ax2)
    plt.show()
    plt.close()


def topAirportsFromToFlights(df):

    df = filterFromToFlights(df)
    topAirportsFrom, countSearchsFrom = getTopAirportFrom(df)
    topAirportsTo, countSearchsTo = getTopAirportTo(df)

    fig = plt.figure(figsize = (15,5))
    ax1 = fig.add_subplot(1,2,1)
    barPlot(topAirportsFrom, countSearchsFrom,'Origens mais procuradas para voos executivos (Ida/Volta)','Número de buscas',ax1)
    ax2 = fig.add_subplot(1,2,2)
    barPlot(topAirportsTo, countSearchsTo,'Destinos mais procurados para voos executivos (Ida/Volta)','Número de buscas',ax2)
    plt.show()
    plt.close()


def averageTripDuration(df):

    df = filterFromToFlights(df)
    airports,_ = getTopAirportTo(df)

    df = df[df['6'].isin(airports)]
    df = df.loc[:, ['6', '9']]
    df = df.groupby(['6']).mean()
    df = df.sort_values(ascending=False, by='9')
    x, y = df.index.tolist(), df.values
    barPlot(x, y,'Duração da viagem nos destinos mais procurados','Média de dias')
    plt.show()
    plt.close()


def averageSearchDuration(df):

    airports,_ = getTopAirportTo(df)
    df = df[df['6'].isin(airports)]
    df = df.loc[:, ['6', '22']]
    idx = df.index[df['22'] < 0].tolist()
    df.loc[idx,'22'] = 0
    df = df.groupby(['6']).mean()
    df = df.sort_values(ascending=False,by='22')
    x, y = df.index.tolist(), df.values
    barPlot(x, y,'Duração das buscas nos destinos mais procurados','Média de tempo (seg)')
    plt.show()
    plt.close()


def relationTopAirports(df):
    
    df = filterFromToFlights(df)
    airportsFrom,_ = getTopAirportFrom(df)
    airportsTo,_ = getTopAirportTo(df)
    
    df = df[(df['5'].isin(airportsFrom)) & (df['6'].isin(airportsTo))]
    result = df.groupby(['5','6']).size()

    X = np.zeros((10,10))

    for i in range(len(airportsFrom)):
        for j in range(len(airportsTo)):
            try:
                X[i,j] = result[(airportsFrom[i],airportsTo[j])]
            except Exception as e:
                pass

    df = pd.DataFrame(X.astype(int), index=airportsFrom, columns=airportsTo)

    plt.figure(figsize = (8,5))
    sns.heatmap(df, annot=True,fmt='d', cmap="YlGnBu")
    plt.show()
    plt.close()


def relationTopAirportsAirlines(df):
    
    df = filterFromToFlights(df)
    airportsTo,_ = getTopAirportTo(df)
    airlines = df.groupby('3').size().index.tolist()
    
    df = df[df['6'].isin(airportsTo)]
    result = df.groupby(['3','6']).size()

    X = np.zeros((3,10))

    for i in range(len(airlines)):
        for j in range(len(airportsTo)):
            try:
                X[i,j] = result[(airlines[i],airportsTo[j])]
            except Exception as e:
                pass

    df = pd.DataFrame(X.astype(int), index=airlines, columns=airportsTo)

    plt.figure(figsize = (8,5))
    sns.heatmap(df, annot=True,fmt='d', cmap="YlGnBu")
    plt.show()
    plt.close()