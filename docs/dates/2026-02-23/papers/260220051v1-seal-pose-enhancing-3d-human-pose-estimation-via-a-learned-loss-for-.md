---
layout: default
title: SEAL-pose: Enhancing 3D Human Pose Estimation via a Learned Loss for Structural Consistency
---

# SEAL-pose: Enhancing 3D Human Pose Estimation via a Learned Loss for Structural Consistency
**arXiv**：[2602.20051v1](https://arxiv.org/abs/2602.20051) · [PDF](https://arxiv.org/pdf/2602.20051.pdf)  
**作者**：Yeonsung Kim, Junggeun Do, Seunguk Do, Sangmin Kim, Jaesik Park, Jay-Yoon Lee  

**一句话要点**：提出SEAL-pose框架，通过可学习损失网络增强3D人体姿态估计的结构一致性。

**关键词**：3D人体姿态估计, 结构一致性, 可学习损失, 关节图, 端到端训练, 数据驱动框架

## 3 点简述
- 核心问题：传统监督损失独立处理关节，难以捕捉复杂局部和全局依赖关系。
- 方法要点：设计基于关节图的可学习损失网络，从数据中学习结构依赖，替代手工先验。
- 实验或效果：在三个基准测试中，SEAL-pose降低关节误差并提升姿态合理性，优于显式约束模型。

## 摘要（原文）

> 3D human pose estimation (HPE) is characterized by intricate local and global dependencies among joints. Conventional supervised losses are limited in capturing these correlations because they treat each joint independently. Previous studies have attempted to promote structural consistency through manually designed priors or rule-based constraints; however, these approaches typically require manual specification and are often non-differentiable, limiting their use as end-to-end training objectives. We propose SEAL-pose, a data-driven framework in which a learnable loss-net trains a pose-net by evaluating structural plausibility. Rather than relying on hand-crafted priors, our joint-graph-based design enables the loss-net to learn complex structural dependencies directly from data. Extensive experiments on three 3D HPE benchmarks with eight backbones show that SEAL-pose reduces per-joint errors and improves pose plausibility compared with the corresponding backbones across all settings. Beyond improving each backbone, SEAL-pose also outperforms models with explicit structural constraints, despite not enforcing any such constraints. Finally, we analyze the relationship between the loss-net and structural consistency, and evaluate SEAL-pose in cross-dataset and in-the-wild settings.

