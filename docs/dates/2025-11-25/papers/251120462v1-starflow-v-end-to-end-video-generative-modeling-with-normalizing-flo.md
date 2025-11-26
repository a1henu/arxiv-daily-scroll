---
layout: default
title: STARFlow-V: End-to-End Video Generative Modeling with Normalizing Flow
---

# STARFlow-V: End-to-End Video Generative Modeling with Normalizing Flow
**arXiv**：[2511.20462v1](https://arxiv.org/abs/2511.20462) · [PDF](https://arxiv.org/pdf/2511.20462.pdf)  
**作者**：Jiatao Gu, Ying Shen, Tianrong Chen, Laurent Dinh, Yuyang Wang, Miguel Angel Bautista, David Berthelot, Josh Susskind, Shuangfei Zhai  

**一句话要点**：提出STARFlow-V以解决视频生成中的时空复杂性和误差累积问题

**关键词**：视频生成, 归一化流, 因果预测, 端到端学习, 似然估计, 自回归模型

## 3 点简述
- 核心问题：视频生成中时空复杂性高，扩散模型易产生误差累积
- 方法要点：采用全局-局部架构和流-得分匹配，实现端到端因果预测
- 实验或效果：在视觉保真度和时间一致性上优于扩散基线，支持多任务生成

## 摘要（原文）

> Normalizing flows (NFs) are end-to-end likelihood-based generative models for continuous data, and have recently regained attention with encouraging progress on image generation. Yet in the video generation domain, where spatiotemporal complexity and computational cost are substantially higher, state-of-the-art systems almost exclusively rely on diffusion-based models. In this work, we revisit this design space by presenting STARFlow-V, a normalizing flow-based video generator with substantial benefits such as end-to-end learning, robust causal prediction, and native likelihood estimation. Building upon the recently proposed STARFlow, STARFlow-V operates in the spatiotemporal latent space with a global-local architecture which restricts causal dependencies to a global latent space while preserving rich local within-frame interactions. This eases error accumulation over time, a common pitfall of standard autoregressive diffusion model generation. Additionally, we propose flow-score matching, which equips the model with a light-weight causal denoiser to improve the video generation consistency in an autoregressive fashion. To improve the sampling efficiency, STARFlow-V employs a video-aware Jacobi iteration scheme that recasts inner updates as parallelizable iterations without breaking causality. Thanks to the invertible structure, the same model can natively support text-to-video, image-to-video as well as video-to-video generation tasks. Empirically, STARFlow-V achieves strong visual fidelity and temporal consistency with practical sampling throughput relative to diffusion-based baselines. These results present the first evidence, to our knowledge, that NFs are capable of high-quality autoregressive video generation, establishing them as a promising research direction for building world models. Code and generated samples are available at https://github.com/apple/ml-starflow.

