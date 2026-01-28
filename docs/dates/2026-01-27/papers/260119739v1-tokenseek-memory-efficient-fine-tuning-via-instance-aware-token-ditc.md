---
layout: default
title: TokenSeek: Memory Efficient Fine Tuning via Instance-Aware Token Ditching
---

# TokenSeek: Memory Efficient Fine Tuning via Instance-Aware Token Ditching
**arXiv**：[2601.19739v1](https://arxiv.org/abs/2601.19739) · [PDF](https://arxiv.org/pdf/2601.19739.pdf)  
**作者**：Runjia Zeng, Qifan Wang, Qiang Guan, Ruixiang Tang, Lifu Huang, Zhenting Wang, Xueling Zhang, Cheng Han, Dongfang Liu  

**一句话要点**：提出TokenSeek插件，通过实例感知的令牌丢弃，实现大语言模型微调的内存高效化。

**关键词**：大语言模型微调, 内存优化, 令牌丢弃, Transformer模型, 激活压缩

## 3 点简述
- 核心问题：大语言模型微调中激活内存消耗高，现有数据无关优化方法效果不稳定。
- 方法要点：基于实例感知动态选择并丢弃令牌，减少激活内存，适用于多种Transformer模型。
- 实验或效果：在Llama3.2 1B等模型上，内存节省显著（如仅需14.8%内存），性能持平或更优。

## 摘要（原文）

> Fine tuning has been regarded as a de facto approach for adapting large language models (LLMs) to downstream tasks, but the high training memory consumption inherited from LLMs makes this process inefficient. Among existing memory efficient approaches, activation-related optimization has proven particularly effective, as activations consistently dominate overall memory consumption. Although prior arts offer various activation optimization strategies, their data-agnostic nature ultimately results in ineffective and unstable fine tuning. In this paper, we propose TokenSeek, a universal plugin solution for various transformer-based models through instance-aware token seeking and ditching, achieving significant fine-tuning memory savings (e.g., requiring only 14.8% of the memory on Llama3.2 1B) with on-par or even better performance. Furthermore, our interpretable token seeking process reveals the underlying reasons for its effectiveness, offering valuable insights for future research on token efficiency. Homepage: https://runjia.tech/iclr_tokenseek/

