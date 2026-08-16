class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for s_el in s:

            if s_el in "([{":
                st.append(s_el)

            else:
                if not st:
                    return False

                if st[-1] != pairs[s_el]:
                    return False

                st.pop()

        return len(st) == 0