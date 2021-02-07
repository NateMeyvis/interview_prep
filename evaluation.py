def test_longest_subarray_with_max_difference(f):
    '''The function should take two parameters, a sequence and a limit'''
    assert (result := f([8,2,4,7], 4)) == 2, f"LeetCode test case 1 ({result})"
    assert (result := f([10,1,2,4,7,2], 5)) == 4, f"LeetCode test case 2 ({result})"
    assert (result := f([4,2,2,2,4,4,2,2], 0)) == 3, f"LeetCode test case with zero limit ({result})"