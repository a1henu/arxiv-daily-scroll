---
layout: default
title: SiMO: Single-Modality-Operable Multimodal Collaborative Perception
---

# SiMO: Single-Modality-Operable Multimodal Collaborative Perception
**arXiv**：[2603.08240v1](https://arxiv.org/abs/2603.08240) · [PDF](https://arxiv.org/pdf/2603.08240.pdf)  
**作者**：Jiageng Wen, Shengjie Zhao, Bing Li, Jiafeng Huang, Kenan Ye, Hao Deng  

**一句话要点**：提出SiMO以解决协同感知中模态失效和语义不匹配问题

**关键词**：协同感知, 多模态融合, 模态失效, 语义对齐, 训练策略

## 3 点简述
- 核心问题：多模态协同感知在关键传感器失效时性能下降，源于特征融合导致语义不匹配
- 方法要点：采用LAMMA自适应处理模态失效，通过Pretrain-Align-Fuse-RD策略保持模态独立性
- 实验或效果：SiMO能对齐多模态特征并保留模态特异性，在所有模态下保持最优性能

## 摘要（原文）

> Collaborative perception integrates multi-agent perspectives to enhance the sensing range and overcome occlusion issues. While existing multimodal approaches leverage complementary sensors to improve performance, they are highly prone to failure--especially when a key sensor like LiDAR is unavailable. The root cause is that feature fusion leads to semantic mismatches between single-modality features and the downstream modules. This paper addresses this challenge for the first time in the field of collaborative perception, introducing Single-Modality-Operable Multimodal Collaborative Perception (SiMO). By adopting the proposed Length-Adaptive Multi-Modal Fusion (LAMMA), SiMO can adaptively handle remaining modal features during modal failures while maintaining consistency of the semantic space. Additionally, leveraging the innovative "Pretrain-Align-Fuse-RD" training strategy, SiMO addresses the issue of modality competition--generally overlooked by existing methods--ensuring the independence of each individual modality branch. Experiments demonstrate that SiMO effectively aligns multimodal features while simultaneously preserving modality-specific features, enabling it to maintain optimal performance across all individual modalities. The implementation details can be found in https://github.com/dempsey-wen/SiMO.

