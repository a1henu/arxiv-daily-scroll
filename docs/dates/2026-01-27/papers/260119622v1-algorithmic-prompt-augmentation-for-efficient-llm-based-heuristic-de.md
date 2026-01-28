---
layout: default
title: Algorithmic Prompt-Augmentation for Efficient LLM-Based Heuristic Design for A* Search
---

# Algorithmic Prompt-Augmentation for Efficient LLM-Based Heuristic Design for A* Search
**arXiv**：[2601.19622v1](https://arxiv.org/abs/2601.19622) · [PDF](https://arxiv.org/pdf/2601.19622.pdf)  
**作者**：Thomas Bömer, Nico Koltermann, Max Disselnmeyer, Bastian Amberg, Anne Meyer  

**一句话要点**：提出算法提示增强策略A-CEoH，以自动化生成A*搜索的启发式函数。

**关键词**：启发式函数设计, A*搜索, 大语言模型, 进化算法, 上下文学习, 自动化优化

## 3 点简述
- 核心问题：传统A*搜索启发式函数依赖手工设计，需大量专业知识，效率低。
- 方法要点：扩展EoH框架，引入领域无关的提示增强策略，将A*代码融入提示以利用上下文学习。
- 实验或效果：在UPMP和SPP问题域测试，A-CEoH显著提升启发式质量，甚至超越专家设计。

## 摘要（原文）

> Heuristic functions are essential to the performance of tree search algorithms such as A*, where their accuracy and efficiency directly impact search outcomes. Traditionally, such heuristics are handcrafted, requiring significant expertise. Recent advances in large language models (LLMs) and evolutionary frameworks have opened the door to automating heuristic design. In this paper, we extend the Evolution of Heuristics (EoH) framework to investigate the automated generation of guiding heuristics for A* search. We introduce a novel domain-agnostic prompt augmentation strategy that includes the A* code into the prompt to leverage in-context learning, named Algorithmic - Contextual EoH (A-CEoH). To evaluate the effectiveness of A-CeoH, we study two problem domains: the Unit-Load Pre-Marshalling Problem (UPMP), a niche problem from warehouse logistics, and the classical sliding puzzle problem (SPP). Our computational experiments show that A-CEoH can significantly improve the quality of the generated heuristics and even outperform expert-designed heuristics.

