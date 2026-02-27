---
layout: default
title: SceneTransporter: Optimal Transport-Guided Compositional Latent Diffusion for Single-Image Structured 3D Scene Generation
---

# SceneTransporter: Optimal Transport-Guided Compositional Latent Diffusion for Single-Image Structured 3D Scene Generation
**arXiv**：[2602.22785v1](https://arxiv.org/abs/2602.22785) · [PDF](https://arxiv.org/pdf/2602.22785.pdf)  
**作者**：Ling Wang, Hao-Xiang Guo, Xinzhou Wang, Fuchun Sun, Kai Sun, Pengkun Liu, Hang Xiao, Zhong Wang, Guangyuan Fu, Eric Li, Yang Liu, Yikai Wang  

**一句话要点**：提出SceneTransporter，通过最优传输引导的潜在扩散，从单图像生成结构化3D场景。

**关键词**：单图像3D场景生成, 结构化场景生成, 最优传输, 潜在扩散模型, 实例分割, 开放世界场景

## 3 点简述
- 核心问题：现有方法生成部分级3D对象，但缺乏结构约束，难以在开放世界场景中组织成独立实例。
- 方法要点：在去噪循环中引入熵最优传输目标，强制图像块与部分级潜在的一对一映射，防止纠缠并促进对象分组。
- 实验或效果：在开放世界场景生成中优于现有方法，显著提升实例级连贯性和几何保真度。

## 摘要（原文）

> We introduce SceneTransporter, an end-to-end framework for structured 3D scene generation from a single image. While existing methods generate part-level 3D objects, they often fail to organize these parts into distinct instances in open-world scenes. Through a debiased clustering probe, we reveal a critical insight: this failure stems from the lack of structural constraints within the model's internal assignment mechanism. Based on this finding, we reframe the task of structured 3D scene generation as a global correlation assignment problem. To solve this, SceneTransporter formulates and solves an entropic Optimal Transport (OT) objective within the denoising loop of the compositional DiT model. This formulation imposes two powerful structural constraints. First, the resulting transport plan gates cross-attention to enforce an exclusive, one-to-one routing of image patches to part-level 3D latents, preventing entanglement. Second, the competitive nature of the transport encourages the grouping of similar patches, a process that is further regularized by an edge-based cost, to form coherent objects and prevent fragmentation. Extensive experiments show that SceneTransporter outperforms existing methods on open-world scene generation, significantly improving instance-level coherence and geometric fidelity. Code and models will be publicly available at https://2019epwl.github.io/SceneTransporter/.

