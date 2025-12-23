---
layout: default
title: ChemATP: A Training-Free Chemical Reasoning Framework for Large Language Models
---

# ChemATP: A Training-Free Chemical Reasoning Framework for Large Language Models
**arXiv**：[2512.19240v1](https://arxiv.org/abs/2512.19240) · [PDF](https://arxiv.org/pdf/2512.19240.pdf)  
**作者**：Mingxu Zhang, Dazhong Shen, Qi Zhang, Ying Sun  

**一句话要点**：提出ChemATP框架，通过原子级知识库实现冻结大语言模型的化学推理，解决化学先验缺失问题。

**关键词**：化学推理框架, 原子级知识库, 训练无关方法, 大语言模型, 先验注入, 分子科学

## 3 点简述
- 核心问题：大语言模型在分子科学中因缺乏化学先验而推理困难，现有方法存在静态耦合或表面提示的局限。
- 方法要点：构建首个原子级文本知识库，动态检索化学知识，解耦知识存储与推理引擎，保持模型通用智能。
- 实验或效果：ChemATP显著优于训练无关基线，媲美训练相关先进模型，证明显式先验注入是有效替代方案。

## 摘要（原文）

> Large Language Models (LLMs) exhibit strong general reasoning but struggle in molecular science due to the lack of explicit chemical priors in standard string representations. Current solutions face a fundamental dilemma. Training-based methods inject priors into parameters, but this static coupling hinders rapid knowledge updates and often compromises the model's general reasoning capabilities. Conversely, existing training-free methods avoid these issues but rely on surface-level prompting, failing to provide the fine-grained atom-level priors essential for precise chemical reasoning. To address this issue, we introduce ChemATP, a framework that decouples chemical knowledge from the reasoning engine. By constructing the first atom-level textual knowledge base, ChemATP enables frozen LLMs to explicitly retrieve and reason over this information dynamically. This architecture ensures interpretability and adaptability while preserving the LLM's intrinsic general intelligence. Experiments show that ChemATP significantly outperforms training-free baselines and rivals state-of-the-art training-based models, demonstrating that explicit prior injection is a competitive alternative to implicit parameter updates.

