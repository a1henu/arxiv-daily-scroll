---
layout: default
title: Tactile Recognition of Both Shapes and Materials with Automatic Feature Optimization-Enabled Meta Learning
---

# Tactile Recognition of Both Shapes and Materials with Automatic Feature Optimization-Enabled Meta Learning
**arXiv**：[2603.08423v1](https://arxiv.org/abs/2603.08423) · [PDF](https://arxiv.org/pdf/2603.08423.pdf)  
**作者**：Hongliang Zhao, Wenhui Yang, Yang Chen, Zhuorui Wang, Baiheng Liu, Longhui Qin  

**一句话要点**：提出自动特征优化原型网络AFOP-ML，通过元学习解决机器人触觉感知中数据稀缺与学习耗时问题。

**关键词**：触觉感知, 元学习, 少样本学习, 自动特征优化, 机器人操作

## 3 点简述
- 核心问题：机器人触觉感知需大量数据，但采集成本高且有时不可行，导致训练数据稀缺和学习过程耗时。
- 方法要点：基于四通道触觉信号，设计自动特征优化原型网络，实现元学习，快速适应新类别并自动确定最优特征空间。
- 实验或效果：在36类基准上，5-way-1-shot准确率达96.08%，极端36-way-1-shot保持88.7%，验证了泛化能力。

## 摘要（原文）

> Tactile perception is indispensable for robots to implement various manipulations dexterously, especially in contact-rich scenarios. However, alongside the development of deep learning techniques, it meanwhile suffers from training data scarcity and a time-consuming learning process in practical applications since the collection of a large amount of tactile data is costly and sometimes even impossible. Hence, we propose an automatic feature optimization-enabled prototypical network to realize meta-learning, i.e., AFOP-ML framework. As a ``learn to learn" network, it not only adapts to new unseen classes rapidly with few-shot, but also learns how to determine the optimal feature space automatically. Based on the four-channel signals acquired from a tactile finger, both shapes and materials are recognized. On a 36-category benchmark, it outperforms several existing approaches by attaining an accuracy of 96.08% in 5-way-1-shot scenario, where only 1 example is available for training. It still remains 88.7% in the extreme 36-way-1-shot case. The generalization ability is further validated through three groups of experiment involving unseen shapes, materials and force/speed perturbations. More insights are additionally provided by this work for the interpretation of recognition tasks and improved design of tactile sensors.

