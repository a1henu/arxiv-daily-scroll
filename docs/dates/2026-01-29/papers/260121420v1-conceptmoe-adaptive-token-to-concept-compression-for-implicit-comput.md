---
layout: default
title: ConceptMoE: Adaptive Token-to-Concept Compression for Implicit Compute Allocation
---

# ConceptMoE: Adaptive Token-to-Concept Compression for Implicit Compute Allocation
**arXiv**：[2601.21420v1](https://arxiv.org/abs/2601.21420) · [PDF](https://arxiv.org/pdf/2601.21420.pdf)  
**作者**：Zihao Huang, Jundong Zhou, Xingwei Qu, Qiyang Min, Ge Zhang  

**一句话要点**：提出ConceptMoE以通过自适应令牌到概念压缩实现隐式计算分配，提升大语言模型效率与性能。

**关键词**：令牌压缩, 混合专家模型, 计算分配, 长上下文理解, 多模态基准, 效率优化

## 3 点简述
- 大语言模型对所有令牌分配均匀计算，忽略序列可预测性差异，导致计算浪费。
- ConceptMoE动态合并语义相似令牌为概念表示，通过可学习分块模块压缩序列，实现隐式令牌级计算分配。
- 在匹配基线FLOPs和参数条件下，ConceptMoE在语言和视觉语言任务中优于标准MoE，并显著减少注意力和KV缓存计算。

## 摘要（原文）

> Large language models allocate uniform computation across all tokens, ignoring that some sequences are trivially predictable while others require deep reasoning. We introduce ConceptMoE, which dynamically merges semantically similar tokens into concept representations, performing implicit token-level compute allocation. A learnable chunk module identifies optimal boundaries by measuring inter-token similarity, compressing sequences by a target ratio $R$ before they enter the compute-intensive concept model. Crucially, the MoE architecture enables controlled evaluation: we reallocate saved computation to match baseline activated FLOPs (excluding attention map computation) and total parameters, isolating genuine architectural benefits. Under these conditions, ConceptMoE consistently outperforms standard MoE across language and vision-language tasks, achieving +0.9 points on language pretraining, +2.3 points on long context understanding, and +0.6 points on multimodal benchmarks. When converting pretrained MoE during continual training with layer looping, gains reach +5.5 points, demonstrating practical applicability. Beyond performance, ConceptMoE reduces attention computation by up to $R^2\times$ and KV cache by $R\times$. At $R=2$, empirical measurements show prefill speedups reaching 175\% and decoding speedups up to 117\% on long sequences. The minimal architectural modifications enable straightforward integration into existing MoE, demonstrating that adaptive concept-level processing fundamentally improves both effectiveness and efficiency of large language models.

