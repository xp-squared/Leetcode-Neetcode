'''
Counter:


Minimum Stack
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
'''

class MinStack:

    def __init__(self):
        # Creating both the regular and minimum stack
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        # Append the value to the main stack
        self.stack.append(val)
        if self.minStack:  # If minStack is not empty
            # Get the minimum from what we are inserting and what is already at the top of the minStack
            # recognize that if we have the value 3 but our min value on our minStack is 1 we get 1 as our minvalue again!
            # when we pop this causes us to pop the value that was last inserted in the regular stack which is good and copy value of the minimum of the MinStack
            min_val = min(val, self.minStack[-1])
        else:  # If minStack is empty, so we know this is the minimum value for now
            min_val = val
        # Append the minimum value to the minStack
        self.minStack.append(min_val)

    def pop(self) -> None:
        # Pop the value from both the main stack and the minStack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top value of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top value of the minStack, which is the minimum value in the main stack
        return self.minStack[-1]
        

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(5)
    minStack.push(3)
    minStack.push(0)
    minStack.push(7)
    minStack.push(9)
    print(minStack.getMin())  
    minStack.pop()
    print(minStack.top())    
    print(minStack.getMin()) 
