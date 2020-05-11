import asyncio


async def test_install(guillotina_scootermpi_requester):  # noqa
    async with guillotina_scootermpi_requester as requester:
        response, _ = await requester('GET', '/db/guillotina/@addons')
        assert 'guillotina_scootermpi' in response['installed']
