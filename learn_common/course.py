class Course:
    def __init__(self, name, price, duration) -> None:
        super().__init__()
        self.name = name
        self.price = price
        self.duration = duration

    def __str__(self) -> str:
        return f'课程名称：{self.name},课程价格{self.price},课程持续时间{self.duration}月'
