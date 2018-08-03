#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import log


class DecisionTree:
    threshold = 0.1
    train_data = []
    feature_names = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
    feat_all_vals = []

    # 从文件加载数据
    # 尚未完成以后写吧
    def load_file_data(self):
        return

    # 加载数据
    def load_train_data(self):
        self.train_data = [
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
        self.feature_names = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
        # 记录数据集中每个特征的不同取值
        for feat_index in range(len(self.feature_names)):
            self.feat_all_vals.append(list(set([feat_vec[feat_index] for feat_vec in self.train_data])))
        return

    def calc_ent(self, dataSet):  # 计算香农熵
        set_size = len(dataSet)
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

    # 分割数据集
    def split_dataset(self, dataset, feature_index, val):
        return_set = []
        for featVec in dataset:
            if featVec[feature_index] == val:
                ret_vec = featVec[:feature_index]
                ret_vec.extend(featVec[feature_index + 1:])
                return_set.append(ret_vec)
        return return_set

    # 选择最优特征
    def choose_best_feat(self, dataset, featname):
        cur_env = self.calc_ent(dataset)

        best_feat_index = -1
        best_feat_gain = 0

        for i in range(len(featname)):
            new_ent = 0
            f_all_val = set([featVec[i] for featVec in dataset])
            for vals in f_all_val:
                v_set = self.split_dataset(dataset, i, vals)
                p = len(v_set) / float(len(dataset))
                new_ent += p * self.calc_ent(v_set)
            if cur_env - new_ent > best_feat_gain:
                best_feat_gain = cur_env - new_ent
                best_feat_index = i
        if best_feat_gain > self.threshold:
            return best_feat_index, best_feat_gain
        else:
            return -1, 0

    # 选择数据集中的多数label返回
    def choose_major_label(self, class_list):
        max_label = 0
        for label in set(class_list):
            if class_list.count(label) > max_label:
                max_label = class_list.count(label)
        return max_label

    # 构建决策树
    def create_decision_tree(self, dataset, featnames):
        feat_name = featnames[:]
        class_list = [feat_vec[-1] for feat_vec in dataset]  # 标签情况

        # 训练集都是一个类别，直接返回该类别
        if class_list.count(class_list[0]) == len(class_list):
            return class_list[0]

        # 特征用尽，返回训练集中多的类别
        if len(feat_name) == 0:
            return self.choose_major_label(class_list)

        # 选取信息增益最大的特征
        best_feat_index, best_feat_gain = self.choose_best_feat(dataset, featnames)
        best_feat_name = feat_name[best_feat_index]
        # 若最大的信息增益小于特征，返回训练集中多的类别
        if best_feat_index == -1:
            return self.choose_major_label(class_list)
        # 从特征集中删除该特征
        feat_name.remove(best_feat_name)
        # 生成决策树root
        decision_tree = {best_feat_name: {}}
        # 生成分支
        f_all_val = set([vec[best_feat_index] for vec in dataset])
        for vals in f_all_val:
            cp_feat_name = feat_name[:]
            decision_tree[best_feat_name][vals] = self.create_decision_tree(
                self.split_dataset(dataset, best_feat_index, vals), cp_feat_name)
        return decision_tree

    # 分类
    # 未完成
    def classify(self, tree, data):
        return
