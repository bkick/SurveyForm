from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render (request, 'survey/index.html')
def process(request):
	request.session['name']=request.POST['name'],
	request.session['dojo']=request.POST['dojo'],
	request.session['language']=request.POST['language'],
	request.session['comment']=request.POST['comment'],
	print(request.session['name'][0])
	return redirect('/submit')
def submit(request):
	return render(request,'survey/submit.html')