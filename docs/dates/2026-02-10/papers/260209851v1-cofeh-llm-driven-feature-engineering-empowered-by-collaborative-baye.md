---
layout: default
title: CoFEH: LLM-driven Feature Engineering Empowered by Collaborative Bayesian Hyperparameter Optimization
---

# CoFEH: LLM-driven Feature Engineering Empowered by Collaborative Bayesian Hyperparameter Optimization
**arXiv**：[2602.09851v1](https://arxiv.org/abs/2602.09851) · [PDF](https://arxiv.org/pdf/2602.09851.pdf)  
**作者**：Beicheng Xu, Keyao Ding, Wei Liu, Yupeng Lu, Bin Cui  

**一句话要点**：提出CoFEH框架，通过LLM驱动的特征工程与贝叶斯超参数优化协同解决AutoML中特征工程瓶颈问题。

**关键词**：特征工程, 超参数优化, 大语言模型, 贝叶斯优化, 自动化机器学习, 协同优化

## 3 点简述
- 传统特征工程方法受限于黑盒搜索和固定搜索空间，缺乏领域感知，导致AutoML性能瓶颈。
- CoFEH结合LLM驱动的特征工程优化器和贝叶斯超参数优化，通过动态调度和互信息机制实现协同优化。
- 实验表明CoFEH在端到端性能上优于传统和基于LLM的基线方法，验证了联合优化的有效性。

## 摘要（原文）

> Feature Engineering (FE) is pivotal in automated machine learning (AutoML) but remains a bottleneck for traditional methods, which treat it as a black-box search, operating within rigid, predefined search spaces and lacking domain awareness. While Large Language Models (LLMs) offer a promising alternative by leveraging semantic reasoning to generate unbounded operators, existing methods fail to construct free-form FE pipelines, remaining confined to isolated subtasks such as feature generation. Most importantly, they are rarely optimized jointly with hyperparameter optimization (HPO) of the ML model, leading to greedy "FE-then-HPO" workflows that cannot capture strong FE-HPO interactions. In this paper, we present CoFEH, a collaborative framework that interleaves LLM-based FE and Bayesian HPO for robust end-to-end AutoML. CoFEH uses an LLM-driven FE optimizer powered by Tree of Thought (ToT) to explore flexible FE pipelines, a Bayesian optimization (BO) module to solve HPO, and a dynamic optimizer selector that realizes interleaved optimization by adaptively scheduling FE and HPO steps. Crucially, we introduce a mutual conditioning mechanism that shares context between LLM and BO, enabling mutually informed decisions. Experiments show that CoFEH not only outperforms traditional and LLM-based FE baselines, but also achieves superior end-to-end performance under joint optimization.

