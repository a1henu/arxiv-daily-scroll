---
layout: default
title: ReLKD: Inter-Class Relation Learning with Knowledge Distillation for Generalized Category Discovery
---

# ReLKD: Inter-Class Relation Learning with Knowledge Distillation for Generalized Category Discovery
**arXiv**：[2512.07229v1](https://arxiv.org/abs/2512.07229) · [PDF](https://arxiv.org/pdf/2512.07229.pdf)  
**作者**：Fang Zhou, Zhiqiang Chen, Martin Pavlovski, Yizhong Zhang  

**一句话要点**：提出ReLKD框架，通过隐式类间关系学习与知识蒸馏解决广义类别发现中的新类分类问题

**关键词**：广义类别发现, 类间关系学习, 知识蒸馏, 表示学习, 新类分类

## 3 点简述
- 核心问题：广义类别发现中，未标记数据包含已知和新类，现有方法常忽略类间关系，影响新类分类。
- 方法要点：ReLKD包含目标粒度模块、粗粒度模块和蒸馏模块，利用隐式类间关系提升表示学习。
- 实验或效果：在四个数据集上验证有效性，尤其在标记数据有限场景下表现优异。

## 摘要（原文）

> Generalized Category Discovery (GCD) faces the challenge of categorizing unlabeled data containing both known and novel classes, given only labels for known classes. Previous studies often treat each class independently, neglecting the inherent inter-class relations. Obtaining such inter-class relations directly presents a significant challenge in real-world scenarios. To address this issue, we propose ReLKD, an end-to-end framework that effectively exploits implicit inter-class relations and leverages this knowledge to enhance the classification of novel classes. ReLKD comprises three key modules: a target-grained module for learning discriminative representations, a coarse-grained module for capturing hierarchical class relations, and a distillation module for transferring knowledge from the coarse-grained module to refine the target-grained module's representation learning. Extensive experiments on four datasets demonstrate the effectiveness of ReLKD, particularly in scenarios with limited labeled data. The code for ReLKD is available at https://github.com/ZhouF-ECNU/ReLKD.

