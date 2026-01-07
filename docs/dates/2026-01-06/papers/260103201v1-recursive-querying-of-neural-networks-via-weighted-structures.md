---
layout: default
title: Recursive querying of neural networks via weighted structures
---

# Recursive querying of neural networks via weighted structures
**arXiv**：[2601.03201v1](https://arxiv.org/abs/2601.03201) · [PDF](https://arxiv.org/pdf/2601.03201.pdf)  
**作者**：Martin Grohe, Christoph Standke, Juno Steegmans, Jan Van den Bussche  

**一句话要点**：提出加权结构上的递归逻辑以查询前馈神经网络，支持模型验证与解释。

**关键词**：加权结构逻辑, 函数不动点, 神经网络查询, 模型无关查询, 多项式时间复杂度

## 3 点简述
- 研究加权结构的逻辑，用于无深度限制神经网络的表达性查询。
- 扩展函数不动点机制，引入标量限制以实现多项式时间数据复杂度。
- 展示简单模型无关查询的NP完全性，并探讨加权结构的迭代转换。

## 摘要（原文）

> Expressive querying of machine learning models - viewed as a form of intentional data - enables their verification and interpretation using declarative languages, thereby making learned representations of data more accessible. Motivated by the querying of feedforward neural networks, we investigate logics for weighted structures. In the absence of a bound on neural network depth, such logics must incorporate recursion; thereto we revisit the functional fixpoint mechanism proposed by Grädel and Gurevich. We adopt it in a Datalog-like syntax; we extend normal forms for fixpoint logics to weighted structures; and show an equivalent "loose" fixpoint mechanism that allows values of inductively defined weight functions to be overwritten. We propose a "scalar" restriction of functional fixpoint logic, of polynomial-time data complexity, and show it can express all PTIME model-agnostic queries over reduced networks with polynomially bounded weights. In contrast, we show that very simple model-agnostic queries are already NP-complete. Finally, we consider transformations of weighted structures by iterated transductions.

