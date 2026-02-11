---
layout: default
title: Large Language Models for Designing Participatory Budgeting Rules
---

# Large Language Models for Designing Participatory Budgeting Rules
**arXiv**：[2602.09349v1](https://arxiv.org/abs/2602.09349) · [PDF](https://arxiv.org/pdf/2602.09349.pdf)  
**作者**：Nguyen Thach, Xingchen Sha, Hau Chan  

**一句话要点**：提出LLMRule框架，利用大语言模型进化搜索自动化设计参与式预算规则

**关键词**：参与式预算, 大语言模型, 进化搜索, 规则设计, 公平性优化

## 3 点简述
- 核心问题：参与式预算规则设计需平衡效用与公平，传统方法依赖领域知识且存在权衡挑战
- 方法要点：结合大语言模型与进化搜索，自动化生成规则，模拟背包问题算法设计
- 实验或效果：在600多个真实世界实例上测试，LLM生成规则在保持公平的同时提升整体效用

## 摘要（原文）

> Participatory budgeting (PB) is a democratic paradigm for deciding the funding of public projects given the residents' preferences, which has been adopted in numerous cities across the world. The main focus of PB is designing rules, functions that return feasible budget allocations for a set of projects subject to some budget constraint. Designing PB rules that optimize both utility and fairness objectives based on agent preferences had been challenging due to the extensive domain knowledge required and the proven trade-off between the two notions. Recently, large language models (LLMs) have been increasingly employed for automated algorithmic design. Given the resemblance of PB rules to algorithms for classical knapsack problems, in this paper, we introduce a novel framework, named LLMRule, that addresses the limitations of existing works by incorporating LLMs into an evolutionary search procedure for automating the design of PB rules. Our experimental results, evaluated on more than 600 real-world PB instances obtained from the U.S., Canada, Poland, and the Netherlands with different representations of agent preferences, demonstrate that the LLM-generated rules generally outperform existing handcrafted rules in terms of overall utility while still maintaining a similar degree of fairness.

