class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        paths = sorted(folder)
        curr_parent_path = paths[0]

        parents = [curr_parent_path]

        for path in paths:
            if not self.subpath_exists(path, curr_parent_path):
                curr_parent_path = path
                parents.append(path)

        return parents

    def subpath_exists(self, curr_path: str, potential_subpath: str) -> bool:
        """
        check if potential_subpath is a subpath of curr_path
        """
        if curr_path == potential_subpath:
            return True

        if len(potential_subpath) > len(curr_path):
            return False

        if len(potential_subpath) < len(curr_path):
            return curr_path.startswith(potential_subpath) \
                and curr_path[len(potential_subpath)] == "/"
