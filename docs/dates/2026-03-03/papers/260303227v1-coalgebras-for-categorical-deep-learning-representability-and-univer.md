---
layout: default
title: Coalgebras for categorical deep learning: Representability and universal approximation
---

# Coalgebras for categorical deep learning: Representability and universal approximation
**arXiv**：[2603.03227v1](https://arxiv.org/abs/2603.03227) · [PDF](https://arxiv.org/pdf/2603.03227.pdf)  
**作者**：Dragan Mašulović  

**一句话要点**：提出范畴深度学习的余代数基础，以统一表示等变性与实现通用逼近定理。

**关键词**：范畴深度学习, 余代数, 等变性, 通用逼近定理, 函子嵌入, 对称性

## 3 点简述
- 核心问题：范畴深度学习需抽象表示等变性，以泛化群作用与等变映射。
- 方法要点：基于余代数形式化，构建从集合到向量空间的函子嵌入，并提升不变行为。
- 实验或效果：证明在广义设置下，连续等变函数可被余代数框架逼近，适用于广泛对称性。

## 摘要（原文）

> Categorical deep learning (CDL) has recently emerged as a framework that leverages category theory to unify diverse neural architectures. While geometric deep learning (GDL) is grounded in the specific context of invariants of group actions, CDL aims to provide domain-independent abstractions for reasoning about models and their properties. In this paper, we contribute to this program by developing a coalgebraic foundation for equivariant representation in deep learning, as classical notions of group actions and equivariant maps are naturally generalized by the coalgebraic formalism. Our first main result demonstrates that, given an embedding of data sets formalized as a functor from SET to VECT, and given a notion of invariant behavior on data sets modeled by an endofunctor on SET, there is a corresponding endofunctor on VECT that is compatible with the embedding in the sense that this lifted functor recovers the analogous notion of invariant behavior on the embedded data. Building on this foundation, we then establish a universal approximation theorem for equivariant maps in this generalized setting. We show that continuous equivariant functions can be approximated within our coalgebraic framework for a broad class of symmetries. This work thus provides a categorical bridge between the abstract specification of invariant behavior and its concrete realization in neural architectures.

