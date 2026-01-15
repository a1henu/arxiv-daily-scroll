---
layout: default
title: SAM3-DMS: Decoupled Memory Selection for Multi-target Video Segmentation of SAM3
---

# SAM3-DMS: Decoupled Memory Selection for Multi-target Video Segmentation of SAM3
**arXiv**：[2601.09699v1](https://arxiv.org/abs/2601.09699) · [PDF](https://arxiv.org/pdf/2601.09699.pdf)  
**作者**：Ruiqi Shen, Chang Liu, Henghui Ding  

**一句话要点**：提出SAM3-DMS以解决SAM3在多目标视频分割中内存选择同步决策的不足

**关键词**：视频分割, 多目标跟踪, 内存选择, 解耦策略, 训练无关方法

## 3 点简述
- 核心问题：SAM3的集体内存选择在多目标场景下因同步决策而忽略个体可靠性
- 方法要点：采用训练无关的解耦策略，对每个目标进行细粒度内存选择
- 实验或效果：在目标密度增加时优势更明显，提升身份保持和跟踪稳定性

## 摘要（原文）

> Segment Anything 3 (SAM3) has established a powerful foundation that robustly detects, segments, and tracks specified targets in videos. However, in its original implementation, its group-level collective memory selection is suboptimal for complex multi-object scenarios, as it employs a synchronized decision across all concurrent targets conditioned on their average performance, often overlooking individual reliability. To this end, we propose SAM3-DMS, a training-free decoupled strategy that utilizes fine-grained memory selection on individual objects. Experiments demonstrate that our approach achieves robust identity preservation and tracking stability. Notably, our advantage becomes more pronounced with increased target density, establishing a solid foundation for simultaneous multi-target video segmentation in the wild.

