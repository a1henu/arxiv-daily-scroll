---
layout: default
title: Beyond Randomness: Understand the Order of the Noise in Diffusion
---

# Beyond Randomness: Understand the Order of the Noise in Diffusion
**arXiv**：[2511.07756v1](https://arxiv.org/abs/2511.07756) · [PDF](https://arxiv.org/pdf/2511.07756.pdf)  
**作者**：Song Yan, Min Li, Bi Xinliang, Jian Yang, Yusen Zhang, Guanye Xiong, Yunwei Lan, Tao Zhang, Wei Zhai, Zheng-Jun Zha  

**一句话要点**：提出语义擦除-注入方法以优化文本驱动扩散模型的生成过程

**关键词**：扩散模型, 文本驱动生成, 噪声分析, 语义调制, 训练免费方法

## 3 点简述
- 核心问题：初始噪声在扩散模型中通常被视为随机，但实际包含可分析语义模式
- 方法要点：基于信息理论，通过两步语义擦除与注入过程调制噪声，无需训练
- 实验或效果：在DiT和UNet架构的多种模型中一致有效，提升生成一致性

## 摘要（原文）

> In text-driven content generation (T2C) diffusion model, semantic of generated content is mostly attributed to the process of text embedding and attention mechanism interaction. The initial noise of the generation process is typically characterized as a random element that contributes to the diversity of the generated content. Contrary to this view, this paper reveals that beneath the random surface of noise lies strong analyzable patterns. Specifically, this paper first conducts a comprehensive analysis of the impact of random noise on the model's generation. We found that noise not only contains rich semantic information, but also allows for the erasure of unwanted semantics from it in an extremely simple way based on information theory, and using the equivalence between the generation process of diffusion model and semantic injection to inject semantics into the cleaned noise. Then, we mathematically decipher these observations and propose a simple but efficient training-free and universal two-step "Semantic Erasure-Injection" process to modulate the initial noise in T2C diffusion model. Experimental results demonstrate that our method is consistently effective across various T2C models based on both DiT and UNet architectures and presents a novel perspective for optimizing the generation of diffusion model, providing a universal tool for consistent generation.

