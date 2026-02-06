---
layout: default
title: SDFP: Speculative Decoding with FIT-Pruned Models for Training-Free and Plug-and-Play LLM Acceleration
---

# SDFP: Speculative Decoding with FIT-Pruned Models for Training-Free and Plug-and-Play LLM Acceleration
**arXiv**：[2602.05499v1](https://arxiv.org/abs/2602.05499) · [PDF](https://arxiv.org/pdf/2602.05499.pdf)  
**作者**：Hanyu Wei, Zunhai Su, Peng Lu, Chao Li, Spandan Tiwari, Ashish Sirasao, Yuhan Dong  

**一句话要点**：提出SDFP框架，通过FIT剪层构建草稿模型，实现免训练、即插即用的LLM加速

**关键词**：推测解码, 模型剪枝, Fisher信息迹, 免训练加速, 即插即用框架, 多媒体应用

## 3 点简述
- 核心问题：LLM自回归解码延迟高，现有推测解码方法需额外训练或复杂优化，部署成本高
- 方法要点：基于Fisher信息迹剪除低影响层，构建紧凑草稿模型，保持与原始模型兼容性
- 实验或效果：在基准测试中实现1.32-1.5倍解码加速，不改变输出分布，支持低延迟多媒体应用

## 摘要（原文）

> Large language models (LLMs) underpin interactive multimedia applications such as captioning, retrieval, recommendation, and creative content generation, yet their autoregressive decoding incurs substantial latency. Speculative decoding reduces latency using a lightweight draft model, but deployment is often limited by the cost and complexity of acquiring, tuning, and maintaining an effective draft model. Recent approaches usually require auxiliary training or specialization, and even training-free methods incur costly search or optimization. We propose SDFP, a fully training-free and plug-and-play framework that builds the draft model via Fisher Information Trace (FIT)-based layer pruning of a given LLM. Using layer sensitivity as a proxy for output perturbation, SDFP removes low-impact layers to obtain a compact draft while preserving compatibility with the original model for standard speculative verification. SDFP needs no additional training, hyperparameter tuning, or separately maintained drafts, enabling rapid, deployment-friendly draft construction. Across benchmarks, SDFP delivers 1.32x-1.5x decoding speedup without altering the target model's output distribution, supporting low-latency multimedia applications.

