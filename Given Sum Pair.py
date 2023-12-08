class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.hashmap1 = {}
        self.hashmap2 = {}
        for i in nums1:
            if i in self.hashmap1:
                self.hashmap1[i] += 1
            else:
                self.hashmap1[i] = 1
        for i in nums2:
            if i in self.hashmap2:
                self.hashmap2[i] += 1
            else:
                self.hashmap2[i] = 1

    def add(self, index, val):
        self.hashmap2[self.nums2[index]] -= 1
        self.nums2[index] += val
        if self.nums2[index] in self.hashmap2:
            self.hashmap2[self.nums2[index]] += 1
        else:
            self.hashmap2[self.nums2[index]] = 1

    def count(self, tot):
        count = 0
        for i in self.hashmap1:
            if tot - i in self.hashmap2:
                count += self.hashmap1[i] * self.hashmap2[tot - i]
        return count