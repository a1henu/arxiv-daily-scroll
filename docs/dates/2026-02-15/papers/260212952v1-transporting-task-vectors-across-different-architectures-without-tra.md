---
layout: default
title: Transporting Task Vectors across Different Architectures without Training
---

# Transporting Task Vectors across Different Architectures without Training
**arXiv**：[2602.12952v1](https://arxiv.org/abs/2602.12952) · [PDF](https://arxiv.org/pdf/2602.12952.pdf)  
**作者**：Filippo Rinaldi, Aniello Panariello, Giacomo Salici, Angelo Porrello, Simone Calderara  

**一句话要点**：提出Theseus方法，无需训练即可跨异构架构传输任务向量，基于功能匹配而非参数对齐。

**关键词**：任务向量传输, 异构模型适配, 功能匹配, 正交Procrustes分析, 无训练方法, 表示对齐

## 3 点简述
- 核心问题：预训练模型适应下游任务时，任务特定更新难以跨不同宽度模型传输，现有方法主要限于相同架构。
- 方法要点：通过正交Procrustes分析对齐表示空间，将任务向量传输形式化为功能匹配问题，获得闭式解以保持更新几何结构。
- 实验或效果：在视觉和语言模型上评估，跨宽度传输任务更新时，相比基线有稳定提升，无需额外训练或反向传播。

## 摘要（原文）

> Adapting large pre-trained models to downstream tasks often produces task-specific parameter updates that are expensive to relearn for every model variant. While recent work has shown that such updates can be transferred between models with identical architectures, transferring them across models of different widths remains largely unexplored. In this work, we introduce Theseus, a training-free method for transporting task-specific updates across heterogeneous models. Rather than matching parameters directly, we characterize a task update by the functional effect it induces on intermediate representations. We formalize task-vector transport as a functional matching problem on observed activations and show that, after aligning representation spaces via orthogonal Procrustes analysis, it admits a stable closed-form solution that preserves the geometry of the update. We evaluate Theseus on vision and language models across different widths, showing consistent improvements over strong baselines without additional training or backpropagation. Our results show that task updates can be meaningfully transferred across architectures when task identity is defined functionally rather than parametrically.

