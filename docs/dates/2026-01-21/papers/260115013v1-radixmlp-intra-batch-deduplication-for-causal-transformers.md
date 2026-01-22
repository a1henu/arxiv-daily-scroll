---
layout: default
title: RadixMLP -- Intra-batch Deduplication for Causal Transformers
---

# RadixMLP -- Intra-batch Deduplication for Causal Transformers
**arXiv**：[2601.15013v1](https://arxiv.org/abs/2601.15013) · [PDF](https://arxiv.org/pdf/2601.15013.pdf)  
**作者**：Michael Feil, Julius Lipp  

**一句话要点**：提出RadixMLP技术，通过批内去重加速因果Transformer推理

**关键词**：因果Transformer, 批推理优化, 前缀去重, MLP加速, 动态压缩

## 3 点简述
- 问题：因果Transformer批推理中，共享前缀导致MLP激活重复计算，降低效率。
- 方法：利用MLP等组件的逐位置特性，动态构建前缀树压缩共享段，仅在注意力边界散射结果。
- 效果：在MS MARCO v1.1基准测试中，Qwen3模型实现1.44-1.59倍加速，合成基准最高达5倍加速。

## 摘要（原文）

> Batch inference workloads for causal transformer models frequently process sequences that share common prefixes, such as system prompts, few-shot examples, or shared queries. Standard inference engines treat each sequence independently, redundantly recomputing identical MLP activations for every copy of the shared prefix. We introduce RadixMLP, a technique that exploits the position-wise nature of MLPs, LayerNorms, linear projections, and embeddings to eliminate this redundancy. RadixMLP dynamically maps batches to a prefix trie, gathering shared segments into a compressed representation for position-wise computation and scattering results back only at attention boundaries. RadixMLP is stateless and operates within a single forward pass. In end-to-end serving benchmarks on MS~MARCO v1.1 with Qwen3 models (0.6B to 8B parameters), RadixMLP achieves 1.44-1.59$\times$ speedups in realistic reranking workloads, with up to $5\times$ speedups on synthetic benchmarks with longer shared prefixes. Our code is available at https://github.com/michaelfeil/radix-mlp.

