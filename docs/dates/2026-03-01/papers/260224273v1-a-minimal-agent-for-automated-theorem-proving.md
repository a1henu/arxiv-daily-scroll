---
layout: default
title: A Minimal Agent for Automated Theorem Proving
---

# A Minimal Agent for Automated Theorem Proving
**arXiv**：[2602.24273v1](https://arxiv.org/abs/2602.24273) · [PDF](https://arxiv.org/pdf/2602.24273.pdf)  
**作者**：Borja Requena Pozo, Austin Letson, Krystian Nowakowski, Izan Beltran Ferreiro, Leopoldo Sarra  

**一句话要点**：提出最小化代理基线以系统比较AI定理证明器架构，实现竞争性能。

**关键词**：定理证明, 代理基线, 迭代精炼, 库搜索, 上下文管理, 开源实现

## 3 点简述
- 核心问题：缺乏系统比较AI定理证明器架构的基准，影响评估与设计选择。
- 方法要点：设计最小化代理，集成迭代证明精炼、库搜索和上下文管理等核心特征。
- 实验或效果：在多样化基准上评估，展示迭代方法在样本效率和成本效益上的优势。

## 摘要（原文）

> We propose a minimal agentic baseline that enables systematic comparison across different AI-based theorem prover architectures. This design implements the core features shared among state-of-the-art systems: iterative proof refinement, library search and context management. We evaluate our baseline using qualitatively different benchmarks and compare various popular models and design choices, and demonstrate competitive performance compared to state-of-the-art approaches, while using a significantly simpler architecture. Our results demonstrate consistent advantages of an iterative approach over multiple single-shot generations, especially in terms of sample efficiency and cost effectiveness. The implementation is released open-source as a candidate reference for future research and as an accessible prover for the community.

