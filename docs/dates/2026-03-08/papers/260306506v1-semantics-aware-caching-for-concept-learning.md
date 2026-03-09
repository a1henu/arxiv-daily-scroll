---
layout: default
title: Semantics-Aware Caching for Concept Learning
---

# Semantics-Aware Caching for Concept Learning
**arXiv**：[2603.06506v1](https://arxiv.org/abs/2603.06506) · [PDF](https://arxiv.org/pdf/2603.06506.pdf)  
**作者**：Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo  

**一句话要点**：提出语义感知缓存以加速概念学习中的实例检索

**关键词**：概念学习, 语义缓存, 实例检索, 符号推理, 神经符号推理, 运行时优化

## 3 点简述
- 概念学习在知识库上迭代搜索，实例检索调用多导致运行时挑战
- 方法使用基于包含关系的缓存，通过集合操作链接概念与实例
- 实验显示缓存能显著减少概念检索和学习时间，适用于符号和神经符号推理器

## 摘要（原文）

> Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

