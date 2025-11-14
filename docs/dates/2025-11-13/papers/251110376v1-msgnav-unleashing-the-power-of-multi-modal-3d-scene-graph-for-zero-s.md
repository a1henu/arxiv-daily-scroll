---
layout: default
title: MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation
---

# MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation
**arXiv**：[2511.10376v1](https://arxiv.org/abs/2511.10376) · [PDF](https://arxiv.org/pdf/2511.10376.pdf)  
**作者**：Xun Huang, Shijia Zhao, Yunxiang Wang, Xin Lu, Wanfa Zhang, Rongsheng Qu, Weixin Li, Yunhong Wang, Chenglu Wen  

**一句话要点**：提出多模态3D场景图MSGNav以解决零样本具身导航中的视觉信息丢失问题

**关键词**：多模态3D场景图, 零样本具身导航, 开放词汇支持, 视觉推理, 闭环推理, 视点决策

## 3 点简述
- 核心问题：现有零样本方法将视觉观察压缩为文本关系，导致高构建成本、视觉证据丢失和词汇受限
- 方法要点：引入多模态3D场景图M3DSG，保留视觉线索，并设计模块支持高效推理和开放词汇
- 实验或效果：在GOAT-Bench和HM3D-OVON数据集上实现最先进性能，代码将开源

## 摘要（原文）

> Embodied navigation is a fundamental capability for robotic agents operating. Real-world deployment requires open vocabulary generalization and low training overhead, motivating zero-shot methods rather than task-specific RL training. However, existing zero-shot methods that build explicit 3D scene graphs often compress rich visual observations into text-only relations, leading to high construction cost, irreversible loss of visual evidence, and constrained vocabularies. To address these limitations, we introduce the Multi-modal 3D Scene Graph (M3DSG), which preserves visual cues by replacing textual relational edges with dynamically assigned images. Built on M3DSG, we propose MSGNav, a zero-shot navigation system that includes a Key Subgraph Selection module for efficient reasoning, an Adaptive Vocabulary Update module for open vocabulary support, and a Closed-Loop Reasoning module for accurate exploration reasoning. Additionally, we further identify the last-mile problem in zero-shot navigation - determining the feasible target location with a suitable final viewpoint, and propose a Visibility-based Viewpoint Decision module to explicitly resolve it. Comprehensive experimental results demonstrate that MSGNav achieves state-of-the-art performance on GOAT-Bench and HM3D-OVON datasets. The open-source code will be publicly available.

