---
layout: default
title: Quartet of Diffusions: Structure-Aware Point Cloud Generation through Part and Symmetry Guidance
---

# Quartet of Diffusions: Structure-Aware Point Cloud Generation through Part and Symmetry Guidance
**arXiv**：[2601.20425v1](https://arxiv.org/abs/2601.20425) · [PDF](https://arxiv.org/pdf/2601.20425.pdf)  
**作者**：Chenliang Zhou, Fangcheng Zhong, Weihao Xia, Albert Miao, Canberk Baykal, Cengiz Oztireli  

**一句话要点**：提出四重扩散框架，通过部件和对称性引导实现结构感知的点云生成

**关键词**：点云生成, 扩散模型, 结构感知, 部件组合, 对称性引导, 三维形状建模

## 3 点简述
- 核心问题：现有方法难以在点云生成中同时保证对称性和部件组合的连贯性
- 方法要点：使用四个协调的扩散模型分别建模全局形状、对称性、语义部件及其空间组装
- 实验或效果：在实验中达到最先进性能，支持细粒度属性控制和高质量输出

## 摘要（原文）

> We introduce the Quartet of Diffusions, a structure-aware point cloud generation framework that explicitly models part composition and symmetry. Unlike prior methods that treat shape generation as a holistic process or only support part composition, our approach leverages four coordinated diffusion models to learn distributions of global shape latents, symmetries, semantic parts, and their spatial assembly. This structured pipeline ensures guaranteed symmetry, coherent part placement, and diverse, high-quality outputs. By disentangling the generative process into interpretable components, our method supports fine-grained control over shape attributes, enabling targeted manipulation of individual parts while preserving global consistency. A central global latent further reinforces structural coherence across assembled parts. Our experiments show that the Quartet achieves state-of-the-art performance. To our best knowledge, this is the first 3D point cloud generation framework that fully integrates and enforces both symmetry and part priors throughout the generative process.

