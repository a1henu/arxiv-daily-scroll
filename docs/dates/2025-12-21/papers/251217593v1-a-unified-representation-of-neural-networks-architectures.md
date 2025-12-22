---
layout: default
title: A Unified Representation of Neural Networks Architectures
---

# A Unified Representation of Neural Networks Architectures
**arXiv**：[2512.17593v1](https://arxiv.org/abs/2512.17593) · [PDF](https://arxiv.org/pdf/2512.17593.pdf)  
**作者**：Christophe Prieur, Mircea Lazar, Bogdan Robu  

**一句话要点**：提出统一神经网络架构表示DiPaNet，以处理无限神经元和隐藏层极限情况下的近似误差分析。

**关键词**：神经网络架构, 连续神经网络, 近似误差分析, 神经ODE, 残差网络, 统一表示

## 3 点简述
- 研究神经网络在神经元和隐藏层数趋于无限时的极限情况，推导近似误差与结构参数的关系。
- 扩展单隐藏层无限宽度表示到深度残差连续网络，并形式化神经ODE与残差网络的近似误差。
- 提出DiPaNet作为统一表示，通过同质化/离散化关联现有有限和无限维架构，讨论与神经场的异同。

## 摘要（原文）

> In this paper we consider the limiting case of neural networks (NNs) architectures when the number of neurons in each hidden layer and the number of hidden layers tend to infinity thus forming a continuum, and we derive approximation errors as a function of the number of neurons and/or hidden layers. Firstly, we consider the case of neural networks with a single hidden layer and we derive an integral infinite width neural representation that generalizes existing continuous neural networks (CNNs) representations. Then we extend this to deep residual CNNs that have a finite number of integral hidden layers and residual connections. Secondly, we revisit the relation between neural ODEs and deep residual NNs and we formalize approximation errors via discretization techniques. Then, we merge these two approaches into a unified homogeneous representation of NNs as a Distributed Parameter neural Network (DiPaNet) and we show that most of the existing finite and infinite-dimensional NNs architectures are related via homogeneization/discretization with the DiPaNet representation. Our approach is purely deterministic and applies to general, uniformly continuous matrix weight functions. Differences and similarities with neural fields are discussed along with further possible generalizations and applications of the DiPaNet framework.

