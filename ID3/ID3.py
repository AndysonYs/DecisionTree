#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import log
import sys

class DecisionTree:
    threshold = 0.1
    trainData = []
    feature_name = ['色泽','根蒂','敲声','纹理','脐部','触感']

    #加载数据
    def load_data(self):
        self.trainData = [
            ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 1],
            ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', 1],
            ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 1],
            ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', 1],
            ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 1],
            ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', 1],
            ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', 1],
            ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', 1],
            ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', 0],
            ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', 0],
            ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', 0],
            ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', 0],
            ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', 0],
            ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', 0],
            ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', 0],
            ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', 0],
            ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', 0]
        ]
        self.feature_name = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']

    def calc_ent(self, dataSet):  # 计算香农熵
        set_size = len()
        label_counts = {}
        for feature_vec in dataSet:
            label = feature_vec[-1]
            if label not in label_counts.keys():
                label_counts[label] = 0
            label_counts[label] += 1
        ent = 0.0
        for key in label_counts.keys():
            p_i = float(label_counts[key] / set_size)
            ent -= p_i * log(p_i, 2)
        return ent

    #计算信息增益
    def calc_gain(self, dataset, feature):

    #记录数据集中每个特征的不同取值
    def feature_vals_count(self, dataset):

    #计算数据集中每个标签出现的次数
    def label_count(self, dataset):

    #分割数据集
    def split_dataset(self, dataset, feature):

    #构建决策树
    def create_decision_tree(self, dataset):
        #训练集都是一个类别，直接返回
        #没特征，返回训练集中多的类别
        #选取信息增益最大的特征
        #若最大的信息增益小于特征，返回训练集中多的类别

    #分类
    def classify(self, data):

def main():
    return 0

if __name__ == "__main__":
    sys.exit(main())

