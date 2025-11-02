from django.shortcuts import render

def info_view(request):
    context = {
        'name': 'მიშო',
        'surname': 'აბუაშვილი',
        'age': 14,
        'height': 175,
    }
    return render(request, 'info.html', context)


def hobbies_view(request):
    context = {
        'hobbies': ['კოდინგი', 'ფეხბურთის თამაში/ყურება', 'youtube ყურება'],
        'grade': 14,
    }
    return render(request, 'hobbies.html', context)