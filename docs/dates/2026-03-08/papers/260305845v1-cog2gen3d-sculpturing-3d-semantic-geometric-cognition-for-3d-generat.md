---
layout: default
title: Cog2Gen3D: Sculpturing 3D Semantic-Geometric Cognition for 3D Generation
---

# Cog2Gen3D: Sculpturing 3D Semantic-Geometric Cognition for 3D Generation
**arXiv**：[2603.05845v1](https://arxiv.org/abs/2603.05845) · [PDF](https://arxiv.org/pdf/2603.05845.pdf)  
**作者**：Haonan Wang, Hanyu Zhou, Haoyue Liu, Tao Gu, Luxin Yan  

**一句话要点**：提出Cog2Gen3D框架，通过语义-几何认知引导扩散模型解决3D生成中的物理合理性问题。

**关键词**：3D生成, 扩散模型, 语义几何融合, 高斯生成, 认知图, 物理合理性

## 3 点简述
- 核心问题：现有3D生成方法缺乏绝对几何约束，导致尺度不一致和物理不合理。
- 方法要点：构建双流语义-几何图，融合为3D认知图以指导高斯扩散生成。
- 实验或效果：在Marble World Labs验证集上，语义保真度和几何合理性显著优于现有方法。

## 摘要（原文）

> Generative models have achieved success in producing semantically plausible 2D images, but it remains challenging in 3D generation due to the absence of spatial geometry constraints. Typically, existing methods utilize geometric features as conditions to enhance spatial awareness. However, these methods can only model relative relationships and are prone to scale inconsistency of absolute geometry. Thus, we argue that semantic information and absolute geometry empower 3D cognition, thereby enabling controllable 3D generation for the physical world. In this work, we propose Cog2Gen3D, a 3D cognition-guided diffusion framework for 3D generation. Our model is guided by three key designs: 1) Cognitive Feature Embeddings. We encode different modalities into semantic and geometric representations and further extract logical representations. 2) 3D Latent Cognition Graph. We structure different representations into dual-stream semantic-geometric graphs and fuse them via common-based cross-attention to obtain a 3D cognition graph. 3) Cognition-Guided Latent Diffusion. We leverage the fused 3D cognition graph as the condition to guide the latent diffusion process for 3D Gaussian generation. Under this unified framework, the 3D cognition graph ensures the physical plausibility and structural rationality of 3D generation. Moreover, we construct a validation subset based on the Marble World Labs. Extensive experiments demonstrate that our Cog2Gen3D significantly outperforms existing methods in both semantic fidelity and geometric plausibility.

