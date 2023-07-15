tri = 286
pent = 165
hex = 143

tri_val = tri * (tri + 1) // 2
pent_val = pent * ((3 * pent) - 1) // 2
hex_val = hex * ((2 * hex) - 1)

while True:
    if tri_val == pent_val == hex_val:
        print(tri_val)
        print(tri, pent, hex)
        break
    tri += 1
    tri_val = tri * (tri + 1) // 2
    if tri_val > hex_val:
        hex += 1
        hex_val = hex * ((2 * hex) - 1)
    if tri_val > pent_val:
        pent += 1
        pent_val = pent * ((3 * pent) - 1) // 2
