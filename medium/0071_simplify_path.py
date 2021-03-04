class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = []

        for component in path.split("/"):
            if component in ("", "."):
                continue

            if component == "..":
                if len(ret) > 0:
                    ret.pop()
                continue

            else:
                ret.append(component)

        return "/" + "/".join(ret)
