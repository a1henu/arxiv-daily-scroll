---
layout: default
title: Better Matching, Less Forgetting: A Quality-Guided Matcher for Transformer-based Incremental Object Detection
---

# Better Matching, Less Forgetting: A Quality-Guided Matcher for Transformer-based Incremental Object Detection
**arXiv**：[2603.01524v1](https://arxiv.org/abs/2603.01524) · [PDF](https://arxiv.org/pdf/2603.01524.pdf)  
**作者**：Qirui Wu, Shizhou Zhang, De Cheng, Yinghui Xing, Lingyan Ran, Dahu Shi, Peng Wang  

**一句话要点**：提出质量引导最小成本最大流匹配器以解决基于Transformer的增量目标检测中的背景前景化问题

**关键词**：增量目标检测, Transformer架构, 背景前景化, 匹配器优化, 灾难性遗忘, COCO数据集

## 3 点简述
- 核心问题：DETR类架构在增量目标检测中因匈牙利匹配器强制分配导致背景前景化，加速灾难性遗忘
- 方法要点：设计Q-MCMF匹配器，基于几何质量剪枝不可信匹配，优化最小成本和最大有效分配
- 实验或效果：在COCO数据集多种增量设置下，方法持续超越现有先进方法

## 摘要（原文）

> Incremental Object Detection (IOD) aims to continuously learn new object classes without forgetting previously learned ones. A persistent challenge is catastrophic forgetting, primarily attributed to background shift in conventional detectors. While pseudo-labeling mitigates this in dense detectors, we identify a novel, distinct source of forgetting specific to DETR-like architectures: background foregrounding. This arises from the exhaustiveness constraint of the Hungarian matcher, which forcibly assigns every ground truth target to one prediction, even when predictions primarily cover background regions (i.e., low IoU). This erroneous supervision compels the model to misclassify background features as specific foreground classes, disrupting learned representations and accelerating forgetting. To address this, we propose a Quality-guided Min-Cost Max-Flow (Q-MCMF) matcher. To avoid forced assignments, Q-MCMF builds a flow graph and prunes implausible matches based on geometric quality. It then optimizes for the final matching that minimizes cost and maximizes valid assignments. This strategy eliminates harmful supervision from background foregrounding while maximizing foreground learning signals. Extensive experiments on the COCO dataset under various incremental settings demonstrate that our method consistently outperforms existing state-of-the-art approaches.

