---
layout: default
title: A Balanced Neuro-Symbolic Approach for Commonsense Abductive Logic
---

# A Balanced Neuro-Symbolic Approach for Commonsense Abductive Logic
**arXiv**：[2601.18595v1](https://arxiv.org/abs/2601.18595) · [PDF](https://arxiv.org/pdf/2601.18595.pdf)  
**作者**：Joseph Cotnareanu, Didier Chetelat, Yingxue Zhang, Mark Coates  

**一句话要点**：提出一种平衡神经与符号的方法，通过迭代反馈增强逻辑问题中的常识关系，以解决LLMs在复杂推理中缺失常识的问题。

**关键词**：常识推理, 神经符号方法, 逻辑求解器, 大型语言模型, 迭代增强

## 3 点简述
- 核心问题：LLMs在需要复杂证明规划时表现不佳，逻辑求解器无法处理缺失的常识关系。
- 方法要点：使用逻辑求解器的反馈迭代地由LLM提供常识关系，通过搜索假设最大化有用事实发现。
- 实验或效果：在去除部分常识信息的纯逻辑推理数据集上，相比现有技术取得显著改进。

## 摘要（原文）

> Although Large Language Models (LLMs) have demonstrated impressive formal reasoning abilities, they often break down when problems require complex proof planning. One promising approach for improving LLM reasoning abilities involves translating problems into formal logic and using a logic solver. Although off-the-shelf logic solvers are in principle substantially more efficient than LLMs at logical reasoning, they assume that all relevant facts are provided in a question and are unable to deal with missing commonsense relations. In this work, we propose a novel method that uses feedback from the logic solver to augment a logic problem with commonsense relations provided by the LLM, in an iterative manner. This involves a search procedure through potential commonsense assumptions to maximize the chance of finding useful facts while keeping cost tractable. On a collection of pure-logical reasoning datasets, from which some commonsense information has been removed, our method consistently achieves considerable improvements over existing techniques, demonstrating the value in balancing neural and symbolic elements when working in human contexts.

