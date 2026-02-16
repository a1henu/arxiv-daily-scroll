---
layout: default
title: Vision Token Reduction via Attention-Driven Self-Compression for Efficient Multimodal Large Language Models
---

# Vision Token Reduction via Attention-Driven Self-Compression for Efficient Multimodal Large Language Models
**arXiv**：[2602.12618v1](https://arxiv.org/abs/2602.12618) · [PDF](https://arxiv.org/pdf/2602.12618.pdf)  
**作者**：Omer Faruk Deniz, Ruiyu Mao, Ruochen Li, Yapeng Tian, Latifur Khan  

**一句话要点**：提出注意力驱动自压缩方法，以高效压缩多模态大语言模型中的视觉令牌

**关键词**：多模态大语言模型, 视觉令牌压缩, 注意力机制, 计算效率, FlashAttention兼容

## 3 点简述
- 多模态大语言模型处理大量视觉令牌导致高计算成本，现有剪枝方法通用性差或与FlashAttention不兼容
- 利用大语言模型自身注意力机制，在选定层均匀下采样视觉令牌，无需额外计算或修改注意力
- 在LLaVA-1.5上减少53.7% FLOPs和56.7% KV缓存内存，保持98.2%性能，优于先前方法

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) incur significant computational cost from processing numerous vision tokens through all LLM layers. Prior pruning methods operate either before the LLM, limiting generality due to diverse encoder-projector designs or within the LLM using heuristics that are incompatible with FlashAttention. We take a different approach: rather than identifying unimportant tokens, we treat the LLM itself as the optimal guide for compression. Observing that deeper layers naturally transmit vision-to-text information, we introduce Attention-Driven Self-Compression (ADSC), a simple, broadly applicable method that progressively reduces vision tokens using only the LLM's attention mechanism. Our method applies uniform token downsampling at selected layers, forming bottlenecks that encourage the model to reorganize and compress information into the remaining tokens. It requires no score computation, auxiliary modules, or attention modification, and remains fully compatible with FlashAttention. Applied to LLaVA-1.5, ADSC reduces FLOPs by 53.7% and peak KV-cache memory by 56.7%, while preserving 98.2% of the original model performance. Across multiple benchmarks, it outperforms prior pruning approaches in both efficiency and accuracy. Crucially, under high compression ratios, our method remains robust while heuristic-based techniques degrade sharply.

