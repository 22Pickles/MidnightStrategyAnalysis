from typing import List

class Strategies:
    @staticmethod
    def str1(roll: List[int], pocket: List[int]) -> List[int]:
        s: List[int] = []
        if 1 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 1:
                    s.append(roll[i])
                    break
        if 4 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 4:
                    s.append(roll[i])
                    break

        for i in range(len(roll)):
            if roll[i] == 6:
                s.append(roll[i])
        if len(s) == 0:
            s.append(max(roll))
        return s

    @staticmethod
    def str2(roll: List[int], pocket: List[int]) -> List[int]:
        s: List[int] = []
        if 1 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 1:
                    s.append(roll[i])
                    break
        if 4 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 4:
                    s.append(roll[i])
                    break
        if len(s) == 0:
            s.append(max(roll))
        return s

    @staticmethod
    def str3(roll: List[int], pocket: List[int]) -> List[int]:
        s: List[int] = []
        if 1 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 1:
                    s.append(roll[i])
                    break
        if 4 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 4:
                    s.append(roll[i])
                    break
        for i in range(len(roll)):
            if roll[i] == 6:
                if len(roll) - len(s) < 4 and ((1 not in pocket) or (4 not in pocket)):
                    break
                else:
                    s.append(roll[i])
        if len(s) == 0:
            s.append(max(roll))
        return s

    @staticmethod
    def str4(roll: List[int], pocket: List[int]) -> List[int]:
        s: List[int] = []
        if 1 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 1:
                    s.append(roll[i])
                    break
        if 4 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 4:
                    s.append(roll[i])
                    break
        for i in range(len(roll)):
            if roll[i] == 6:
                if len(roll) - len(s) < 5 and ((1 not in pocket) or (4 not in pocket)):
                    break
                else:
                    s.append(roll[i])
        if len(s) == 0:
            s.append(max(roll))
        return s

    @staticmethod
    def str5(roll: List[int], pocket: List[int]) -> List[int]:
        s: List[int] = []
        if 1 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 1:
                    s.append(roll[i])
                    break
        if 4 not in pocket:
            for i in range(len(roll)):
                if roll[i] == 4:
                    s.append(roll[i])
                    break
        for i in range(len(roll)):
            if roll[i] == 6:
                if len(roll) - len(s) < 6 and ((1 not in pocket) or (4 not in pocket)):
                    break
                else:
                    s.append(roll[i])
        if len(s) == 0:
            s.append(max(roll))
        return s
