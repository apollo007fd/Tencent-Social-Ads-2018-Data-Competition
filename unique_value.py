##--函数功能：统计某个表中一个字段包含哪些unique value--##
##--输入：
##-----field:包含数字字符串的一个字段；--##
##-----dframe:某个数据表--##
def unique_value(field, dframe):
    if (field in dframe.columns)==False:
        return '';
    uni_val = []
    values = dframe[field]
    values = values.unique()
    flag = [False for j in range(2000000)];
    length = values.shape[0]
    print('length:%d'%length)
    for j in range(length):
        if(j%100000==0): print(j);
        val = values[j];
        if val is np.nan: continue
        if isinstance(val, str):
            vals = val.split()
            vals = list(map(int, vals));
            for v in vals: flag[v] = True;
        else:
            flag[val] = True;
    for k in range(2000000):
        if flag[k] is True: uni_val.append(k);
    return uni_val;