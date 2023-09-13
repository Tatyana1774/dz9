# 1) Нахождение корней квадратного уравнения


def decor(func):
      decor_dict = {}
      count = 5

      def wrapper(a, b, c):
         for _ in range(count):
             result = func(a, b, c)
             arg = str(f"{a=} {b=} {c=}")
             decor_dict.update({arg: result})
             a += 1
             b += 1
             c += 1
         return decor_dict
      return wrapper
 

@decor

def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        x = (-b) / (2 * a)
        return round(x, 3)
    if discriminant < 0:
        return ()
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return round(x1, 3), round(x2, 3)


print(roots(3, 5, -10))

def viet(a, b, c):
     x1 = x2 = 0
     points = [i for i in range(-100, 100)]
     for i in points:
         x1 = i
         for j in points:
             x2 = j
             if x1 + x2 == -b / a and x1 * x2 == c / a:
                 return x1, x2
print(viet(1, -2, -3))