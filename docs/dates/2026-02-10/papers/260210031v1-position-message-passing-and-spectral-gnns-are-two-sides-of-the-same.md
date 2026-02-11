---
layout: default
title: Position: Message-passing and spectral GNNs are two sides of the same coin
---

# Position: Message-passing and spectral GNNs are two sides of the same coin
**arXiv**：[2602.10031v1](https://arxiv.org/abs/2602.10031) · [PDF](https://arxiv.org/pdf/2602.10031.pdf)  
**作者**：Antonis Vasileiou, Juan Cervino, Pascal Frossard, Charilaos I. Kanatsoulis, Christopher Morris, Michael T. Schaub, Pierre Vandergheynst, Zhiyang Wang, Guy Wolf, Ron Levie  

**一句话要点**：提出统一视角，将消息传递与谱图神经网络视为图信号置换等变算子的不同参数化

**关键词**：图神经网络, 消息传递神经网络, 谱图神经网络, 置换等变性, 图信号处理, 理论统一

## 3 点简述
- 核心问题：消息传递与谱图神经网络的分割阻碍图学习进展，需统一理论框架
- 方法要点：基于置换等变算子视角，分析两者表达力等价性与互补优势
- 实验或效果：未知，但强调理论分析促进领域加速发展

## 摘要（原文）

> Graph neural networks (GNNs) are commonly divided into message-passing neural networks (MPNNs) and spectral graph neural networks, reflecting two largely separate research traditions in machine learning and signal processing. This paper argues that this divide is mostly artificial, hindering progress in the field. We propose a viewpoint in which both MPNNs and spectral GNNs are understood as different parametrizations of permutation-equivariant operators acting on graph signals. From this perspective, many popular architectures are equivalent in expressive power, while genuine gaps arise only in specific regimes. We further argue that MPNNs and spectral GNNs offer complementary strengths. That is, MPNNs provide a natural language for discrete structure and expressivity analysis using tools from logic and graph isomorphism research, while the spectral perspective provides principled tools for understanding smoothing, bottlenecks, stability, and community structure. Overall, we posit that progress in graph learning will be accelerated by clearly understanding the key similarities and differences between these two types of GNNs, and by working towards unifying these perspectives within a common theoretical and conceptual framework rather than treating them as competing paradigms.

