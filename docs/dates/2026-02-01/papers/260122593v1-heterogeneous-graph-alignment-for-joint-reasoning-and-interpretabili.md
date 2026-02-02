---
layout: default
title: Heterogeneous Graph Alignment for Joint Reasoning and Interpretability
---

# Heterogeneous Graph Alignment for Joint Reasoning and Interpretability
**arXiv**：[2601.22593v1](https://arxiv.org/abs/2601.22593) · [PDF](https://arxiv.org/pdf/2601.22593.pdf)  
**作者**：Zahra Moslemi, Ziyi Liang, Norbert Fortin, Babak Shahbaba  

**一句话要点**：提出多图元变换器以解决异构图对齐与联合推理问题

**关键词**：异构图对齐, 多图学习, 图变换器, 元图构建, 可解释性, 神经科学应用

## 3 点简述
- 核心问题：异构图在拓扑、规模和语义上差异大，缺乏共享节点身份，信息整合困难。
- 方法要点：使用图变换器编码，构建元图连接功能对齐超节点，实现跨图联合推理。
- 实验或效果：在合成和真实神经科学数据上，MGMT在预测任务中优于现有模型，并提供可解释表示。

## 摘要（原文）

> Multi-graph learning is crucial for extracting meaningful signals from collections of heterogeneous graphs. However, effectively integrating information across graphs with differing topologies, scales, and semantics, often in the absence of shared node identities, remains a significant challenge. We present the Multi-Graph Meta-Transformer (MGMT), a unified, scalable, and interpretable framework for cross-graph learning. MGMT first applies Graph Transformer encoders to each graph, mapping structure and attributes into a shared latent space. It then selects task-relevant supernodes via attention and builds a meta-graph that connects functionally aligned supernodes across graphs using similarity in the latent space. Additional Graph Transformer layers on this meta-graph enable joint reasoning over intra- and inter-graph structure. The meta-graph provides built-in interpretability: supernodes and superedges highlight influential substructures and cross-graph alignments. Evaluating MGMT on both synthetic datasets and real-world neuroscience applications, we show that MGMT consistently outperforms existing state-of-the-art models in graph-level prediction tasks while offering interpretable representations that facilitate scientific discoveries. Our work establishes MGMT as a unified framework for structured multi-graph learning, advancing representation techniques in domains where graph-based data plays a central role.

