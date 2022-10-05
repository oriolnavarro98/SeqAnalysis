ascii_scores = "CCCFFFFFHHGHHJIJJJJJJJJJHIJJJJJJJJJJIJIIJJJJJJJJJJJJJJIJJIJJICHJJJJIIJJJIJHFFFFEEEEEEDDDDBDDDDDDDDDA\n"
definition = "@SRR2073165.20697288 HWI-ST384R:326:C68VYACXX:7:2302:4950:29241 length=100\n"

#substring = definition.split("length=")
#print(int(substring[-1]))

test = definition.split("length=")[-1]
test = int(test.split("\\n")[0])
print(test)
#print(ascii_scores[:test])
#int_scores = sum(ord(ascii_scores))
