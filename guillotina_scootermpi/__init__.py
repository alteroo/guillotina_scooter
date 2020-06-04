from guillotina import configure


app_settings = {
    # "applications": [
    #     "guillotina.contrib.dbusers",
    #     # "guillotina.contrib.catalog.pg",
    #     "guillotina_elasticsearch",
    # ],
    # "elasticsearch": {
    #     "index_name_prefix": "guillotina-",
    #     "connection_settings": {
    #         "hosts": ["elasticsearch:9200"],
    #         "sniffer_timeout": 15,
    #         "sniff_timeout": 120
    #         "sniff_on_start": True,
    #     },
    #     "security_query_builder": "guillotina_elasticsearch.queries.build_security_query",
    # },
}


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan("guillotina_scootermpi.api")
    configure.scan("guillotina_scootermpi.install")
    configure.scan("guillotina_scootermpi.content")
    configure.scan("guillotina_scootermpi.services")
