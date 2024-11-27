from math import sqrt

WIDTH, HEIGHT = 1500, 1200

radius = 100
a = radius
h = radius * sqrt(3) / 2

hexagon_4x4 = [(WIDTH / 2, HEIGHT / 2),

               (WIDTH / 2 + a, HEIGHT / 2), (WIDTH / 2 + a / 2, HEIGHT / 2 - h), (WIDTH / 2 - a / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a, HEIGHT / 2), (WIDTH / 2 - a / 2, HEIGHT / 2 + h), (WIDTH / 2 + a / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + 2 * a, HEIGHT / 2), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + a, HEIGHT / 2 - 2 * h), (WIDTH / 2, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a, HEIGHT / 2 - 2 * h), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a * 2, HEIGHT / 2), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + h),
               (WIDTH / 2 - a, HEIGHT / 2 + 2 * h), (WIDTH / 2, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 + a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + 3 * a, HEIGHT / 2), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + 2 * a, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 + a / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - a / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - 2 * a, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 - h), (WIDTH / 2 - a * 3, HEIGHT / 2),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 + h), (WIDTH / 2 - a * 2, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 - a / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + a / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + 2 * a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 + h)]

hexagon_5x5 = [(WIDTH / 2, HEIGHT / 2),

               (WIDTH / 2 + a, HEIGHT / 2), (WIDTH / 2 + a / 2, HEIGHT / 2 - h), (WIDTH / 2 - a / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a, HEIGHT / 2), (WIDTH / 2 - a / 2, HEIGHT / 2 + h), (WIDTH / 2 + a / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + 2 * a, HEIGHT / 2), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + a, HEIGHT / 2 - 2 * h), (WIDTH / 2, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a, HEIGHT / 2 - 2 * h), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a * 2, HEIGHT / 2), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + h),
               (WIDTH / 2 - a, HEIGHT / 2 + 2 * h), (WIDTH / 2, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 + a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + 3 * a, HEIGHT / 2), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + 2 * a, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 + a / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - a / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - 2 * a, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 - h), (WIDTH / 2 - a * 3, HEIGHT / 2),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 + h), (WIDTH / 2 - a * 2, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 - a / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + a / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + 2 * a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + a * 4, HEIGHT / 2), (WIDTH / 2 + a * 7 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + a * 3, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 + a * 2, HEIGHT / 2 - h * 4),
               (WIDTH / 2 + a, HEIGHT / 2 - h * 4),
               (WIDTH / 2, HEIGHT / 2 - h * 4), (WIDTH / 2 - a, HEIGHT / 2 - h * 4),
               (WIDTH / 2 - a * 2, HEIGHT / 2 - h * 4),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - a * 3, HEIGHT / 2 - h * 2),
               (WIDTH / 2 - a * 7 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a * 4, HEIGHT / 2), (WIDTH / 2 - a * 7 / 2, HEIGHT / 2 + h),
               (WIDTH / 2 - a * 3, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 - a * 2, HEIGHT / 2 + 4 * h),
               (WIDTH / 2 - a, HEIGHT / 2 + 4 * h),
               (WIDTH / 2, HEIGHT / 2 + 4 * h), (WIDTH / 2 + a, HEIGHT / 2 + h * 4),
               (WIDTH / 2 + a * 2, HEIGHT / 2 + h * 4),
               (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 + a * 3, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 + a * 7 / 2, HEIGHT / 2 + h)
               ]

hexagon_6x6 = [(WIDTH / 2, HEIGHT / 2),

               (WIDTH / 2 + a, HEIGHT / 2), (WIDTH / 2 + a / 2, HEIGHT / 2 - h), (WIDTH / 2 - a / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a, HEIGHT / 2), (WIDTH / 2 - a / 2, HEIGHT / 2 + h), (WIDTH / 2 + a / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + 2 * a, HEIGHT / 2), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + a, HEIGHT / 2 - 2 * h), (WIDTH / 2, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a, HEIGHT / 2 - 2 * h), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a * 2, HEIGHT / 2), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + h),
               (WIDTH / 2 - a, HEIGHT / 2 + 2 * h), (WIDTH / 2, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 + a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + 3 * a, HEIGHT / 2), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + 2 * a, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 + a / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - a / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - 2 * a, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 - h), (WIDTH / 2 - a * 3, HEIGHT / 2),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 + h), (WIDTH / 2 - a * 2, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 - a / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + a / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + 2 * a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + a * 4, HEIGHT / 2), (WIDTH / 2 + a * 7 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + a * 3, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 + a * 2, HEIGHT / 2 - h * 4),
               (WIDTH / 2 + a, HEIGHT / 2 - h * 4),
               (WIDTH / 2, HEIGHT / 2 - h * 4), (WIDTH / 2 - a, HEIGHT / 2 - h * 4),
               (WIDTH / 2 - a * 2, HEIGHT / 2 - h * 4),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - a * 3, HEIGHT / 2 - h * 2),
               (WIDTH / 2 - a * 7 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 - a * 4, HEIGHT / 2), (WIDTH / 2 - a * 7 / 2, HEIGHT / 2 + h),
               (WIDTH / 2 - a * 3, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 - a * 2, HEIGHT / 2 + 4 * h),
               (WIDTH / 2 - a, HEIGHT / 2 + 4 * h),
               (WIDTH / 2, HEIGHT / 2 + 4 * h), (WIDTH / 2 + a, HEIGHT / 2 + h * 4),
               (WIDTH / 2 + a * 2, HEIGHT / 2 + h * 4),
               (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 + a * 3, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 + a * 7 / 2, HEIGHT / 2 + h),

               (WIDTH / 2 + a * 5, HEIGHT / 2), (WIDTH / 2 + a * 9 / 2, HEIGHT / 2 - h),
               (WIDTH / 2 + 4 * a, HEIGHT / 2 - 2 * h), (WIDTH / 2 + a * 7 / 2, HEIGHT / 2 - 3 * h),
               (WIDTH / 2 + a * 3, HEIGHT / 2 - 4 * h), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 - 5 * h),
               (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 - 5 * h), (WIDTH / 2 + a / 2, HEIGHT / 2 - 5 * h),
               (WIDTH / 2 - a / 2, HEIGHT / 2 - 5 * h), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 - 5 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 - 5 * h), (WIDTH / 2 - a * 3, HEIGHT / 2 - 4 * h),
               (WIDTH / 2 - a * 7 / 2, HEIGHT / 2 - 3 * h), (WIDTH / 2 - a * 4, HEIGHT / 2 - 2 * h),
               (WIDTH / 2 - a * 9 / 2, HEIGHT / 2 - h), (WIDTH / 2 - 5 * a, HEIGHT / 2),
               (WIDTH / 2 - a * 9 / 2, HEIGHT / 2 + h), (WIDTH / 2 - a * 4, HEIGHT / 2 + 2 * h),
               (WIDTH / 2 - a * 7 / 2, HEIGHT / 2 + 3 * h), (WIDTH / 2 - a * 3, HEIGHT / 2 + 4 * h),
               (WIDTH / 2 - a * 5 / 2, HEIGHT / 2 + 5 * h), (WIDTH / 2 - a * 3 / 2, HEIGHT / 2 + 5 * h),
               (WIDTH / 2 - a / 2, HEIGHT / 2 + 5 * h), (WIDTH / 2 + a / 2, HEIGHT / 2 + 5 * h),
               (WIDTH / 2 + a * 3 / 2, HEIGHT / 2 + 5 * h), (WIDTH / 2 + a * 5 / 2, HEIGHT / 2 + 5 * h),
               (WIDTH / 2 + 3 * a, HEIGHT / 2 + 4 * h), (WIDTH / 2 + a * 7 / 2, HEIGHT / 2 + 3 * h),
               (WIDTH / 2 + 4 * a, HEIGHT / 2 + 2 * h), (WIDTH / 2 + a * 9 / 2, HEIGHT / 2 + h),
               (WIDTH / 2 + 5 * a, HEIGHT / 2)
               ]

#  ZAJEBA SE 💀💀
