---
layout: default
title: Dual-Axis RCCL: Representation-Complete Convergent Learning for Organic Chemical Space
---

# Dual-Axis RCCL: Representation-Complete Convergent Learning for Organic Chemical Space
**arXiv**：[2512.14418v1](https://arxiv.org/abs/2512.14418) · [PDF](https://arxiv.org/pdf/2512.14418.pdf)  
**作者**：Dejun Hu, Zhiming Li, Jia-Rui Shen, Jia-Ning Tu, Zi-Hao Ye, Junliang Zhang  

**一句话要点**：提出双轴表示完全收敛学习策略，以解决有机化学空间中模型收敛学习问题。

**关键词**：化学空间建模, 表示完全学习, 图神经网络, 分子表示, 收敛学习, 数据集构建

## 3 点简述
- 核心问题：化学空间规模巨大（10^30-10^60），模型能否实现收敛学习是开放科学问题。
- 方法要点：结合图卷积网络编码局部价环境和无桥图编码环/笼拓扑，构建表示完全框架。
- 实验或效果：开发FD25数据集，训练图神经网络实现收敛学习，外部基准预测误差约1.0 kcal/mol MAE。

## 摘要（原文）

> Machine learning is profoundly reshaping molecular and materials modeling; however, given the vast scale of chemical space (10^30-10^60), it remains an open scientific question whether models can achieve convergent learning across this space. We introduce a Dual-Axis Representation-Complete Convergent Learning (RCCL) strategy, enabled by a molecular representation that integrates graph convolutional network (GCN) encoding of local valence environments, grounded in modern valence bond theory, together with no-bridge graph (NBG) encoding of ring/cage topologies, providing a quantitative measure of chemical-space coverage. This framework formalizes representation completeness, establishing a principled basis for constructing datasets that support convergent learning for large models. Guided by this RCCL framework, we develop the FD25 dataset, systematically covering 13,302 local valence units and 165,726 ring/cage topologies, achieving near-complete combinatorial coverage of organic molecules with H/C/N/O/F elements. Graph neural networks trained on FD25 exhibit representation-complete convergent learning and strong out-of-distribution generalization, with an overall prediction error of approximately 1.0 kcal/mol MAE across external benchmarks. Our results establish a quantitative link between molecular representation, structural completeness, and model generalization, providing a foundation for interpretable, transferable, and data-efficient molecular intelligence.

