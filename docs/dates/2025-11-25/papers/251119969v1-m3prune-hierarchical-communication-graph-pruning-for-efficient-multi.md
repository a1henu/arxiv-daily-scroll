---
layout: default
title: M$^3$Prune: Hierarchical Communication Graph Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation
---

# M$^3$Prune: Hierarchical Communication Graph Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation
**arXiv**：[2511.19969v1](https://arxiv.org/abs/2511.19969) · [PDF](https://arxiv.org/pdf/2511.19969.pdf)  
**作者**：Weizi Shao, Taolin Zhang, Zijie Zhou, Chen Chen, Chengyu Wang, Xiaofeng He  

**一句话要点**：提出M³Prune框架以优化多模态多代理检索增强生成的通信效率

**关键词**：多模态检索增强生成, 多代理系统, 图剪枝, 通信优化, 令牌效率

## 3 点简述
- 核心问题：多代理系统存在高令牌开销和计算成本，阻碍大规模部署。
- 方法要点：通过层次化图剪枝，去除冗余边，平衡性能与开销。
- 实验效果：在多个基准测试中优于单代理和多代理系统，显著减少令牌消耗。

## 摘要（原文）

> Recent advancements in multi-modal retrieval-augmented generation (mRAG), which enhance multi-modal large language models (MLLMs) with external knowledge, have demonstrated that the collective intelligence of multiple agents can significantly outperform a single model through effective communication. Despite impressive performance, existing multi-agent systems inherently incur substantial token overhead and increased computational costs, posing challenges for large-scale deployment. To address these issues, we propose a novel Multi-Modal Multi-agent hierarchical communication graph PRUNING framework, termed M$^3$Prune. Our framework eliminates redundant edges across different modalities, achieving an optimal balance between task performance and token overhead. Specifically, M$^3$Prune first applies intra-modal graph sparsification to textual and visual modalities, identifying the edges most critical for solving the task. Subsequently, we construct a dynamic communication topology using these key edges for inter-modal graph sparsification. Finally, we progressively prune redundant edges to obtain a more efficient and hierarchical topology. Extensive experiments on both general and domain-specific mRAG benchmarks demonstrate that our method consistently outperforms both single-agent and robust multi-agent mRAG systems while significantly reducing token consumption.

