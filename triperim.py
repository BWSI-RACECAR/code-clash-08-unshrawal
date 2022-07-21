"""
inputs. Each of the inputs will be list types, and your code will return a float. 

Test Cases:
Input: v1 = [3, 6]; v2 = [1, 2]; v3 = [8, 2];       Output = 17.875
Input: v1 = [0, -1]; v2 = [-5, 2]; v3 = [-3, -2];   Output = 13.465
Input: v1 = [0, 0]; v2 = [1, 2]; v3 = [3, 2];       Output = 7.842
"""

class Solution:
    def tri_perimeter(self,v1, v2, v3):
        # type v1: list
        # type v2: list
        # type v3: list
        # return: int

      d1 = ((v2[1]-v1[1])**2+(v2[0]-v1[0])**2)**0.5
      d2 = ((v3[1]-v1[1])**2+(v3[0]-v1[0])**2)**0.5
      d3 = ((v3[1]-v2[1])**2+(v3[0]-v2[0])**2)**0.5
      return d1 + d2 + d3

def main():
    array1 = input().split(" ")
    array2 = input().split(" ")
    array3 = input().split(" ")

    for x in range (0, len(array1)):
        array1[x] = int(array1[x])

    for x in range (0, len(array2)):
        array2[x] = int(array2[x])

    for x in range (0, len(array3)):
        array3[x] = int(array3[x])

    tc1 = Solution()
    ans = tc1.tri_perimeter(array1,array2,array3)
    ans = round(ans,3)
    print(ans)

if __name__ == "__main__":
    main()
