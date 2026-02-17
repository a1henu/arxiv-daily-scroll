---
layout: default
title: Lifted Relational Probabilistic Inference via Implicit Learning
---

# Lifted Relational Probabilistic Inference via Implicit Learning
**arXiv**：[2602.14890v1](https://arxiv.org/abs/2602.14890) · [PDF](https://arxiv.org/pdf/2602.14890.pdf)  
**作者**：Luise Ge, Brendan Juba, Kris Nilsson, Alison Shao  

**一句话要点**：提出隐式学习框架以解决一阶关系概率逻辑中的查询推理问题

**关键词**：一阶关系概率逻辑, 隐式学习, 提升推理, 平方和层次, 多项式时间框架

## 3 点简述
- 核心问题：在部分、噪声观测下，一阶关系概率逻辑的归纳学习与演绎推理难以调和
- 方法要点：通过隐式学习合并不完整公理与样本，利用平方和层次进行多项式时间推理
- 实验或效果：未知

## 摘要（原文）

> Reconciling the tension between inductive learning and deductive reasoning in first-order relational domains is a longstanding challenge in AI. We study the problem of answering queries in a first-order relational probabilistic logic through a joint effort of learning and reasoning, without ever constructing an explicit model. Traditional lifted inference assumes access to a complete model and exploits symmetry to evaluate probabilistic queries; however, learning such models from partial, noisy observations is intractable in general. We reconcile these two challenges through implicit learning to reason and first-order relational probabilistic inference techniques. More specifically, we merge incomplete first-order axioms with independently sampled, partially observed examples into a bounded-degree fragment of the sum-of-squares (SOS) hierarchy in polynomial time. Our algorithm performs two lifts simultaneously: (i) grounding-lift, where renaming-equivalent ground moments share one variable, collapsing the domain of individuals; and (ii) world-lift, where all pseudo-models (partial world assignments) are enforced in parallel, producing a global bound that holds across all worlds consistent with the learned constraints. These innovations yield the first polynomial-time framework that implicitly learns a first-order probabilistic logic and performs lifted inference over both individuals and worlds.

