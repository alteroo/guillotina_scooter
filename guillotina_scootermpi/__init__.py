from guillotina import configure


app_settings = {
    # provide custom application settings here...
}


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan("guillotina_scootermpi.api")
    configure.scan("guillotina_scootermpi.install")
    configure.scan("guillotina_scootermpi.content")
