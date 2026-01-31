---
layout: default
title: Few-Shot Domain Adaptation with Temporal References and Static Priors for Glacier Calving Front Delineation
---

# Few-Shot Domain Adaptation with Temporal References and Static Priors for Glacier Calving Front Delineation
**arXiv**：[2601.21663v1](https://arxiv.org/abs/2601.21663) · [PDF](https://arxiv.org/pdf/2601.21663.pdf)  
**作者**：Marcel Dreier, Nora Gourmelon, Dakota Pyles, Thorsten Seehaus, Matthias H. Braun, Andreas Maier, Vincent Christlein  

**一句话要点**：提出结合时空参考与静态先验的少样本域适应方法，以提升冰川崩解前沿分割在新研究点的准确性。

**关键词**：冰川崩解前沿分割, 少样本域适应, 时空参考, 静态先验, 深度学习分割

## 3 点简述
- 核心问题：基准模型在新研究点因域偏移导致分割精度不足，影响科学分析。
- 方法要点：采用少样本域适应策略，整合空间静态先验知识和时间序列中的夏季参考图像。
- 实验或效果：无需架构修改，分割误差从1131.6米降至68.7米，建立全球监测框架。

## 摘要（原文）

> During benchmarking, the state-of-the-art model for glacier calving front delineation achieves near-human performance. However, when applied in a real-world setting at a novel study site, its delineation accuracy is insufficient for calving front products intended for further scientific analyses. This site represents an out-of-distribution domain for a model trained solely on the benchmark dataset. By employing a few-shot domain adaptation strategy, incorporating spatial static prior knowledge, and including summer reference images in the input time series, the delineation error is reduced from 1131.6 m to 68.7 m without any architectural modifications. These methodological advancements establish a framework for applying deep learning-based calving front segmentation to novel study sites, enabling calving front monitoring on a global scale.

