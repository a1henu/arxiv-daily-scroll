---
layout: default
title: $\texttt{lrnnx}$: A library for Linear RNNs
---

# $\texttt{lrnnx}$: A library for Linear RNNs
**arXiv**：[2602.08810v1](https://arxiv.org/abs/2602.08810) · [PDF](https://arxiv.org/pdf/2602.08810.pdf)  
**作者**：Karan Bania, Soham Kalburgi, Manit Tanwar, Dhruthi, Aditya Nagarsekar, Harshvardhan Mestha, Naman Chibber, Raj Deshmukh, Anish Sathyanarayanan, Aarush Rathore, Pratham Chheda  

**一句话要点**：提出lrnnx库以统一实现多种线性循环神经网络架构，提升可访问性和可扩展性。

**关键词**：线性循环神经网络, 序列建模, 软件库, 统一接口, 开源实现

## 3 点简述
- 现有LRNN实现分散且依赖框架特定优化，阻碍使用和比较。
- lrnnx库提供统一接口实现多种现代LRNN架构，支持多级控制。
- 库旨在改善LRNN研究的可访问性、可重复性和可扩展性，代码开源。

## 摘要（原文）

> Linear recurrent neural networks (LRNNs) provide a structured approach to sequence modeling that bridges classical linear dynamical systems and modern deep learning, offering both expressive power and theoretical guarantees on stability and trainability. In recent years, multiple LRNN-based architectures have been proposed, each introducing distinct parameterizations, discretization schemes, and implementation constraints. However, existing implementations are fragmented across different software frameworks, often rely on framework-specific optimizations, and in some cases require custom CUDA kernels or lack publicly available code altogether. As a result, using, comparing, or extending LRNNs requires substantial implementation effort. To address this, we introduce $\texttt{lrnnx}$, a unified software library that implements several modern LRNN architectures under a common interface. The library exposes multiple levels of control, allowing users to work directly with core components or higher-level model abstractions. $\texttt{lrnnx}$ aims to improve accessibility, reproducibility, and extensibility of LRNN research and applications. We make our code available under a permissive MIT license.

