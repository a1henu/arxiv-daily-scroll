---
layout: default
title: ShapeUP: Scalable Image-Conditioned 3D Editing
---

# ShapeUP: Scalable Image-Conditioned 3D Editing
**arXiv**：[2602.05676v1](https://arxiv.org/abs/2602.05676) · [PDF](https://arxiv.org/pdf/2602.05676.pdf)  
**作者**：Inbar Gat, Dana Cohen-Bar, Guy Levy, Elad Richardson, Daniel Cohen-Or  

**一句话要点**：提出ShapeUP框架，通过图像条件化监督学习实现可扩展的3D编辑，解决现有方法在可控性、一致性和效率上的权衡问题。

**关键词**：3D编辑, 图像条件化, 监督学习, 扩散变换器, 潜在映射, 可扩展性

## 3 点简述
- 核心问题：现有3D编辑方法在视觉可控性、几何一致性和可扩展性之间存在困难权衡，如优化方法慢、多视图传播有视觉漂移、无训练方法受限于固定先验。
- 方法要点：基于预训练3D基础模型，使用图像作为提示，通过监督训练学习从源3D形状到编辑后3D形状的潜在到潜在映射，采用3D扩散变换器实现精细控制和隐式定位。
- 实验或效果：在身份保持和编辑保真度上优于当前训练和无训练基线，提供稳健且可扩展的原生3D内容创建范例。

## 摘要（原文）

> Recent advancements in 3D foundation models have enabled the generation of high-fidelity assets, yet precise 3D manipulation remains a significant challenge. Existing 3D editing frameworks often face a difficult trade-off between visual controllability, geometric consistency, and scalability. Specifically, optimization-based methods are prohibitively slow, multi-view 2D propagation techniques suffer from visual drift, and training-free latent manipulation methods are inherently bound by frozen priors and cannot directly benefit from scaling. In this work, we present ShapeUP, a scalable, image-conditioned 3D editing framework that formulates editing as a supervised latent-to-latent translation within a native 3D representation. This formulation allows ShapeUP to build on a pretrained 3D foundation model, leveraging its strong generative prior while adapting it to editing through supervised training. In practice, ShapeUP is trained on triplets consisting of a source 3D shape, an edited 2D image, and the corresponding edited 3D shape, and learns a direct mapping using a 3D Diffusion Transformer (DiT). This image-as-prompt approach enables fine-grained visual control over both local and global edits and achieves implicit, mask-free localization, while maintaining strict structural consistency with the original asset. Our extensive evaluations demonstrate that ShapeUP consistently outperforms current trained and training-free baselines in both identity preservation and edit fidelity, offering a robust and scalable paradigm for native 3D content creation.

