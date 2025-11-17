---
layout: default
title: Free3D: 3D Human Motion Emerges from Single-View 2D Supervision
---

# Free3D: 3D Human Motion Emerges from Single-View 2D Supervision
**arXiv**：[2511.11368v1](https://arxiv.org/abs/2511.11368) · [PDF](https://arxiv.org/pdf/2511.11368.pdf)  
**作者**：Sheng Liu, Yuanzhi Liang, Sidan Du  

**一句话要点**：提出Free3D框架，通过单视图2D监督生成3D人体运动

**关键词**：3D人体运动生成, 2D监督学习, 运动提升, 视图一致性, 物理合理性, 泛化能力

## 3 点简述
- 现有3D运动生成模型依赖精确3D监督，导致泛化能力受限。
- 引入ML-RQ模型和3D无监督正则化，从2D运动映射到3D一致空间。
- 实验显示，Free3D生成多样、连贯的3D运动，性能媲美3D监督方法。

## 摘要（原文）

> Recent 3D human motion generation models demonstrate remarkable reconstruction accuracy yet struggle to generalize beyond training distributions. This limitation arises partly from the use of precise 3D supervision, which encourages models to fit fixed coordinate patterns instead of learning the essential 3D structure and motion semantic cues required for robust generalization.To overcome this limitation, we propose Free3D, a framework that synthesizes realistic 3D motions without any 3D motion annotations. Free3D introduces a Motion-Lifting Residual Quantized VAE (ML-RQ) that maps 2D motion sequences into 3D-consistent latent spaces, and a suite of 3D-free regularization objectives enforcing view consistency, orientation coherence, and physical plausibility. Trained entirely on 2D motion data, Free3D generates diverse, temporally coherent, and semantically aligned 3D motions, achieving performance comparable to or even surpassing fully 3D-supervised counterparts. These results suggest that relaxing explicit 3D supervision encourages stronger structural reasoning and generalization, offering a scalable and data-efficient paradigm for 3D motion generation.

