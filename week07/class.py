from abc import ABCMeta, abstractmethod


# 动物园类
class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal):
        species = animal.__class__.__name__
        if not self.animals.get(species):
            self.animals[species] = animal
            print(animal, '已成功加入动物园')
        else:
            print('该类动物已存在')

    def __getattr__(self, class_name):
        return True if self.animals.get(class_name) else False


# 动物类
class Animal(metaclass=ABCMeta):
    def __init__(self, species, size, nature):
        self.species = species
        self.size = size
        self.nature = nature

    @property
    def violent(self):
        return self.size != '小' and self.species == '食肉' and self.nature == '凶猛'


# 猫类
class Cat(Animal):
    _yell = "喵"

    def __init__(self, name, species, size, nature):
        super().__init__(species, size, nature)
        self.name = name

    @property
    def petable(self):
        return not self.violent


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')

