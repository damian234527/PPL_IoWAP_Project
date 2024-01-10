from django.shortcuts import render
from . import forms
from .models import Prompt, Answer
import requests
from django.core.paginator import Paginator

def send_question(question):
    api_url = "https://api.bibleai.com/search"
    params = {
        "question": question,
        "translation": "polUBG",
        "language": "pl-PL"
    }
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except Exception as e:
        return e


def index(request):
    if request.method == "POST":
        prompt_form = forms.PromptForm(request.POST)
        if prompt_form.is_valid():
            prompt = prompt_form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                prompt.ip = x_forwarded_for.split(',')[0]
            else:
                prompt.ip = request.META.get('REMOTE_ADDR')
            prompt.save()
            answers = send_question(prompt.question)
            if answers:
                answers = answers["data"]
                print(answers)
                for answer in answers:
                    print(type(answer))
                    Answer.objects.create(answer=answer["text"], reference=answer["referenceLocal"], question=prompt)
    else:
        prompt_form = forms.PromptForm()
    questions = Prompt.objects.all().order_by("-date").values()
    paginator = Paginator(questions, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "help/index.html", {"prompt_form": prompt_form, "page_obj": page_obj})

def prompts_list(request):
    questions_with_answers = Prompt.objects.prefetch_related('answer_set').all().order_by("-date")
    paginator = Paginator(questions_with_answers, 5)
    page_number = request.GET.get("page")
    print(page_number)
    page_obj = paginator.get_page(page_number)
    return render(request, "help/prompts_list.html", {"page_obj": page_obj})
    #return render(request, "help/prompts_list.html", {"questions_with_answers": questions_with_answers})

