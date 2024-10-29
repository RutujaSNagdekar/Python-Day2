#!/usr/bin/python3
import pandas as pp

# dd = pp.read_csv('dataframes1.csv')
# print(dd.dtypes)

# dd = pp.read_csv('dataframes1.csv')
# print(dd.set_index('key1'))

#
# dd = pp.read_csv('dataframes1.csv', index_col='key1')
# print(dd)
#
# out = pp.read_csv('dataframes1.csv')
# print(out[['key1', 'key2']])
#
# pp.__version__
# out = pp.read_csv('dataframes1.csv')
# print(out.columns) #### Index all columns
# print(out[out.columns[1:2]]) ####### Slice the columns


#
# out.loc[2,"key1"] = "New_data" ## Replace 2nd index of "Col_name" column with "New_data"
# print(out)
#
# print(out.loc[[2,3],["key1","key2"]]) ## Print 2nd index from Col1 and 3rd index from Col2
#
# print(out.loc[:,["key1","key2"]]) ## Print ':' (means all indexes) from Col1 and Col2
#
# print(out.loc[["key1","key2"],:]) ## Print ':' (means all indexes) from Col1 and Col2 in reverse order
#

out = pp.read_csv('dataframes1.csv')
#print(out)
print(out.iloc[2])   ## print only row 2
# print(out.iloc[[2]])   ## bcoz of [[]], it will put it in DataFrame
# print(out.iloc[6, 2])   ## print row 6 and column 2
# print(out.iloc[:5, :5])   ## It also work with slices, print 5 rows from 5 first columns


