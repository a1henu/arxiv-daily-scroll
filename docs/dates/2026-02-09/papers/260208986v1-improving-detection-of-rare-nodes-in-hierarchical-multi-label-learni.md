---
layout: default
title: Improving Detection of Rare Nodes in Hierarchical Multi-Label Learning
---

# Improving Detection of Rare Nodes in Hierarchical Multi-Label Learning
**arXiv**：[2602.08986v1](https://arxiv.org/abs/2602.08986) · [PDF](https://arxiv.org/pdf/2602.08986.pdf)  
**作者**：Isaac Xu, Martin Gillis, Ayushi Sharma, Benjamin Misiuk, Craig J. Brown, Thomas Trappenberg  

**一句话要点**：提出加权损失目标以解决层次多标签学习中罕见节点检测难题

**关键词**：层次多标签学习, 罕见节点检测, 加权损失函数, 集成不确定性, 卷积神经网络, 不平衡分类

## 3 点简述
- 核心问题：层次多标签分类中，罕见节点因频率低和层次约束导致模型难以深入预测。
- 方法要点：结合节点不平衡加权和焦点加权，利用集成不确定性强调罕见节点和不确定节点。
- 实验或效果：在基准数据集上召回率提升高达五倍，F1分数显著提高，并增强卷积网络性能。

## 摘要（原文）

> In hierarchical multi-label classification, a persistent challenge is enabling model predictions to reach deeper levels of the hierarchy for more detailed or fine-grained classifications. This difficulty partly arises from the natural rarity of certain classes (or hierarchical nodes) and the hierarchical constraint that ensures child nodes are almost always less frequent than their parents. To address this, we propose a weighted loss objective for neural networks that combines node-wise imbalance weighting with focal weighting components, the latter leveraging modern quantification of ensemble uncertainties. By emphasizing rare nodes rather than rare observations (data points), and focusing on uncertain nodes for each model output distribution during training, we observe improvements in recall by up to a factor of five on benchmark datasets, along with statistically significant gains in $F_{1}$ score. We also show our approach aids convolutional networks on challenging tasks, as in situations with suboptimal encoders or limited data.

