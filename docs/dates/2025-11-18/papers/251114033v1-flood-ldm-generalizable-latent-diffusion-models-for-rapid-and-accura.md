---
layout: default
title: Flood-LDM: Generalizable Latent Diffusion Models for rapid and accurate zero-shot High-Resolution Flood Mapping
---

# Flood-LDM: Generalizable Latent Diffusion Models for rapid and accurate zero-shot High-Resolution Flood Mapping
**arXiv**：[2511.14033v1](https://arxiv.org/abs/2511.14033) · [PDF](https://arxiv.org/pdf/2511.14033.pdf)  
**作者**：Sun Han Neo, Sachith Seneviratne, Herath Mudiyanselage Viraj Vidura Herath, Abhishek Saha, Sanka Rasnayaka, Lucy Amanda Marshall  

**一句话要点**：提出Flood-LDM以解决高分辨率洪水地图快速生成与泛化性问题

**关键词**：洪水地图超分辨率, 潜在扩散模型, 零样本泛化, 物理信息输入, 实时洪水风险管理

## 3 点简述
- 传统物理模型计算密集，难以实时大规模应用洪水预测
- 利用潜在扩散模型对粗网格洪水图进行超分辨率重建
- 实验显示模型在保持精度下显著减少推理时间，并提升跨区域泛化能力

## 摘要（原文）

> Flood prediction is critical for emergency planning and response to mitigate human and economic losses. Traditional physics-based hydrodynamic models generate high-resolution flood maps using numerical methods requiring fine-grid discretization; which are computationally intensive and impractical for real-time large-scale applications. While recent studies have applied convolutional neural networks for flood map super-resolution with good accuracy and speed, they suffer from limited generalizability to unseen areas. In this paper, we propose a novel approach that leverages latent diffusion models to perform super-resolution on coarse-grid flood maps, with the objective of achieving the accuracy of fine-grid flood maps while significantly reducing inference time. Experimental results demonstrate that latent diffusion models substantially decrease the computational time required to produce high-fidelity flood maps without compromising on accuracy, enabling their use in real-time flood risk management. Moreover, diffusion models exhibit superior generalizability across different physical locations, with transfer learning further accelerating adaptation to new geographic regions. Our approach also incorporates physics-informed inputs, addressing the common limitation of black-box behavior in machine learning, thereby enhancing interpretability. Code is available at https://github.com/neosunhan/flood-diff.

