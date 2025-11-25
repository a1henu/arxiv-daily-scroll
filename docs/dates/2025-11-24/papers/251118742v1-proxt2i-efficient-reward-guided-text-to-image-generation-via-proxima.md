---
layout: default
title: ProxT2I: Efficient Reward-Guided Text-to-Image Generation via Proximal Diffusion
---

# ProxT2I: Efficient Reward-Guided Text-to-Image Generation via Proximal Diffusion
**arXiv**：[2511.18742v1](https://arxiv.org/abs/2511.18742) · [PDF](https://arxiv.org/pdf/2511.18742.pdf)  
**作者**：Zhenghan Fang, Jian Zheng, Qiaozi Gao, Xiaofeng Gao, Jeremias Sulam  

**一句话要点**：提出ProxT2I方法，通过近端扩散和奖励优化提升文本到图像生成效率与质量。

**关键词**：文本到图像生成, 扩散模型, 近端算子, 奖励优化, 高效采样, 轻量模型

## 3 点简述
- 核心问题：基于前向离散化的扩散模型采样慢且不稳定，影响生成质量。
- 方法要点：使用后向离散化和条件近端算子替代分数函数，结合强化学习优化奖励。
- 实验或效果：在采样效率和人类偏好对齐上优于基线，模型更轻量且性能相当。

## 摘要（原文）

> Diffusion models have emerged as a dominant paradigm for generative modeling across a wide range of domains, including prompt-conditional generation. The vast majority of samplers, however, rely on forward discretization of the reverse diffusion process and use score functions that are learned from data. Such forward and explicit discretizations can be slow and unstable, requiring a large number of sampling steps to produce good-quality samples. In this work we develop a text-to-image (T2I) diffusion model based on backward discretizations, dubbed ProxT2I, relying on learned and conditional proximal operators instead of score functions. We further leverage recent advances in reinforcement learning and policy optimization to optimize our samplers for task-specific rewards. Additionally, we develop a new large-scale and open-source dataset comprising 15 million high-quality human images with fine-grained captions, called LAION-Face-T2I-15M, for training and evaluation. Our approach consistently enhances sampling efficiency and human-preference alignment compared to score-based baselines, and achieves results on par with existing state-of-the-art and open-source text-to-image models while requiring lower compute and smaller model size, offering a lightweight yet performant solution for human text-to-image generation.

