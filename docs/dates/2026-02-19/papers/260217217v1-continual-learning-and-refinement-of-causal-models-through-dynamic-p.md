---
layout: default
title: Continual learning and refinement of causal models through dynamic predicate invention
---

# Continual learning and refinement of causal models through dynamic predicate invention
**arXiv**：[2602.17217v1](https://arxiv.org/abs/2602.17217) · [PDF](https://arxiv.org/pdf/2602.17217.pdf)  
**作者**：Enrique Crespo-Fernandez, Oliver Ray, Telmo de Menezes e Silva Filho, Peter Flach  

**一句话要点**：提出在线构建符号因果世界模型的框架，以解决复杂环境中样本效率低和可扩展性差的问题。

**关键词**：持续学习, 因果模型, 谓词发明, 元解释学习, 符号世界建模

## 3 点简述
- 核心问题：标准世界建模方法在样本效率、透明度和可扩展性方面存在不足。
- 方法要点：集成元解释学习和谓词发明，在线学习并修复符号因果模型。
- 实验或效果：在复杂关系动态领域实现高样本效率，优于PPO神经网络基线。

## 摘要（原文）

> Efficiently navigating complex environments requires agents to internalize the underlying logic of their world, yet standard world modelling methods often struggle with sample inefficiency, lack of transparency, and poor scalability. We propose a framework for constructing symbolic causal world models entirely online by integrating continuous model learning and repair into the agent's decision loop, by leveraging the power of Meta-Interpretive Learning and predicate invention to find semantically meaningful and reusable abstractions, allowing an agent to construct a hierarchy of disentangled, high-quality concepts from its observations. We demonstrate that our lifted inference approach scales to domains with complex relational dynamics, where propositional methods suffer from combinatorial explosion, while achieving sample-efficiency orders of magnitude higher than the established PPO neural-network-based baseline.

