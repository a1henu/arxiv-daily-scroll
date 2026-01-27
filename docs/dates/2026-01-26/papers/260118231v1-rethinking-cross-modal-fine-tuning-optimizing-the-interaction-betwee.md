---
layout: default
title: Rethinking Cross-Modal Fine-Tuning: Optimizing the Interaction between Feature Alignment and Target Fitting
---

# Rethinking Cross-Modal Fine-Tuning: Optimizing the Interaction between Feature Alignment and Target Fitting
**arXiv**：[2601.18231v1](https://arxiv.org/abs/2601.18231) · [PDF](https://arxiv.org/pdf/2601.18231.pdf)  
**作者**：Trong Khiem Tran, Manh Cuong Dao, Phi Le Nguyen, Thao Nguyen Truong, Trong Nghia Hoang  

**一句话要点**：提出理论框架以优化跨模态微调中特征对齐与目标拟合的交互

**关键词**：跨模态微调, 特征对齐, 泛化理论, 特征标签失真, 知识迁移

## 3 点简述
- 核心问题：跨模态微调中特征对齐与目标拟合的交互缺乏理论理解，导致泛化性能下降
- 方法要点：建立可证明的泛化界，通过特征标签失真概念解释交互，指导算法设计
- 实验或效果：在多个基准数据集上显著优于现有方法，验证框架有效性

## 摘要（原文）

> Adapting pre-trained models to unseen feature modalities has become increasingly important due to the growing need for cross-disciplinary knowledge integration.~A key challenge here is how to align the representation of new modalities with the most relevant parts of the pre-trained model's representation space to enable accurate knowledge transfer.~This requires combining feature alignment with target fine-tuning, but uncalibrated combinations can exacerbate misalignment between the source and target feature-label structures and reduce target generalization.~Existing work however lacks a theoretical understanding of this critical interaction between feature alignment and target fitting.~To bridge this gap, we develop a principled framework that establishes a provable generalization bound on the target error, which explains the interaction between feature alignment and target fitting through a novel concept of feature-label distortion.~This bound offers actionable insights into how this interaction should be optimized for practical algorithm design. The resulting approach achieves significantly improved performance over state-of-the-art methods across a wide range of benchmark datasets.

