---
layout: default
title: Highly Efficient Test-Time Scaling for T2I Diffusion Models with Text Embedding Perturbation
---

# Highly Efficient Test-Time Scaling for T2I Diffusion Models with Text Embedding Perturbation
**arXiv**：[2512.03996v1](https://arxiv.org/abs/2512.03996) · [PDF](https://arxiv.org/pdf/2512.03996.pdf)  
**作者**：Hang Xu, Linjiang Huang, Feng Zhao  

**一句话要点**：提出文本嵌入扰动以增强T2I扩散模型的测试时缩放性能

**关键词**：文本到图像生成, 扩散模型, 测试时缩放, 文本嵌入扰动, 频域分析

## 3 点简述
- 核心问题：T2I扩散模型中噪声随机性对测试时缩放性能的影响未被充分探索。
- 方法要点：结合空间噪声与文本嵌入扰动，基于频域分析设计步进式扰动策略。
- 实验或效果：在多个基准上显著提升生成多样性与质量，几乎无额外计算开销。

## 摘要（原文）

> Test-time scaling (TTS) aims to achieve better results by increasing random sampling and evaluating samples based on rules and metrics. However, in text-to-image(T2I) diffusion models, most related works focus on search strategies and reward models, yet the impact of the stochastic characteristic of noise in T2I diffusion models on the method's performance remains unexplored. In this work, we analyze the effects of randomness in T2I diffusion models and explore a new format of randomness for TTS: text embedding perturbation, which couples with existing randomness like SDE-injected noise to enhance generative diversity and quality. We start with a frequency-domain analysis of these formats of randomness and their impact on generation, and find that these two randomness exhibit complementary behavior in the frequency domain: spatial noise favors low-frequency components (early steps), while text embedding perturbation enhances high-frequency details (later steps), thereby compensating for the potential limitations of spatial noise randomness in high-frequency manipulation. Concurrently, text embedding demonstrates varying levels of tolerance to perturbation across different dimensions of the generation process. Specifically, our method consists of two key designs: (1) Introducing step-based text embedding perturbation, combining frequency-guided noise schedules with spatial noise perturbation. (2) Adapting the perturbation intensity selectively based on their frequency-specific contributions to generation and tolerance to perturbation. Our approach can be seamlessly integrated into existing TTS methods and demonstrates significant improvements on multiple benchmarks with almost no additional computation. Code is available at \href{https://github.com/xuhang07/TEP-Diffusion}{https://github.com/xuhang07/TEP-Diffusion}.

