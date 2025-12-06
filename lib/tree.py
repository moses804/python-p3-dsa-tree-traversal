class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        # Start search from the root node
        return self._dfs(self.root, target_id)

    def _dfs(self, node, target_id):
        # Base case: if this node has the id we want, return it
        if node['id'] == target_id:
            return node
        
        # Otherwise, recursively search in its children
        for child in node['children']:
            found = self._dfs(child, target_id)
            if found:
                return found
        
        # If nothing was found below, return None
        return None
