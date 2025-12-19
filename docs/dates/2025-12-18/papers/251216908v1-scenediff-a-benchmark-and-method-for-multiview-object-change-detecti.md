---
layout: default
title: SceneDiff: A Benchmark and Method for Multiview Object Change Detection
---

# SceneDiff: A Benchmark and Method for Multiview Object Change Detection
**arXiv**：[2512.16908v1](https://arxiv.org/abs/2512.16908) · [PDF](https://arxiv.org/pdf/2512.16908.pdf)  
**作者**：Yuqun Wu, Chih-hao Lin, Henry Che, Aditi Tiwari, Chuhang Zou, Shenlong Wang, Derek Hoiem  

**一句话要点**：提出SceneDiff基准和方法，以解决多视角场景中物体变化检测的挑战。

**关键词**：多视角变化检测, 物体实例标注, 免训练方法, 3D对齐, 语义特征比较, 基准数据集

## 3 点简述
- 核心问题：识别不同时间捕获的同一场景中物体的添加、移除或移动，需克服视角变化导致的误检。
- 方法要点：利用预训练3D、分割和图像编码模型，通过3D对齐、物体区域提取和特征比较实现免训练变化检测。
- 实验或效果：在多个基准测试中大幅超越现有方法，相对AP提升94%和37.4%。

## 摘要（原文）

> We investigate the problem of identifying objects that have been added, removed, or moved between a pair of captures (images or videos) of the same scene at different times. Detecting such changes is important for many applications, such as robotic tidying or construction progress and safety monitoring. A major challenge is that varying viewpoints can cause objects to falsely appear changed. We introduce SceneDiff Benchmark, the first multiview change detection benchmark with object instance annotations, comprising 350 diverse video pairs with thousands of changed objects. We also introduce the SceneDiff method, a new training-free approach for multiview object change detection that leverages pretrained 3D, segmentation, and image encoding models to robustly predict across multiple benchmarks. Our method aligns the captures in 3D, extracts object regions, and compares spatial and semantic region features to detect changes. Experiments on multi-view and two-view benchmarks demonstrate that our method outperforms existing approaches by large margins (94% and 37.4% relative AP improvements). The benchmark and code will be publicly released.

