from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from dj_practice.models import Memo
from dj_practice.serializers import MemoSerializer

@csrf_exempt
def memo_list(request):
    if request.method=='GET':
        memos=Memo.objects.all()
        serializer=MemoSerializer(memos,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=MemoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def memo_detail(request,pk):
    try:
        memo=Memo.objects.get(pk=pk)
    except Memo.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer=MemoSerializer(memo)
        return JsonResponse(serializer.data)
    
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=MemoSerializer(memo,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method=='DELETE':
        memo.delete()
        return HttpResponse(status=204)