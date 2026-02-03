---
layout: default
title: Multi-Task Learning for Robot Perception with Imbalanced Data
---

# Multi-Task Learning for Robot Perception with Imbalanced Data
**arXiv**：[2602.01899v1](https://arxiv.org/abs/2602.01899) · [PDF](https://arxiv.org/pdf/2602.01899.pdf)  
**作者**：Ozgur Erkent  

**一句话要点**：提出多任务学习方法以解决机器人感知中数据不平衡问题

**关键词**：多任务学习, 机器人感知, 数据不平衡, 语义分割, 深度估计

## 3 点简述
- 核心问题：多任务学习中数据不平衡导致样本不足，影响机器人感知性能。
- 方法要点：在部分任务缺乏真实标签时仍能学习，并分析任务间交互以提升性能。
- 实验或效果：在NYUDv2和Cityscapes数据集上验证语义分割与深度估计任务。

## 摘要（原文）

> Multi-task problem solving has been shown to improve the accuracy of the individual tasks, which is an important feature for robots, as they have a limited resource. However, when the number of labels for each task is not equal, namely imbalanced data exist, a problem may arise due to insufficient number of samples, and labeling is not very easy for mobile robots in every environment. We propose a method that can learn tasks even in the absence of the ground truth labels for some of the tasks. We also provide a detailed analysis of the proposed method. An interesting finding is related to the interaction of the tasks. We show a methodology to find out which tasks can improve the performance of other tasks. We investigate this by training the teacher network with the task outputs such as depth as inputs. We further provide empirical evidence when trained with a small amount of data. We use semantic segmentation and depth estimation tasks on different datasets, NYUDv2 and Cityscapes.

