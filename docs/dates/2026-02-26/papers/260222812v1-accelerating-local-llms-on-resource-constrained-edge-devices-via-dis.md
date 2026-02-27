---
layout: default
title: Accelerating Local LLMs on Resource-Constrained Edge Devices via Distributed Prompt Caching
---

# Accelerating Local LLMs on Resource-Constrained Edge Devices via Distributed Prompt Caching
**arXiv**：[2602.22812v1](https://arxiv.org/abs/2602.22812) · [PDF](https://arxiv.org/pdf/2602.22812.pdf)  
**作者**：Hiroki Matsutani, Naoki Matsuda, Naoto Sugiura  

**一句话要点**：提出分布式提示缓存以加速资源受限边缘设备上的本地LLM推理

**关键词**：边缘计算, 大语言模型推理, 分布式缓存, 提示优化, 资源受限设备

## 3 点简述
- 核心问题：本地LLM推理在资源受限边缘设备上存在严重性能瓶颈
- 方法要点：通过分布式缓存共享中间处理状态，支持部分匹配以减少通信开销
- 实验或效果：在Raspberry Pi Zero 2W平台上，TTFT和TTLT平均降低93.12%和50.07%

## 摘要（原文）

> Since local LLM inference on resource-constrained edge devices imposes a severe performance bottleneck, this paper proposes distributed prompt caching to enhance inference performance by cooperatively sharing intermediate processing states across multiple low-end edge devices. To fully utilize prompt similarity, our distributed caching mechanism also supports partial matching. As this approach introduces communication overhead associated with state sharing over a wireless network, we introduce a Bloom-filter-based data structure, referred to as a catalog, to determine whether a remote server possesses the desired internal states, thereby suppressing unnecessary communication. Experiments using the Gemma-3 270M model and the MMLU dataset on the Raspberry Pi Zero 2W platform demonstrate that the proposed approach reduces TTFT (Time to First Token) and TTLT (Time to Last Token) by 93.12% and 50.07% on average, respectively.

