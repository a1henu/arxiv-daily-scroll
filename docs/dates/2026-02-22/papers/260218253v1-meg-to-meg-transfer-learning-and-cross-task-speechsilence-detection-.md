---
layout: default
title: MEG-to-MEG Transfer Learning and Cross-Task Speech/Silence Detection with Limited Data
---

# MEG-to-MEG Transfer Learning and Cross-Task Speech/Silence Detection with Limited Data
**arXiv**：[2602.18253v1](https://arxiv.org/abs/2602.18253) · [PDF](https://arxiv.org/pdf/2602.18253.pdf)  
**作者**：Xabier de Zuazo, Vincenzo Verbeni, Eva Navas, Ibon Saratxaga, Mathieu Bourguignon, Nicola Molinaro  

**一句话要点**：提出MEG跨任务迁移学习方法，在有限数据下提升语音/静默检测性能

**关键词**：脑机接口, 迁移学习, MEG解码, 语音检测, 跨任务解码, 数据高效学习

## 3 点简述
- 核心问题：脑机接口中数据高效的神经解码是主要挑战，需在有限MEG数据下实现跨任务解码。
- 方法要点：基于Conformer模型，在50小时单被试听音数据上预训练，再在18名被试各5分钟数据上微调，支持感知与产生任务间迁移。
- 实验或效果：迁移学习带来1-6%准确率提升，证实预训练模型能可靠解码跨任务，反映共享神经表征而非任务特异性活动。

## 摘要（原文）

> Data-efficient neural decoding is a central challenge for speech brain-computer interfaces. We present the first demonstration of transfer learning and cross-task decoding for MEG-based speech models spanning perception and production. We pre-train a Conformer-based model on 50 hours of single-subject listening data and fine-tune on just 5 minutes per subject across 18 participants. Transfer learning yields consistent improvements, with in-task accuracy gains of 1-4% and larger cross-task gains of up to 5-6%. Not only does pre-training improve performance within each task, but it also enables reliable cross-task decoding between perception and production. Critically, models trained on speech production decode passive listening above chance, confirming that learned representations reflect shared neural processes rather than task-specific motor activity.

