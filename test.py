def main():
    print("Start")
    import sys

        
    def sum_of_squares(number_of_digits, index):
        ("Print Sqaring now :")
        input_digits = input()
        data = input_digits.strip().split()
        print(data)
        numbers = data
        
        def calc_sum(nums):
            if not nums:
                return 0
            head, *tail = nums
            head = int(head)
            if head < 0:
                return calc_sum(tail)
            else:
                return head * head + calc_sum(tail)
        
        return calc_sum(numbers), index + 1 + number_of_digits

    
    
    def process_cases(n, idx):
        if n == 0:
            return
        number_of_digits = int(input())
        print(number_of_digits)
        result, new_idx = sum_of_squares(number_of_digits, idx)
        results.append(result)
        process_cases(n - 1, new_idx)

    
    
    def print_result(result , idx):
        if idx < 0 :
            return
        
        print(results[idx])
        print_result(result,idx-1)
        
        
    number_of_cases = int(input())
        
    index = 1
    results = []
        
    process_cases(number_of_cases, index)
    print_result(results,number_of_cases-1)

if __name__ == "__main__":
    main()
