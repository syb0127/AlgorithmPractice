class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1, split2 = version1.split('.'), version2.split('.')
        maxLength = max(len(split1), len(split2))

        for i in range(maxLength):
            v1 = int(split1[i]) if i < len(split1) else 0
            v2 = int(split2[i]) if i < len(split2) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        # No need for additional loop, since the zero-padding handles the non-zero check implicitly
        return 0