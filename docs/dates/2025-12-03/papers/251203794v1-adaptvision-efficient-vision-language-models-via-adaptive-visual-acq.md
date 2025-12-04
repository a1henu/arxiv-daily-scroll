---
layout: default
title: AdaptVision: Efficient Vision-Language Models via Adaptive Visual Acquisition
---

# AdaptVision: Efficient Vision-Language Models via Adaptive Visual Acquisition
**arXiv**：[2512.03794v1](https://arxiv.org/abs/2512.03794) · [PDF](https://arxiv.org/pdf/2512.03794.pdf)  
**作者**：Zichuan Lin, Yicheng Liu, Yang Yang, Lvfang Tao, Deheng Ye  

**一句话要点**：提出AdaptVision，通过自适应视觉获取解决视觉语言模型计算开销大的问题。

**关键词**：视觉语言模型, 自适应视觉获取, 强化学习, 解耦策略优化, 视觉问答

## 3 点简述
- 核心问题：现有高效VLM方法采用固定压缩比，无法根据任务需求自适应调整视觉令牌数量。
- 方法要点：引入粗到细的自适应视觉令牌获取机制，结合强化学习框架和解耦策略优化。
- 实验或效果：在多个VQA基准测试中，以更少视觉令牌实现优于现有高效方法的性能。

## 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable success in visual question answering tasks, but their reliance on large numbers of visual tokens introduces significant computational overhead. While existing efficient VLM approaches reduce visual tokens through fixed-ratio compression, they operate passively and lack the ability to adapt to varying task requirements. This motivates a fundamental question: Can VLMs autonomously determine the minimum number of visual tokens required for each sample? Inspired by human active vision mechanisms, we introduce AdaptVision, an efficient VLM paradigm that enables adaptive visual token acquisition through a coarse-to-fine approach. Our model initially processes compressed visual tokens from low-resolution images and selectively acquires additional visual information by invoking a bounding box tool to crop key regions when necessary. We train AdaptVision using a reinforcement learning framework that carefully balances accuracy and efficiency. Central to our approach is Decoupled Turn Policy Optimization (DTPO), which decouples the learning objective into two components: (1) tool learning, which optimizes correct tool utilization, and (2) accuracy improvement, which refines the generated responses to improve answer correctness. Based on this formulation, we further decouple advantage estimation by computing separate advantages for tokens associated with each objective. This formulation enables more effective optimization for AdaptVision compared to vanilla GRPO. Comprehensive experiments across multiple VQA benchmarks demonstrate that AdaptVision achieves superior performance while consuming substantially fewer visual tokens than state-of-the-art efficient VLM methods.

