class Solution:
    def lenLongestFibSubseq(self, arr) -> int:
        i = 0
        sum = 0
        while i != len(arr) - 1:
            print('----- ------- ------- -------')
            temp_var1 = arr[i]
            for j in range(len(arr[i:]) - 1):
                temp_var2 = arr[i + j + 1]
                sum_i = 1
                while True:
                    temp_var = temp_var1 + temp_var2
                    print(f'{temp_var1} + {temp_var2} = {temp_var}')
                    if temp_var in arr:
                        temp_var1 = temp_var2
                        temp_var2 = temp_var
                        sum_i += 1
                    else:
                        if sum_i > sum:
                            sum = sum_i + 1
                        print('sum_i = ', sum_i)
                        print('----- ------- ------- -------')
                        break
            i += 1
        return sum

    def lenLongestFibSubseq1(self, arr) -> int:
        sum_result = 0
        for i in range(len(arr) - 1, 0, -1):
            sum = 1
            print('-- -------- ------- ------- ----')
            j = i
            var1 = arr[j]
            for j in range(i-1, 0, -1):
                var2 = arr[j]
                print(f'---{arr[j]}---')

                while True:
                    var_result = var1 - var2
                    if var_result> var1/2:
                        print(f'{var1}-{var2}={var_result}', end=' | ')
                    if var_result in arr:
                        var1, var2 = var2, var_result
                        sum += 1

                    else:
                        if sum > sum_result:
                            sum_result = sum
                        break

                print()
        return sum_result


b = [1, 2, 3, 4, 5, 6, 7, 8]
c = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
# print('sum = ', Solution.lenLongestFibSubseq(self=Solution, arr=b))
print('sum = ', Solution.lenLongestFibSubseq1(self=Solution, arr=b))
