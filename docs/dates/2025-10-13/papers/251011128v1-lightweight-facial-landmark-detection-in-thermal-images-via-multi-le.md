---
layout: default
title: Lightweight Facial Landmark Detection in Thermal Images via Multi-Level Cross-Modal Knowledge Transfer
---

# Lightweight Facial Landmark Detection in Thermal Images via Multi-Level Cross-Modal Knowledge Transfer
**arXiv**：[2510.11128v1](https://arxiv.org/abs/2510.11128) · [PDF](https://arxiv.org/pdf/2510.11128.pdf)  
**作者**：Qiyi Tong, Olivia Nocentini, Marta Lagomarsino, Kuanqi Cai, Marta Lorenzini, Arash Ajoudani  

**一句话要点**：提出多级跨模态知识蒸馏以解决热图像中轻量级面部关键点检测问题

**关键词**：面部关键点检测, 热图像分析, 跨模态知识蒸馏, 轻量级模型, 模态不变特征

## 3 点简述
- 核心问题：热图像面部关键点检测缺乏丰富视觉线索，传统跨模态方法计算昂贵或引入结构伪影
- 方法要点：引入双向双注入知识蒸馏，通过闭环监督学习模态不变特征，确保语义对齐
- 实验或效果：在公开基准上实现新SOTA，显著降低计算开销并超越先前方法

## 摘要（原文）

> Facial Landmark Detection (FLD) in thermal imagery is critical for
> applications in challenging lighting conditions, but it is hampered by the lack
> of rich visual cues. Conventional cross-modal solutions, like feature fusion or
> image translation from RGB data, are often computationally expensive or
> introduce structural artifacts, limiting their practical deployment. To address
> this, we propose Multi-Level Cross-Modal Knowledge Distillation (MLCM-KD), a
> novel framework that decouples high-fidelity RGB-to-thermal knowledge transfer
> from model compression to create both accurate and efficient thermal FLD
> models. A central challenge during knowledge transfer is the profound modality
> gap between RGB and thermal data, where traditional unidirectional distillation
> fails to enforce semantic consistency across disparate feature spaces. To
> overcome this, we introduce Dual-Injected Knowledge Distillation (DIKD), a
> bidirectional mechanism designed specifically for this task. DIKD establishes a
> connection between modalities: it not only guides the thermal student with rich
> RGB features but also validates the student's learned representations by
> feeding them back into the frozen teacher's prediction head. This closed-loop
> supervision forces the student to learn modality-invariant features that are
> semantically aligned with the teacher, ensuring a robust and profound knowledge
> transfer. Experiments show that our approach sets a new state-of-the-art on
> public thermal FLD benchmarks, notably outperforming previous methods while
> drastically reducing computational overhead.

