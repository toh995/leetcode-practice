class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province_count = 0
        should_check = set(range(n))

        def check_city(city1: int, province: Set[int]) -> None:
            should_check.remove(city1)

            for city2 in range(n):
                if isConnected[city1][city2] == 1:
                    province.add(city2)

                    if city2 in should_check:
                        check_city(city2, province)

        while should_check:
            city = next(iter(should_check))
            new_province = set({city})
            province_count += 1

            check_city(city, new_province)

        return province_count
