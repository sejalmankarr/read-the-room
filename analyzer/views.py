from django.shortcuts import render
from .sentiment import analyze_text
from .models import Analysis


def index(request):
    context = {}
    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            result = analyze_text(text)
            Analysis.objects.create(
                text=text, label=result["label"], score=result["score"]
            )
            context["text"] = text
            context["result"] = result
    return render(request, "analyzer/index.html", context)


def history(request):
    analyses = Analysis.objects.order_by("-created_at")[:50]
    return render(request, "analyzer/history.html", {"analyses": analyses})