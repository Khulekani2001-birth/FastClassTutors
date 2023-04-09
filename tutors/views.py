from django.shortcuts import render, redirect
from .models import Tutor, CsvImportForm
# Create your views here.
import csv 
from django.http import HttpResponse, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



acc_tutors = Tutor.objects.exclude(Accounting="NA")
afrikaans_tutors =Tutor.objects.exclude(Afrikaans_Second_Language="NA")

bio_tutors = Tutor.objects.exclude(Biology_or_Life_Sciences="NA")
bus_tutors =Tutor.objects.exclude(Business="NA")

chem_tutors = Tutor.objects.exclude(Chemistry="NA")
eco_tutors =Tutor.objects.exclude(Economics="NA")

eng_tutors = Tutor.objects.exclude(English="NA")
geo_tutors =Tutor.objects.exclude(Geography="NA")

history_tutors = Tutor.objects.exclude(History="NA")

ICT_tutors =Tutor.objects.exclude(ICT="NA")
isiXhosa_tutors = Tutor.objects.exclude(isiXhosa="NA")


math_tutors = Tutor.objects.exclude(Mathematics="NA")
ap_math_tutors =Tutor.objects.exclude(Mathematics_AP="NA")

physical_tutors = Tutor.objects.exclude(Physical_Sciences="NA")


def Home(request):
    tutors = Tutor.objects.all()
    return render(request, 
                  'tutors/allTutors.html', 
                  {'tutors' : tutors}
                  )

def FilterBySubject(request, subject):
    if (subject=='Accounting'):
        tutors = acc_tutors
    if (subject=='Afrikaans_Second_Language'):
        tutors = afrikaans_tutors
    if (subject=='Biology_or_Life_Sciences'):
        tutors = bio_tutors
    if (subject=='Business'):
        tutors = bus_tutors
    if (subject=='Chemistry'):
        tutors = chem_tutors
    if (subject=='Economics'):
        tutors = eco_tutors
    if (subject=='English'):
        tutors = eng_tutors
    if (subject=='Geography'):
        tutors = geo_tutors
    if (subject=='History'):
        tutors = history_tutors
    if (subject=='ICT'):
        tutors = ICT_tutors
    if (subject=='isiXhosa'):
        tutors = isiXhosa_tutors
    if (subject=='Mathematics'):
        tutors = math_tutors
    if (subject=='Mathematics_AP'):
        tutors = ap_math_tutors
    if (subject=='Physical_Sciences'):
        tutors = physical_tutors

    if len(tutors) != 0:
        return render(request, 
                    'tutors/bySubject.html',
                    {'tutors': tutors,
                    'subject': subject,
                     },                  
                    )
    else:
        return render(request, 
                    'tutors/bySubjectNone.html',
                    {'subject': subject,}                 
                    )

def BulkUpload(request):
    if request.method == 'POST':
        form = CsvImportForm(request.POST, request.FILES)
        csv_file = request.FILES['upload_csv']
        print(csv_file.readline())
        data = csv_file.read().decode('utf-8')
        csv_data = data.split('\n')

        for i in range(len(csv_data)-1):
            fields = csv_data[i].split(",")
            print(fields)
            Tutor.objects.update_or_create(
                name = fields[0],
                surname = fields[1],
                address = fields[2],
                cell = "0"+fields[3],
                email = fields[4],
                id_or_passport = fields[5],
                academic_year = fields[6],
                degree_or_major = fields[7],
                number_of_hours = fields[8],
                Accounting = fields[9],
                Afrikaans_Second_Language = fields[10],
                Biology_or_Life_Sciences = fields[11],
                Business = fields[12],
                Chemistry = fields[13],
                Economics = fields[14],
                English = fields[15],
                Geography = fields[16],
                History = fields[17],
                ICT = fields[18],
                isiXhosa = fields[19],
                Mathematics = fields[20],
                Mathematics_AP = fields[21],
                Physical_Sciences =fields[22],
                Other_1 = fields[23],
                Other_2 = fields[24]
            )
        return redirect('home')
    form = CsvImportForm()
    return render(request, 
                  'tutors/bulkUpload.html',
                  {'form' : form}
                  )

def DownloadTutors(request,):
    buf =io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    text_ob = c.beginText()
    text_ob.setTextOrigin(inch,inch)
    text_ob.setFont('Helvetica', 14)

    tutors = Tutor.objects.all()
    lines = []
    title = "All Tutors"
    lines.append(title)
    lines.append(" ")
    for tutor in list(tutors):
        lines.append(str(tutor.name+" "+tutor.surname))
        lines.append(tutor.degree_or_major)
        lines.append(tutor.cell)
        lines.append(tutor.email)
        lines.append("========")

    for line in lines:
        print(line)
        text_ob.textLine(line)
    
    c.drawText(text_ob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename=f'All-Tutors.pdf')
    

def DownloadBySubject(request, subject):
    buf =io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    text_ob = c.beginText()
    text_ob.setTextOrigin(inch,inch)
    text_ob.setFont('Helvetica', 14)


    if (subject=='Accounting'):
        tutors = acc_tutors
    if (subject=='Afrikaans_Second_Language'):
        tutors = afrikaans_tutors
    if (subject=='Biology_or_Life_Sciences'):
        tutors = bio_tutors
    if (subject=='Business'):
        tutors = bus_tutors
    if (subject=='Chemistry'):
        tutors = chem_tutors
    if (subject=='Economics'):
        tutors = eco_tutors
    if (subject=='English'):
        tutors = eng_tutors
    if (subject=='Geography'):
        tutors = geo_tutors
    if (subject=='History'):
        tutors = history_tutors
    if (subject=='ICT'):
        tutors = ICT_tutors
    if (subject=='isiXhosa'):
        tutors = isiXhosa_tutors
    if (subject=='Mathematics'):
        tutors = math_tutors
    if (subject=='Mathematics_AP'):
        tutors = ap_math_tutors
    if (subject=='Physical_Sciences'):
        tutors = physical_tutors
    
    lines = []
    title = "Tutors for "+ str(subject)

    lines.append(title)
    lines.append(" ")
    for tutor in list(tutors):
        lines.append(str(tutor.name+" "+tutor.surname))
        lines.append(tutor.degree_or_major)
        lines.append(tutor.cell)
        lines.append(tutor.email)
        lines.append("========")

    for line in lines:
        print(line)
        text_ob.textLine(line)
    
    c.drawText(text_ob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename=f'{subject}.pdf')