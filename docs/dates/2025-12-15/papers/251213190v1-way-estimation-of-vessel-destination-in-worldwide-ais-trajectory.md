---
layout: default
title: WAY: Estimation of Vessel Destination in Worldwide AIS Trajectory
---

# WAY: Estimation of Vessel Destination in Worldwide AIS Trajectory
**arXiv**：[2512.13190v1](https://arxiv.org/abs/2512.13190) · [PDF](https://arxiv.org/pdf/2512.13190.pdf)  
**作者**：Jin Sob Kim, Hyun Joon Park, Wooseok Shin, Dongil Park, Sung Won Han  

**一句话要点**：提出WAY方法，基于全球AIS数据通过嵌套序列结构和深度学习估计船舶目的地

**关键词**：船舶目的地估计, AIS轨迹分析, 深度学习架构, 梯度丢弃, 多任务学习, 时空数据处理

## 3 点简述
- 核心问题：AIS数据存在可靠性问题和时间间隔不规则，影响船舶目的地估计的准确性。
- 方法要点：将长轨迹重构为嵌套序列，使用多通道表示和CASP块进行深度学习，并引入梯度丢弃技术优化训练。
- 实验或效果：在5年AIS数据上验证，WAY优于传统方法，梯度丢弃提升性能，并探索多任务学习应用。

## 摘要（原文）

> The Automatic Identification System (AIS) enables data-driven maritime surveillance but suffers from reliability issues and irregular intervals. We address vessel destination estimation using global-scope AIS data by proposing a differentiated approach that recasts long port-to-port trajectories as a nested sequence structure. Using spatial grids, this method mitigates spatio-temporal bias while preserving detailed resolution. We introduce a novel deep learning architecture, WAY, designed to process these reformulated trajectories for long-term destination estimation days to weeks in advance. WAY comprises a trajectory representation layer and Channel-Aggregative Sequential Processing (CASP) blocks. The representation layer generates multi-channel vector sequences from kinematic and non-kinematic features. CASP blocks utilize multi-headed channel- and self-attention for aggregation and sequential information delivery. Additionally, we propose a task-specialized Gradient Dropout (GD) technique to enable many-to-many training on single labels, preventing biased feedback surges by stochastically blocking gradient flow based on sample length. Experiments on 5-year AIS data demonstrate WAY's superiority over conventional spatial grid-based approaches regardless of trajectory progression. Results further confirm that adopting GD leads to performance gains. Finally, we explore WAY's potential for real-world application through multitask learning for ETA estimation.

