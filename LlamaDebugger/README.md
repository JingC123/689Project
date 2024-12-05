This is LlamaDebugger Repo.


## Setup

1. Clone this repository and navigate into the project directory

    ```shell
    git clone https://github.com/JingC123/LlamaDebugger.git
    cd frontend || cd backend
    ```

2. Using `pnpm` to install frontend dependencies
  
    ```shell
    pnpm install
    ```


3. Run the backend server

    ```shell
    python server.py
    ```

4. Run the frontend server, and open [http://localhost:3000](http://localhost:3000) in your browser

    ```shell
    pnpm dev
    ```


5. Build the project for production

    ```shell
    pnpm build
    ```

class Solution:        def maxDepth(self, root: Optional[TreeNode]) -> int:            stack = [root]            res = -1            while stack:                node = stack.pop()                if node:                    res = max(res, 1 + self.maxDepth(node.left))                    res = max(res, 1 + self.maxDepth(node.right))            return res