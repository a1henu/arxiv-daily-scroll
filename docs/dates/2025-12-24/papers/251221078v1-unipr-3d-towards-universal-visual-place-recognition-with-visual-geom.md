---
layout: default
title: UniPR-3D: Towards Universal Visual Place Recognition with Visual Geometry Grounded Transformer
---

# UniPR-3D: Towards Universal Visual Place Recognition with Visual Geometry Grounded Transformer
**arXiv**：[2512.21078v1](https://arxiv.org/abs/2512.21078) · [PDF](https://arxiv.org/pdf/2512.21078.pdf)  
**作者**：Tianchen Deng, Xun Chen, Ziming Li, Hongming Shen, Danwei Wang, Javier Civera, Hesheng Wang  

**一句话要点**：提出UniPR-3D，通过视觉几何基础Transformer实现通用视觉地点识别

**关键词**：视觉地点识别, 多视图检索, Transformer, 3D表示, 特征聚合, 通用性

## 3 点简述
- 传统视觉地点识别基于单图像检索，多视图方法未充分探索且泛化性差
- UniPR-3D基于VGGT编码多视图3D表示，设计特征聚合器融合2D和3D特征
- 实验显示UniPR-3D在单视图和多视图基准上达到新最优性能

## 摘要（原文）

> Visual Place Recognition (VPR) has been traditionally formulated as a single-image retrieval task. Using multiple views offers clear advantages, yet this setting remains relatively underexplored and existing methods often struggle to generalize across diverse environments. In this work we introduce UniPR-3D, the first VPR architecture that effectively integrates information from multiple views. UniPR-3D builds on a VGGT backbone capable of encoding multi-view 3D representations, which we adapt by designing feature aggregators and fine-tune for the place recognition task. To construct our descriptor, we jointly leverage the 3D tokens and intermediate 2D tokens produced by VGGT. Based on their distinct characteristics, we design dedicated aggregation modules for 2D and 3D features, allowing our descriptor to capture fine-grained texture cues while also reasoning across viewpoints. To further enhance generalization, we incorporate both single- and multi-frame aggregation schemes, along with a variable-length sequence retrieval strategy. Our experiments show that UniPR-3D sets a new state of the art, outperforming both single- and multi-view baselines and highlighting the effectiveness of geometry-grounded tokens for VPR. Our code and models will be made publicly available on Github https://github.com/dtc111111/UniPR-3D.

