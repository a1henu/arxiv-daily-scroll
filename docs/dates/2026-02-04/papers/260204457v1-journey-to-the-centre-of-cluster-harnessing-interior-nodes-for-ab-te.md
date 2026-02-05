---
layout: default
title: Journey to the Centre of Cluster: Harnessing Interior Nodes for A/B Testing under Network Interference
---

# Journey to the Centre of Cluster: Harnessing Interior Nodes for A/B Testing under Network Interference
**arXiv**：[2602.04457v1](https://arxiv.org/abs/2602.04457) · [PDF](https://arxiv.org/pdf/2602.04457.pdf)  
**作者**：Qianyi Chen, Anpeng Wu, Bo Li, Lu Deng, Yong Wang  

**一句话要点**：提出基于内部节点的增强MII估计器，以降低网络干扰下A/B测试的方差与偏差。

**关键词**：A/B测试, 网络干扰, 聚类随机化, 内部节点, 反事实预测, 半监督学习

## 3 点简述
- 核心问题：网络干扰导致A/B测试中单元结果受邻居处理影响，传统聚类随机化方法方差高。
- 方法要点：直接平均内部节点构建MII估计器，并用全网络训练的反事实预测器调整协变量分布偏移。
- 实验或效果：模拟研究显示增强MII估计器在多种设置下性能优异，显著降低方差与偏差。

## 摘要（原文）

> A/B testing on platforms often faces challenges from network interference, where a unit's outcome depends not only on its own treatment but also on the treatments of its network neighbors. To address this, cluster-level randomization has become standard, enabling the use of network-aware estimators. These estimators typically trim the data to retain only a subset of informative units, achieving low bias under suitable conditions but often suffering from high variance. In this paper, we first demonstrate that the interior nodes - units whose neighbors all lie within the same cluster - constitute the vast majority of the post-trimming subpopulation. In light of this, we propose directly averaging over the interior nodes to construct the mean-in-interior (MII) estimator, which circumvents the delicate reweighting required by existing network-aware estimators and substantially reduces variance in classical settings. However, we show that interior nodes are often not representative of the full population, particularly in terms of network-dependent covariates, leading to notable bias. We then augment the MII estimator with a counterfactual predictor trained on the entire network, allowing us to adjust for covariate distribution shifts between the interior nodes and full population. By rearranging the expression, we reveal that our augmented MII estimator embodies an analytical form of the point estimator within prediction-powered inference framework. This insight motivates a semi-supervised lens, wherein interior nodes are treated as labeled data subject to selection bias. Extensive and challenging simulation studies demonstrate the outstanding performance of our augmented MII estimator across various settings.

