from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
	context = {
		"inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
		"greeting": "Thank you for visiting", 
	}
	return render(request, "home.html", context)

class AboutPageView(TemplateView):
	template_name = "about.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["contact_address"] = "123 Cool Guy Street"
		context["phone_number"] = "111-222-3333"
		return context

class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Product_A"] = "Helium-3 Isotope |"
        context["Product_B"] = "Fresh Hay |"
        context["Product_C"] = "Tires (1 left in stock |"
        context["Product_D"] = "My stupid iphone charger that makes a weird buzzing sound whenever i plug it in |"
        return context
