IO_BASE_PROMPT = """
    You are a helpful coding assistant collaborating with a user to generate or refine code. Your responses should be clear,\n 
    informative, and help the user achieve their goals efficiently.
    ``` Look the example of debugging Q&A, which may help you undetstand how to debug.

    Q: I am having trouble understanding this code. Can you explain what this code is trying to do? I also noticed that the return statement is empty. 
    What should I return as the output of this function? Lastly, can you explain the purpose of the variables 'start' and 'max_length'? 
    Here is my code: ```python def longest_palindromic_substring(s: str) -> str: n = len(s) if n == 0: return "" start, max_length = 0, 1 for i in range(n): l, 
    r = i, i while r < n - 1 and s[r] == s[r + 1]: r += 1 i = r while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]: l -= 1 r += 1 length = r - l + 1 
    if length > max_length: start, max_length = l, length return s[start:start + max_length] ```
    
    A: Sure, I would be happy to help. First, let me explain what the code is trying to do. The function `longest_palindromic_substring` takes a string `s` as input and 
    returns the longest palindromic substring in `s`. A palindromic string is a string that reads the same backward as forward, for example, "racecar" is a palindromic string. 
    The function works by iterating through each character in the string `s` and checking whether there is a palindromic string that starts with that character. 
    To do this, it checks whether there are any palindromes that are centered around that character. If there are, it updates the `start` and `max_length` variables to 
    keep track of the longest palindromic substring seen so far. Now, let's move on to the bugs in the code. The first bug is on line 3, where the function returns nothing 
    if the length of the input string `s` is 0. This is problematic because the function is expected to return a string value. We can fix this by changing the return statement 
    to `return ""` so that the function returns an empty string if the input string is empty. The second bug is on line 22, where the function returns nothing after performing 
    all the necessary computations. This is also problematic because the function is expected to return the longest palindromic substring as a string value. We can fix this by 
    changing the return statement to `return s[start:start + max_length]` so that the function returns the longest palindromic substring. Finally, the purpose of 
    the `start` and `max_length` variables is to keep track of the starting index and length of the longest palindromic substring seen so far. The `start` variable is 
    initially set to 0, and the `max_length` variable is initially set to 1. These values are updated whenever a longer palindromic substring is found. 
    To summarize, the bugs in the code are related to the return statements, and we can fix them by changing them to return the appropriate string values. 
    The purpose of the `start` and `max_length` variables is to keep track of the longest palindromic substring seen so far. Here is the corrected code: 
    ```python def longest_palindromic_substring(s: str) -> str: n = len(s) if n == 0: return "" start, max_length = 0, 1 for i in range(n): l, r = i, i 
    while r < n - 1 and s[r] == s[r + 1]: r += 1 i = r while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]: l -= 1 r += 1 length = r - l + 1 if length > max_length: 
    start, max_length = l, length return s[start:start + max_length] ```

Observe the following {LANG} faulty code which is complete with no extra context. Your task is to fix the code.

Before writing your final answer, carefully analyze the code step by step to identify any bugs or errors and determine how to fix them. carefully read the code you fixed before and check if there is still any issue.  Do not include this analysis in your final response.

Your final response should:

- Provide the fixed code enclosed within <code></code> tags.
- Include a short explanation of the modification in less than 20 words, enclosed within <exp></exp> tags.
- Do not write anything else besides the code and the explanation within the specified tags.

Your reply should be formatted as follows:

<code>
[Your fixed code here]
</code>
<exp>
[Your short explanation here]
</exp>
"""
IO_INTENTION_PROMPT = """Observe the function intention and its corresponding {LANG} implementation which is complete with no extra context. The implementation is faulty. Your task is to fix up the code and explain on the modification in less than 20 words.
You have to write the fixed code again. You should put <code></code> and <exp></exp> on the boundary of the code and the explanation. Do not write anything else in your response. Your reply should be like this:
<code>
fixed code
</code>
<exp>
short explanation about the bug
</exp>"""

IO_EX_PROMPT = """"""

IO_TRACEBACK_PROMPT = """Observe the following {LANG} faulty code which is complete with no extra context and its traceback messages. Your task is to fix up the code and explain on the modification in less than 20 words.
You have to write the fixed code again. You should put <code></code> and <exp></exp> on the boundary of the code and the explanation. Do not write anything else in your response. Your reply should be like this:
<code>
fixed code
</code>
<exp>
short explanation about the bug
</exp>"""

IO_COMPLETE_SYSTEM_INFO = """Observe the program question and {LANG} implementation schema. Your task is to complete the implementation. 
You should write the completed code again. You should put <code></code> on the boundary of the code. Do not write anything else in your response. Your reply should be like this:
<code>
completed code
</code>"""

IO_COMPLETE_USER_PROMPT = """- Program Question
{INTENTION}
- Implementation Schema
{SIGNATURE}
"""

EXTRACT_SIGNATURE_PROMPT = """Observe the following code. Your task extract ONLY the class & function SIGNATURE. Wrap the cleaned code with <code>, </code>. Do not write anything else in the response. Do not forget the class. Do not miss any functions.
Here are some examples.

- User Input
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {

        if(str1+str2==str2+str1)
        {
            return str1.substr(0,gcd(str1.length(),str2.length()));
        }
        else{
            return "";
        }
        
    }
};
- Response
<code>class Solution {
public:
    string gcdOfStrings(string str1, string str2);
};</code>

- User Input
class Solution {
    public Node connect(Node node) {
        Map<Integer, List<Node>> map = new HashMap<>();
        goDFS(0, node, map);
        for (int key : map.keySet()) {
            List<Node> list = map.get(key);
            for (int i = 1; i < list.size(); i++) {
                list.get(i - 1).next = list.get(i);
            }
        }
        return node;
    }

    private void goDFS(int lvl, Node node, Map<Integer, List<Node>> map) {
        if (node == null) return;

        List<Node> list = map.computeIfAbsent(lvl, k -> new ArrayList<>());
        list.add(node);
        lvl++;
        goDFS(lvl, node.left, map);
        goDFS(lvl, node.right, map);
    }
}
- Response
<code>class Solution {
    public Node connect(Node node);
    private void goDFS(int lvl, Node node, Map<Integer, List<Node>> map);
}</code>

- User Input
def tsum(root):
    if(root==None):
        return 0
    x= root.val+tsum(root.left)+tsum(root.right)
    return x
def fun(root,sm,mx):
    if(root==None):
        return 0
    a=fun(root.left,sm,mx)
    b=fun(root.right,sm,mx)
    mx[0]=max(mx[0],a*(sm-a),b*(sm-b))
    return a+b+root.val
    
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mx=[0]
        sm=tsum(root)
        memo={}
        fun(root,sm,mx)
        return mx[0]%(10**9+7)
- Response
<code>def tsum(root):
def fun(root,sm,mx):
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:</code>
"""