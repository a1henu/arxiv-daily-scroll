---
layout: default
title: SoundWeaver: Semantic Warm-Starting for Text-to-Audio Diffusion Serving
---

# SoundWeaver: Semantic Warm-Starting for Text-to-Audio Diffusion Serving
**arXiv**：[2603.07865v1](https://arxiv.org/abs/2603.07865) · [PDF](https://arxiv.org/pdf/2603.07865.pdf)  
**作者**：Ayush Barik, Sofia Stoica, Nikhil Sarda, Arnav Kethana, Abhinav Khanduja, Muchen Xu, Fan Lai  

**一句话要点**：提出SoundWeaver系统，通过语义预热加速文本到音频扩散模型的服务性能

**关键词**：文本到音频生成, 扩散模型加速, 语义缓存, 服务系统, 训练无关优化

## 3 点简述
- 核心问题：文本到音频扩散模型推理延迟高，影响实时应用
- 方法要点：基于语义相似缓存音频进行训练无关的预热启动，减少函数评估次数
- 实验或效果：在真实音频轨迹上，实现1.8-3.0倍延迟降低，保持或提升感知质量

## 摘要（原文）

> Text-to-audio diffusion models produce high-fidelity audio but require tens of function evaluations (NFEs), incurring multi-second latency and limited throughput. We present SoundWeaver, the first training-free, model-agnostic serving system that accelerates text-to-audio diffusion by warm-starting from semantically similar cached audio. SoundWeaver introduces three components: a Reference Selector that retrieves and temporally aligns cached candidates via semantic and duration-aware gating; a Skip Gater that dynamically determines the percentage of NFEs to skip; and a lightweight Cache Manager that maintains cache utility through quality-aware eviction and refinement. On real-world audio traces, SoundWeaver achieves 1.8--3.0$ \times $ latency reduction with a cache of only ${\sim}$1K entries while preserving or improving perceptual quality.

