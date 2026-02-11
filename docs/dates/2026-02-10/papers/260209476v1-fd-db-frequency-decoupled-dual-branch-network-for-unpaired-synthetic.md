---
layout: default
title: FD-DB: Frequency-Decoupled Dual-Branch Network for Unpaired Synthetic-to-Real Domain Translation
---

# FD-DB: Frequency-Decoupled Dual-Branch Network for Unpaired Synthetic-to-Real Domain Translation
**arXiv**：[2602.09476v1](https://arxiv.org/abs/2602.09476) · [PDF](https://arxiv.org/pdf/2602.09476.pdf)  
**作者**：Chuanhai Zang, Jiabao Hu, XW Song  

**一句话要点**：提出FD-DB频率解耦双分支网络，以解决无配对合成到真实域翻译中真实感与结构稳定性的权衡问题。

**关键词**：域适应, 无配对翻译, 频率解耦, 双分支网络, 语义分割

## 3 点简述
- 核心问题：合成与真实域间外观和成像差异导致域偏移，现有方法在真实感和结构稳定性间存在权衡。
- 方法要点：通过频率解耦双分支模型，分离外观转移为低频可解释编辑和高频残差补偿，结合门控融合机制。
- 实验或效果：在YCB-V数据集上，FD-DB提升外观一致性，显著增强下游语义分割性能，同时保持几何和语义结构。

## 摘要（原文）

> Synthetic data provide low-cost, accurately annotated samples for geometry-sensitive vision tasks, but appearance and imaging differences between synthetic and real domains cause severe domain shift and degrade downstream performance. Unpaired synthetic-to-real translation can reduce this gap without paired supervision, yet existing methods often face a trade-off between photorealism and structural stability: unconstrained generation may introduce deformation or spurious textures, while overly rigid constraints limit adaptation to real-domain statistics. We propose FD-DB, a frequency-decoupled dual-branch model that separates appearance transfer into low-frequency interpretable editing and high-frequency residual compensation. The interpretable branch predicts physically meaningful editing parameters (white balance, exposure, contrast, saturation, blur, and grain) to build a stable low-frequency appearance base with strong content preservation. The free branch complements fine details through residual generation, and a gated fusion mechanism combines the two branches under explicit frequency constraints to limit low-frequency drift. We further adopt a two-stage training schedule that first stabilizes the editing branch and then releases the residual branch to improve optimization stability. Experiments on the YCB-V dataset show that FD-DB improves real-domain appearance consistency and significantly boosts downstream semantic segmentation performance while preserving geometric and semantic structures.

