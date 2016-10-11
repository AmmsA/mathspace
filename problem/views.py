from django.views.generic import TemplateView
from .forms import ProblemForm
from .solution import get_solution


class ViewProblemView(TemplateView):
    template_name = "problem.html"
    form_class = ProblemForm

    def get_context_data(self, **kwargs):
        context = super(ViewProblemView, self).get_context_data(**kwargs)
        form = ProblemForm(self.request.POST or None)
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            context["path"] = get_solution(context["form"].cleaned_data['problem_input'])
        else:
            context["invalid_form"] = True
        return super(TemplateView, self).render_to_response(context)
