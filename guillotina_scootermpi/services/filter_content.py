from guillotina.api import search
from elasticsearch_dsl.search import Search
from elasticsearch_dsl.query import Q
from guillotina import task_vars
from guillotina import configure
from guillotina.interfaces import IContainer
from guillotina_scootermpi.utils import json_response


@configure.service(
    context=IContainer,
    permission="guillotina.Public",
    name="@patient-filter",
    allow_access=True,
    method="GET"
)
async def patient_filter(context, request):
    search_value = request.query.get("query")
    query = Q("match", type_name='Patient') | Q("match", type_name='ScooterTag')
    s = Search().query(query)
    search_text = Q("match", title={"query": search_value, "fuzziness": 2})
    s = s.query(search_text)
    print(s.to_dict())
    request.query = {"query": s.to_dict()}
    search_result = await search.search_get(task_vars.container.get(),
                                            request)
    return json_response(200, search_result)
