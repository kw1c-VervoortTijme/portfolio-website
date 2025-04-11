from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')
    
def stage_1(request):
    return render(request, 'portfolio/stage_1.html')
    
def stage_2(request):
    return render(request, 'portfolio/stage_2.html')
    
def stage_3(request):
    return render(request, 'portfolio/stage_3.html')
    
def portfolio_page(request):
    return render(request, 'portfolio/portfolio_page.html')
