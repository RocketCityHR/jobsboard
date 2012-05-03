from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object

from webgljobs.main.forms import JobForm
from webgljobs.main.models import Job

urlpatterns = patterns("",
    url(
        r"^$",
        direct_to_template,
        {
            "template": "main_page.html",
            "extra_context": {
                "jobs": lambda: Job.objects.all().filter(approved=True)
            }
        },
        name="main_page"
    ),
    url(
        r"^about/$",
        direct_to_template,
        {
            "template": "about.html",
        },
        name="about_page"
    ),
    url(
        r"^add/$",
        create_object,
        {
            "form_class": JobForm,
            "template_name": "create_new_job.html",
            "post_save_redirect": "/add/thanks",
        },
        name="create_new_job"
    ),
    url(
        r"^add/thanks$",
        direct_to_template,
        {
            "template": "create_new_job_thanks.html",
        },
        name="create_new_job_thanks"
    ),
)
