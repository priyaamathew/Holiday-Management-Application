from django.shortcuts import render

# Create your views here.
import requests
import os
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Holiday

API_KEY = os.getenv("CALENDARIFIC_API_KEY")

@api_view(['GET'])
def get_holidays(request):
    country = request.GET.get('country', 'US')
    year = request.GET.get('year', '2024')

    cache_key = f"holidays_{country}_{year}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)
    

    url = f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country={country}&year={year}"
    response = requests.get(url)
    data = response.json()
    print(data)

    if 'response' in data:
        holidays = []
        for holiday in data['response']['holidays']:
            holidays.append({
                'name': holiday['name'],
                'date': holiday['date']['iso'],
                'type': ", ".join(holiday.get('type', [])),
                'description': holiday.get('description', ''),
                'country': country
            })
        cache.set(cache_key, holidays, timeout=86400)  # Cache for 24 hours
        return Response(holidays)
    
    return Response({"error": "Unable to fetch holidays"}, status=400)

