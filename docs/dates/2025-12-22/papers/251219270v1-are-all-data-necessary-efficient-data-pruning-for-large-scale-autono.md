---
layout: default
title: Are All Data Necessary? Efficient Data Pruning for Large-scale Autonomous Driving Dataset via Trajectory Entropy Maximization
---

# Are All Data Necessary? Efficient Data Pruning for Large-scale Autonomous Driving Dataset via Trajectory Entropy Maximization
**arXiv**：[2512.19270v1](https://arxiv.org/abs/2512.19270) · [PDF](https://arxiv.org/pdf/2512.19270.pdf)  
**作者**：Zhaoyang Liu, Weitao Zhou, Junze Wen, Cheng Jing, Qian Cheng, Kun Jiang, Diange Yang  

**一句话要点**：提出基于轨迹熵最大化的数据剪枝方法，以高效管理大规模自动驾驶数据集。

**关键词**：自动驾驶数据集, 数据剪枝, 轨迹熵最大化, 信息论, 模仿学习, NuPlan基准

## 3 点简述
- 问题：大规模自动驾驶数据集中存在大量重复低价值样本，增加存储成本且对策略学习贡献有限。
- 方法：基于信息论评估轨迹分布熵，以模型无关方式迭代选择高价值样本，保持原始数据统计特性。
- 效果：在NuPlan基准测试中，数据集可缩减达40%，同时保持闭环性能不变。

## 摘要（原文）

> Collecting large-scale naturalistic driving data is essential for training robust autonomous driving planners. However, real-world datasets often contain a substantial amount of repetitive and low-value samples, which lead to excessive storage costs and bring limited benefits to policy learning. To address this issue, we propose an information-theoretic data pruning method that effectively reduces the training data volume without compromising model performance. Our approach evaluates the trajectory distribution information entropy of driving data and iteratively selects high-value samples that preserve the statistical characteristics of the original dataset in a model-agnostic manner. From a theoretical perspective, we show that maximizing trajectory entropy effectively constrains the Kullback-Leibler divergence between the pruned subset and the original data distribution, thereby maintaining generalization ability. Comprehensive experiments on the NuPlan benchmark with a large-scale imitation learning framework demonstrate that the proposed method can reduce the dataset size by up to 40% while maintaining closed-loop performance. This work provides a lightweight and theoretically grounded approach for scalable data management and efficient policy learning in autonomous driving systems.

