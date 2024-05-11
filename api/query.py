import strawberry
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists
from .types.playlist import Playlist

@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be featured to all users.")
    async def featured_playlists(self, info: strawberry.Info) -> list[Playlist]:
        spotify_client = info.context["spotify_client"]

        data = await get_featured_playlists.asyncio(client=spotify_client)

        return [
            Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description,
            )
            for playlist in data.playlists.items
        ]