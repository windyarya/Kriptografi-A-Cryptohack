from Crypto.Util.number import long_to_bytes

def find_cube_root(n):
       low = 0
       high = n
       while low < high:
           mid = (low+high)//2
           if mid**3 < n:
               low = mid+1
           else:
               high = mid
       return(low)

ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

print(long_to_bytes(find_cube_root(ct)))