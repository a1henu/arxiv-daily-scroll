---
layout: default
title: Sticky-Glance: Robust Intent Recognition for Human Robot Collaboration via Single-Glance
---

# Sticky-Glance: Robust Intent Recognition for Human Robot Collaboration via Single-Glance
**arXiv**：[2603.06121v1](https://arxiv.org/abs/2603.06121) · [PDF](https://arxiv.org/pdf/2603.06121.pdf)  
**作者**：Yuzhi Lai, Shenghai Yuan, Peizheng Li, Andreas Zell  

**一句话要点**：提出基于对象中心凝视锚定的粘性凝视算法，以增强多对象环境中人机协作的意图识别鲁棒性。

**关键词**：凝视意图识别, 人机协作, 对象中心凝视锚定, 粘性凝视算法, 多模态交互, 鲁棒性增强

## 3 点简述
- 核心问题：多对象环境中基于凝视的意图识别受噪声、微眼动和动态对象干扰，鲁棒性不足。
- 方法要点：通过粘性凝视算法联合建模几何距离和方向趋势，稳定意图锚定，仅需最少3个凝视样本。
- 实验或效果：在动态目标跟踪率0.94、静态目标选择准确率0.98，任务时长减少近10%，优于基线。

## 摘要（原文）

> Gaze is a valuable means of communication for impaired people with extremely limited motor capabilities. However, robust gaze-based intent recognition in multi-object environments is challenging due to gaze noise, micro-saccades, viewpoint changes, and dynamic objects. To address this, we propose an object-centric gaze grounding framework that stabilizes intent through a sticky-glance algorithm, jointly modeling geometric distance and direction trends. The inferred intent remains anchored to the object even under short glances with minimal 3 gaze samples, achieving a tracking rate of 0.94 for dynamic targets and selection accuracy of 0.98 for static targets. We further introduce a continuous shared control and multi-modal interaction paradigm, enabling high-readiness control and human-in-loop feedback, thereby reducing task duration for nearly 10 \%. Experiments across dynamic tracking, multi-perspective alignment, a baseline comparison, user studies, and ablation studies demonstrate improved robustness, efficiency, and reduced workload compared to representative baselines.

