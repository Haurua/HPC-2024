from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Clients, Inspections
from .forms import ClientForm, ClientNoteForm, InspectionForm
from django.db.models import Q
import datetime


# Dashboard CBV
class Dashboard(LoginRequiredMixin, ListView):
    """ Dashboard view that shows upcoming, overdue and completed inspections. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Inspections
    context_object_name = "inspections"
    template_name = "crm_jobs/dashboard.html"

    def get_queryset(self):
        """ Overriding this function to filter inspection objects. """
        queryset = {
            "upcoming": Inspections.objects.all().filter(date__gte=datetime.date.today(),
                                                         client__status="ACTIVE",
                                                         completed="NO"),
            "overdue": Inspections.objects.all().filter(date__lt=datetime.date.today(),
                                                        client__status="ACTIVE",
                                                        completed="NO"),
            "complete": Inspections.objects.all().filter(completed="YES")
        }
        return queryset


# Client CBVs
class ClientList(LoginRequiredMixin, ListView):
    """ List view that shows active and inactive clients. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Clients
    context_object_name = "clients"
    template_name = "crm_jobs/client/client_list.html"

    def get_queryset(self):
        """ Overriding this function to filter between active and inactive clients, including search function. """
        if self.request.GET.get("search_query"):
            search_query = self.request.GET.get("search_query")
            query_set = {
                "active": Clients.objects.filter(
                    Q(first_name__icontains=search_query) |
                    Q(last_name__icontains=search_query)).filter(status="ACTIVE"),
                "inactive": Clients.objects.filter(
                    Q(first_name__icontains=search_query) |
                    Q(last_name__icontains=search_query)).filter(status="INACTIVE")
            }

            if query_set["active"].values() or query_set["inactive"].values():
                messages.add_message(self.request, messages.SUCCESS, f"Search results for \"{search_query}\".")
            else:
                messages.add_message(self.request, messages.ERROR, f"No results for \"{search_query}\".")
            return query_set

        query_set = {
            "active": Clients.objects.filter(status="ACTIVE"),
            "inactive": Clients.objects.filter(status="INACTIVE")
        }
        return query_set


class ClientCreate(LoginRequiredMixin, CreateView):
    """ View to create new clients. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Clients
    form_class = ClientForm
    template_name = "crm_jobs/client/client_create.html"

    def get_success_url(self):
        """ Overriding this function to display success message upon client object creation. """
        messages.add_message(self.request, messages.SUCCESS, "Client created successfully.")
        return reverse_lazy("client-list")


class ClientNoteCreate(LoginRequiredMixin, UpdateView):
    """ View to create new clients. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Clients
    form_class = ClientNoteForm
    template_name = "crm_jobs/client/client_note_create.html"

    def get_success_url(self):
        """ Overriding this function to show success message upon inspection update. """
        messages.add_message(self.request, messages.SUCCESS, "Client Note edited successfully.")
        pk = self.kwargs['pk']
        return reverse("client-detail", kwargs={"pk": pk})


class ClientDetail(LoginRequiredMixin, DetailView):
    """ View to view specific client details. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Clients
    template_name = "crm_jobs/client/client_detail.html"


class ClientUpdate(LoginRequiredMixin, UpdateView):
    """ View to update specific client details. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Clients
    form_class = ClientForm
    template_name = "crm_jobs/client/client_update.html"

    def get_success_url(self):
        """ Overriding this function to show success message upon inspection update. """
        messages.add_message(self.request, messages.SUCCESS, "Client updated successfully.")
        pk = self.kwargs['pk']
        return reverse("client-detail", kwargs={"pk": pk})


class ClientDelete(LoginRequiredMixin, DeleteView):
    """ View to delete specific client. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Clients
    template_name = "crm_jobs/client/client_delete.html"

    def get_success_url(self):
        """ Overriding this function to show success message upon inspection update. """
        messages.add_message(self.request, messages.SUCCESS, "Client deleted successfully.")
        return reverse("client-list")


# Inspection CBVs
class InspectionList(LoginRequiredMixin, ListView):
    """ View to view all inspections. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Inspections
    template_name = "crm_jobs/inspection/inspection_list.html"


class InspectionCreate(LoginRequiredMixin, CreateView):
    """ View to create new inspection objects. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Inspections
    form_class = InspectionForm
    template_name = "crm_jobs/inspection/inspection_create.html"

    def get_initial(self):
        """ Overriding this function to retrieve the client name for the client form field. """
        client = Clients.objects.get(id=self.kwargs['pk'])
        return {"client": client}

    def form_valid(self, form):
        """ Overriding this function to automatically fill the client form field. """
        form.instance.client = Clients.objects.get(id=self.kwargs['pk'])
        return super(InspectionCreate, self).form_valid(form)

    def get_success_url(self):
        """ Overriding this function to show success message upon inspection update. """
        messages.add_message(self.request, messages.SUCCESS, "Inspection created successfully.")
        pk = self.kwargs['pk']
        return reverse("client-detail", kwargs={"pk": pk})


class InspectionDetail(LoginRequiredMixin, DetailView):
    """ View to view inspection details. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Inspections
    template_name = "crm_jobs/inspection/inspection_detail.html"


class InspectionUpdate(LoginRequiredMixin, UpdateView):
    """ View to update inspection details. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Inspections
    form_class = InspectionForm
    template_name = "crm_jobs/inspection/inspection_update.html"

    def get_success_url(self):
        """ Overriding this function to show success message upon inspection update. """
        messages.add_message(self.request, messages.SUCCESS, "Inspection updated successfully.")
        pk = self.kwargs['pk']
        return reverse("inspection-detail", kwargs={"pk": pk})


class InspectionDelete(LoginRequiredMixin, DeleteView):
    """ View to delete inspection objects. """
    login_url = reverse_lazy("login")
    redirect_field_name = "login"
    model = Inspections
    template_name = "crm_jobs/inspection/inspection_delete.html"

    def get_success_url(self):
        """ Overriding this function to show success message upon inspection update. """
        messages.add_message(self.request, messages.SUCCESS, "Inspection deleted successfully.")
        return reverse("inspection-list")
