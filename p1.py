def main():
	inp=input("Enter the Plain text:")
	sentence = []
	for i in inp:
		if i==" ":
			continue
		else:
			sentence.append(i)
	rsp="".join(str(x) for x in sentence)
	#print(rsp)
	k=8-(len(rsp)%8)
	while (k>0):
		sentence.append(" ")
		k=k-1
	#print(sentence)
	fip="".join(str(x) for x in sentence)
	#print(fip)
	binary=[]
	for i in fip:
		binary.append('{0:08b}'.format(ord(i)))
	input1="".join(str(x) for x in binary)
	print(input1[0:63])
	blklen=int(len(input1)/64)
	blocks=[[ None for i in range(64)] for j in range(blklen) ]
	for i in range(blklen):
		k=i*64
		blocks[i]=input1[k:k+63]
	print(blocks)

if __name__ == '__main__':
	main()