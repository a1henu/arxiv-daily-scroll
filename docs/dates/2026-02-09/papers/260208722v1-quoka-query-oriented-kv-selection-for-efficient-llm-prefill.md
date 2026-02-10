---
layout: default
title: QUOKA: Query-Oriented KV Selection For Efficient LLM Prefill
---

# QUOKA: Query-Oriented KV Selection For Efficient LLM Prefill
**arXiv**：[2602.08722v1](https://arxiv.org/abs/2602.08722) · [PDF](https://arxiv.org/pdf/2602.08722.pdf)  
**作者**：Dalton Jones, Junyoung Park, Matthew Morse, Mingu Lee, Chris Lott, Harper Langston  

**一句话要点**：提出QUOKA查询导向KV选择算法，以加速分块预填充阶段的Transformer推理

**关键词**：稀疏注意力, Transformer推理加速, 查询导向选择, 分块预填充, 硬件无关算法

## 3 点简述
- 核心问题：Transformer推理中分块预填充阶段注意力计算效率低，需处理大量键值对
- 方法要点：基于查询余弦相似度，优先选择低相似度查询及其对齐键，实现训练无关的稀疏注意力
- 实验或效果：在GPU和CPU上实现3-7倍加速，减少88%键值对使用，保持接近基线准确度

## 摘要（原文）

> We present QUOKA: Query-oriented KV selection for efficient attention, a training-free and hardware agnostic sparse attention algorithm for accelerating transformer inference under chunked prefill. While many queries focus on a smaller group of keys in the attention operator, we observe that queries with low cosine similarity with respect to the mean query interact more strongly with more keys and have the greatest contribution to final attention logits. By prioritizing these low cosine similarity queries, the behavior of full attention during the prefill stage can be closely approximated. QUOKA leverages this observation, accelerating attention by (1) first retaining a small set of representative queries and (2) then subselectin the keys most aligned with those queries. Through experiments on Needle-In-A-Haystack, LongBench, RULER, and Math500, we show that, while realizing a 3x reduction in time-to-first-token, 5x speedup in attention on Nvidia GPUs and up to nearly a 7x speedup on Intel Xeon CPUs, QUOKA achieves near-baseline accuracy, utilizing 88% fewer key-value pairs per attention evaluation.

