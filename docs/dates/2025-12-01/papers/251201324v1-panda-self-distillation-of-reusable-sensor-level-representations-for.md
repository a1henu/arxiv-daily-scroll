---
layout: default
title: Panda: Self-distillation of Reusable Sensor-level Representations for High Energy Physics
---

# Panda: Self-distillation of Reusable Sensor-level Representations for High Energy Physics
**arXiv**：[2512.01324v1](https://arxiv.org/abs/2512.01324) · [PDF](https://arxiv.org/pdf/2512.01324.pdf)  
**作者**：Samuel Young, Kazuhiro Terao  

**一句话要点**：提出Panda模型，通过自蒸馏学习可重用传感器级表示，以解决液态氩时间投影室物理重建中的标签依赖问题。

**关键词**：液态氩时间投影室, 传感器级表示学习, 自蒸馏, 稀疏3D编码, 原型学习, 粒子识别

## 3 点简述
- 核心问题：液态氩时间投影室物理重建依赖复杂、需大量标注数据的特定管道，校准耗时。
- 方法要点：结合分层稀疏3D编码器和多视图原型自蒸馏目标，直接从原始未标注数据学习表示。
- 实验或效果：在模拟数据上，用千分之一标签超越先前语义分割模型，并实现与先进重建工具相当的粒子识别。

## 摘要（原文）

> Liquid argon time projection chambers (LArTPCs) provide dense, high-fidelity 3D measurements of particle interactions and underpin current and future neutrino and rare-event experiments. Physics reconstruction typically relies on complex detector-specific pipelines that use tens of hand-engineered pattern recognition algorithms or cascades of task-specific neural networks that require extensive, labeled simulation that requires a careful, time-consuming calibration process. We introduce \textbf{Panda}, a model that learns reusable sensor-level representations directly from raw unlabeled LArTPC data. Panda couples a hierarchical sparse 3D encoder with a multi-view, prototype-based self-distillation objective. On a simulated dataset, Panda substantially improves label efficiency and reconstruction quality, beating the previous state-of-the-art semantic segmentation model with 1,000$\times$ fewer labels. We also show that a single set-prediction head 1/20th the size of the backbone with no physical priors trained on frozen outputs from Panda can result in particle identification that is comparable with state-of-the-art (SOTA) reconstruction tools. Full fine-tuning further improves performance across all tasks.

