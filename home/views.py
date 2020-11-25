from django.shortcuts import render
import csv
from home.models import Airport1,Airport2

# Create your views here.
def createdb1():
    csv_file = open('airport_info.csv', 'r')
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        next(csv_reader)
        x = Airport1(iata=line[0], icao=line[1], name=line[2], location=line[3], gps=line[4])
        x.save()

def createdb2():
    csv_file = open('airport_database.csv', 'r',  encoding="utf8")
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        x = Airport2(id=line[0], airport_type=line[1], airport_name=line[2], country=line[3], city=line[4],
                         iso_region=line[5], municipality=line[6], gps_code=line[7], iata=line[8], altitude=line[9],
                         continent=line[10], local_code=line[11], coordinates=line[12])
        x.save()



def getfile(request):
    data = Airport1.objects.all()
    if len(data)==0: # check if data already exists
        createdb1()
    data2 = Airport2.objects.all()
    if len(data2) == 0:# check if data already exists
        createdb2()
    return render(request, 'home.html')

def checkMissing(line):
    pct_missing = 0
    for j in range(len(line)):
        if line[j] == "unknown":
            pct_missing = pct_missing + 1
    pct = round(pct_missing / 5 * 100)
    return pct

def makeChanges(request):
    data=[]
    for i in Airport1.objects.all():
        if Airport2.objects.filter(iata=i.iata).exists():
            j=Airport2.objects.filter(iata=i.iata)
            line = [i.iata, i.icao, i.name, i.location, i.gps]
            #line2= [j.iata, j.airport_name, j.city, j.coordinates]
            row = [i.iata, i.name, j[0].airport_name,i.location, j[0].city, i.gps,j[0].coordinates]
            data.append(row)
            pct= checkMissing(line)

            if pct == 0:
                obj= Airport2.objects.get(iata=i.iata)
                obj.airport_name=i.name
                obj.city=i.location
                obj.coordinates=i.gps
                obj.local_code = i.icao
                obj.save()

    return render(request, 'changes.html', {'list':data})



def foundData(request):
    csv_infofile1 = open('D:\Internship\Github/airport/found.csv', 'w')
    csv_writer1 = csv.writer(csv_infofile1)
    csv_writer1.writerow(['iata', 'icao', 'airport_name', 'location', 'gps'])
    data=[]
    for i in Airport1.objects.all():
        line=[i.iata,i.icao,i.name,i.location,i.gps]
        pct = checkMissing(line)
        if pct == 0:
            row = [i.iata, i.icao, i.name, i.location, i.gps]
            data.append(row)
            csv_writer1.writerow([i.iata, i.icao, i.name, i.location, i.gps])
    return render(request, 'found.html',{'list': data})

def missingData(request):
    csv_infofile2 = open('D:\Internship\Github/airport/missing.csv', 'w')
    csv_writer2 = csv.writer(csv_infofile2)
    csv_writer2.writerow(['iata', 'icao', 'airport_name', 'location', 'gps'])
    data = []
    for i in Airport1.objects.all():
        line = [i.iata, i.icao, i.name, i.location, i.gps]
        pct = checkMissing(line)
        if pct > 0:
            row = [i.iata, i.icao, i.name, i.location, i.gps]
            data.append(row)
            csv_writer2.writerow([i.iata, i.icao, i.name, i.location, i.gps])

    return render(request, 'missing.html', {'list': data})