from django.shortcuts import render, redirect
from models import *
from forms import *
from django.core.urlresolvers import reverse
from datetime import datetime

import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json

# Create your views here.
def index(request):
    context = {}
    return render(request, 'tool.html', context)


def result(request, id):
    patient_id = id
    print("patient_id"+patient_id)
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PatientForm(request.POST)
    else:
        form = PatientForm()

    patient = Patient.objects.get(patient_id=patient_id)
    print(patient.first_name)
    print(patient.last_name)

    patient_measurement = Measurement.objects.get(patient=patient)
    print(patient_measurement.age)
    print(patient_measurement.height)

    reports = Report.objects.filter(patient=patient)
    count = reports.count()
    r_num = "%05d" % (count+1)
    print("report num:")
    print(count)
    print(r_num)
    report_id = "P"+patient_id+"587R"+r_num
    print("report id:")
    print(report_id)
    r_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("report date:")
    print(r_date)

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

    measurement = "Pregnancies "+str(Pregnancies)+" Glucose "+str(Glucose)+" BloodPressure "+str(BloodPressure)+" SkinThickness "+str(SkinThickness)+" Insulin "+str(Insulin)+" BMI "+str(BMI)+" DiabetesPedigreeFunction "+str(DiabetesPedigreeFunction)+" Age "+str(Age)
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

    if request.method == 'POST':
         # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
    else:
        form = CommentForm()

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
    prediction=finalResult
    suggestion="Giving Metformin oral or Humulin r injection"
    context["Suggestion"]=suggestion

    report = Report(patient=patient, report_id=report_id,date=r_date, measurement=measurement, prediction=prediction, suggestion=suggestion, comments=DoctorComments)
    report.save()
    print("rep_mea:  "+report.measurement)
    context["report_id"]=report_id

    return render(request, 'd_result.html', context)


def dashboard(request, id):
    context={}

    patient = Patient.objects.get(patient_id=id)
    records = Report.objects.filter(patient=patient)
    context["records"]=records
    context["patient_id"]=id
    return render(request, 'd_dashboard.html',context)

def tool(request):
    content={}

    # Report.objects.all().delete()
    # Measurement.objects.all().delete()
    # test=Measurement.objects.all().count()
    # print("delete m")
    # print(test)

    # p=Patient.objects.get(patient_id="1000")
    # m = Measurement(patient=p, age="50", height="178", weight="50", pregnancies="15", glucose="194", insulin="0", blood_pressure="72", skin_thickness="35", bmi="33.6", diabetes_predigree_function="0.627", heartbeat="87")
    # m.save()
    # p2=Patient.objects.get(patient_id="1001")
    # m = Measurement(patient=p2, age="31", height="145", weight="70", pregnancies="0", glucose="138", insulin="0", blood_pressure="66", skin_thickness="29", bmi="26.6", diabetes_predigree_function="0.351", heartbeat="90")
    # m.save()
    # test1=Measurement.objects.all().count()
    # print("add m")
    # print(test1)


    patient_id = request.POST.get('patient_id')
    content['patient_id'] = patient_id
    print("patientid"+content['patient_id'])
    return render(request,'tool.html', content)

def role(request):
    context={}
    context['role']=request.POST['role']
    #Check the password match the username
    print(request.POST['Username'])
    print(request.POST['Password'])

    if request.POST['role']=='D':
        return render(request,'d_patient_id.html',context)
    else:
        patient_id=request.POST['Username']

        patient = Patient.objects.get(patient_id=patient_id)
        if patient.password == request.POST['Password']:
            context['patient_id']=patient_id
            records = Report.objects.filter(patient=patient).order_by('date')
            # records = Report.objects.all()
            # posts = Post.objects.filter(user=currentUser).order_by('-time')
            # r = Report(patient=patient, report_id="D100058700014",date="2017-04-20 20:20:52",measurement="Pregnancies 100 Glucose 100 BloodPressure 100 SkinThickness 100",prediction="100%",suggestion="Giving Metformin oral or Humulin r injection",comments="")
            # r.save()
            print(records)
            context['records']=records
            return render(request,'p_dashboard.html',context)
        else:
            return render(request,'login.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)

def comment(request, id):
    context={}

    report = Report.objects.get(report_id=id)

    measurement = report.measurement
    print("measurement: "+measurement)
    m_list=measurement.split(" ")
    Pregnancies = m_list[1]
    print("Pregnancies: "+Pregnancies)
    Glucose = m_list[3]
    BloodPressure = m_list[5]
    SkinThickness = m_list[7]
    Insulin = m_list[9]
    BMI =m_list[11]
    DiabetesPedigreeFunction = m_list[13]
    Age = m_list[15]

    context["patient_id"]=report.patient.patient_id
    context["Pregnancies"]=Pregnancies
    context["Glucose"]=Glucose
    context["BloodPressure"]=BloodPressure
    context["SkinThickness"]=SkinThickness
    context["Insulin"]=Insulin
    context["BMI"]=BMI
    context["DiabetesPedigreeFunction"]=DiabetesPedigreeFunction
    context["Age"]=Age

    context["Possibility"]=report.prediction
    context["Suggestion"]=report.suggestion
    context["DoctorComments"]=request.POST.get('DoctorComments')
    report.comments = request.POST.get('DoctorComments')
    report.save()

    # Report.objects.get(report_id=id).update(comments=request.POST.get('DoctorComments'))

    return render(request, 'd_final_result.html', context)

def final_result(request, id):
    context={}
    print("p id: "+id)
    patient = Patient.objects.get(patient_id=id)
    count = Report.objects.filter(patient=patient).count()
    print("count: "+str(count))
    r_num = "%05d" % count
    print("r_num: "+r_num)
    report_id = "P"+id+"587R"+r_num
    print("report_id: "+report_id)
    report = Report.objects.get(report_id=report_id)
    print(report.measurement)

    measurement = report.measurement
    print("measurement: "+measurement)
    m_list=measurement.split(" ")
    Pregnancies = m_list[1]
    print("Pregnancies: "+Pregnancies)
    Glucose = m_list[3]
    BloodPressure = m_list[5]
    SkinThickness = m_list[7]
    Insulin = m_list[9]
    BMI =m_list[11]
    DiabetesPedigreeFunction = m_list[13]
    Age = m_list[15]


    context["patient_id"]=id
    context["Pregnancies"]=Pregnancies
    context["Glucose"]=Glucose
    context["BloodPressure"]=BloodPressure
    context["SkinThickness"]=SkinThickness
    context["Insulin"]=Insulin
    context["BMI"]=BMI
    context["DiabetesPedigreeFunction"]=DiabetesPedigreeFunction
    context["Age"]=Age

    context["Possibility"]=report.prediction
    context["Suggestion"]=report.suggestion
    context["DoctorComments"]=report.comments
    return render(request, 'd_final_result.html', context)

def p_final_result(request,id):
    context={}
    report = Report.objects.get(report_id=id)

    measurement = report.measurement
    print("measurement: "+measurement)
    m_list=measurement.split(" ")
    Pregnancies = m_list[1]
    print("Pregnancies: "+Pregnancies)
    Glucose = m_list[3]
    BloodPressure = m_list[5]
    SkinThickness = m_list[7]
    Insulin = m_list[9]
    BMI =m_list[11]
    DiabetesPedigreeFunction = m_list[13]
    Age = m_list[15]

    context["patient_id"]=report.patient.patient_id
    context["Pregnancies"]=Pregnancies
    context["Glucose"]=Glucose
    context["BloodPressure"]=BloodPressure
    context["SkinThickness"]=SkinThickness
    context["Insulin"]=Insulin
    context["BMI"]=BMI
    context["DiabetesPedigreeFunction"]=DiabetesPedigreeFunction
    context["Age"]=Age

    context["Possibility"]=report.prediction
    context["Suggestion"]=report.suggestion
    context["DoctorComments"]=report.comments

    return render(request, 'p_final_result.html', context)

def p_dashboard(request):
    context={}
    records = Report.objects.get(patient=context['patient_id'])
    print("%%%%%"+records)
    context["records"]=records
    return render(request, 'p_dashboard.html',context)


