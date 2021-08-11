#задание 3


class Worker:                                           #класс работник
  def __init__(self, name, surname, position, wage, bonus):
      self.name =  name                                 #атрибут имя
      self.surname = surname                            #атрибут фамилия
      self.position = position                          #атрибут должность
      self._income = {"wage": wage, "bonus": bonus}     #атрибут доход защищённый


class Position(Worker):   #класс Position на базе класса Worker
      def get_full_name(self):
        return self.name, self.surname                      #возвращаем Имя и Фамилию


      def get_total_income(self):
        return self._income["wage"] + self._income["bonus"] #возвращаем оклад плюс премия


rabotnik_1 = Position ("Ivan", "Ivanov", "Director", 100000, 10000)
print (rabotnik_1.name)
print (rabotnik_1.surname)

print (rabotnik_1._income)
print (rabotnik_1.get_full_name())
print (rabotnik_1.get_total_income())