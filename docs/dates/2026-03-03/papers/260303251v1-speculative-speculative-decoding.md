---
layout: default
title: Speculative Speculative Decoding
---

# Speculative Speculative Decoding
**arXiv**：[2603.03251v1](https://arxiv.org/abs/2603.03251) · [PDF](https://arxiv.org/pdf/2603.03251.pdf)  
**作者**：Tanishq Kumar, Tri Dao, Avner May  

**一句话要点**：提出推测性推测解码以并行化推测与验证，加速自回归解码

**关键词**：推测解码, 并行推理, 自回归加速, 草稿模型, 验证预测, Saguaro算法

## 3 点简述
- 核心问题：推测解码中推测与验证的序列依赖成为新瓶颈
- 方法要点：在验证进行时，草稿模型预测验证结果并预准备推测
- 实验或效果：Saguaro算法比优化推测解码快达2倍，比自回归解码快达5倍

## 摘要（原文）

> Autoregressive decoding is bottlenecked by its sequential nature. Speculative decoding has become a standard way to accelerate inference by using a fast draft model to predict upcoming tokens from a slower target model, and then verifying them in parallel with a single target model forward pass. However, speculative decoding itself relies on a sequential dependence between speculation and verification. We introduce speculative speculative decoding (SSD) to parallelize these operations. While a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them. If the actual verification outcome is then in the predicted set, a speculation can be returned immediately, eliminating drafting overhead entirely. We identify three key challenges presented by speculative speculative decoding, and suggest principled methods to solve each. The result is Saguaro, an optimized SSD algorithm. Our implementation is up to 2x faster than optimized speculative decoding baselines and up to 5x faster than autoregressive decoding with open source inference engines.

