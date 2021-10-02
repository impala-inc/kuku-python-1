# xx_2_9
#
#

import traceback


def func_a():
    func_b()


def func_b():
    func_c()


def func_c():
    func_d()


def func_d():
    traceback.print_stack(limit=5)


func_a()
