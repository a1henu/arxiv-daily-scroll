---
layout: default
title: Brewing Stronger Features: Dual-Teacher Distillation for Multispectral Earth Observation
---

# Brewing Stronger Features: Dual-Teacher Distillation for Multispectral Earth Observation
**arXiv**：[2602.19863v1](https://arxiv.org/abs/2602.19863) · [PDF](https://arxiv.org/pdf/2602.19863.pdf)  
**作者**：Filip Wolf, Blaž Rolih, Luka Čehovin Zajc  

**一句话要点**：提出双教师对比蒸馏框架，以解决多光谱地球观测中跨模态知识迁移问题。

**关键词**：多光谱地球观测, 对比蒸馏, 跨模态学习, 知识迁移, 语义分割

## 3 点简述
- 核心问题：地球观测传感器多样，单一通用模型不现实，需高效跨模态知识迁移。
- 方法要点：结合多光谱教师和光学视觉基础模型教师，通过对比蒸馏对齐预训练目标。
- 实验或效果：在光学和多光谱基准测试中均取得最优性能，平均提升语义分割3.64个百分点。

## 摘要（原文）

> Foundation models are transforming Earth Observation (EO), yet the diversity of EO sensors and modalities makes a single universal model unrealistic. Multiple specialized EO foundation models (EOFMs) will likely coexist, making efficient knowledge transfer across modalities essential. Most existing EO pretraining relies on masked image modeling, which emphasizes local reconstruction but provides limited control over global semantic structure. To address this, we propose a dual-teacher contrastive distillation framework for multispectral imagery that aligns the student's pretraining objective with the contrastive self-distillation paradigm of modern optical vision foundation models (VFMs). Our approach combines a multispectral teacher with an optical VFM teacher, enabling coherent cross-modal representation learning. Experiments across diverse optical and multispectral benchmarks show that our model adapts to multispectral data without compromising performance on optical-only inputs, achieving state-of-the-art results in both settings, with an average improvement of 3.64 percentage points in semantic segmentation, 1.2 in change detection, and 1.31 in classification tasks. This demonstrates that contrastive distillation provides a principled and efficient approach to scalable representation learning across heterogeneous EO data sources. Code: Coming soon.

