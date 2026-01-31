---
layout: default
title: MemOCR: Layout-Aware Visual Memory for Efficient Long-Horizon Reasoning
---

# MemOCR: Layout-Aware Visual Memory for Efficient Long-Horizon Reasoning
**arXiv**：[2601.21468v1](https://arxiv.org/abs/2601.21468) · [PDF](https://arxiv.org/pdf/2601.21468.pdf)  
**作者**：Yaorui Shi, Shugui Liu, Yu Yang, Wenyu Mao, Yuxin Chen, Qi GU, Hui Su, Xunliang Cai, Xiang Wang, An Zhang  

**一句话要点**：提出MemOCR，通过视觉布局自适应分配内存空间，以提升有限上下文预算下的长时程推理效率。

**关键词**：长时程推理, 视觉内存, 自适应压缩, 强化学习训练, 多模态智能体, 上下文预算优化

## 3 点简述
- 核心问题：长时程智能体推理需压缩交互历史，但现有文本内存系统均匀分配令牌成本，浪费预算于低价值细节。
- 方法要点：MemOCR维护结构化富文本内存，渲染为图像供智能体访问，视觉优先关键证据并压缩辅助细节。
- 实验或效果：在长上下文多跳和单跳问答基准上，MemOCR优于文本基线，在极端预算下实现更有效的上下文利用。

## 摘要（原文）

> Long-horizon agentic reasoning necessitates effectively compressing growing interaction histories into a limited context window. Most existing memory systems serialize history as text, where token-level cost is uniform and scales linearly with length, often spending scarce budget on low-value details. To this end, we introduce MemOCR, a multimodal memory agent that improves long-horizon reasoning under tight context budgets by allocating memory space with adaptive information density through visual layout. Concretely, MemOCR maintains a structured rich-text memory (e.g., headings, highlights) and renders it into an image that the agent consults for memory access, visually prioritizing crucial evidence while aggressively compressing auxiliary details. To ensure robustness across varying memory budgets, we train MemOCR with reinforcement learning under budget-aware objectives that expose the agent to diverse compression levels. Across long-context multi-hop and single-hop question-answering benchmarks, MemOCR outperforms strong text-based baselines and achieves more effective context utilization under extreme budgets.

