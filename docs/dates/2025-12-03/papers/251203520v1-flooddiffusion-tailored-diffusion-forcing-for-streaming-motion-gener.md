---
layout: default
title: FloodDiffusion: Tailored Diffusion Forcing for Streaming Motion Generation
---

# FloodDiffusion: Tailored Diffusion Forcing for Streaming Motion Generation
**arXiv**：[2512.03520v1](https://arxiv.org/abs/2512.03520) · [PDF](https://arxiv.org/pdf/2512.03520.pdf)  
**作者**：Yiyi Cai, Yuhan Wu, Kunhang Li, You Zhou, Bo Zheng, Haiyang Liu  

**一句话要点**：提出FloodDiffusion框架，通过定制扩散强制实现文本驱动的流式人体运动生成

**关键词**：流式运动生成, 扩散模型, 文本驱动, 时间序列生成, 人体运动

## 3 点简述
- 核心问题：现有方法在时变文本提示下生成流式运动时，难以保证实时延迟和分布建模准确性
- 方法要点：采用扩散强制框架，定制双向注意力、下三角时间调度器和连续文本条件引入
- 实验或效果：在HumanML3D基准上达到FID 0.057，实现最先进性能

## 摘要（原文）

> We present FloodDiffusion, a new framework for text-driven, streaming human motion generation. Given time-varying text prompts, FloodDiffusion generates text-aligned, seamless motion sequences with real-time latency. Unlike existing methods that rely on chunk-by-chunk or auto-regressive model with diffusion head, we adopt a diffusion forcing framework to model this time-series generation task under time-varying control events. We find that a straightforward implementation of vanilla diffusion forcing (as proposed for video models) fails to model real motion distributions. We demonstrate that to guarantee modeling the output distribution, the vanilla diffusion forcing must be tailored to: (i) train with a bi-directional attention instead of casual attention; (ii) implement a lower triangular time scheduler instead of a random one; (iii) utilize a continues time-varying way to introduce text conditioning. With these improvements, we demonstrate in the first time that the diffusion forcing-based framework achieves state-of-the-art performance on the streaming motion generation task, reaching an FID of 0.057 on the HumanML3D benchmark. Models, code, and weights are available. https://shandaai.github.io/FloodDiffusion/

