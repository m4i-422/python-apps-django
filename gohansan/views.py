import openai
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


openai.api_key = settings.OPENAI_API_KEY


def index(request):
    return HttpResponse("ごはんさんアプリへようこそ！")


@csrf_exempt
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )

        answer = response.choices[0].message.content
        return JsonResponse({"answer": answer})
    else:
        # GET のときは簡単な入力フォームを返す
        html = """
        <form id="chatForm">
          <input type="text" id="message" placeholder="メッセージを入力">
          <button type="submit">送信</button>
        </form>
        <pre id="response"></pre>
        <script>
        const form = document.getElementById('chatForm');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const msg = document.getElementById('message').value;
            const res = await fetch('', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: msg})
            });
            const data = await res.json();
            document.getElementById('response').textContent = data.answer || data.error;
        });
        </script>
        """
        return HttpResponse(html)
