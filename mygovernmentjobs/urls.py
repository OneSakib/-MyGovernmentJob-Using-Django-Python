"""mygovernmentjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "MyGovernmentJob.co.in "
admin.site.site_title = "My MyGovernment Job Admin Portal"
admin.site.index_title = "My MyGovernment Job"
urlpatterns = [
    path("", views.index, name="Index Page "),
    path("jobs/<str:slug>", views.jobs, name="Details of the Post"),
    path("admitcard/<str:slug>", views.admitcard, name="Details of the Admit Card"),
    path("govtplan/<str:slug>", views.govtplan, name="View govtplan"),
    path("private/<str:slug>", views.private, name="View govtplan"),
    path("diploma/<str:slug>", views.diploma, name="View govtplan"),
    path("admission/<str:slug>", views.admission, name="View govtplan"),
    path("offline/<str:slug>", views.offline, name="View govtplan"),
    path("syllabus/<str:slug>", views.syllabus, name="View syllabus"),
    path("schooluni/<str:slug>", views.schooluni, name="View School Univesity"),
    path("certification/<str:slug>", views.certification, name="View Certification"),
    path("other/<str:slug>", views.other, name="View other"),
    path("answerkey/<str:slug>", views.answerkey, name="View Answer Key"),
    path("result/<str:slug>", views.result, name="View Result"),
    path("contactus", views.contactus, name="View Contact Us "),
    path("aboutus", views.aboutus, name="View About Us"),
    path("ssc", views.ssc, name="View About Us"),
    path("railway", views.railway, name="View About Us"),
    path("bank", views.bank, name="View About Us"),
    path("defence", views.defence, name="View About Us"),
    path("army", views.army, name="View About Us"),
    path("state", views.state, name="state page"),
    path("police", views.police, name="View About Us"),
    path("allbasic/<str:slug>", views.allbasic, name="View About Us"),
    path("PostComment", views.PostComments, name="Comments"),
    path("AdmitCardComment", views.AdmitCardComments, name="Comments"),
    path("BankComment", views.BankComments, name="Comments"),
    path("CertificationComment", views.CertificationComments, name="Comments"),
    path("DefencesComment", views.DefencesComments, name="Comments"),
    path("GovtPlanComment", views.GovtPlanComments, name="Comments"),
    path("PrivateComment", views.PrivateComments, name="Comments"),
    path("OfflineComment", views.OfflineComments, name="Comments"),
    path("AdmissionComment", views.AdmissionComments, name="Comments"),
    path("DiplomaComment", views.DiplomaComments, name="Comments"),
    path("IndianArmyComment", views.IndianArmyComments, name="Comments"),
    path("OtherComment", views.OtherComments, name="Comments"),
    path("PoliceComment", views.PoliceComments, name="Comments"),
    path("RailwayComment", views.RailwayComments, name="Comments"),
    path("ResultComment", views.ResultComments, name="Comments"),
    path("SchoolUniComment", views.SchoolUniComments, name="Comments"),
    path("SSCComment", views.SSCComments, name="Comments"),
    path("StateComment", views.StatesComments, name="Comments"),
    path("SyllabusComment", views.SyllabusComments, name="Comments"),
    path("AnswerKeyComment", views.AnswerKeyComments, name="Comments"),
    path("NewsPaperComment", views.NewsPaperComments, name="Comments"),
    path("search", views.search, name="search page"),
    path("newspaper/<str:slug>", views.newspaper, name="News Paper page"),
    path("previouspaper/<str:slug>", views.Previouspaper, name="News Paper page"),
    path("PreviousPaperComment", views.PreviousPaperComments, name="News Paper page Comment"),
    path("exammaterial/<str:slug>", views.ExamMaterials, name="Exam material"),
    path("ExamMaterialComment", views.ExamMaterialComments, name="exam material Comment")

]
