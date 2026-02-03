---
layout: default
title: Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models
---

# Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models
**arXiv**：[2602.02197v1](https://arxiv.org/abs/2602.02197) · [PDF](https://arxiv.org/pdf/2602.02197.pdf)  
**作者**：Xindian Ma, Yidi Lu, Peng Zhang, Jing Zhang  

**一句话要点**：提出分层自适应淘汰框架以优化多模态语言模型中的KV缓存管理

**关键词**：KV缓存管理, 多模态语言模型, 注意力剪枝, 内存优化, 推理加速

## 3 点简述
- 核心问题：Transformer架构的二次内存和计算成本在多模态LLMs中成为瓶颈，现有KV缓存淘汰策略未处理视觉与文本令牌的异构注意力分布。
- 方法要点：HAE框架包括预填充阶段的双注意力剪枝和生成阶段的动态解码淘汰策略，优化文本-视觉令牌交互并减少KV缓存使用。
- 实验或效果：在图像理解任务中减少KV缓存内存41%且精度损失仅0.3%，在故事生成推理中加速1.5倍并保持输出质量。

## 摘要（原文）

> The integration of visual information into Large Language Models (LLMs) has enabled Multimodal LLMs (MLLMs), but the quadratic memory and computational costs of Transformer architectures remain a bottleneck. Existing KV cache eviction strategies fail to address the heterogeneous attention distributions between visual and text tokens, leading to suboptimal efficiency or degraded performance. In this paper, we propose Hierarchical Adaptive Eviction (HAE), a KV cache eviction framework that optimizes text-visual token interaction in MLLMs by implementing Dual-Attention Pruning during pre-filling (leveraging visual token sparsity and attention variance) and a Dynamic Decoding Eviction Strategy (inspired by OS Recycle Bins) during decoding. HAE minimizes KV cache usage across layers, reduces computational overhead via index broadcasting, and theoretically ensures superior information integrity and lower error bounds compared to greedy strategies, enhancing efficiency in both comprehension and generation tasks. Empirically, HAE reduces KV-Cache memory by 41\% with minimal accuracy loss (0.3\% drop) in image understanding tasks and accelerates story generation inference by 1.5x while maintaining output quality on Phi3.5-Vision-Instruct model.

