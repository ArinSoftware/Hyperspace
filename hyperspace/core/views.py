from django.shortcuts import render
from services.models import Service
from blog.models import Blog


def index(request):

    static_content = """
    		<div class="inner">
			<h1>Hyperspace</h1>
			<p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
			and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
			<ul class="actions">
				<li><a href="#one" class="button scrolly">Learn more</a></li>
			</ul>
		</div>
    """
	
    featured_services = Service.objects.filter(is_featured=True)
    latest_posts = Blog.objects.all()[:3]

    context = {
        'static_content': static_content,
        'featured_services': featured_services,
        'latest_posts': latest_posts
    }

    return render(request, 'core/index.html', context)