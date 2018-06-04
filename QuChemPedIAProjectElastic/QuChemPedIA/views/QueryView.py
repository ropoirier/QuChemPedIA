from xml.dom.minidom import _clear_id_cache
from django.shortcuts import render
from QuChemPedIA.forms.QueryForm import QueryForm
from QuChemPedIA.search import *
from django.http.response import HttpResponseRedirect
from django.urls import reverse
import urllib.parse
import math


def build_url(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urllib.parse.urlencode(get)
    return url


def query(request):
    """
    controler that make research on different condition
    :param request: environment variable that contains arguement of the research
    :return: template html with dictionnary of value to display
    """
    query_form = QueryForm(request.GET or None)
    results = None
    try:
        page = int(request.GET.get('page'))
    except Exception as error:
        print(error)
        page = 0

    try:
        nbrpp = 10  # nombre de résultat par page
    except Exception as error:
        print(error)
        nbrpp = 10

    try:
        # switch on what we are looking for
        if 'CID' in request.GET.get('typeQuery'):
            results = search_cid(cid_value=request.GET.get('search'), nbrpp=nbrpp, page=page)

        if 'IUPAC' in request.GET.get('typeQuery'):
            results = search_iupac(iupac_value=request.GET.get('search'), nbrpp=nbrpp, page=page)

        if 'InChi' in request.GET.get('typeQuery'):
            # here we looking for inchi wich contain a part of what we looking for
            results = search_inchi(inchi_value=request.GET.get('search'), nbrpp=nbrpp, page=page)

        if 'Formula' in request.GET.get('typeQuery'):
            results = search_formula(formula_value=request.GET.get('search'), nbrpp=nbrpp, page=page)

        if 'SMILES' in request.GET.get('typeQuery'):
            results = search_smiles(smiles_value=request.GET.get('search'), nbrpp=nbrpp, page=page)

        if 'id_log' in request.GET.get('typeQuery'):
            # if we want to access to an id we forward it to the details page as a parameter
            url = build_url('details', get={'id': request.GET.get('search')})
            return HttpResponseRedirect(url)
        """
        if 'homo_alpha_energy' in request.GET.get('typeQuery'):
            results = list(Query.objects.filter(homo_alpha_energy=request.GET.get('search')))

        if 'homo_beta_energy' in request.GET.get('typeQuery'):
            results = list(Query.objects.filter(homo_beta_energy=request.GET.get('search')))

        if 'lumo_alpha_energy' in request.GET.get('typeQuery'):
            results = list(Query.objects.filter(lumo_alpha_energy=request.GET.get('search')))

        if 'lumo_beta_energy' in request.GET.get('typeQuery'):
            results = list(Query.objects.filter(lumo_beta_energy=request.GET.get('search')))
        """
    except Exception as error:
        print("error :")
        print(error)

    # if we have only one result we display the details of the molecule
    if results is None:
        results = '{}'
    test_result = json.loads(results)
    if test_result['nbresult'] == 0 or len(test_result) == 1:
        results = '{}'
        test_result = json.loads(results)

    print(len(test_result))
    if len(test_result) == 2 and request.GET.get('page') == 1:
        # if we have only one result we forward it to the detail page
        url = reverse('details', args={'id': int(test_result["0"][0]["id_log"])})
        return HttpResponseRedirect(url)

    return render(request, 'QuChemPedIA/query.html', {'results': test_result, 'query_form': query_form})
