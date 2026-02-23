---
layout: default
title: Unifying approach to uniform expressivity of graph neural networks
---

# Unifying approach to uniform expressivity of graph neural networks
**arXiv**：[2602.18409v1](https://arxiv.org/abs/2602.18409) · [PDF](https://arxiv.org/pdf/2602.18409.pdf)  
**作者**：Huan Luo, Jonni Virtema  

**一句话要点**：提出模板图神经网络统一框架，以分析图神经网络表达能力

**关键词**：图神经网络, 表达能力, 模板框架, 模态逻辑, 统一分析

## 3 点简述
- 核心问题：标准图神经网络表达能力有限，仅聚合邻域或全局信息
- 方法要点：引入模板图神经网络框架，通过模板嵌入聚合提升表达能力
- 实验或效果：建立与模板模态逻辑的等价性，统一分析现有图神经网络变体

## 摘要（原文）

> The expressive power of Graph Neural Networks (GNNs) is often analysed via correspondence to the Weisfeiler-Leman (WL) algorithm and fragments of first-order logic. Standard GNNs are limited to performing aggregation over immediate neighbourhoods or over global read-outs. To increase their expressivity, recent attempts have been made to incorporate substructural information (e.g. cycle counts and subgraph properties). In this paper, we formalize this architectural trend by introducing Template GNNs (T-GNNs), a generalized framework where node features are updated by aggregating over valid template embeddings from a specified set of graph templates. We propose a corresponding logic, Graded template modal logic (GML(T)), and generalized notions of template-based bisimulation and WL algorithm. We establish an equivalence between the expressive power of T-GNNs and GML(T), and provide a unifying approach for analysing GNN expressivity: we show how standard AC-GNNs and its recent variants can be interpreted as instantiations of T-GNNs.

