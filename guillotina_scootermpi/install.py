# -*- coding: utf-8 -*-
from guillotina import configure
from guillotina.addons import Addon
from guillotina.content import create_content_in_container
from guillotina.interfaces import IRolePermissionManager
from guillotina.utils import get_registry


@configure.addon(
    name="guillotina_scootermpi",
    title="A Master Patient Index ")
class ManageAddon(Addon):

    @classmethod
    async def install(cls, container, request):
        registry = await get_registry(container)  # noqa
        if not await container.async_contains('patients'):
            patients = await create_content_in_container(
                container, 'PatientFolder', 'patients',
                id='patients', creators=('root',),
                title="Patients",
                contributors=('root',))
            roleperm = IRolePermissionManager(patients)
            roleperm.grant_permission_to_role(
                'guillotina.AddContent', 'guillotina.Member')
            roleperm.grant_permission_to_role(
                'guillotina.AccessContent', 'guillotina.Member')

    @classmethod
    async def uninstall(cls, container, request):
        registry = await get_registry(container)  # noqa
        # uninstall logic here...
