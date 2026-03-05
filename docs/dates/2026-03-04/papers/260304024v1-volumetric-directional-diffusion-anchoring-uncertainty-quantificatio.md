---
layout: default
title: Volumetric Directional Diffusion: Anchoring Uncertainty Quantification in Anatomical Consensus for Ambiguous Medical Image Segmentation
---

# Volumetric Directional Diffusion: Anchoring Uncertainty Quantification in Anatomical Consensus for Ambiguous Medical Image Segmentation
**arXiv**：[2603.04024v1](https://arxiv.org/abs/2603.04024) · [PDF](https://arxiv.org/pdf/2603.04024.pdf)  
**作者**：Chao Wu, Kangxian Xie, Mingchen Gao  

**一句话要点**：提出Volumetric Directional Diffusion以解决医学图像分割中模糊区域的不确定性量化问题

**关键词**：医学图像分割, 不确定性量化, 扩散模型, 三维边界残差, 多标注数据集, 解剖一致性

## 3 点简述
- 核心问题：医学图像分割存在观察者间高变异性，传统确定性模型忽略不确定性，生成模型易产生结构断裂或解剖幻觉。
- 方法要点：VDD通过锚定确定性共识先验，限制生成空间为3D边界残差场，探索几何变化而不破坏拓扑结构。
- 实验或效果：在三个多标注数据集上验证，VDD在不确定性量化方面达到先进水平，分割精度与确定性模型竞争。

## 摘要（原文）

> Equivocal 3D lesion segmentation exhibits high inter-observer variability. Conventional deterministic models ignore this aleatoric uncertainty, producing over-confident masks that obscure clinical risks. Conversely, while generative methods (e.g., standard diffusion) capture sample diversity, recovering complex topology from pure noise frequently leads to severe structural fractures and out-of-distribution anatomical hallucinations. To resolve this fidelity-diversity trade-off, we propose Volumetric Directional Diffusion (VDD). Unlike standard diffusion models that denoise isotropic Gaussian noise, VDD mathematically anchors the generative trajectory to a deterministic consensus prior. By restricting the generative search space to iteratively predict a 3D boundary residual field, VDD accurately explores the fine-grained geometric variations inherent in expert disagreements without risking topological collapse. Extensive validation on three multi-rater datasets (LIDC-IDRI, KiTS21, and ISBI 2015) demonstrates that VDD achieves state-of-the-art uncertainty quantification (significantly improving GED and CI) while remaining highly competitive in segmentation accuracy against deterministic upper bounds. Ultimately, VDD provides clinicians with anatomically coherent uncertainty maps, enabling safer decision-making and mitigating risks in downstream tasks (e.g., radiotherapy planning or surgical margin assessment).

