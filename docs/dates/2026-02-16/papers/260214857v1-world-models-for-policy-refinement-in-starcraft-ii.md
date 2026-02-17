---
layout: default
title: World Models for Policy Refinement in StarCraft II
---

# World Models for Policy Refinement in StarCraft II
**arXiv**：[2602.14857v1](https://arxiv.org/abs/2602.14857) · [PDF](https://arxiv.org/pdf/2602.14857.pdf)  
**作者**：Yixin Zhang, Ziyi Wang, Yiming Rong, Haoxi Wang, Jinling Jiang, Shuang Xu, Haoran Wu, Shiyu Zhou, Bo Xu  

**一句话要点**：提出StarWM世界模型以增强星际争霸II中基于大语言模型的决策策略

**关键词**：世界模型, 星际争霸II, 大语言模型, 决策策略, 部分可观测性, 结构化表示

## 3 点简述
- 现有LLM-based星际争霸II代理忽视可学习的动作条件转移模型集成，导致决策循环不完整
- 引入结构化文本表示分解观测为五个语义模块，并构建首个指令调优数据集SC2-Dynamics-50k
- 在线评估显示StarWM-Agent在Hard至VeryHard难度下胜率提升15%-30%，宏观管理稳定性改善

## 摘要（原文）

> Large Language Models (LLMs) have recently shown strong reasoning and generalization capabilities, motivating their use as decision-making policies in complex environments. StarCraft II (SC2), with its massive state-action space and partial observability, is a challenging testbed. However, existing LLM-based SC2 agents primarily focus on improving the policy itself and overlook integrating a learnable, action-conditioned transition model into the decision loop. To bridge this gap, we propose StarWM, the first world model for SC2 that predicts future observations under partial observability. To facilitate learning SC2's hybrid dynamics, we introduce a structured textual representation that factorizes observations into five semantic modules, and construct SC2-Dynamics-50k, the first instruction-tuning dataset for SC2 dynamics prediction. We further develop a multi-dimensional offline evaluation framework for predicted structured observations. Offline results show StarWM's substantial gains over zero-shot baselines, including nearly 60% improvements in resource prediction accuracy and self-side macro-situation consistency. Finally, we propose StarWM-Agent, a world-model-augmented decision system that integrates StarWM into a Generate--Simulate--Refine decision loop for foresight-driven policy refinement. Online evaluation against SC2's built-in AI demonstrates consistent improvements, yielding win-rate gains of 30%, 15%, and 30% against Hard (LV5), Harder (LV6), and VeryHard (LV7), respectively, alongside improved macro-management stability and tactical risk assessment.

