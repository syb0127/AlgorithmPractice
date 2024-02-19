class Solution:
    def simplifyPath(self, path: str) -> str:

        split_path = path.split("/")
        stack = []

        for path in split_path:
          if len(path)>0 and path != '.':
                if path == '..' and stack:
                    stack.pop()
                elif path != '..':
                    stack.append(path)
        
        return "/"+"/".join(stack)
    