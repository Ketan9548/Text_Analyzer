from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Kapil Chauhan</h1>")
    Info = {'Company':'TCS','Salary':'7.8 LPA'}
    return render(request,'index.html')

def analyze(request):
    # string input
    djtext = request.POST.get('text','default') 
    
    # check the checbox
    removepuc = request.POST.get('removepunc','Off')
    Fullcaps = request.POST.get('fullcaps','Off')
    newlineRemover = request.POST.get('newlineremove','off')
    Extraspaceremover = request.POST.get('extraspaceremover','off')
    CountCharacters = request.POST.get('CountChar','off')
    print(djtext)
    print(removepuc)

    # check is on or off
    if removepuc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose':'Remove Punctuation', 'analayed_text': analyzed}  
        print(param)
        return render(request,'analyze.html',param)
    elif(Fullcaps == "on"):
        analyzedA = " "
        for char in djtext:
            analyzedA = analyzedA + char.upper()
        param = {'purpose':'Change To Uppercase', 'analayed_text':analyzedA}  
        print(param)
        return render(request,'analyze.html',param)
    
    elif(newlineRemover=="on"):
        analyzedR = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzedR = analyzedR + char

        param = {'purpose':'Remove the New Line', 'analayed_text':analyzedR}  
        print(param)
        return render(request,'analyze.html',param)
    
    elif(Extraspaceremover=="on"):
        analyzedEX = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzedEX = analyzedEX + char

        param = {'purpose':'Remove Extra Space', 'analayed_text':analyzedEX}  
        print(param)
        return render(request,'analyze.html',param)
    
    elif(CountCharacters=="on"):
        Charctorcount = len(djtext)
        param = {'purpose':'Remove Extra Space', 'Count_Char':Charctorcount}  
        print(param)
        return render(request,'analyze.html',param)
    else:
        return HttpResponse("<h1>ERROR</h1>")
