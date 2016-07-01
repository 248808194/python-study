#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print  ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")


print(
'''
= 和 == 有什么不同？
= (single-equal) 的作用是将右边的值赋予左边的变量名。`==` (double-equal) 的作用是检查左右
离岸边是否相等。习题 27 中你会学到 == 的用法。
'''
)