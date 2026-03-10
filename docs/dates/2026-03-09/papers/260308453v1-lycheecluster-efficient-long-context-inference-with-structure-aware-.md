---
layout: default
title: LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing
---

# LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing
**arXiv**：[2603.08453v1](https://arxiv.org/abs/2603.08453) · [PDF](https://arxiv.org/pdf/2603.08453.pdf)  
**作者**：Dongfang Li, Zixuan Liu, Gang Lin, Baotian Hu, Min Zhang  

**一句话要点**：提出LycheeCluster方法，通过结构感知分块和层次化KV索引优化长上下文推理效率

**关键词**：长上下文推理, KV缓存管理, 结构感知分块, 层次化索引, 高效推理, 大语言模型

## 3 点简述
- 核心问题：注意力机制二次复杂度和KV缓存内存占用导致长上下文推理计算和内存挑战
- 方法要点：采用边界感知分块保持语义连贯性，基于三角不等式构建递归层次索引实现对数时间检索
- 实验或效果：实验显示端到端推理速度提升最高3.6倍，模型性能下降可忽略，优于现有方法

## 摘要（原文）

> The quadratic complexity of the attention mechanism and the substantial memory footprint of the Key-Value (KV) cache present severe computational and memory challenges for Large Language Models (LLMs) processing long contexts. Existing retrieval-based methods often compromise semantic integrity through fixed-size chunking and suffer from inefficient linear scanning. In this paper, we propose LycheeCluster, a novel method for efficient KV cache management. LycheeCluster preserves local semantic coherence via boundary-aware chunking and constructs a recursive hierarchical index rooted in the triangle inequality. This design transforms cache retrieval from a linear scan into a theoretically bounded, logarithmic-time pruning process, while a lazy update strategy supports efficient streaming generation. Experiments demonstrate that LycheeCluster achieves up to a 3.6x end-to-end inference speedup with negligible degradation in model performance, outperforming state-of-the-art KV cache management methods (e.g., Quest, ClusterKV). We will release our code and kernels after publication.

