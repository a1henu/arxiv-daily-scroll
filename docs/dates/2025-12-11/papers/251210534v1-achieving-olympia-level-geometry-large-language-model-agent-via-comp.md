---
layout: default
title: Achieving Olympia-Level Geometry Large Language Model Agent via Complexity Boosting Reinforcement Learning
---

# Achieving Olympia-Level Geometry Large Language Model Agent via Complexity Boosting Reinforcement Learning
**arXiv**：[2512.10534v1](https://arxiv.org/abs/2512.10534) · [PDF](https://arxiv.org/pdf/2512.10534.pdf)  
**作者**：Haiteng Zhao, Junhao Shen, Yiming Zhang, Songyang Gao, Kuikun Liu, Tianyou Ma, Fan Zheng, Dahua Lin, Wenwei Zhang, Kai Chen  

**一句话要点**：提出InternGeometry与复杂度提升强化学习，构建奥林匹克级几何大语言模型代理

**关键词**：几何问题求解, 大语言模型代理, 复杂度提升强化学习, 符号引擎验证, 动态内存机制, 国际数学奥林匹克

## 3 点简述
- 核心问题：几何问题求解中，大语言模型代理因辅助构造启发式弱，依赖专家模型如AlphaGeometry 2。
- 方法要点：通过迭代命题与辅助构造、符号引擎验证及反馈反思，结合动态内存机制实现多轮交互。
- 实验或效果：在50道IMO几何题中解决44道，超越金牌平均分，仅用13K训练示例，数据量仅为AlphaGeometry 2的0.004%。

## 摘要（原文）

> Large language model (LLM) agents exhibit strong mathematical problem-solving abilities and can even solve International Mathematical Olympiad (IMO) level problems with the assistance of formal proof systems. However, due to weak heuristics for auxiliary constructions, AI for geometry problem solving remains dominated by expert models such as AlphaGeometry 2, which rely heavily on large-scale data synthesis and search for both training and evaluation. In this work, we make the first attempt to build a medalist-level LLM agent for geometry and present InternGeometry. InternGeometry overcomes the heuristic limitations in geometry by iteratively proposing propositions and auxiliary constructions, verifying them with a symbolic engine, and reflecting on the engine's feedback to guide subsequent proposals. A dynamic memory mechanism enables InternGeometry to conduct more than two hundred interactions with the symbolic engine per problem. To further accelerate learning, we introduce Complexity-Boosting Reinforcement Learning (CBRL), which gradually increases the complexity of synthesized problems across training stages. Built on InternThinker-32B, InternGeometry solves 44 of 50 IMO geometry problems (2000-2024), exceeding the average gold medalist score (40.9), using only 13K training examples, just 0.004% of the data used by AlphaGeometry 2, demonstrating the potential of LLM agents on expert-level geometry tasks. InternGeometry can also propose novel auxiliary constructions for IMO problems that do not appear in human solutions. We will release the model, data, and symbolic engine to support future research.

