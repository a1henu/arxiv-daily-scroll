---
layout: default
title: Occlusion-Aware SORT: Observing Occlusion for Robust Multi-Object Tracking
---

# Occlusion-Aware SORT: Observing Occlusion for Robust Multi-Object Tracking
**arXiv**：[2603.06034v1](https://arxiv.org/abs/2603.06034) · [PDF](https://arxiv.org/pdf/2603.06034.pdf)  
**作者**：Chunjiang Li, Jianbo Ma, Li Shen, Yanru Chen, Liangyin Chen  

**一句话要点**：提出Occlusion-Aware SORT框架以解决多目标跟踪中部分遮挡导致的成本混淆问题

**关键词**：多目标跟踪, 遮挡处理, 成本混淆, 高斯图, 无训练框架, 轨迹分析

## 3 点简述
- 核心问题：2D多目标跟踪中部分遮挡引起位置成本混淆，影响轨迹分析和对象计数
- 方法要点：引入Occlusion-Aware Module、Occlusion-Aware Offset和Bias-Aware Momentum，无需训练即可分析遮挡状态并减少背景影响
- 实验或效果：在DanceTrack等数据集上验证，OA-SORT提升HOTA和IDF1指标，集成到其他跟踪器平均提高性能

## 摘要（原文）

> Multi-object tracking (MOT) involves analyzing object trajectories and counting the number of objects in video sequences. However, 2D MOT faces challenges due to positional cost confusion arising from partial occlusion. To address this issue, we present the novel Occlusion-Aware SORT (OA-SORT) framework, a plug-and-play and training-free framework that includes the Occlusion-Aware Module (OAM), the Occlusion-Aware Offset (OAO), and the Bias-Aware Momentum (BAM). Specifically, OAM analyzes the occlusion status of objects, where a Gaussian Map (GM) is introduced to reduce background influence. In contrast, OAO and BAM leverage the OAM-described occlusion status to mitigate cost confusion and suppress estimation instability. Comprehensive evaluations on the DanceTrack, SportsMOT, and MOT17 datasets demonstrate the importance of occlusion handling in MOT. On the DanceTrack test set, OA-SORT achieves 63.1% and 64.2% in HOTA and IDF1, respectively. Furthermore, integrating the Occlusion-Aware framework into the four additional trackers improves HOTA and IDF1 by an average of 2.08% and 3.05%, demonstrating the reusability of the occlusion awareness.

