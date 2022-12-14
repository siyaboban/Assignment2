# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:25:00 2022

@author: siya
"""
#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    """
    

    Parameters
    ----------
    filename : excel file

    Returns
    -------
    df : dataframe with years as columns
    dftrans : dataframe with countries as columns
    
    """
    df=pd.read_excel(filename)
    print("standard deviation",np.std(df))
#transposing and returning the data
    dftrans = df.set_index('Country Name').transpose()
    return df, dftrans

#creating list of countries to plot barchart and linechart
Countries = ["Australia", "Canada", "China", "France", "India", "South Africa", "United Kingdom", "United States"]

#creating the function to filter the data in order to plot the barchart
def filter_bar_chart(df):
    df = df[['Country Name', 'Indicator Name', '1995', '2000', '2005', '2010', '2015', '2020']]
    df = df[(df["Country Name"]=="Australia")|
             (df["Country Name"]=="Canada")|
             (df["Country Name"]=="China")|
             (df["Country Name"]=="France")|
             (df["Country Name"]=="India")|
             (df["Country Name"]=="South Africa")|
             (df["Country Name"]=="United Kingdom")|
             (df["Country Name"]=="United States")]
    return df

#creating the function to filter the data in order to plot the linechart
def filter_line_chart(df):
    df = df[['Country Name', 'Indicator Name', '1995', '2000', '2005', '2010', '2015', '2020']]
    df = df[(df["Country Name"]=="Australia")|
             (df["Country Name"]=="Canada")|
             (df["Country Name"]=="China")|
             (df["Country Name"]=="France")|
             (df["Country Name"]=="India")|
             (df["Country Name"]=="South Africa")|
             (df["Country Name"]=="United Kingdom")|
             (df["Country Name"]=="United States")]
    return df
#function to plot barchart
def bar_chart(df,lab_1,lab_2):
    plt.figure(figsize=(25,16))
    ax = plt.subplot(1,1,1)
    x = np.arange(8)
    width = 0.12
    
    bar1 = ax.bar(x, df["1995"], width, label=1995)
    bar2 = ax.bar(x+width, df["2000"], width, label=2000)
    bar3 = ax.bar(x+width*2, df["2005"], width, label=2005)
    bar4 = ax.bar(x+width*3, df["2010"], width, label=2010)
    bar5 = ax.bar(x+width*4, df["2015"], width, label=2015)
    
    ax.set_xlabel("Countries", fontsize=35)
    ax.set_ylabel(lab_1, fontsize=35)
    ax.set_title(lab_2, fontsize=45)
    ax.set_xticks(x, Countries, fontsize=20)
    ax.legend(fontsize=30)
    
    ax.bar_label(bar1, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar4, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar5, padding=2, rotation=90, fontsize=18)
    plt.savefig("barchart.png")
    plt.show()
    
#function to plot linechart  
def line_chart(df,lab_1,lab_2):
    plt.figure(figsize=(25,20))
    y=df.set_index('Country Name')
    tran=y.transpose()
    tran=tran.drop(index=['Indicator Name'])
    
    for i in range(len(Countries)):
        plt.plot(tran.index,tran[Countries[i]], label=Countries[i], linestyle='dashed', linewidth='3')
        
    plt.title(lab_2, size=50)
    plt.xlabel("Years", size=35)
    plt.ylabel(lab_1, size=30)
   
    plt.legend(fontsize=30)
    plt.savefig("line_chart.png")
    plt.show()
    
#bringing the excel files by providing the path of the data using functions        
PG_data,PG_data1 = read_file("C:/Users/siya/Downloads/PG.xlsx")
PG_data= filter_bar_chart(PG_data)

CO2_data,C02_data1 = read_file("C:/Users/siya/Downloads/CO2.xlsx")
CO2_data = filter_bar_chart(CO2_data)

Fertilizer_data,Fertilizer_data1 = read_file("C:/Users/siya/Downloads/FC.xlsx")
Fertilizer_data = filter_line_chart(Fertilizer_data)
    
Cereal_data,Cereal_data1 = read_file("C:/Users/siya/Downloads/cereal yield.xlsx")
Cereal_data = filter_line_chart(Cereal_data)

#giving labels for x-axis and y-axis
bar_chart(PG_data, "Population Growth  (annual %)","Population Growth")
bar_chart(CO2_data, "CO2 Emissions (metric tons per capita)","CO2 Emissions") 

line_chart(Fertilizer_data, "Fertilizer Consumption (kilograms per hectare of arable land)", "Fertilizer Consumption")
line_chart(Cereal_data, "Cereal yield (kg per hectare)","Cereal Yield")