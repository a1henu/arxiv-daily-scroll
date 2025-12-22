---
layout: default
title: SHARP-QoS: Sparsely-gated Hierarchical Adaptive Routing for joint Prediction of QoS
---

# SHARP-QoS: Sparsely-gated Hierarchical Adaptive Routing for joint Prediction of QoS
**arXiv**：[2512.17262v1](https://arxiv.org/abs/2512.17262) · [PDF](https://arxiv.org/pdf/2512.17262.pdf)  
**作者**：Suraj Kumar, Arvind Kumar, Soumi Chattopadhyay  

**一句话要点**：提出SHARP-QoS联合预测QoS，解决稀疏性、负迁移和表示学习不足问题。

**关键词**：QoS预测, 联合学习, 双曲卷积, 自适应特征共享, 损失平衡, 服务计算

## 3 点简述
- 核心问题：QoS数据稀疏、噪声大，现有方法预测单参数导致计算成本高、泛化差，联合预测易受负迁移影响。
- 方法要点：使用双曲卷积提取层次特征，自适应特征共享与门控融合，EMA损失平衡策略稳定优化。
- 实验或效果：在三个数据集上优于单任务和多任务基线，有效处理稀疏性、异常值和冷启动，计算开销适中。

## 摘要（原文）

> Dependable service-oriented computing relies on multiple Quality of Service (QoS) parameters that are essential to assess service optimality. However, real-world QoS data are extremely sparse, noisy, and shaped by hierarchical dependencies arising from QoS interactions, and geographical and network-level factors, making accurate QoS prediction challenging. Existing methods often predict each QoS parameter separately, requiring multiple similar models, which increases computational cost and leads to poor generalization. Although recent joint QoS prediction studies have explored shared architectures, they suffer from negative transfer due to loss-scaling caused by inconsistent numerical ranges across QoS parameters and further struggle with inadequate representation learning, resulting in degraded accuracy. This paper presents an unified strategy for joint QoS prediction, called SHARP-QoS, that addresses these issues using three components. First, we introduce a dual mechanism to extract the hierarchical features from both QoS and contextual structures via hyperbolic convolution formulated in the Poincaré ball. Second, we propose an adaptive feature-sharing mechanism that allows feature exchange across informative QoS and contextual signals. A gated feature fusion module is employed to support dynamic feature selection among structural and shared representations. Third, we design an EMA-based loss balancing strategy that allows stable joint optimization, thereby mitigating the negative transfer. Evaluations on three datasets with two, three, and four QoS parameters demonstrate that SHARP-QoS outperforms both single- and multi-task baselines. Extensive study shows that our model effectively addresses major challenges, including sparsity, robustness to outliers, and cold-start, while maintaining moderate computational overhead, underscoring its capability for reliable joint QoS prediction.

