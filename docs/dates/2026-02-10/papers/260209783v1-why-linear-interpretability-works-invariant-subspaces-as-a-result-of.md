---
layout: default
title: Why Linear Interpretability Works: Invariant Subspaces as a Result of Architectural Constraints
---

# Why Linear Interpretability Works: Invariant Subspaces as a Result of Architectural Constraints
**arXiv**：[2602.09783v1](https://arxiv.org/abs/2602.09783) · [PDF](https://arxiv.org/pdf/2602.09783.pdf)  
**作者**：Andres Saurez, Yousung Lee, Dongsoo Har  

**一句话要点**：提出不变子空间必要性定理，解释线性可解释性在Transformer中的工作原理

**关键词**：线性可解释性, Transformer架构, 不变子空间, 自参考属性, 语义特征提取

## 3 点简述
- 核心问题：为何线性探针和稀疏自编码器能在深度非线性Transformer中有效提取语义结构
- 方法要点：基于架构约束，证明语义特征必须占据上下文不变线性子空间，提出自参考属性
- 实验或效果：在八个分类任务和四个模型家族中验证类令牌与语义实例的对齐

## 摘要（原文）

> Linear probes and sparse autoencoders consistently recover meaningful structure from transformer representations -- yet why should such simple methods succeed in deep, nonlinear systems? We show this is not merely an empirical regularity but a consequence of architectural necessity: transformers communicate information through linear interfaces (attention OV circuits, unembedding matrices), and any semantic feature decoded through such an interface must occupy a context-invariant linear subspace. We formalize this as the \emph{Invariant Subspace Necessity} theorem and derive the \emph{Self-Reference Property}: tokens directly provide the geometric direction for their associated features, enabling zero-shot identification of semantic structure without labeled data or learned probes. Empirical validation in eight classification tasks and four model families confirms the alignment between class tokens and semantically related instances. Our framework provides \textbf{a principled architectural explanation} for why linear interpretability methods work, unifying linear probes and sparse autoencoders.

