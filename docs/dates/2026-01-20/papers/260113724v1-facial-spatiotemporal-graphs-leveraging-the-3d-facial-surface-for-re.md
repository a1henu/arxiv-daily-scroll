---
layout: default
title: Facial Spatiotemporal Graphs: Leveraging the 3D Facial Surface for Remote Physiological Measurement
---

# Facial Spatiotemporal Graphs: Leveraging the 3D Facial Surface for Remote Physiological Measurement
**arXiv**：[2601.13724v1](https://arxiv.org/abs/2601.13724) · [PDF](https://arxiv.org/pdf/2601.13724.pdf)  
**作者**：Sam Cantrill, David Ahmedt-Aristizabal, Lars Petersson, Hanna Suominen, Mohammad Ali Armin  

**一句话要点**：提出面部时空图以解决远程光电容积描记中3D面部表面未对齐的问题

**关键词**：远程光电容积描记, 3D面部建模, 时空图卷积网络, 生理信号估计, 表面对齐处理

## 3 点简述
- 核心问题：现有方法未将感受野与3D面部表面（rPPG信号的空间支持）显式对齐。
- 方法要点：引入面部时空图，基于3D面部网格序列编码颜色和结构，实现表面对齐的时空处理。
- 实验或效果：MeshPhys在四个基准数据集上实现最先进或竞争性能，消融研究验证了表面约束和3D感知特征的重要性。

## 摘要（原文）

> Facial remote photoplethysmography (rPPG) methods estimate physiological signals by modeling subtle color changes on the 3D facial surface over time. However, existing methods fail to explicitly align their receptive fields with the 3D facial surface-the spatial support of the rPPG signal. To address this, we propose the Facial Spatiotemporal Graph (STGraph), a novel representation that encodes facial color and structure using 3D facial mesh sequences-enabling surface-aligned spatiotemporal processing. We introduce MeshPhys, a lightweight spatiotemporal graph convolutional network that operates on the STGraph to estimate physiological signals. Across four benchmark datasets, MeshPhys achieves state-of-the-art or competitive performance in both intra- and cross-dataset settings. Ablation studies show that constraining the model's receptive field to the facial surface acts as a strong structural prior, and that surface-aligned, 3D-aware node features are critical for robustly encoding facial surface color. Together, the STGraph and MeshPhys constitute a novel, principled modeling paradigm for facial rPPG, enabling robust, interpretable, and generalizable estimation. Code is available at https://samcantrill.github.io/facial-stgraph-rppg/ .

