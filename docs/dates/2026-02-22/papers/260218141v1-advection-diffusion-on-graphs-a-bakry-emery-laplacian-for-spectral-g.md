---
layout: default
title: Advection-Diffusion on Graphs: A Bakry-Emery Laplacian for Spectral Graph Neural Networks
---

# Advection-Diffusion on Graphs: A Bakry-Emery Laplacian for Spectral Graph Neural Networks
**arXiv**：[2602.18141v1](https://arxiv.org/abs/2602.18141) · [PDF](https://arxiv.org/pdf/2602.18141.pdf)  
**作者**：Pierre-Gabriel Berlureau, Ali Hariri, Victor Kawasaki-Borruat, Mia Zosso, Pierre Vandergheynst  

**一句话要点**：提出Bakry-Emery拉普拉斯算子以解决图神经网络长距离信息传播问题

**关键词**：图神经网络, 谱图学习, 拉普拉斯算子, 长距离推理, 自适应传播, 可解释性

## 3 点简述
- 图神经网络常因过平滑和过压缩而难以长距离传播信息
- 引入可学习节点势的Bakry-Emery拉普拉斯算子，在不改变图结构下实现任务依赖的传播动态
- 基于此开发mu-ChebNet，在合成和真实基准测试中表现优异，提供可解释的信息流路由

## 摘要（原文）

> Graph Neural Networks (GNNs) often struggle to propagate information across long distances due to oversmoothing and oversquashing. Existing remedies such as graph transformers or rewiring typically incur high computational cost or require altering the graph structure. We introduce a Bakry-Emery graph Laplacian that integrates diffusion and advection through a learnable node-wise potential, inducing task-dependent propagation dynamics without modifying topology. This operator has a well-behaved spectral decomposition and acts as a drop-in replacement for standard Laplacians in spectral GNNs. Building on this insight, we develop mu-ChebNet, a spectral architecture that jointly learns the potential and Chebyshev filters, effectively bridging message-passing adaptivity and spectral efficiency. Our theoretical analysis shows how the potential modulates the spectrum, enabling control of key graph properties. Empirically, mu-ChebNet delivers consistent gains on synthetic long-range reasoning tasks, as well as real-world benchmarks, while offering an interpretable routing field that reveals how information flows through the graph. This establishes the Bakry-Emery Laplacian as a principled and efficient foundation for adaptive spectral graph learning.

