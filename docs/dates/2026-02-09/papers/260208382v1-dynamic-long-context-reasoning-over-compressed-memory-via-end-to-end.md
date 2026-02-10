---
layout: default
title: Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning
---

# Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning
**arXiv**：[2602.08382v1](https://arxiv.org/abs/2602.08382) · [PDF](https://arxiv.org/pdf/2602.08382.pdf)  
**作者**：Zhuoen Chen, Dongfang Li, Meishan Zhang, Baotian Hu, Min Zhang  

**一句话要点**：提出基于分块压缩与选择性记忆调用的认知启发框架，以解决大语言模型长上下文推理中的效率与遗忘问题。

**关键词**：长上下文推理, 记忆压缩, 强化学习优化, 选择性记忆调用, 多跳推理, 效率提升

## 3 点简述
- 核心问题：大语言模型处理长上下文时面临二次计算成本、信息遗忘和检索增强生成中的上下文碎片化挑战。
- 方法要点：通过分块压缩输入、动态选择相关记忆块，并结合强化学习优化压缩器与推理器，实现高效长上下文推理。
- 实验或效果：在RULER-HQA等基准上达到竞争性准确率，上下文长度从7K扩展到1.75M令牌，相比基线减少GPU内存使用并加速推理。

## 摘要（原文）

> Large Language Models (LLMs) face significant challenges in long-context processing, including quadratic computational costs, information forgetting, and the context fragmentation inherent in retrieval-augmented generation (RAG). We propose a cognitively inspired framework for efficient long-context inference based on chunk-wise compression and selective memory recall, rather than processing all raw tokens. The framework segments long inputs into chunks and encodes each chunk into compressed memory representations using a learned compressor. A gating module dynamically selects relevant memory blocks, which are then iteratively processed by a reasoning module with an evolving working memory to solve downstream tasks. The compressor and reasoner are jointly optimized via end-to-end reinforcement learning, while the gating module is trained separately as a classifier. Experimental results show that the proposed method achieves competitive accuracy on multi-hop reasoning benchmarks such as RULER-HQA, extrapolates context length from 7K to 1.75M tokens, and offers a favorable accuracy-efficiency trade-off compared to strong long-context baselines. In particular, it achieves up to a 2 times reduction in peak GPU memory usage and a 6 times inference speedup over MemAgent.

