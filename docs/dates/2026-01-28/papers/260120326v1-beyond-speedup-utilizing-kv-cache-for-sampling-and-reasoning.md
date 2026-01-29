---
layout: default
title: Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning
---

# Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning
**arXiv**：[2601.20326v1](https://arxiv.org/abs/2601.20326) · [PDF](https://arxiv.org/pdf/2601.20326.pdf)  
**作者**：Zeyu Xing, Xing Li, Hui-Ling Zhen, Mingxuan Yuan, Sinno Jialin Pan  

**一句话要点**：提出将KV缓存作为轻量级表征，用于采样和推理任务，无需额外计算成本。

**关键词**：KV缓存, 表征复用, 采样推理, 轻量级表征, LLM推理优化

## 3 点简述
- 核心问题：KV缓存通常仅用于加速自回归解码，其编码的上下文信息未被充分利用。
- 方法要点：将KV缓存视为轻量级表征，避免重新计算或存储完整隐藏状态。
- 实验效果：在嵌入链和快慢思维切换任务中，KV表征实现竞争性性能，最高减少5.7倍token生成。

## 摘要（原文）

> KV caches, typically used only to speed up autoregressive decoding, encode contextual information that can be reused for downstream tasks at no extra cost. We propose treating the KV cache as a lightweight representation, eliminating the need to recompute or store full hidden states. Despite being weaker than dedicated embeddings, KV-derived representations are shown to be sufficient for two key applications: \textbf{(i) Chain-of-Embedding}, where they achieve competitive or superior performance on Llama-3.1-8B-Instruct and Qwen2-7B-Instruct; and \textbf{(ii) Fast/Slow Thinking Switching}, where they enable adaptive reasoning on Qwen3-8B and DeepSeek-R1-Distil-Qwen-14B, reducing token generation by up to $5.7\times$ with minimal accuracy loss. Our findings establish KV caches as a free, effective substrate for sampling and reasoning, opening new directions for representation reuse in LLM inference. Code: https://github.com/cmd2001/ICLR2026_KV-Embedding.

