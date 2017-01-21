from django.shortcuts import render
from django_web.models import Test


# Create your views here.
def pure_index(request):
    context = {
        'all': Test.objects.all()
    }
    return render(request, "index.html", context =context)

def testdb(request):
    # makeData()
    all = Test.objects.all()
    context = {
        'all': all
    }
    return render(request,"testdb.html",context=context)


def makeData():
    n = 0
    while n <= 10:
        test1 = Test(name='www'+str(n), score='10'+str(n))
        test1.save()
        n += 1