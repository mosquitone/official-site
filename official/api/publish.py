import os
import subprocess
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/')
def publish(request):
    env = os.environ.copy()
    env["SYNC_SIZE_ONLY"] = 'false' if 'force' in request.GET else 'true'

    pipe = subprocess.Popen([os.path.join(settings.BASE_DIR, 'bin', 'publish')],
                            stdout=subprocess.PIPE,
                            env=env)
    result = pipe.stdout.read()

    response = HttpResponse(content_type='text/html')
    response.write(
        '<html><body><pre><code>{}</code></pre></body></html>'.format(result)
    )
    return response
