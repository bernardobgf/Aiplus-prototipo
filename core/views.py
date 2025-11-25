from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage, Config
import os
import json
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

def get_config():
    conf = Config.objects.first()
    if not conf:
        conf = Config.objects.create()
    return conf

def home(request):
    messages = ChatMessage.objects.all().order_by('created_at')
    return render(request, 'core/home.html', {'messages': messages, 'page': 'home'})

def dashboard(request):
    return render(request, 'core/dashboard.html', {'page': 'dashboard'})

def settings_view(request):
    config = get_config()
    if request.method == "POST":
        config.company_name = request.POST.get('company_name')
        config.target_audience = request.POST.get('target_audience')
        config.tone = request.POST.get('tone')
        config.creativity = float(request.POST.get('creativity'))
        config.save()
        return redirect('settings')
    return render(request, 'core/settings.html', {'config': config, 'page': 'settings'})

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_msg = data.get('message')
        
        ChatMessage.objects.create(role='user', content=user_msg)
        
        try:
            client = genai.Client(api_key=API_KEY)
            config = get_config()
            
            # Instrução de Sistema Poderosa
            sys_instruct = (
                f"Você é o AIplus Pro. Trabalha para a empresa '{config.company_name}'. "
                f"Público Alvo: '{config.target_audience}'. Tom de voz: '{config.tone}'. "
                "Responda de forma fluida, moderna e sem formatação técnica (markdown complexo)."
            )
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_msg,
                config={"system_instruction": sys_instruct, "temperature": config.creativity}
            )
            ai_text = response.text
        except Exception as e:
            ai_text = f"Erro de conexão com a IA: {str(e)}"

        ChatMessage.objects.create(role='model', content=ai_text)
        return JsonResponse({'response': ai_text})
    return JsonResponse({'error': 'Invalid request'}, status=400)


# core/views.py

def clear_chat(request):
    # Apaga todas as mensagens do banco de dados
    ChatMessage.objects.all().delete()
    # Volta para a home limpa
    return redirect('home')