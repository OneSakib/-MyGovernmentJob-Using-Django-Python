from django.db import models

# Create your models here.
from django.utils.timezone import now

newspaper_category = (
    ("THE_HINDU", "THE HINDU"),
    ("TIMES_OF_INDIA", "TIMES OF INDIA"),
    ("HINDUSTAN_TIMES", "HINDUSTAN TIMES"),
    ("AMAR_UJALA", "AMAR UJALA"),
    ("DAINIK_JAGRAN", "DAINIK JAGRAN"),

)
ExamMaterialCategory = (
    ('currentaffairs', 'Current Affairs'),
    ('gk', 'Gk'),
    ('math', 'Math'),
    ('advancemath', 'Advance Math'),
    ('savidhan', "Bhartiya Savidhan"),
    ('hindi', 'Hindi'),
    ('english', 'English'),
    ('reasoning', 'Reasoning'),
    ('ccc', 'CCC'),
    ('geography', 'Geography'),
    ('history', 'Indian History'),
    ('economy', 'Indian Economy'),
    ('science', 'Science'),
    ('other', 'Other'),
    ('computer', 'Computer'),
    ('allbook', 'All Book'),
)
POST_CATEGORY = (
    ("bank", "Bank"),
    ("railway", "Railway"),
    ("ssc", "SSC"),
    ("defence", "Defence"),
    ("army", "Indian Army"),
    ("police", "Police"),
    ("other", "Other"),
    ("state", "State"),
)
PREVIOUS_CATEGORY = (
    ('ntpc', 'RRB NTPC'),
    ('groupd', 'RRB Group D'),
    ('locopilot', 'RRB Loco Pilot'),
    ('rjunior', 'RRB Junior Engineer'),
    ('rother', 'RRB Other'),
    ('cgl', 'SSC CGL'),
    ('gd', 'SSC GD'),
    ('stenographer', 'SSC Stenographer'),
    ('mts', 'SSC MTS'),
    ('cpo', 'SSC CPO'),
    ('sscgraduate', 'SSC Graduate Lavel'),
    ('chsl', 'SSC CHSL'),
    ('sother', 'SSC Other'),
    ('cds', 'Defence CDS'),
    ('indiannavy', 'Defence Indian Navy'),
    ('indianairforce', 'Defence Indian Air Force'),
    ('dother', 'Defence Other'),
    ('allbank', 'Bank'),
    ('uppolice', 'UP Police'),
    ('hrpolice', 'Haryana Police'),
    ('delhipolice', 'Delhi Police'),
    ('biharpolice', 'Bihar Police'),
    ('upstate', 'Up State'),
    ('hrstate', 'Haryana State'),
    ('delhistate', 'Delhi State'),
    ('biharstate', 'Bihar State'),
)
COLOR = (
    ('bg-secondary', 'Secondary'),
    ('bg-info', 'Info'),
    ('bg-danger', 'Danger'),
    ('bg-warning', 'Warning'),
    ('bg-primary', 'Primary'),
    ('bg-success', 'Success'),
    ('bg-dark', 'Dark')
)


class IndexCounter(models.Model):
    viewc = models.IntegerField(default=0)

    def __str__(self):
        return "View Counter"


class JobsData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(JobsData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    post_name = models.CharField(default="", max_length=200)
    post_category = models.CharField(default="", max_length=50, choices=POST_CATEGORY)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    last_date = models.DateField(blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.post_name


class AdmitCardData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(AdmitCardData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    admit_card_name = models.CharField(max_length=600, default="")
    post_name = models.CharField(default="", max_length=200)
    post_category = models.CharField(default="", max_length=50, choices=POST_CATEGORY)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    post_information = models.CharField(default="", max_length=1000)
    admit_card_date = models.CharField(default="", max_length=30)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.admit_card_name


class SyllabusData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(SyllabusData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    syllabus_name = models.CharField(max_length=600, default="")
    post_name = models.CharField(default="", max_length=200)
    post_category = models.CharField(default="", max_length=50, choices=POST_CATEGORY)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.syllabus_name


class AnswerKeyData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(AnswerKeyData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    answerkey_name = models.CharField(max_length=600, default="")
    post_name = models.CharField(default="", max_length=200)
    post_category = models.CharField(default="", max_length=50, choices=POST_CATEGORY)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.answerkey_name


class ResultData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(ResultData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    result_name = models.CharField(max_length=600, default="")
    post_name = models.CharField(default="", max_length=200)
    post_category = models.CharField(default="", max_length=50, choices=POST_CATEGORY)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.result_name


class SchoolUniData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(SchoolUniData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    post_name = models.CharField(default="", max_length=200)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    last_date = models.DateField(blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.post_name


class CertificationData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(CertificationData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    post_name = models.CharField(default="", max_length=200)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    last_date = models.DateField(blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.post_name


class OtherData(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(OtherData, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    post_name = models.CharField(default="", max_length=200)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    post_date_update = models.DateTimeField(auto_now_add=True, blank=True)
    last_date = models.DateField(blank=True)
    post_information = models.CharField(default="", max_length=1000)
    post_detail = models.TextField(default="")

    def __str__(self):
        return self.post_name


class GovernmentPlan(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(GovernmentPlan, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    plan_name = models.CharField(max_length=600, default="")
    plan_date = models.DateTimeField(blank=True, null=True)
    plan_date_update = models.DateTimeField(blank=True, null=True)
    plan_last_date = models.DateField(blank=True)
    plan_info = models.CharField(default="", max_length=1000)
    plan_detail = models.TextField(default="")

    def __str__(self):
        return self.plan_name


class Diploma(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(Diploma, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    plan_name = models.CharField(max_length=600, default="")
    plan_date = models.DateTimeField(blank=True, null=True)
    plan_date_update = models.DateTimeField(blank=True, null=True)
    plan_last_date = models.DateField(blank=True)
    plan_info = models.CharField(default="", max_length=1000)
    plan_detail = models.TextField(default="")

    def __str__(self):
        return self.plan_name


class Admission(models.Model):
    viewc = models.IntegerField(default=0)

    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(Admission, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    plan_name = models.CharField(max_length=600, default="")
    plan_date = models.DateTimeField(blank=True, null=True)
    plan_date_update = models.DateTimeField(blank=True, null=True)
    plan_last_date = models.DateField(blank=True)
    plan_info = models.CharField(default="", max_length=1000)
    plan_detail = models.TextField(default="")

    def __str__(self):
        return self.plan_name


class PrivateJobs(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(PrivateJobs, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    plan_name = models.CharField(max_length=600, default="")
    plan_date = models.DateTimeField(blank=True, null=True)
    plan_date_update = models.DateTimeField(blank=True, null=True)
    plan_last_date = models.DateField(blank=True)
    plan_info = models.CharField(default="", max_length=1000)
    plan_detail = models.TextField(default="")

    def __str__(self):
        return self.plan_name


class OfflineForm(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=600, default='')

    def save(self):
        if not self.s_no:
            self.slug = self.slug.replace(" ", "-")
        super(OfflineForm, self).save()

    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    title = models.CharField(default="", max_length=200)
    plan_name = models.CharField(max_length=600, default="")
    plan_date = models.DateTimeField(blank=True, null=True)
    plan_date_update = models.DateTimeField(blank=True, null=True)
    plan_last_date = models.DateField(blank=True)
    plan_info = models.CharField(default="", max_length=1000)
    plan_detail = models.TextField(default="")

    def __str__(self):
        return self.plan_name


class TopPost(models.Model):
    post_name = models.CharField(max_length=600, default="")
    color = models.CharField(max_length=20, choices=COLOR, default="")
    link = models.CharField(max_length=600, default='/')

    def __str__(self):
        return self.post_name


class TopMarquee(models.Model):
    s_no = models.AutoField(primary_key=True)
    post_name1 = models.CharField(max_length=600, default="")
    link1 = models.CharField(max_length=600, default='/')
    post_name2 = models.CharField(max_length=600, default="")
    link2 = models.CharField(max_length=600, default='/')
    post_name3 = models.CharField(max_length=600, default="")
    link3 = models.CharField(max_length=600, default='/')
    post_name4 = models.CharField(max_length=600, default="")
    link4 = models.CharField(max_length=600, default='/')
    post_name5 = models.CharField(max_length=600, default="")
    link5 = models.CharField(max_length=600, default='/')
    post_name6 = models.CharField(max_length=600, default="")
    link6 = models.CharField(max_length=600, default='/')
    post_name7 = models.CharField(max_length=600, default="")
    link7 = models.CharField(max_length=600, default='/')
    post_name8 = models.CharField(max_length=600, default="")
    link8 = models.CharField(max_length=600, default='/')
    post_name9 = models.CharField(max_length=600, default="")
    link9 = models.CharField(max_length=600, default='/')
    post_name10 = models.CharField(max_length=600, default="")
    link10 = models.CharField(max_length=600, default='/')
    post_name11 = models.CharField(max_length=600, default="")
    link11 = models.CharField(max_length=600, default='/')
    post_name12 = models.CharField(max_length=600, default="")
    link12 = models.CharField(max_length=600, default='/')

    def __str__(self):
        return "Marquee Data "


class Railway(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class SSC(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class Bank(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class IndianArmy(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class Defence(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class Police(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class State(models.Model):
    viewc = models.IntegerField(default=0)
    s_no = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    name = models.CharField(max_length=800, default="")
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(JobsData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class AdmitCardComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(AdmitCardData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class ResultComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(ResultData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class GovtPlanComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(GovernmentPlan, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class SyllabusComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(SyllabusData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class AnswerKeyComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(AnswerKeyData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class CerttificationComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(CertificationData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class OtherComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(OtherData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class SchoolUniComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(SchoolUniData, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class AdmissionComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(Admission, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class DiplomaComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(Diploma, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class PrivateJobComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(PrivateJobs, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class OfflineFormComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(OfflineForm, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class BankComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class DefenceComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class IndianArmyComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class PoliceComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class RailwayComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class SSCComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class StatesComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class ContactUs(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    phone = models.CharField(default="", max_length=4000)
    comment = models.TextField()

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class NewsPaper(models.Model):
    viewc = models.IntegerField(default=0)
    sno = models.AutoField(primary_key=True)
    meta_desc = models.CharField(max_length=4000,
                                 default="MyGovernment Jobs On Fill the Online Government Job Form Easily You Can Find the Any type of Job in this Website You can Set the notification for the Next Government Job")
    meta_keywords = models.CharField(max_length=4000,
                                     default="Government Jobs,Sarkari Jobs,Government Naukari,Sarkari Naukari,Online Exam Online "
                                             "Government Jobs,Sarkari Result, latest sarkari results, Sarkariresult, Sarkari, "
                                             "Sarkariresults,Samani Computers Online Form,CCSU,Aktu,CCSU Online Exam,Aktu Online Exam"
                                             "Up Board Results,Intermediate Results ,Uttar Pradesh Board,Uttar Pradesh Yojnaye, सरकारी नौकरी,ccs यूनिवर्सिटी ऑनलाइन फॉर्म,AKTU ऑनलाइन फॉर्म,UP बोर्ड रिजल्ट, 12 रिजल्ट,10 रिजल्ट ")
    category = models.CharField(default="", choices=newspaper_category, max_length=400)
    timestamp = models.DateField(default=now)
    news_link = models.CharField(default="", max_length=500)

    def __str__(self):
        return self.category


class NewsPaperComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class PreviousYearPaper(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(choices=PREVIOUS_CATEGORY, max_length=100)
    name = models.CharField(default="", max_length=400)
    size = models.CharField(default="", max_length=10)
    image = models.ImageField(upload_to='media/', default="")
    link = models.CharField(default="", max_length=500)

    def __str__(self):
        return self.name


class PreviousComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name


class ExamMaterial(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(choices=ExamMaterialCategory, max_length=100)
    name = models.CharField(default="", max_length=400)
    size = models.CharField(default="", max_length=10)
    image = models.ImageField(upload_to='media/', default="")
    link = models.CharField(default="", max_length=500)

    def __str__(self):
        return self.name


class ExamMaterialComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name
