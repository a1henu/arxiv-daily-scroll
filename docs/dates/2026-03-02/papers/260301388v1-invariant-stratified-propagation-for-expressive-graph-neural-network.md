---
layout: default
title: Invariant-Stratified Propagation for Expressive Graph Neural Networks
---

# Invariant-Stratified Propagation for Expressive Graph Neural Networks
**arXiv**：[2603.01388v1](https://arxiv.org/abs/2603.01388) · [PDF](https://arxiv.org/pdf/2603.01388.pdf)  
**作者**：Asela Hevapathige, Ahad N. Zehmakan, Asiri Wijesinghe, Saman Halgamuge  

**一句话要点**：提出不变分层传播框架以增强图神经网络表达力并捕获结构异质性

**关键词**：图神经网络, 表达力增强, 结构异质性, 不变分层传播, 图分类, 节点分类

## 3 点简述
- 标准GNN受限于1-WL测试，无法区分高阶结构模式
- ISP通过分层处理节点，编码结构异质性，提升表达力
- 实验在分类和估计任务中优于基准方法，理论分析支持

## 摘要（原文）

> Graph Neural Networks (GNNs) face fundamental limitations in expressivity and capturing structural heterogeneity. Standard message-passing architectures are constrained by the 1-dimensional Weisfeiler-Leman (1-WL) test, unable to distinguish graphs beyond degree sequences, and aggregate information uniformly from neighbors, failing to capture how nodes occupy different structural positions within higher-order patterns. While methods exist to achieve higher expressivity, they incur prohibitive computational costs and lack unified frameworks for flexibly encoding diverse structural properties. To address these limitations, we introduce Invariant-Stratified Propagation (ISP), a framework comprising both a novel WL variant (ISP-WL) and its efficient neural network implementation (ISPGNN). ISP stratifies nodes according to graph invariants, processing them in hierarchical strata that reveal structural distinctions invisible to 1-WL. Through hierarchical structural heterogeneity encoding, ISP quantifies differences in nodes' structural positions within higher-order patterns, distinguishing interactions where participants occupy different roles from those with uniform participation. We provide formal theoretical analysis establishing enhanced expressivity beyond 1-WL, convergence guarantees, and inherent resistance to oversmoothing. Extensive experiments across graph classification, node classification, and influence estimation demonstrate consistent improvements over standard architectures and state-of-the-art expressive baselines.

