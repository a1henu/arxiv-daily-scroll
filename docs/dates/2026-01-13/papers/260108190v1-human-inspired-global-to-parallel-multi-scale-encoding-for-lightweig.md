---
layout: default
title: Human-inspired Global-to-Parallel Multi-scale Encoding for Lightweight Vision Models
---

# Human-inspired Global-to-Parallel Multi-scale Encoding for Lightweight Vision Models
**arXiv**：[2601.08190v1](https://arxiv.org/abs/2601.08190) · [PDF](https://arxiv.org/pdf/2601.08190.pdf)  
**作者**：Wei Xu  

**一句话要点**：提出GPM编码以构建轻量视觉模型，平衡参数、计算与性能

**关键词**：轻量视觉模型, 多尺度编码, 人类视觉启发, 全局局部特征, 参数效率

## 3 点简述
- 轻量视觉模型常面临参数与计算效率的权衡难题，现有方法可能牺牲参数规模
- GPM通过全局洞察生成器与并行多尺度分支，模拟人类视觉的全局到局部感知机制
- 实验显示H-GPE网络在分类、检测和分割任务中实现高效性能平衡

## 摘要（原文）

> Lightweight vision networks have witnessed remarkable progress in recent years, yet achieving a satisfactory balance among parameter scale, computational overhead, and task performance remains difficult. Although many existing lightweight models manage to reduce computation considerably, they often do so at the expense of a substantial increase in parameter count (e.g., LSNet, MobileMamba), which still poses obstacles for deployment on resource-limited devices. In parallel, some studies attempt to draw inspiration from human visual perception, but their modeling tends to oversimplify the visual process, making it hard to reflect how perception truly operates. Revisiting the cooperative mechanism of the human visual system, we propose GPM (Global-to-Parallel Multi-scale Encoding). GPM first employs a Global Insight Generator (GIG) to extract holistic cues, and subsequently processes features of different scales through parallel branches: LSAE emphasizes mid-/large-scale semantic relations, while IRB (Inverted Residual Block) preserves fine-grained texture information, jointly enabling coherent representation of global and local features. As such, GPM conforms to two characteristic behaviors of human vision perceiving the whole before focusing on details, and maintaining broad contextual awareness even during local attention. Built upon GPM, we further develop the lightweight H-GPE network. Experiments on image classification, object detection, and semantic segmentation show that H-GPE achieves strong performance while maintaining a balanced footprint in both FLOPs and parameters, delivering a more favorable accuracy-efficiency trade-off compared with recent state-of-the-art lightweight models.

