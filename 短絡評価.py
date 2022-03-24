"""
目標: 短絡評価の仕組みを知る.
背景: if文を短く書いて可読性を上げたい.

"""

# 短絡評価なし
def sample(input_dict):
    if 'banana' in input_dict:
        if input_dict['banana'] >= 2:
            print("True")

# 短絡評価なし
def sample2(input_dict):
    """
    処理の順番は, 
    'banana' in input_dict -> input_dict['banana'] >= 2
    
    """
    if 'banana' in input_dict and input_dict['banana'] >= 2:
        print('True')

if __name__ == "__main__":
    input = {'apple':1, 'banana':3, 'orange':10, 'pine':5}
    
    sample(input)
    sample2(input)


