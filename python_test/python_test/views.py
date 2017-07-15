"""View moduel fo client."""
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from forms import AddClientForm
from forms import EditClientForm
from models import Client


class ClientView(TemplateView):
    """View moduel fo client."""

    template_name = 'client/list.html'

    def get(self, request):
        """Get clients."""
        clients = Client.objects.all()

        return render(request, self.template_name, {'clients': clients})


class ClientAdd(TemplateView):
    """View module to add client."""

    template_name = 'client/add.html'

    def get(self, request):
        """Show Form to add client."""
        form = AddClientForm()

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        """Save client."""
        form = AddClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['name']
            form = AddClientForm()
            return redirect(reverse('client'))

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class ClientEdit(TemplateView):
    """View module to edit client information."""

    template_name = 'client/add.html'

    def get(self, request, pk):
        """Show Form to add client."""
        client = Client.objects.get(pk=pk)
        form = EditClientForm(instance=client)

        args = {'form': form, 'client': client}
        return render(request, self.template_name, args)

    def post(self, request, pk):
        """Save editted client information."""
        client = Client.objects.get(pk=pk)
        form = EditClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return redirect(reverse('client'))
