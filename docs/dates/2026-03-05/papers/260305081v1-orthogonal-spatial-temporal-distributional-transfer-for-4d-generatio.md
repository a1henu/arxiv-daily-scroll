---
layout: default
title: Orthogonal Spatial-temporal Distributional Transfer for 4D Generation
---

# Orthogonal Spatial-temporal Distributional Transfer for 4D Generation
**arXiv**：[2603.05081v1](https://arxiv.org/abs/2603.05081) · [PDF](https://arxiv.org/pdf/2603.05081.pdf)  
**作者**：Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  

**一句话要点**：提出正交时空分布迁移框架以解决4D生成中数据稀缺问题

**关键词**：4D生成, 时空解耦, 分布迁移, 扩散模型, HexPlane建模

## 3 点简述
- 核心问题：缺乏大规模4D数据集，导致模型难以学习高质量4D生成所需的时空特征。
- 方法要点：设计时空解耦的4D扩散模型，通过正交分布迁移机制从3D和视频模型中转移先验知识。
- 实验或效果：方法显著优于现有方法，在时空一致性和4D合成质量上表现优越。

## 摘要（原文）

> In the AIGC era, generating high-quality 4D content has garnered increasing research attention. Unfortunately, current 4D synthesis research is severely constrained by the lack of large-scale 4D datasets, preventing models from adequately learning the critical spatial-temporal features necessary for high-quality 4D generation, thus hindering progress in this domain. To combat this, we propose a novel framework that transfers rich spatial priors from existing 3D diffusion models and temporal priors from video diffusion models to enhance 4D synthesis. We develop a spatial-temporal-disentangled 4D (STD-4D) Diffusion model, which synthesizes 4D-aware videos through disentangled spatial and temporal latents. To facilitate the best feature transfer, we design a novel Orthogonal Spatial-temporal Distributional Transfer (Orster) mechanism, where the spatiotemporal feature distributions are carefully modeled and injected into the STD-4D Diffusion. Furthermore, during the 4D construction, we devise a spatial-temporal-aware HexPlane (ST-HexPlane) to integrate the transferred spatiotemporal features, thereby improving 4D deformation and 4D Gaussian feature modeling. Experiments demonstrate that our method significantly outperforms existing approaches, achieving superior spatial-temporal consistency and higher-quality 4D synthesis.

