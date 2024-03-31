from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from dataclasses import dataclass

# Create your views here.
zodiac_dict = {'aries': 'Овен - первый знак зодиака, Марс',
               'taurus': 'Телец - второй знак зодиака, Венера',
               'gemini': 'Близнецы -  третий знак, Меркурий',
               'cancer': 'Рак - четвертый знак, Луна',
               'leo': 'Лев - пятый знак зодиака, Солнце',
               'virgo': 'Дева -  шестой знак, Меркурий',
               'libra': 'Весы -  седьмой знак, Венера',
               'scorpios': 'Скорпион -  восьмой знак, Марс',
               'sagittarius': 'Стрелец -  девятый знак, Юпитер',
               'capricorn': 'Козерог -  десятый знак, Сатурн',
               'aquarius': 'Водолей - одиннадцатый знак, Уран и Сатурн',
               'pisces': 'Рыбы -  двенедцатый знак, Юпитер',
               }

four_forces_dict = {'fire': ['aries', 'leo', 'sagittarius'],
                    'earth': ['taurus', 'virgo', 'capricorn'],
                    'air': ['gemini', 'libra', 'aquarius'],
                    'water': ['cancer', 'scorpio', 'pisces']
                    }


def index(request, ):
    znaks = list(zodiac_dict)
    #     li_element += f"<li> <a href='{redirect_path}'>{sing.title()} </a> </li>"
    context = {'znaks': znaks,
               'zodiac_dict': zodiac_dict}
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sing_zodiac(request, znak_zodiac: str):
    description = zodiac_dict.get(znak_zodiac)
    # znaks = list(zodiac_dict)
    data = {'description': description,
            'znak': znak_zodiac.title(),
            # 'znak_name': description.split()[0],
            'znaks': zodiac_dict,
            }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sing_zodiac_by_now(request, znak_zodiac: int):
    znak = list(zodiac_dict)
    if znak_zodiac > len(znak):
        return HttpResponseNotFound(f'Неправильный номер - {znak_zodiac}')
    name = znak[znak_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name])
    return HttpResponseRedirect(redirect_url)
