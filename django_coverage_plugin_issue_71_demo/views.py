from django.views.generic import TemplateView


class FrontPage(TemplateView):
    template_name = 'django_coverage_plugin_issue_71_demo/template1.html'
