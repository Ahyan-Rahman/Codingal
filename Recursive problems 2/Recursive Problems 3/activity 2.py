Keypad=["","","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def PrintCombination(combination, curr, output, n):
    if(curr==n):
        print(*output,sep=",")
        return
    for i in range(len(Keypad[combination[curr]])):
        output.append(Keypad[combination[curr[i]]])
        PrintCombination(combination,curr + 1, output, n)
        output.pop()
        if(combination[curr]==0 or combination[curr]==1):

            return
        
combination=[4,3,4]
n=len(combination)
PrintCombination(combination, 0, [], n)

