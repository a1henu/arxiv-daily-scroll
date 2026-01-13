---
layout: default
title: Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference
---

# Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference
**arXiv**：[2601.07667v1](https://arxiv.org/abs/2601.07667) · [PDF](https://arxiv.org/pdf/2601.07667.pdf)  
**作者**：Rei Taniguchi, Yuyang Dong, Makoto Onizuka, Chuan Xiao  

**一句话要点**：提出ASL方法以自适应选择层进行KV缓存剪枝，优化大语言模型推理性能

**关键词**：KV缓存减少, 层间令牌剪枝, 自适应层选择, 大语言模型推理, 注意力机制, 训练免费方法

## 3 点简述
- 核心问题：现有层间令牌剪枝方法使用预定义层，导致任务间准确率波动，在困难任务中性能下降
- 方法要点：ASL基于注意力分数方差自适应选择剪枝层，无需训练，平衡不同任务性能并满足KV缓存预算
- 实验或效果：在InfiniteBench等基准测试中，ASL结合一次性令牌选择优于现有方法，保持解码速度和缓存减少

## 摘要（原文）

> Due to the prevalence of large language models (LLMs), key-value (KV) cache reduction for LLM inference has received remarkable attention. Among numerous works that have been proposed in recent years, layer-wise token pruning approaches, which select a subset of tokens at particular layers to retain in KV cache and prune others, are one of the most popular schemes. They primarily adopt a set of pre-defined layers, at which tokens are selected. Such design is inflexible in the sense that the accuracy significantly varies across tasks and deteriorates in harder tasks such as KV retrieval. In this paper, we propose ASL, a training-free method that adaptively chooses the selection layer for KV cache reduction, exploiting the variance of token ranks ordered by attention score. The proposed method balances the performance across different tasks while meeting the user-specified KV budget requirement. ASL operates during the prefilling stage and can be jointly used with existing KV cache reduction methods such as SnapKV to optimize the decoding stage. By evaluations on the InfiniteBench, RULER, and NIAH benchmarks, we show that equipped with one-shot token selection, where tokens are selected at a layer and propagated to deeper layers, ASL outperforms state-of-the-art layer-wise token selection methods in accuracy while maintaining decoding speed and KV cache reduction.

