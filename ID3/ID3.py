#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import log
from operator import itemgetter
import sys

class DecisionTree:
    threshold = 0.1
    trainData = []
    trainLabel = []
    featureVals = [[] for i in range (6)]    #存放特征可能取值
    tree = []
    m = 0   #训练集个数
    n = 0   #特征数

    #初始化
    def __init__(self):


    #加载数据
    def load_data(self):
        #未完成的文件读入
        #f = open('../西瓜.txt', 'r+', encoding = 'utf-8')
        #f.read()
        self.trainData = [
            ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑'],
            ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑'],
            ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑'],
            ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑'],
            ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑'],
            ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘'],
            ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘'],
            ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑'],
            ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑'],
            ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘'],
            ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑'],
            ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘'],
            ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑'],
            ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑'],
            ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘'],
            ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑'],
            ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑']
        ]

        self.trainLabel[0:7] = [1]
        self.trainLabel[8:16] = [0]
        self.m = 17
        self.n = 6

    #计算Shannon熵
    def calc_ent(self, dataset):

        t = 0
        f = 0
        for i in range (0, len(dataset)):
            if dataset[i][-1] == 1:
                t += 1
            else:
                f += 1

        t_rate = t / len(dataset)
        f_rate = f / len(dataset)
        return - t_rate * log(t_rate) - f_rate * log(f_rate)

    #计算信息增益
    def calc_gain(self, dataset, feature):
        old_ent = self.calc_ent(dataset)
        list_split = self.split_dataset(dataset, feature)
        new_ent = self.calc_ent(list_split)
        return old_ent - new_ent


    #记录数据集中每个特征的不同取值
    def feature_vals_count(self, dataset):
        for i in dataset:
            for j in i:
                if j not in self.featureVals[i]:
                    self.featureVals[i].append(j)

    #计算数据集中每个标签出现的次数
    def label_count(self, dataset):
        labelCount = {}
        for i in dataset:
            if self.trainLabel[i] in labelCount.keys():
                labelCount[self.trainLabel[i]] += 1
            else:
                labelCount[self.trainLabel[i]] = 1
        return labelCount

    #分割数据集
    def split_dataset(self, dataset, feature):
        res = {}
        for i in dataset:
            if i[feature] not in res.keys():
                res[i[feature]]= [i]
            else:
                res[i[feature]].append(i)
        return res



    #构建决策树
    def create_decision_tree(self, dataset):
        #训练集都是一个类别，直接返回
        if self.label_count(dataset) == 1:
            self.tree.append(self.label_count(dataset).keys()[0])
            return self.tree
        #没特征，返回训练集中多的类别
        if len(self.featureVals) == 0:
            out = max(self.label_count(dataset).keys())
            self.tree.append(out)
            return self.tree
        #初始化阈值
        maxG = self.threshold
        chosen_feature = -1
        #选取信息增益最大的特征
        for i in range n:
            gain = self.calc_gain(dataset, i)
            if gain > maxG:
                maxG = gain
                chosen_feature = i
        #若最大的信息增益小于特征，返回训练集中多的类别
        if chosen_feature == -1:
            out = max(self.label_count(dataset).keys())
            self.tree.append(out)
            return self.tree
        else:
            new_dataset = self.split_dataset(dataset, chosen_feature)
            self.tree.append(chosen_feature)
            for i in self.split_dataset(dataset, chosen_feature)
            self.tree.append()
            for i in new_dataset:
                self.create_decision_tree(i)
            return



    #分类
    def classify(self, data):

def main():
    dt = DecisionTree()
    return 0

if __name__ == "__main__":
    sys.exit(main())

