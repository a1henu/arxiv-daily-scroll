---
layout: default
title: Multi-Level Feature Fusion for Continual Learning in Visual Quality Inspection
---

# Multi-Level Feature Fusion for Continual Learning in Visual Quality Inspection
**arXiv**：[2601.00725v1](https://arxiv.org/abs/2601.00725) · [PDF](https://arxiv.org/pdf/2601.00725.pdf)  
**作者**：Johannes C. Bauer, Paul Geng, Stephan Trattnig, Petr Dokládal, Rüdiger Daub  

**一句话要点**：提出多级特征融合方法以解决制造业视觉质量检测中的持续学习问题

**关键词**：持续学习, 特征融合, 视觉质量检测, 灾难性遗忘, 制造业自动化

## 3 点简述
- 核心问题：制造业中产品与缺陷模式频繁变化，导致深度学习模型需持续适应，面临灾难性遗忘与计算效率挑战。
- 方法要点：利用预训练网络不同深度的特征表示进行融合，减少可训练参数，提升模型适应性与泛化能力。
- 实验或效果：在多种质量检测任务中匹配端到端训练性能，显著降低遗忘，增强对新产品类型或缺陷的鲁棒性。

## 摘要（原文）

> Deep neural networks show great potential for automating various visual quality inspection tasks in manufacturing. However, their applicability is limited in more volatile scenarios, such as remanufacturing, where the inspected products and defect patterns often change. In such settings, deployed models require frequent adaptation to novel conditions, effectively posing a continual learning problem. To enable quick adaptation, the necessary training processes must be computationally efficient while still avoiding effects like catastrophic forgetting. This work presents a multi-level feature fusion (MLFF) approach that aims to improve both aspects simultaneously by utilizing representations from different depths of a pretrained network. We show that our approach is able to match the performance of end-to-end training for different quality inspection problems while using significantly less trainable parameters. Furthermore, it reduces catastrophic forgetting and improves generalization robustness to new product types or defects.

