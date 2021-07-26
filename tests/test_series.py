from math_series.series import fibonacci , list_fibonacci , lucas , list_lucas,list_sum_series,sum_series




def test_fibonacci():
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    actual = list_fibonacci([0 , 1, 2, 3, 4, 5, 6, 7])
    assert  expected == actual


def test_list_lucas():
    expected = [2, 1, 3, 4, 7, 11, 18, 29]
    actual = list_lucas([0 , 1, 2, 3, 4, 5, 6, 7])
    assert  expected == actual





def test_sum_series_fibonacci_seven():
    expected = 13
    actual = sum_series(7 ,0 ,1)
    assert  expected == actual
def test_sum_series_lucas_seven():
    expected = 29
    actual = sum_series(7 ,2 ,1)
    assert  expected == actual
def test_sum_series_seven_tow_one():
    expected = 50
    actual = sum_series(7 ,3 ,2)
    assert  expected == actual
def test_list_sum_series_fibonacci():
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 0 , 1)
    assert  expected == actual
def test_list_sum_series_lucas():
    expected = [2, 1, 3, 4, 7, 11, 18, 29]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 2 , 1)
    assert  expected == actual
def test_list_sum_series_n_4_two():
    expected = [4, 2, 6, 8, 14, 22, 36, 58]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 4 , 2)
    assert  expected == actual
def test_list_sum_series_n_six_five():
    expected = [6, 5, 11, 16, 27, 43, 70, 113]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 6 , 5)
    assert  expected == actual