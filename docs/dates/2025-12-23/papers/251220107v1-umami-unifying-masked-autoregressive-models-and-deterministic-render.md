---
layout: default
title: UMAMI: Unifying Masked Autoregressive Models and Deterministic Rendering for View Synthesis
---

# UMAMI: Unifying Masked Autoregressive Models and Deterministic Rendering for View Synthesis
**arXiv**：[2512.20107v1](https://arxiv.org/abs/2512.20107) · [PDF](https://arxiv.org/pdf/2512.20107.pdf)  
**作者**：Thanh-Tung Le, Tuan Pham, Tung Nguyen, Deying Kong, Xiaohui Xie, Stephan Mandt  

**一句话要点**：提出UMAMI框架，结合掩码自回归模型与确定性渲染以提升新视角合成的效率与质量。

**关键词**：新视角合成, 掩码自回归模型, 确定性渲染, Transformer编码, 扩散模型, 端到端训练

## 3 点简述
- 核心问题：现有新视角合成方法在渲染速度与图像质量间存在权衡，确定性网络快速但模糊，扩散方法高质量但计算成本高。
- 方法要点：使用双向Transformer编码多视图信息，通过回归头处理几何明确区域，掩码自回归扩散头补全遮挡或未见区域。
- 实验或效果：在实验中达到最先进图像质量，相比全生成基线渲染时间减少一个数量级。

## 摘要（原文）

> Novel view synthesis (NVS) seeks to render photorealistic, 3D-consistent images of a scene from unseen camera poses given only a sparse set of posed views. Existing deterministic networks render observed regions quickly but blur unobserved areas, whereas stochastic diffusion-based methods hallucinate plausible content yet incur heavy training- and inference-time costs. In this paper, we propose a hybrid framework that unifies the strengths of both paradigms. A bidirectional transformer encodes multi-view image tokens and Plucker-ray embeddings, producing a shared latent representation. Two lightweight heads then act on this representation: (i) a feed-forward regression head that renders pixels where geometry is well constrained, and (ii) a masked autoregressive diffusion head that completes occluded or unseen regions. The entire model is trained end-to-end with joint photometric and diffusion losses, without handcrafted 3D inductive biases, enabling scalability across diverse scenes. Experiments demonstrate that our method attains state-of-the-art image quality while reducing rendering time by an order of magnitude compared with fully generative baselines.

