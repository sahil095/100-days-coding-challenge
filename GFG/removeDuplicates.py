def removeDups(self, S):
	res_list = []
	res = ''
	list_s = list(s)
	for i in list_s:
	    if i not in res_list:
	        res_list.append(i)
	res = ''.join(res_list)
	return res