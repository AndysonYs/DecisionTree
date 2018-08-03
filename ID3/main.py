#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ID3
import sys


def main():
    dt = ID3.DecisionTree()
    dt.load_train_data()
    tree = dt.create_decision_tree(dt.train_data, dt.feature_names)
    print(tree)
    # test_data = ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', 0]
    # print(dt.classify(test_data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
