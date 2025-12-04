---
layout: default
title: PULSE: A Unified Multi-Task Architecture for Cardiac Segmentation, Diagnosis, and Few-Shot Cross-Modality Clinical Adaptation
---

# PULSE: A Unified Multi-Task Architecture for Cardiac Segmentation, Diagnosis, and Few-Shot Cross-Modality Clinical Adaptation
**arXiv**：[2512.03848v1](https://arxiv.org/abs/2512.03848) · [PDF](https://arxiv.org/pdf/2512.03848.pdf)  
**作者**：Hania Ghouse, Maryam Alsharqi, Farhad R. Nezami, Muzammil Behzad  

**一句话要点**：提出PULSE统一多任务架构，以解决心脏图像分析中分割、诊断和跨模态适应任务碎片化问题。

**关键词**：心脏图像分析, 多任务学习, 自监督表示, 跨模态适应, 临床报告生成, 统一架构

## 3 点简述
- 核心问题：心脏图像分析任务（如分割、分类、报告生成）通常由独立网络处理，缺乏统一框架。
- 方法要点：基于自监督表示，通过复合监督策略平衡区域重叠、像素分类和边界IoU优化，实现多任务统一。
- 实验或效果：模型学习任务不变先验，在数据集间泛化强，可适应新成像模态，支持从像素到临床推理的过渡。

## 摘要（原文）

> Cardiac image analysis remains fragmented across tasks: anatomical segmentation, disease classification, and grounded clinical report generation are typically handled by separate networks trained under different data regimes. No existing framework unifies these objectives within a single architecture while retaining generalization across imaging modalities and datasets. We introduce PULSE, a multi-task vision-language framework built on self-supervised representations and optimized through a composite supervision strategy that balances region overlap learning, pixel wise classification fidelity, and boundary aware IoU refinement. A multi-scale token reconstruction decoder enables anatomical segmentation, while shared global representations support disease classification and clinically grounded text output allowing the model to transition from pixels to structures and finally clinical reasoning within one architecture. Unlike prior task-specific pipelines, PULSE learns task-invariant cardiac priors, generalizes robustly across datasets, and can be adapted to new imaging modalities with minimal supervision. This moves the field closer to a scalable, foundation style cardiac analysis framework.

