---
layout: default
title: MemAdapter: Fast Alignment across Agent Memory Paradigms via Generative Subgraph Retrieval
---

# MemAdapter: Fast Alignment across Agent Memory Paradigms via Generative Subgraph Retrieval
**arXiv**：[2602.08369v1](https://arxiv.org/abs/2602.08369) · [PDF](https://arxiv.org/pdf/2602.08369.pdf)  
**作者**：Xin Zhang, Kailai Yang, Chenyue Li, Hao Li, Qiyu Wei, Jun'ichi Tsujii, Sophia Ananiadou  

**一句话要点**：提出MemAdapter框架，通过生成式子图检索实现跨代理内存范式的快速对齐

**关键词**：代理内存系统, 生成式子图检索, 跨范式对齐, 对比学习, 轻量对齐模块, 零样本融合

## 3 点简述
- 核心问题：现有代理内存系统范式孤立，检索方法紧耦合，阻碍跨范式泛化与融合
- 方法要点：采用两阶段训练策略，包括统一内存空间训练生成式子图检索器和轻量对齐模块适应新范式
- 实验或效果：在三个基准测试中优于五种强基线，跨范式对齐仅需13分钟，计算成本低于5%

## 摘要（原文）

> Memory mechanism is a core component of LLM-based agents, enabling reasoning and knowledge discovery over long-horizon contexts. Existing agent memory systems are typically designed within isolated paradigms (e.g., explicit, parametric, or latent memory) with tightly coupled retrieval methods that hinder cross-paradigm generalization and fusion. In this work, we take a first step toward unifying heterogeneous memory paradigms within a single memory system. We propose MemAdapter, a memory retrieval framework that enables fast alignment across agent memory paradigms. MemAdapter adopts a two-stage training strategy: (1) training a generative subgraph retriever from the unified memory space, and (2) adapting the retriever to unseen memory paradigms by training a lightweight alignment module through contrastive learning. This design improves the flexibility for memory retrieval and substantially reduces alignment cost across paradigms. Comprehensive experiments on three public evaluation benchmarks demonstrate that the generative subgraph retriever consistently outperforms five strong agent memory systems across three memory paradigms and agent model scales. Notably, MemAdapter completes cross-paradigm alignment within 13 minutes on a single GPU, achieving superior performance over original memory retrievers with less than 5% of training compute. Furthermore, MemAdapter enables effective zero-shot fusion across memory paradigms, highlighting its potential as a plug-and-play solution for agent memory systems.

