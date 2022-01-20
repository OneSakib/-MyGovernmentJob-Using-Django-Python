from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import JobsData, AdmitCardData, GovernmentPlan, SyllabusData, ResultData, AnswerKeyData, SchoolUniData, CertificationData, OtherData, \
    TopPost, Railway, SSC, Bank, Defence, IndianArmy, Police, State, PostComment, AdmitCardComment, AnswerKeyComment, BankComment, \
    CerttificationComment, DefenceComment, GovtPlanComment, SSCComment, RailwayComment, ResultComment, SyllabusComment, IndianArmyComment, \
    OtherComment, \
    PoliceComment, SchoolUniComment, StatesComment, ContactUs, TopMarquee, NewsPaper, NewsPaperComment, IndexCounter, Diploma, DiplomaComment, AdmissionComment, Admission, PrivateJobComment, \
    PrivateJobs, OfflineFormComment, OfflineForm, PreviousYearPaper, PreviousComment, ExamMaterial, ExamMaterialComment


def index(request):
    indexc = IndexCounter.objects.all()[0]
    indexc.viewc = indexc.viewc + 1
    indexc.save()
    alljobs = JobsData.objects.values('title', 'post_date_update', 'last_date', 'slug').order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.values('title', 'post_date_update', 'admit_card_date', 'slug').order_by('post_date_update')[::-1]
    allgovtpan = GovernmentPlan.objects.values('title', 'plan_last_date', 'plan_date_update', 'slug').order_by('plan_date_update')[::-1]
    allprivate = PrivateJobs.objects.values('title', 'plan_last_date', 'plan_date_update', 'slug').order_by('plan_date_update')[::-1]
    alloffline = OfflineForm.objects.values('title', 'plan_last_date', 'plan_date_update', 'slug').order_by('plan_date_update')[::-1]
    alladmission = Admission.objects.values('title', 'plan_last_date', 'plan_date_update', 'slug').order_by('plan_date_update')[::-1]
    alldiploma = Diploma.objects.values('title', 'plan_last_date', 'plan_date_update', 'slug').order_by('plan_date_update')[::-1]
    syllabusdata = SyllabusData.objects.values('title', 'post_date_update', 'slug').order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.values('title', 'post_date_update', 'slug').order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.values('title', 'post_date_update', 'slug').order_by('post_date_update')[::-1]
    schoolunidata = SchoolUniData.objects.values('title', 'post_date_update', 'last_date', 'slug').order_by('post_date_update')[::-1]
    certificationdata = CertificationData.objects.values('title', 'post_date_update', 'last_date', 'slug').order_by('post_date_update')[::-1]
    otherdata = OtherData.objects.values('title', 'post_date_update', 'last_date', 'slug').order_by('post_date_update')[::-1]
    toppost = TopPost.objects.all()
    topmarquees = TopMarquee.objects.all()
    params = {'alljobs': alljobs[0:20], 'alladmitcard': alladmitcard[0:20], 'allgovtplan': allgovtpan[0:20], 'alladmission': alladmission[0:20], 'alldiploma': alldiploma[0:20], 'alloffline': alloffline[0:20], 'allprivate': allprivate[0:20], 'syllabusdata': syllabusdata[0:20],
              'resultdata': resultsdata[0:20], 'answerkeydata': answerkeydata[0:20], 'schoolunidata': schoolunidata[0:20],
              "certificationdata": certificationdata[0:20], "otherdata": otherdata[0:20], 'toppost': toppost, 'topmarquee': topmarquees[0],
              'viewcounter': indexc.viewc}

    return render(request, "index.html", params)


def jobs(requset, slug):
    jobs = JobsData.objects.get(slug=slug)
    jobs.viewc = jobs.viewc + 1
    jobs.save()
    toppost = TopPost.objects.all()
    comments = PostComment.objects.filter(post=jobs, parent=None)
    replies = PostComment.objects.filter(post=jobs).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'jobs': jobs, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "jobs.html", params)


def admitcard(requset, slug):
    admit = AdmitCardData.objects.get(slug=slug)
    admit.viewc = admit.viewc + 1
    admit.save()
    comments = AdmitCardComment.objects.filter(post=admit, parent=None)
    replies = AdmitCardComment.objects.filter(post=admit).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    toppost = TopPost.objects.all()
    params = {'admitcard': admit, 'jobs': jobs, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "admitcard.html", params)


def govtplan(requset, slug):
    govtplans = GovernmentPlan.objects.get(slug=slug)
    govtplans.viewc = govtplans.viewc + 1
    govtplans.save()
    toppost = TopPost.objects.all()
    comments = GovtPlanComment.objects.filter(post=govtplans, parent=None)
    replies = GovtPlanComment.objects.filter(post=govtplans).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    parmas = {'govtplan': govtplans, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "govtplan.html", parmas)


def diploma(requset, slug):
    diplomas = Diploma.objects.get(slug=slug)
    diplomas.viewc = diplomas.viewc + 1
    diplomas.save()
    toppost = TopPost.objects.all()
    comments = DiplomaComment.objects.filter(post=diplomas, parent=None)
    replies = DiplomaComment.objects.filter(post=diplomas).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    parmas = {'diploma': diplomas, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "diploma.html", parmas)


def admission(requset, slug):
    admissions = Admission.objects.get(slug=slug)
    admissions.viewc = admissions.viewc + 1
    admissions.save()
    toppost = TopPost.objects.all()
    comments = AdmissionComment.objects.filter(post=admissions, parent=None)
    replies = AdmissionComment.objects.filter(post=admissions).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    parmas = {'admission': admissions, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "admission.html", parmas)


def private(requset, slug):
    privatejobs = PrivateJobs.objects.get(slug=slug)
    privatejobs.viewc = privatejobs.viewc + 1
    privatejobs.save()
    toppost = TopPost.objects.all()
    comments = PrivateJobComment.objects.filter(post=privatejobs, parent=None)
    replies = PrivateJobComment.objects.filter(post=privatejobs).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    parmas = {'private': privatejobs, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "private.html", parmas)


def offline(requset, slug):
    offlines = OfflineForm.objects.get(slug=slug)
    offlines.viewc = offlines.viewc + 1
    offlines.save()
    toppost = TopPost.objects.all()
    comments = OfflineFormComment.objects.filter(post=offlines, parent=None)
    replies = OfflineFormComment.objects.filter(post=offlines).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    parmas = {'offline': offlines, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "offline.html", parmas)


def syllabus(requset, slug):
    syllabusdata = SyllabusData.objects.get(slug=slug)
    syllabusdata.viewc = syllabusdata.viewc + 1
    syllabusdata.save()
    toppost = TopPost.objects.all()
    comments = SyllabusComment.objects.filter(post=syllabusdata, parent=None)
    replies = SyllabusComment.objects.filter(post=syllabusdata).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'syllabusdata': syllabusdata, 'jobs': jobs, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "syllabus.html", params)


def newspaper(requset, slug):
    newspaper = NewsPaper.objects.filter(category=slug).order_by('timestamp')[::-1]
    newspaper[0].viewc = newspaper[0].viewc + 1
    newspaper[0].save()
    toppost = TopPost.objects.all()
    comments = NewsPaperComment.objects.filter(parent=None)
    replies = NewsPaperComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'newspaper': newspaper, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict, 'slug': slug,
              'newspaperc': newspaper[0].viewc}
    return render(requset, "newspaper.html", params)


def result(requset, slug):
    resultdata = ResultData.objects.get(slug=slug)
    resultdata.viewc = resultdata.viewc + 1
    resultdata.save()
    toppost = TopPost.objects.all()
    comments = ResultComment.objects.filter(post=resultdata, parent=None)
    replies = ResultComment.objects.filter(post=resultdata).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'resultdata': resultdata, 'jobs': jobs, 'toppost': toppost, "comments": comments[::-1], 'replyDict': replyDict}
    return render(requset, "result.html", params)


def schooluni(requset, slug):
    schoolunidata = SchoolUniData.objects.get(slug=slug)
    schoolunidata.viewc = schoolunidata.viewc + 1
    schoolunidata.save()
    toppost = TopPost.objects.all()
    comments = SchoolUniComment.objects.filter(post=schoolunidata, parent=None)
    replies = SchoolUniComment.objects.filter(post=schoolunidata).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'schoolunidata': schoolunidata, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "SchoolUniversity.html", params)


def certification(requset, slug):
    certificationdata = CertificationData.objects.get(slug=slug)
    certificationdata.viewc = certificationdata.viewc + 1
    certificationdata.save()
    toppost = TopPost.objects.all()
    comments = CerttificationComment.objects.filter(post=certificationdata, parent=None)
    replies = CerttificationComment.objects.filter(post=certificationdata).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'certificationdata': certificationdata, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "certification.html", params)


def other(requset, slug):
    otherdata = OtherData.objects.get(slug=slug)
    otherdata.viewc = otherdata.viewc + 1
    otherdata.save()
    toppost = TopPost.objects.all()
    comments = OtherComment.objects.filter(post=otherdata, parent=None)
    replies = OtherComment.objects.filter(post=otherdata).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'otherdata': otherdata, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "other.html", params)


def answerkey(requset, slug):
    answerkeydata = AnswerKeyData.objects.get(slug=slug)
    answerkeydata.viewc = answerkeydata.viewc + 1
    answerkeydata.save()
    toppost = TopPost.objects.all()
    comments = AnswerKeyComment.objects.filter(post=answerkeydata, parent=None)
    replies = AnswerKeyComment.objects.filter(post=answerkeydata).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'answerkeydata': answerkeydata, 'jobs': jobs, 'toppost': toppost, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(requset, "answerkey.html", params)


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('content')
        if len(name) > 2 and len(email) > 5 and len(phone) > 9 and len(comment) != 0:
            contact = ContactUs(name=name, email=email, phone=phone, comment=comment)
            contact.save()
            messages.success(request, " Your Details is Successfuly Save")
        else:
            messages.error(request, " Please Fill the Right Details")
    return render(request, "contactus.html")


def aboutus(requset):
    return render(requset, "aboutus.html")


def ssc(requset):
    sscs = SSC.objects.all()
    sscc = SSC.objects.all()[0]
    sscc.viewc = sscc.viewc + 1
    sscc.save()
    comments = SSCComment.objects.filter(parent=None)
    replies = SSCComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'ssc'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'ssc': sscs[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "ssc.html", params)


def railway(requset):
    railways = Railway.objects.all()
    railwaysc = Railway.objects.all()[0]
    railwaysc.viewc = railwaysc.viewc + 1
    railwaysc.save()
    comments = RailwayComment.objects.filter(parent=None)
    replies = RailwayComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'railway'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'railway': railways[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "railway.html", params)


def bank(requset):
    banks = Bank.objects.all()
    banksc = Bank.objects.all()[0]
    banksc.viewc = banksc.viewc + 1
    banksc.save()
    comments = BankComment.objects.filter(parent=None)
    replies = BankComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'bank'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'bank': banks[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "bank.html", params)


def state(requset):
    states = State.objects.all()
    statesc = State.objects.all()[0]
    statesc.viewc = statesc.viewc + 1
    statesc.save()
    comments = StatesComment.objects.filter(parent=None)
    replies = StatesComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'state'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'state': states[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "state.html", params)


def army(requset):
    armys = IndianArmy.objects.all()
    armysc = IndianArmy.objects.all()[0]
    armysc.viewc = armysc.viewc + 1
    armysc.save()
    comments = IndianArmyComment.objects.filter(parent=None)
    replies = IndianArmyComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'army'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'army': armys[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "army.html", params)


def defence(requset):
    defences = Defence.objects.all()
    defencesc = Defence.objects.all()[0]
    defencesc.viewc = defencesc.viewc + 1
    defencesc.save()
    comments = DefenceComment.objects.filter(parent=None)
    replies = DefenceComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'defence'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'defence': defences[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "defence.html", params)


def police(requset):
    polices = Police.objects.all()
    policesc = Police.objects.all()[0]
    policesc.viewc = policesc.viewc + 1
    policesc.save()
    comments = PoliceComment.objects.filter(parent=None)
    replies = PoliceComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    category = 'police'
    alljobs = JobsData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    alladmitcard = AdmitCardData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    syllabusdata = SyllabusData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    resultsdata = ResultData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    answerkeydata = AnswerKeyData.objects.filter(post_category=category).order_by('post_date_update')[::-1]
    params = {'alljobs': alljobs[0:11], 'alladmitcard': alladmitcard[0:11], 'syllabusdata': syllabusdata[0:11],
              'resultdata': resultsdata[0:11], 'answerkeydata': answerkeydata, 'police': polices[0], 'comments': comments[::-1],
              'replyDict': replyDict}
    return render(requset, "police.html", params)


def allbasic(requset, slug):
    if slug == "offline":
        offlines = OfflineForm.objects.values('plan_name', 'slug', 'plan_last_date')
        all = [{'post_name': offlines[i]['plan_name'], 'slug': "/offline/" + offlines[i]['slug'], 'lastdate': offlines[i]['plan_last_date']} for i in range(len(offlines))]
        params = {'all': all[::-1], 'title': 'Offline Jobs'}
        return render(requset, "allbasic.html", params)
    if slug == "admission":
        admissions = Admission.objects.values('plan_name', 'slug', 'plan_last_date')
        all = [{'post_name': admissions[i]['plan_name'], 'slug': "/admission/" + admissions[i]['slug'], 'lastdate': admissions[i]['plan_last_date']} for i in range(len(admissions))]
        params = {'all': all[::-1], 'title': 'Admission Form'}
        return render(requset, "allbasic.html", params)
    if slug == "diploma":
        diplomas = Diploma.objects.values('plan_name', 'slug', 'plan_last_date')
        all = [{'post_name': diplomas[i]['plan_name'], 'slug': "/diploma/" + diplomas[i]['slug'], 'lastdate': diplomas[i]['plan_last_date']} for i in range(len(diplomas))]
        params = {'all': all[::-1], 'title': 'Diploma(ITI/CCC)'}
        return render(requset, "allbasic.html", params)
    if slug == "private":
        privates = PrivateJobs.objects.values('plan_name', 'slug', 'plan_last_date')
        all = [{'post_name': privates[i]['plan_name'], 'slug': "/private/" + privates[i]['slug'], 'lastdate': privates[i]['plan_last_date']} for i in range(len(privates))]
        params = {'all': all[::-1], 'title': 'Private Jobs'}
        return render(requset, "allbasic.html", params)
    if slug == "jobs":
        jobs = JobsData.objects.values('post_name', 'slug', 'last_date')
        all = [{'post_name': jobs[i]['post_name'], 'slug': "/jobs/" + jobs[i]['slug'], 'lastdate': jobs[i]['last_date']} for i in range(len(jobs))]
        params = {'all': all[::-1], 'title': 'Government Jobs'}
        return render(requset, "allbasic.html", params)
    elif slug == "admitcard":
        admitcard = AdmitCardData.objects.values('admit_card_name', 'slug', 'admit_card_date')
        all = [{'post_name': admitcard[i]['admit_card_name'], 'slug': '/admitcard/' + admitcard[i]['slug'], 'lastdate': admitcard[i]['admit_card_date']} for i in range(len(admitcard))]
        params = {'all': all[::-1], 'title': 'Admit Card'}
        return render(requset, "allbasic.html", params)
    elif slug == "govtplan":
        govplan = GovernmentPlan.objects.values('plan_name', 'slug', 'plan_last_date')
        all = [{'post_name': govplan[i]['plan_name'], 'slug': '/govtplan/' + govplan[i]['slug'], 'lastdate': govplan[i]['plan_last_date']} for i in range(len(govplan))]
        params = {'all': all[::-1], 'title': 'Government Yojnaye'}
        return render(requset, "allbasic.html", params)
    elif slug == "result":
        result = ResultData.objects.values('result_name', 'slug', 'post_date_update')
        all = [{'post_name': result[i]['result_name'], 'slug': '/result/' + result[i]['slug'], 'lastdate': result[i]['post_date_update']} for i in range(len(result))]
        params = {'all': all[::-1], 'title': 'Result'}
        return render(requset, "allbasic.html", params)
    elif slug == "answerkey":
        answerkey = AnswerKeyData.objects.values('answerkey_name', 'slug', 'post_date_update')
        all = [{'post_name': answerkey[i]['answerkey_name'], 'slug': '/answerkey/' + answerkey[i]['slug'], 'lastdate': answerkey[i]['post_date_update']} for i in range(len(answerkey))]
        params = {'all': all[::-1], 'title': 'Answer Keys'}
        return render(requset, "allbasic.html", params)
    elif slug == "syllabus":
        syllabus = SyllabusData.objects.values('syllabus_name', 'slug', 'post_date_update')
        all = [{'post_name': syllabus[i]['syllabus_name'], 'slug': '/syllabus/' + syllabus[i]['slug'], 'lastdate': syllabus[i]['post_date_update']} for i in range(len(syllabus))]
        params = {'all': all[::-1], 'title': 'Syllabus'}
        return render(requset, "allbasic.html", params)
    elif slug == "schooluni":
        schooluni = SchoolUniData.objects.values('post_name', 'slug', 'last_date')
        all = [{'post_name': schooluni[i]['post_name'], 'slug': '/schooluni/' + schooluni[i]['slug'], 'lastdate': schooluni[i]['last_date']} for i in range(len(schooluni))]
        params = {'all': all[::-1], 'title': 'School/University'}
        return render(requset, "allbasic.html", params)
    elif slug == "certification":
        certification = CertificationData.objects.values('post_name', 'slug', 'last_date')
        all = [{'post_name': certification[i]['post_name'], 'slug': '/certification/' + certification[i]['slug'], 'lastdate': certification[i]['last_date']} for i in range(len(certification))]
        params = {'all': all[::-1], 'title': 'Certification'}
        return render(requset, "allbasic.html", params)
    elif slug == "other":
        other = OtherData.objects.values('post_name', 'slug', 'last_date')
        all = [{'post_name': other[i]['post_name'], 'slug': '/other/' + other[i]['slug'], 'lastdate': other[i]['last_date']} for i in range(len(other))]
        params = {'all': all[::-1], 'title': 'Others'}
        return render(requset, "allbasic.html", params)
    else:
        return HttpResponse("No Data Found")


def PostComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = JobsData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = PostComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = PostComment.objects.get(sno=parentSno)
            comment = PostComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/jobs/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def AdmitCardComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = AdmitCardData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = AdmitCardComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = AdmitCardComment.objects.get(sno=parentSno)
            comment = AdmitCardComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/admitcard/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def AnswerKeyComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = AnswerKeyData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = AnswerKeyComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = AnswerKeyComment.objects.get(sno=parentSno)
            comment = AnswerKeyComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        # messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/answerkey/{post.slug}')
        #

    else:
        # messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def BankComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BankComment(name=name, email=email, comment=comment)
        else:
            parent = BankComment.objects.get(sno=parentSno)
            comment = BankComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/bank')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def CertificationComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = CertificationData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = CerttificationComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = CerttificationComment.objects.get(sno=parentSno)
            comment = CerttificationComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/certification/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def DefencesComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = DefenceComment(name=name, email=email, comment=comment)
        else:
            parent = DefenceComment.objects.get(sno=parentSno)
            comment = DefenceComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/defence')


    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def GovtPlanComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = GovernmentPlan.objects.get(s_no=postSno)
        if parentSno == "":
            comment = GovtPlanComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = GovtPlanComment.objects.get(sno=parentSno)
            comment = GovtPlanComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/govtplan/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def AdmissionComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = Admission.objects.get(s_no=postSno)
        if parentSno == "":
            comment = AdmissionComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = AdmissionComment.objects.get(sno=parentSno)
            comment = AdmissionComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/admission/{post.slug}')

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def PrivateComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = PrivateJobs.objects.get(s_no=postSno)
        if parentSno == "":
            comment = PrivateJobComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = PrivateJobComment.objects.get(sno=parentSno)
            comment = PrivateJobComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/private/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def OfflineComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = OfflineForm.objects.get(s_no=postSno)
        if parentSno == "":
            comment = OfflineFormComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = OfflineFormComment.objects.get(sno=parentSno)
            comment = OfflineFormComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/offline/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def DiplomaComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = Diploma.objects.get(s_no=postSno)
        if parentSno == "":
            comment = DiplomaComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = DiplomaComment.objects.get(sno=parentSno)
            comment = DiplomaComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/diploma/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def IndianArmyComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = IndianArmyComment(name=name, email=email, comment=comment)
        else:
            parent = IndianArmyComment.objects.get(sno=parentSno)
            comment = IndianArmyComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/army')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def OtherComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = OtherData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = OtherComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = OtherComment.objects.get(sno=parentSno)
            comment = OtherComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/other/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def PoliceComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = PoliceComment(name=name, email=email, comment=comment)
        else:
            parent = PoliceComment.objects.get(sno=parentSno)
            comment = PoliceComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/police')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def RailwayComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = RailwayComment(name=name, email=email, comment=comment)
        else:
            parent = RailwayComment.objects.get(sno=parentSno)
            comment = RailwayComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/railway')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def ResultComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = ResultData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = ResultComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = ResultComment.objects.get(sno=parentSno)
            comment = ResultComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/result/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def SchoolUniComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = SchoolUniData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = SchoolUniComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = SchoolUniComment.objects.get(sno=parentSno)
            comment = SchoolUniComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/schooluni/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def SSCComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = SSCComment(name=name, email=email, comment=comment)
        else:
            parent = SSCComment.objects.get(sno=parentSno)
            comment = SSCComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/ssc')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def StatesComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = StatesComment(name=name, email=email, comment=comment)
        else:
            parent = StatesComment.objects.get(sno=parentSno)
            comment = StatesComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/state')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def NewsPaperComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        category = request.POST.get('category')
        if parentSno == "":
            comment = NewsPaperComment(name=name, email=email, comment=comment)
        else:
            parent = NewsPaperComment.objects.get(sno=parentSno)
            comment = NewsPaperComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/newspaper/{category}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def SyllabusComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = SyllabusData.objects.get(s_no=postSno)
        if parentSno == "":
            comment = SyllabusComment(name=name, email=email, comment=comment, post=post)
        else:
            parent = SyllabusComment.objects.get(sno=parentSno)
            comment = SyllabusComment(name=name, email=email, comment=comment, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/syllabus/{post.slug}')
        #

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def search(request):
    if request.method == 'GET':
        searchtext = request.GET.get('searchtext')
        if len(searchtext) < 2:
            messages.error(request, " Search Text is too Small")
            alljobs = {}
            alladmitcard = {}
            allgovtpan = {}
            syllabusdata = {}
            resultsdata = {}
            alljobs = {}
            answerkeydata = {}
            schoolunidata = {}
            certificationdata = {}
            otherdata = {}

        else:
            alljobs = JobsData.objects.filter(post_name__icontains=searchtext)
            alladmitcard = AdmitCardData.objects.filter(admit_card_name__icontains=searchtext)
            allgovtpan = GovernmentPlan.objects.filter(plan_name__icontains=searchtext)
            syllabusdata = SyllabusData.objects.filter(syllabus_name__icontains=searchtext)
            resultsdata = ResultData.objects.filter(result_name__icontains=searchtext)
            answerkeydata = AnswerKeyData.objects.filter(answerkey_name__icontains=searchtext)
            schoolunidata = SchoolUniData.objects.filter(post_name__icontains=searchtext)
            certificationdata = CertificationData.objects.filter(post_name__icontains=searchtext)
            otherdata = OtherData.objects.filter(post_name__icontains=searchtext)
            private = PrivateJobs.objects.filter(plan_name__icontains=searchtext)
            offline = OfflineForm.objects.filter(plan_name__icontains=searchtext)
            diploma = Diploma.objects.filter(plan_name__icontains=searchtext)
            admission = Admission.objects.filter(plan_name__icontains=searchtext)
            messages.success(request, " Search is Success ")

        params = {'alljobs': alljobs, 'alladmitcard': alladmitcard, 'allgovtplan': allgovtpan, 'alladmission': admission, 'alldiploma': diploma, 'alloffline': offline, 'allprivate': private, 'syllabusdata': syllabusdata,
                  'resultdata': resultsdata, 'answerkeydata': answerkeydata, 'schoolunidata': schoolunidata,
                  "certificationdata": certificationdata, "otherdata": otherdata}
    return render(request, "search.html", params)


def Previouspaper(request, slug):
    allpaper = PreviousYearPaper.objects.filter(slug=slug)
    comments = PreviousComment.objects.filter(parent=None)
    replies = PreviousComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'allpaper': allpaper, 'slug': slug, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(request, 'previouspaper.html', params)


def PreviousPaperComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        slug = request.POST.get('slug')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = PreviousComment(name=name, email=email, comment=comment)
        else:
            parent = PreviousComment.objects.get(sno=parentSno)
            comment = PreviousComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/previouspaper/{slug}')

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')


def ExamMaterials(request, slug):
    allmaterial = ExamMaterial.objects.filter(slug=slug)
    comments = ExamMaterialComment.objects.filter(parent=None)
    replies = ExamMaterialComment.objects.filter().exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'allmaterial': allmaterial, 'slug': slug, 'comments': comments[::-1], 'replyDict': replyDict}
    return render(request, 'exammaterial.html', params)


def ExamMaterialComments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        slug = request.POST.get('slug')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = ExamMaterialComment(name=name, email=email, comment=comment)
        else:
            parent = ExamMaterialComment.objects.get(sno=parentSno)
            comment = ExamMaterialComment(name=name, email=email, comment=comment, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/exammaterial/{slug}')

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')
