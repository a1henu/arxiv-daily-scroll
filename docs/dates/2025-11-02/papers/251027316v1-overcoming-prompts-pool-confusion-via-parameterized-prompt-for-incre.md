---
layout: default
title: Overcoming Prompts Pool Confusion via Parameterized Prompt for Incremental Object Detection
---

# Overcoming Prompts Pool Confusion via Parameterized Prompt for Incremental Object Detection
**arXiv**：[2510.27316v1](https://arxiv.org/abs/2510.27316) · [PDF](https://arxiv.org/pdf/2510.27316.pdf)  
**作者**：Zijia An, Boyu Diao, Ruiqi Liu, Libo Huang, Chuanguang Yang, Fei Wang, Zhulin An, Yongjun Xu  

**一句话要点**：提出参数化提示方法P²IOD以解决增量目标检测中的提示池混淆问题

**关键词**：增量目标检测, 参数化提示, 提示池混淆, 知识整合, 神经网络提示

## 3 点简述
- 核心问题：增量目标检测中，现有提示池方法忽略类共现，导致未标记对象引发提示池混淆。
- 方法要点：使用神经网络作为参数化提示，自适应整合任务知识，并通过融合策略约束更新。
- 实验或效果：在PASCAL VOC2007和MS COCO数据集上验证有效性，达到当前最优性能。

## 摘要（原文）

> Recent studies have demonstrated that incorporating trainable prompts into
> pretrained models enables effective incremental learning. However, the
> application of prompts in incremental object detection (IOD) remains
> underexplored. Existing prompts pool based approaches assume disjoint class
> sets across incremental tasks, which are unsuitable for IOD as they overlook
> the inherent co-occurrence phenomenon in detection images. In co-occurring
> scenarios, unlabeled objects from previous tasks may appear in current task
> images, leading to confusion in prompts pool. In this paper, we hold that
> prompt structures should exhibit adaptive consolidation properties across
> tasks, with constrained updates to prevent catastrophic forgetting. Motivated
> by this, we introduce Parameterized Prompts for Incremental Object Detection
> (P$^2$IOD). Leveraging neural networks global evolution properties, P$^2$IOD
> employs networks as the parameterized prompts to adaptively consolidate
> knowledge across tasks. To constrain prompts structure updates, P$^2$IOD
> further engages a parameterized prompts fusion strategy. Extensive experiments
> on PASCAL VOC2007 and MS COCO datasets demonstrate that P$^2$IOD's
> effectiveness in IOD and achieves the state-of-the-art performance among
> existing baselines.

