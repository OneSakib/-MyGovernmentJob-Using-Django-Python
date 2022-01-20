from django.contrib import admin
from .models import JobsData, AdmitCardData, GovernmentPlan, SyllabusData, AnswerKeyData, ResultData, SchoolUniData, CertificationData, OtherData, \
    TopPost, Railway, SSC, Bank, Defence, IndianArmy, Police, State, PostComment, AdmitCardComment, ResultComment, GovtPlanComment, SyllabusComment, \
    AnswerKeyComment, CerttificationComment, OtherComment, SchoolUniComment, BankComment, DefenceComment, IndianArmyComment, PoliceComment, \
    RailwayComment, \
    SSCComment, StatesComment, ContactUs, TopMarquee, NewsPaper, NewsPaperComment, IndexCounter, Diploma, Admission, PrivateJobs, OfflineForm, DiplomaComment, AdmissionComment, \
    PrivateJobComment, OfflineFormComment, PreviousYearPaper, PreviousComment, ExamMaterial, ExamMaterialComment

# Register your models here.
admin.site.register(TopPost),
admin.site.register(PostComment),
admin.site.register(AdmitCardComment),
admin.site.register(GovtPlanComment),
admin.site.register(ResultComment),
admin.site.register(SyllabusComment),
admin.site.register(AnswerKeyComment),
admin.site.register(CerttificationComment),
admin.site.register(OtherComment),
admin.site.register(SchoolUniComment),
admin.site.register(BankComment),
admin.site.register(DefenceComment),
admin.site.register(IndianArmyComment),
admin.site.register(PoliceComment),
admin.site.register(RailwayComment),
admin.site.register(SSCComment),
admin.site.register(StatesComment),
admin.site.register(ContactUs),
admin.site.register(TopMarquee),
admin.site.register(NewsPaper),
admin.site.register(NewsPaperComment),
admin.site.register(IndexCounter),
admin.site.register(DiplomaComment),
admin.site.register(AdmissionComment),
admin.site.register(PrivateJobComment),
admin.site.register(OfflineFormComment),
admin.site.register(PreviousYearPaper),
admin.site.register(PreviousComment),
admin.site.register(ExamMaterial),
admin.site.register(ExamMaterialComment),


@admin.register(Diploma)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(Admission)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(PrivateJobs)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(OfflineForm)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(JobsData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(CertificationData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(Bank)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(Defence)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(GovernmentPlan)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(IndianArmy)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(OtherData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(Police)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(Railway)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(SchoolUniData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(SSC)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(State)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(AdmitCardData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(SyllabusData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(ResultData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


@admin.register(AnswerKeyData)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)
