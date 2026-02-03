---
layout: default
title: Grappa: Gradient-Only Communication for Scalable Graph Neural Network Training
---

# Grappa: Gradient-Only Communication for Scalable Graph Neural Network Training
**arXiv**：[2602.01872v1](https://arxiv.org/abs/2602.01872) · [PDF](https://arxiv.org/pdf/2602.01872.pdf)  
**作者**：Chongyang Xu, Christoph Siebenbrunner, Laurent Bindschaedler  

**一句话要点**：提出Grappa框架，通过仅梯度通信解决分布式图神经网络训练中的跨分区边成本问题。

**关键词**：分布式图神经网络训练, 梯度通信优化, 图分区, 梯度聚合校正, 大规模图处理

## 3 点简述
- 核心问题：分布式GNN训练中，跨分区边导致的远程特征和激活获取成本随图深度和分区数增加而激增。
- 方法要点：采用梯度唯一通信，分区独立训练，结合周期性重分区和覆盖校正梯度聚合以恢复精度。
- 实验或效果：在真实和合成图上，Grappa平均训练速度提升4倍，支持万亿边规模，且模型无关。

## 摘要（原文）

> Cross-partition edges dominate the cost of distributed GNN training: fetching remote features and activations per iteration overwhelms the network as graphs deepen and partition counts grow. Grappa is a distributed GNN training framework that enforces gradient-only communication: during each iteration, partitions train in isolation and exchange only gradients for the global update. To recover accuracy lost to isolation, Grappa (i) periodically repartitions to expose new neighborhoods and (ii) applies a lightweight coverage-corrected gradient aggregation inspired by importance sampling. We prove the corrected estimator is asymptotically unbiased under standard support and boundedness assumptions, and we derive a batch-level variant for compatibility with common deep-learning packages that minimizes mean-squared deviation from the ideal node-level correction. We also introduce a shrinkage version that improves stability in practice. Empirical results on real and synthetic graphs show that Grappa trains GNNs 4 times faster on average (up to 13 times) than state-of-the-art systems, achieves better accuracy especially for deeper models, and sustains training at the trillion-edge scale on commodity hardware. Grappa is model-agnostic, supports full-graph and mini-batch training, and does not rely on high-bandwidth interconnects or caching.

