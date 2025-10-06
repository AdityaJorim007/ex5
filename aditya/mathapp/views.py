from django.shortcuts import render

def power_calculator(request):
    context = {'p': '0', 'i': '0', 'r': '0'}
    
    if request.method == 'POST':
        print("POST method is used")
        i = request.POST.get('intensity', '0')
        r = request.POST.get('resistance', '0')
        print('Intensity (I) =', i)
        print('Resistance (R) =', r)
        
        try:
            power = (float(i) ** 2) * float(r)
            context['p'] = round(power, 3)
        except ValueError:
            context['p'] = "Invalid input"
        
        context['i'] = i
        context['r'] = r
        print('Power (P) =', context['p'])
    
    return render(request, 'mathapp/math.html', context)
