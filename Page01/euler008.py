#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 8
        The four adjacent digits in the 1000-digit number that have
        the greatest product are 9 × 9 × 8 × 9 = 5832.

         73167176531330624919225119674426574742355349194934
         96983520312774506326239578318016984801869478851843
         85861560789112949495459501737958331952853208805511
         12540698747158523863050715693290963295227443043557
         66896648950445244523161731856403098711121722383113
         62229893423380308135336276614282806444486645238749
         30358907296290491560440772390713810515859307960866
         70172427121883998797908792274921901699720888093776
         65727333001053367881220235421809751254540594752243
         52584907711670556013604839586446706324415722155397
         53697817977846174064955149290862569321978468622482
         83972241375657056057490261407972968652414535100474
         82166370484403199890008895243450658541227588666881
         16427171479924442928230863465674813919123162824586
         17866458359124566529476545682848912883142607690042
         24219022671055626321111109370544217506941658960408
         07198403850962455444362981230987879927244284909188
         84580156166097919133875499200524063689912560717606
         05886116467109405077541002256983155200055935729725
         71636269561882670428252483600823257530420752963450

         Find the thirteen adjacent digits in the 1000-digit number
         that have the greatest product. What is the value of this product?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 23514624000
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

MATRIX_STR = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

# OPTIMIZADO

def mult_slide(slide):
    """
    slide  es un string de enteros "abcde..."
    devuelve un entero a*b*c*d*e*...
    """

    res = 1
    for i in slide:
        res *= int(i)
    return res

def evaluate(slide):
    """
    slide es un string de enteros "abcde..."
    devuelve la posicion del ultimo 0 encontrado +1.
             si no hay ninguno devuelve -1
    """

    zero_pos = slide.rfind("0")
    if zero_pos >= 0:
        return zero_pos + 1
    return -1

def euler8(slider_size, matrix):
    """
    recorre la matriz en  sliders de tamano slider_size.
    si el slider no tiene ningun 0, evalua cual de ellos tiene la mayor
    multiplicacion entre sus elementos
    """

#   i es el inicio del slide, puede ir de la 0 hasta canvas-size (incluido)
    i = 0
    maximum = 0, 0
    while i <= len(matrix) - slider_size:
        # Si el slide contiene un 0. lo tiro y el siguiente slide empieza
        # despues del ultimo 0. Esto salta muchas iteraciones.
        slide = matrix[i:i+slider_size]
        gap = evaluate(slide)
        if gap is not -1:
            i += gap
            continue
        else:
            # me guardo en una tupla los numeros consecutivos y
            # su multiplicacion que sean maximos en cada validacion de slide
            multiplied_terms = mult_slide(slide)
            if multiplied_terms >= maximum[1]:
                maximum = slide, multiplied_terms
            i += 1
    return maximum[1]

if __name__ == "__main__":
    print(euler8(4, MATRIX_STR))
#   5832
    print(euler8(13, MATRIX_STR)) #330 iteraciones
#   23514624000