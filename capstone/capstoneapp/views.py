from django.shortcuts import render, redirect
from models import *
from forms import *
from django.core.urlresolvers import reverse

import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json

# Create your views here.
def index(request):
    context = {}
    return render(request, 'tool.html', context)


# def result(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = PatientForm(request.POST)
#     else:
#         form = PatientForm()
#
#     patient_id = request.POST.get('patientId')
#     print(patient_id)
#     patient = Patient.objects.get(pk=1)
#     print(patient.first_name)
#     print(patient.last_name)
#     patient_measurement = Measurement.objects.get(pk=1)
#     print(patient_measurement.age)
#     print(patient_measurement.height)
#
#     context = {}
#     # If you are using Python 3+, import urllib instead of urllib2
#     Pregnancies=patient_measurement.pregnancies
#     Glucose=patient_measurement.glucose
#     BloodPressure=patient_measurement.blood_pressure
#     SkinThickness=patient_measurement.skin_thickness
#     Insulin=patient_measurement.insulin
#     BMI=patient_measurement.bmi
#     DiabetesPedigreeFunction=patient_measurement.diabetes_predigree_function
#     Age=patient_measurement.age
#     Outcome=1
#     DoctorComments=""
#     data =  {
#         "Inputs": {
#             "input1":{
#                 "ColumnNames": ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"],
#                 "Values": [ [ Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome]]
#             },
#         },
#         "GlobalParameters": {
#         }
#     }
#
#     body = str.encode(json.dumps(data))
#
#     url = 'https://ussouthcentral.services.azureml.net/workspaces/b1f7d78580dd4c58a07358ee0bc4c192/services/37e6cf9820224c93837449ff8c97a908/execute?api-version=2.0&details=true'
#     api_key = 'gXF+v1g+42IGGOQdtKPvkj97MviDpjwTEZbhhPdX3J+hfqWIdNLIJPYTW+5akEDcOpoNju2PXg7FJJImHqH3kQ==' # Replace this with the API key for the web service
#     headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
#
#     req = urllib2.Request(url, body, headers)
#
#     try:
#         response = urllib2.urlopen(req)
#
#         # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
#         # req = urllib.request.Request(url, body, headers)
#         # response = urllib.request.urlopen(req)
#
#         result = response.read()
#         valuesResult=result.split("\"Values\":[[")[1]
#         valuesList=valuesResult.split(",")
#         size=len(valuesList)
#         finalResultString=valuesList[size-1]
#         finalResult=finalResultString[3]+finalResultString[4]+"."+finalResultString[5]+finalResultString[6]
#         print(result)
#         print(finalResult)
#     except urllib2.HTTPError, error:
#         print("The request failed with status code: " + str(error.code))
#
#         # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
#         print(error.info())
#
#         print(json.loads(error.read()))
#     context["patient_id"]=patient_id
#     context["Pregnancies"]=Pregnancies
#     context["Glucose"]=Glucose
#     context["BloodPressure"]=BloodPressure
#     context["SkinThickness"]=SkinThickness
#     context["Insulin"]=Insulin
#     context["BMI"]=BMI
#     context["DiabetesPedigreeFunction"]=DiabetesPedigreeFunction
#     context["Age"]=Age
#     context["Outcome"]=Outcome
#     context["DoctorComments"]=DoctorComments
#     context["Possibility"]=finalResult
#     return render(request, 'result.html',context)

def result(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PatientForm(request.POST)
    else:
        form = PatientForm()

    #when patient_id is 00001
    # patient_id = request.POST.get('patientId')
    # print(patient_id)
    # pk_id = patient_id.lstrip('0')
    # print(pk_id)
    # patient = Patient.objects.get(pk=pk_id)
    # print(patient.first_name)
    # print(patient.last_name)
    # patient_measurement = Measurement.objects.get(pk=pk_id)

    # Measurement.objects.get(pk=pk_id)

    # print(patient_measurement.age)
    # print(patient_measurement.height)
    patient_id = request.POST.get('patientId')
    patient = Patient.objects.get(patient_id=patient_id)
    print(patient.first_name)
    print(patient.last_name)
    patient_measurement = Measurement.objects.get(patient=patient)
    print(patient_measurement.age)
    print(patient_measurement.height)

    context = {}
    # If you are using Python 3+, import urllib instead of urllib2
    Pregnancies=patient_measurement.pregnancies
    Glucose=patient_measurement.glucose
    BloodPressure=patient_measurement.blood_pressure
    SkinThickness=patient_measurement.skin_thickness
    Insulin=patient_measurement.insulin
    BMI=patient_measurement.bmi
    DiabetesPedigreeFunction=patient_measurement.diabetes_predigree_function
    Age=patient_measurement.age
    Outcome=1
    DoctorComments=""

    data =  {
        "Inputs": {
            "input1":{
                "ColumnNames": ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"],
                "Values": [ [ Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome]]
            },
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/b1f7d78580dd4c58a07358ee0bc4c192/services/37e6cf9820224c93837449ff8c97a908/execute?api-version=2.0&details=true'
    api_key = 'gXF+v1g+42IGGOQdtKPvkj97MviDpjwTEZbhhPdX3J+hfqWIdNLIJPYTW+5akEDcOpoNju2PXg7FJJImHqH3kQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)
    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        result = response.read()
        valuesResult=result.split("\"Values\":[[")[1]
        valuesList=valuesResult.split(",")
        size=len(valuesList)
        finalResultString=valuesList[size-1]
        finalResult=finalResultString[3]+finalResultString[4]+"."+finalResultString[5]+finalResultString[6]
        print(result)
        print(finalResult)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))

    # report = Report.objects.get(id=id)

    # new_comment = request.POST.get('DoctorComments')
    # form = CommentForm(request.POST, instance=new_comment)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
    else:
        form = CommentForm()

    # DoctorComments=request.POST.get('DoctorComments')

    context["patient_id"]=patient_id
    context["Pregnancies"]=Pregnancies
    context["Glucose"]=Glucose
    context["BloodPressure"]=BloodPressure
    context["SkinThickness"]=SkinThickness
    context["Insulin"]=Insulin
    context["BMI"]=BMI
    context["DiabetesPedigreeFunction"]=DiabetesPedigreeFunction
    context["Age"]=Age
    context["Outcome"]=Outcome
    context["DoctorComments"]=DoctorComments
    context["Possibility"]=finalResult
    return render(request, 'result.html', context)

def dashboard(request):
    context={}
    # r=Report(report_id="D100058700010",date="2017-03-28 20:20:52",measurement="Pregnancies 15 Glucose 194 BloodPressure 72 SkinThickness 35",prediction="89%",suggestion="Giving Metformin oral or Humulin r injection",comments="")
    # r.save()
    records = Report.objects.all()
    context["records"]=records


    return render(request, 'dashboard.html',context)

def tool(request):
    context={}
    context['role']=request.POST['role']
    if request.POST['role']=='D':
        return render(request,'tool.html',context)
    else:
        return render(request,'p_dashboard.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)

def comment(request, id):
    context={}
    patient = Patient.objects.get(patient_id=1000)
    print(patient.first_name)
    patient_measurement = Measurement.objects.get(patient=patient)
    context["patient_id"]=id
    context["Pregnancies"]=patient_measurement.pregnancies
    context["Glucose"]=patient_measurement.glucose
    context["BloodPressure"]=patient_measurement.blood_pressure
    context["SkinThickness"]=patient_measurement.skin_thickness
    context["Insulin"]=patient_measurement.insulin
    context["BMI"]=patient_measurement.bmi
    context["DiabetesPedigreeFunction"]=patient_measurement.diabetes_predigree_function
    context["Age"]=patient_measurement.age
    context["Possibility"]=request.POST.get('Possibility')

    context["DoctorComments"]=request.POST.get('DoctorComments')
    return render(request, 'final_result.html', context)

def p_final_result(request):
    context={}
    return render(request, 'p_final_result.html', context)
