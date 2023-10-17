#admin_dahsboard_calculations
#admin_dashboard_reports
#total_vaccant_share_choose_branches
from django.shortcuts import render
from django.contrib import messages

from myapp.models import *

import branch12app
import branch13app
import branch14app

def total_guest():
    tg=[]

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br14))

    return sum(tg)

def branchwise_total_guest(request):
    tg=[]

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br14))

    context={
        'tg' : tg,
    }
    return render(request,'admindashboard/admin_dashboard_reports/branchwise_total_guest_choose_branches.html', context)


def total_vaccant_share1():
    tsv = []

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    return sum(tsv)

def total_vaccant_share2():
    tsv = []

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    return sum(tsv)

def total_vaccant_share3():
    tsv = []

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    return sum(tsv)

def total_vaccant_share4():
    tsv = []

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    return sum(tsv)

def total_vaccant_share5():
    tsv = []

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    return sum(tsv)

def total_vaccant_share6():
    tsv = []

    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    return sum(tsv)

def total_vaccant_room():
    tsv = []
    total_vaccant_room_br1 = total_vaccant_share1()
    tsv.append(total_vaccant_room_br1)
    total_vaccant_room_br2 = total_vaccant_share2()
    tsv.append(total_vaccant_room_br2)
    total_vaccant_room_br3 = total_vaccant_share3()
    tsv.append(total_vaccant_room_br3)
    total_vaccant_room_br4 = total_vaccant_share4()
    tsv.append(total_vaccant_room_br4)
    total_vaccant_room_br5 = total_vaccant_share5()
    tsv.append(total_vaccant_room_br5)
    total_vaccant_room_br6 = total_vaccant_share6()
    tsv.append(total_vaccant_room_br6)

    return sum(tsv)




def total_vaccant_share_branch12():
    tsv = []
    total_guest_br1 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch13():
    tsv = []
    total_guest_br1 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch14():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv



def total_vaccant_share_choose_branches(request):
    context = {

        'br12': total_vaccant_share_branch12(),
        'br13': total_vaccant_share_branch13(),
        'br14': total_vaccant_share_branch14(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/total_vaccant_share_choose_branches.html',context)

######TOTAL COLLECTION START HERE

def total_gtc():

    a12 = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    a13 = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    a14 = branch14app.admin_dashboard_calculations_br14.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    l=[]

    l.append(a12[cm])
    l.append(a13[cm])
    l.append(a14[cm])

    gtc=sum(l)
    print('this is total branch gtc sum',gtc)
    return gtc

def total_advance():

    a12 = branch12app.admin_dashboard_calculations_br12.total_collection_advance()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collection_advance()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collection_advance()

    l = []

    l.append(a12)
    l.append(a13)
    l.append(a14)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def total_discount():

    a12 = branch12app.admin_dashboard_calculations_br12.total_discount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_discount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_discount()

    l = []

    l.append(a12)
    l.append(a13)
    l.append(a14)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_collatable_amount():

    a12 = branch12app.admin_dashboard_calculations_br12.total_colatable_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_colatable_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_colatable_amount()

    l = []

    l.append(a12)
    l.append(a13)
    l.append(a14)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_collected_amount():

    a12 = branch12app.admin_dashboard_calculations_br12.total_collected_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collected_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collected_amount()

    l = []

    l.append(a12)
    l.append(a13)
    l.append(a14)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_due():

    a12 = branch12app.admin_dashboard_calculations_br12.total_due()
    a13 = branch13app.admin_dashboard_calculations_br13.total_due()
    a14 = branch14app.admin_dashboard_calculations_br14.total_due()

    l = []

    l.append(a12)
    l.append(a13)
    l.append(a14)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

#*************************************
#####LIST OF TOTAL COLLECTION
#*************************************

def branchwise_total_collection(request):

    a12 = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    a13 = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    a14 = branch14app.admin_dashboard_calculations_br14.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    list_total_gtc = []

    list_total_gtc.append(a12[cm])
    list_total_gtc.append(a13[cm])
    list_total_gtc.append(a14[cm])

#******list_total_advance


    a12 = branch12app.admin_dashboard_calculations_br12.total_collection_advance()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collection_advance()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collection_advance()

    list_total_advance = []

    list_total_advance.append(a12)
    list_total_advance.append(a13)
    list_total_advance.append(a14)

#***********list_total_discount


    a12 = branch12app.admin_dashboard_calculations_br12.total_discount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_discount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_discount()

    total_discount = []

    total_discount.append(a12)
    total_discount.append(a13)
    total_discount.append(a14)


#******list_all_total_collatable_amount


    a12 = branch12app.admin_dashboard_calculations_br12.total_colatable_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_colatable_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_colatable_amount()

    total_colatable_amount = []

    total_colatable_amount.append(a12)
    total_colatable_amount.append(a13)
    total_colatable_amount.append(a14)

#*******list_all_total_collected_amount


    a12 = branch12app.admin_dashboard_calculations_br12.total_collected_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collected_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collected_amount()

    total_collected_amount = []

    total_collected_amount.append(a12)
    total_collected_amount.append(a13)
    total_collected_amount.append(a14)


#*****list_all_total_due


    a12 = branch12app.admin_dashboard_calculations_br12.total_due()
    a13 = branch13app.admin_dashboard_calculations_br13.total_due()
    a14 = branch14app.admin_dashboard_calculations_br14.total_due()

    total_due = []

    total_due.append(a12)
    total_due.append(a13)
    total_due.append(a14)


    context={
        'grand_total_collection':list_total_gtc,
        'total_collection_advance': list_total_advance,
        'total_discount': total_discount,

        'total_colatable_amount': total_colatable_amount,
        'total_collected_amount': total_collected_amount,
        'total_due': total_due
    }
    return render(request,'admindashboard/admin_dashboard_reports/branchwise_total_collection.html', context)





######TOTAL COLLECTION END HERE

def details_branch12(request):
    a = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch12app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch12app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch12app.admin_dashboard_calculations_br12.total_collection_advance(),
        'total_discount': branch12app.admin_dashboard_calculations_br12.total_discount(),

        'total_colatable_amount': branch12app.admin_dashboard_calculations_br12.total_colatable_amount(),
        'total_collected_amount': branch12app.admin_dashboard_calculations_br12.total_collected_amount(),
        'total_due': branch12app.admin_dashboard_calculations_br12.total_due(),
        'l': branch12app.admin_dashboard_calculations_br12.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


def details_branch13(request):
    a = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch13app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch13app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch13app.admin_dashboard_calculations_br13.total_collection_advance(),
        'total_discount': branch13app.admin_dashboard_calculations_br13.total_discount(),

        'total_colatable_amount': branch13app.admin_dashboard_calculations_br13.total_colatable_amount(),
        'total_collected_amount': branch13app.admin_dashboard_calculations_br13.total_collected_amount(),
        'total_due': branch13app.admin_dashboard_calculations_br13.total_due(),
        'l': branch13app.admin_dashboard_calculations_br13.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


def details_branch14(request):
    a = branch14app.admin_dashboard_calculations_br14.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch14app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch14app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch14app.admin_dashboard_calculations_br14.total_collection_advance(),
        'total_discount': branch14app.admin_dashboard_calculations_br14.total_discount(),

        'total_colatable_amount': branch14app.admin_dashboard_calculations_br14.total_colatable_amount(),
        'total_collected_amount': branch14app.admin_dashboard_calculations_br14.total_collected_amount(),
        'total_due': branch14app.admin_dashboard_calculations_br14.total_due(),
        'l': branch14app.admin_dashboard_calculations_br14.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

