---
layout: default
title: MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion
---

# MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion
**arXiv**：[2510.13702v1](https://arxiv.org/abs/2510.13702) · [PDF](https://arxiv.org/pdf/2510.13702.pdf)  
**作者**：Minjung Shin, Hyunin Cho, Sooyeon Go, Jin-Hwa Kim, Youngjung Uh  

**一句话要点**：提出MVCustom框架以解决多视角生成与定制化统一问题

**关键词**：多视角生成, 定制化扩散, 几何一致性, 特征场表示, 时空注意力

## 3 点简述
- 核心问题：现有模型无法同时实现多视角一致性和提示定制化
- 方法要点：使用特征场表示和扩散模型，增强时空注意力与几何渲染
- 实验或效果：在实验中唯一实现忠实多视角生成与定制化

## 摘要（原文）

> Multi-view generation with camera pose control and prompt-based customization
> are both essential elements for achieving controllable generative models.
> However, existing multi-view generation models do not support customization
> with geometric consistency, whereas customization models lack explicit
> viewpoint control, making them challenging to unify. Motivated by these gaps,
> we introduce a novel task, multi-view customization, which aims to jointly
> achieve multi-view camera pose control and customization. Due to the scarcity
> of training data in customization, existing multi-view generation models, which
> inherently rely on large-scale datasets, struggle to generalize to diverse
> prompts. To address this, we propose MVCustom, a novel diffusion-based
> framework explicitly designed to achieve both multi-view consistency and
> customization fidelity. In the training stage, MVCustom learns the subject's
> identity and geometry using a feature-field representation, incorporating the
> text-to-video diffusion backbone enhanced with dense spatio-temporal attention,
> which leverages temporal coherence for multi-view consistency. In the inference
> stage, we introduce two novel techniques: depth-aware feature rendering
> explicitly enforces geometric consistency, and consistent-aware latent
> completion ensures accurate perspective alignment of the customized subject and
> surrounding backgrounds. Extensive experiments demonstrate that MVCustom is the
> only framework that simultaneously achieves faithful multi-view generation and
> customization.

