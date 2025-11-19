---
layout: default
title: AdaTok: Adaptive Token Compression with Object-Aware Representations for Efficient Multimodal LLMs
---

# AdaTok: Adaptive Token Compression with Object-Aware Representations for Efficient Multimodal LLMs
**arXiv**：[2511.14169v1](https://arxiv.org/abs/2511.14169) · [PDF](https://arxiv.org/pdf/2511.14169.pdf)  
**作者**：Xinliang Zhang, Lei Zhu, Hangzhou He, Shuang Zeng, Ourui Fu, Jiakui Hu, Zhengjian Yao, Yanye Lu  

**一句话要点**：提出自适应令牌压缩方法以解决多模态大模型图像令牌冗余问题

**关键词**：多模态大语言模型, 令牌压缩, 对象感知表示, 计算效率优化, 视觉认知对齐

## 3 点简述
- 核心问题：图像补丁级令牌化导致令牌数量二次增长，增加计算负担和幻觉风险
- 方法要点：采用对象级令牌合并策略，自适应压缩令牌，对齐人类视觉认知
- 实验或效果：在多个基准测试中，平均使用10%令牌实现约96%原模型性能

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated substantial value in unified text-image understanding and reasoning, primarily by converting images into sequences of patch-level tokens that align with their architectural paradigm. However, patch-level tokenization leads to a quadratic growth in image tokens, burdening MLLMs' understanding and reasoning with enormous computation and memory. Additionally, the traditional patch-wise scanning tokenization workflow misaligns with the human vision cognition system, further leading to hallucination and computational redundancy. To address this issue, we propose an object-level token merging strategy for Adaptive Token compression, revealing the consistency with human vision system. The experiments are conducted on multiple comprehensive benchmarks, which show that our approach averagely, utilizes only 10% tokens while achieving almost 96% of the vanilla model's performance. More extensive experimental results in comparison with relevant works demonstrate the superiority of our method in balancing compression ratio and performance. Our code will be available.

