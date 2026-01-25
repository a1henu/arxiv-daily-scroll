---
layout: default
title: Understanding the Transfer Limits of Vision Foundation Models
---

# Understanding the Transfer Limits of Vision Foundation Models
**arXiv**：[2601.15888v1](https://arxiv.org/abs/2601.15888) · [PDF](https://arxiv.org/pdf/2601.15888.pdf)  
**作者**：Shiqi Huang, Yipei Wang, Natasha Thorley, Alexander Ng, Shaheer Saeed, Mark Emberton, Shonit Punwani, Veeru Kasivisvanathan, Dean Barratt, Daniel Alexander, Yipeng Hu  

**一句话要点**：评估视觉基础模型在临床影像任务中的迁移限制，强调预训练与下游任务对齐的重要性

**关键词**：视觉基础模型, 迁移学习, 预训练对齐, 临床影像分析, 最大均值差异, 下游任务性能

## 3 点简述
- 核心问题：视觉基础模型在下游任务中表现不均，源于预训练目标与任务需求不匹配
- 方法要点：通过最大均值差异等指标量化预训练与下游任务对齐度，分析其对迁移性能的影响
- 实验或效果：在五个前列腺多参数MR成像任务中，对齐度更高的模型表现更优且收敛更快

## 摘要（原文）

> Foundation models leverage large-scale pretraining to capture extensive knowledge, demonstrating generalization in a wide range of language tasks. By comparison, vision foundation models (VFMs) often exhibit uneven improvements across downstream tasks, despite substantial computational investment. We postulate that this limitation arises from a mismatch between pretraining objectives and the demands of downstream vision-and-imaging tasks. Pretraining strategies like masked image reconstruction or contrastive learning shape representations for tasks such as recovery of generic visual patterns or global semantic structures, which may not align with the task-specific requirements of downstream applications including segmentation, classification, or image synthesis. To investigate this in a concrete real-world clinical area, we assess two VFMs, a reconstruction-focused MAE-based model (ProFound) and a contrastive-learning-based model (ProViCNet), on five prostate multiparametric MR imaging tasks, examining how such task alignment influences transfer performance, i.e., from pretraining to fine-tuning. Our findings indicate that better alignment between pretraining and downstream tasks, measured by simple divergence metrics such as maximum-mean-discrepancy (MMD) between the same features before and after fine-tuning, correlates with greater performance improvements and faster convergence, emphasizing the importance of designing and analyzing pretraining objectives with downstream applicability in mind.

