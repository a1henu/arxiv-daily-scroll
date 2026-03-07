---
layout: default
title: InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context
---

# InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context
**arXiv**：[2603.05353v1](https://arxiv.org/abs/2603.05353) · [PDF](https://arxiv.org/pdf/2603.05353.pdf)  
**作者**：Xin Teng, Canyu Zhang, Shaoyi Zheng, Danyang Zhuo, Tianyi Zhou, Shengjie Wang  

**一句话要点**：提出信息流感知的KV重计算以优化长上下文检索增强生成的推理效率

**关键词**：检索增强生成, KV缓存, 长上下文处理, 信息流建模, 推理优化, 注意力机制

## 3 点简述
- 核心问题：长上下文问答中，推理时对大检索上下文进行预填充成为瓶颈，现有KV重计算方法依赖启发式或表示差异，未建模所选令牌是否能有效影响生成。
- 方法要点：将选择性KV重计算建模为信息流问题，利用查询的注意力范数信号在推理一致的RoPE几何下识别语义相关且结构上能传播信息的令牌，并引入信息流引导的块重排序策略。
- 实验或效果：在LLM和VLM基准测试中，在可比效率预算下，相比先前方法实现了一致的性能提升。

## 摘要（原文）

> Retrieval-augmented generation (RAG) for long-context question answering is bottlenecked by inference-time prefilling over large retrieved contexts. A common strategy is to precompute key-value (KV) caches for individual documents and selectively recompute a small subset of tokens to restore global causal dependencies, but existing methods rely on heuristics or representation discrepancies without modeling whether selected tokens can effectively influence generation. We cast selective KV recomputation as an information flow problem and show that a simple attention-norm signal from the query reliably identifies tokens that are both semantically relevant and structurally positioned to propagate information, when computed under an inference-consistent RoPE geometry. We therefore reconstruct global positional assignments for retrieved chunks and introduce an information-flow-guided chunk reordering strategy. Experiments on LLM and VLM benchmarks demonstrate consistent gains over prior methods under comparable efficiency budgets.

