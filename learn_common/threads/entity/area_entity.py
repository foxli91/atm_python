class Area:
    id = 0
    ara_name = ''
    area_code = ''

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f'id:{self.id},area_code:{self.area_code},ara_name:{self.ara_name}'
