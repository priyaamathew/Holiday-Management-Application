from django.shortcuts import render

# Create your views here.
import requests
import os
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Holiday

API_KEY = os.getenv("CALENDARIFIC_API_KEY")

import requests
import os
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

API_KEY = os.getenv("CALENDARIFIC_API_KEY")

@api_view(['GET'])
def get_holidays(request):
    country = request.GET.get('country', 'IN')  # Default to 'IN' if not provided
    year = request.GET.get('year', '2024')  # Default to 2024 if not provided
    month = request.GET.get('month', None)  # Optional month filter
    day = request.GET.get('day', None)  # Optional day filter

    # Construct cache key based on parameters
    cache_key = f"holidays_{country}_{year}"
    if month:
        cache_key += f"_month{month}"
    if day:
        cache_key += f"_day{day}"

    # Check if cached data exists
    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    # Build API request URL dynamically
    url = f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country={country}&year={year}"
    if month:
        url += f"&month={month}"
    if day:
        url += f"&day={day}"

    # Fetch holidays from Calendarific API
    response = requests.get(url)
    data = response.json()

    # Handle API response
    if 'response' in data and 'holidays' in data['response']:
        holidays = [
            {
                'name': holiday['name'],
                'date': holiday['date']['iso'],
                'type': ", ".join(holiday.get('type', [])),
                'description': holiday.get('description', ''),
                'country': country
            }
            for holiday in data['response']['holidays']
        ]

        # Cache the results for 24 hours
        cache.set(cache_key, holidays, timeout=86400)
        return Response(holidays)

    return Response({"error": "Unable to fetch holidays"}, status=400)


