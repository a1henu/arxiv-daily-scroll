---
layout: default
title: MOSIV: Multi-Object System Identification from Videos
---

# MOSIV: Multi-Object System Identification from Videos
**arXiv**：[2603.06022v1](https://arxiv.org/abs/2603.06022) · [PDF](https://arxiv.org/pdf/2603.06022.pdf)  
**作者**：Chunjiang Liu, Xiaoyuan Wang, Qingran Lin, Albert Xiao, Haoyu Chen, Shizheng Wen, Hao Zhang, Lu Qi, Ming-Hsuan Yang, Laszlo A. Jeni, Min Xu, Yizhou Zhao  

**一句话要点**：提出MOSIV框架，通过可微分模拟器优化连续物体材料参数，解决视频中多物体系统识别问题。

**关键词**：多物体系统识别, 可微分模拟器, 连续材料参数, 视频几何目标, 合成基准

## 3 点简述
- 核心问题：现有方法不适用于视频中多物体系统识别，因其专注于单物体场景或离散材料分类。
- 方法要点：使用基于视频几何目标的可微分模拟器，直接优化每个物体的连续材料参数。
- 实验或效果：在新合成基准上，MOSIV显著提升接地精度和长时程模拟保真度，优于基线方法。

## 摘要（原文）

> We introduce the challenging problem of multi-object system identification from videos, for which prior methods are ill-suited due to their focus on single-object scenes or discrete material classification with a fixed set of material prototypes. To address this, we propose MOSIV, a new framework that directly optimizes for continuous, per-object material parameters using a differentiable simulator guided by geometric objectives derived from video. We also present a new synthetic benchmark with contact-rich, multi-object interactions to facilitate evaluation. On this benchmark, MOSIV substantially improves grounding accuracy and long-horizon simulation fidelity over adapted baselines, establishing it as a strong baseline for this new task. Our analysis shows that object-level fine-grained supervision and geometry-aligned objectives are critical for stable optimization in these complex, multi-object settings. The source code and dataset will be released.

