from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import os
from groq import Groq

# Set up Groq client
groq_client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def home(request):
    return render(request, 'chatbot/home.html')

@csrf_exempt
@require_POST
def groq_query(request): 
    query = request.POST.get('query', '')

    try:
        # Create a chat completion
        response = groq_client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": "Format your responses with bold subheadings (using Markdown **bold**) and bullet points where appropriate."
            },{
                "role":"user",
                "content":query

            }],
            model="llama3-8b-8192",  # Replace with the desired Groq model
            max_tokens=500
        )

        answer = response.choices[0].message.content

        return JsonResponse({'answer': answer})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
