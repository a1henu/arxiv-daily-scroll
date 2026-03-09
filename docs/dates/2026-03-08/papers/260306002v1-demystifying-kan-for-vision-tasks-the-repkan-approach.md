---
layout: default
title: Demystifying KAN for Vision Tasks: The RepKAN Approach
---

# Demystifying KAN for Vision Tasks: The RepKAN Approach
**arXiv**：[2603.06002v1](https://arxiv.org/abs/2603.06002) · [PDF](https://arxiv.org/pdf/2603.06002.pdf)  
**作者**：Minjong Cheon  

**一句话要点**：提出RepKAN架构，结合CNN与KAN，用于遥感图像分类以实现可解释性。

**关键词**：遥感图像分类, 可解释AI, KAN架构, 双路径设计, 光谱指纹, 物理交互流形

## 3 点简述
- 核心问题：遥感图像分类中CNN和Transformer作为黑盒模型缺乏可解释性。
- 方法要点：采用双路径设计（空间线性与光谱非线性），自主发现类别特定光谱指纹和物理交互流形。
- 实验或效果：在EuroSAT和NWPU-RESISC45数据集上超越先进模型，提供物理可解释推理。

## 摘要（原文）

> Remote sensing image classification is essential for Earth observation, yet standard CNNs and Transformers often function as uninterpretable black-boxes. We propose RepKAN, a novel architecture that integrates the structural efficiency of CNNs with the non-linear representational power of KANs. By utilizing a dual-path design -- Spatial Linear and Spectral Non-linear -- RepKAN enables the autonomous discovery of class-specific spectral fingerprints and physical interaction manifolds. Experimental results on the EuroSAT and NWPU-RESISC45 datasets demonstrate that RepKAN provides explicit physically interpretable reasoning while outperforming state-of-the-art models. These findings indicate that RepKAN holds significant potential to serve as the backbone for future interpretable visual foundation models.

