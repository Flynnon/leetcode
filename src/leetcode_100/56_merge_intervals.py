# 给出一个区间的集合，请合并所有重叠的区间。

# DEMO:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
            排序合并即可
        :type intervals: list
        :rtype: List[Interval]
        """
        # 处理空输入
        if not intervals:
            return []
        # 排序, 才能遍历..
        intervals.sort(key=lambda x:x.start)
        # 初始化结果集
        result = [intervals[0]]
        # 遍历
        for i in range(1, len(intervals)):
            # 得到 前一个范围 和 当前范围
            prev, current = result[-1], intervals[i]
            # 若有重合, 合并
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            # 没有重合, 将当前节点加入
            else:
                result.append(current)
        return result