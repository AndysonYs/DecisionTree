# DecisionTree
python3 decision tree ID3  
参考whatbag的个人主页中决策树专栏：
>http://whatbeg.com/2016/04/23/decisiontree.html

##ID3算法介绍

##Dateset:  
in breastcancer.txt  
###from  
>http://whatbeg.com/2016/04/23/decisiontree.html#%E5%9C%A8%E4%B9%B3%E8%85%BA%E7%99%8C%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E6%B5%8B%E8%AF%95%E4%B8%8E%E8%A1%A8%E7%8E%B0

  
###format
这里我选择了威斯康辛女性乳腺癌的数据。数据总共有9列，每一列分别代表，以逗号分割.
1 Sample code number （病人ID）  
2 Clump Thickness 肿块厚度  
3 Uniformity of Cell Size 细胞大小的均匀性  
4 Uniformity of Cell Shape 细胞形状的均匀性  
5 Marginal Adhesion 边缘粘  
6 Single Epithelial Cell Size 单上皮细胞的大小  
7 Bare Nuclei 裸核  
8 Bland Chromatin 乏味染色体  
9 Normal Nucleoli 正常核  
10 Mitoses 有丝分裂  
11 Class: 2 for benign, 4 formalignant（恶性或良性分类）

总共700条左右的数据，选取最后80条作为测试集，前面作为训练集，进行学习。
