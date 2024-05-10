import strawberry

@strawberry.type (
    description="HELLOOOOOOOO"
)
class Playlist:
    id: strawberry.ID
    name: str
    description: str | None