from django.shortcuts import redirect, render
from django.contrib import messages
import warnings
from django.http import HttpResponseRedirect
import pandas as pd
from datetime import datetime
import pickle
import numpy as np
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

warnings.filterwarnings("ignore")

def getPredictions(date):
    filename = "ml_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))

    df = pd.read_csv("TSLA.csv")
    
    date = datetime.strptime(date, "%d-%m-%Y")
    start_Date = datetime.strptime("21-10-2020", "%d-%m-%Y")
    delta = date - start_Date
    
    days = delta.days
    
    y_predicted = loaded_model[2].predict([[days]])
    y = df["Close"].values
    final_list = [ str(y_predicted[0])]
    
    return final_list

# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/login/')
def predict(request):
    if request.method == "POST":
        day1 = request.POST['day']
        month1 = request.POST['month']
        year1 = request.POST['year']

        final_str = str(day1) + '-' + str(month1) + '-' + str(year1)

        result = getPredictions(final_str)
        print("Predicted Tesla stock closing value: " + str(result[0]))
        messages.info(request, "Predicted Tesla stock closing value : " + str(result[0]) )
        return HttpResponseRedirect(request.path_info)
    else:
        return render(request,'prediction/pred.html')

