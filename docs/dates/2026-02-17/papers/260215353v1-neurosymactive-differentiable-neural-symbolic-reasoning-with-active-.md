---
layout: default
title: NeuroSymActive: Differentiable Neural-Symbolic Reasoning with Active Exploration for Knowledge Graph Question Answering
---

# NeuroSymActive: Differentiable Neural-Symbolic Reasoning with Active Exploration for Knowledge Graph Question Answering
**arXiv**：[2602.15353v1](https://arxiv.org/abs/2602.15353) · [PDF](https://arxiv.org/pdf/2602.15353.pdf)  
**作者**：Rong Fu, Yang Li, Zeyu Zhang, Jiekai Wu, Yaohua Liu, Shuaishuai Cao, Yangchen Zeng, Yuhang Zhang, Xiaojing Du, Chuang Zhao, Kangning Cui, Simon Fong  

**一句话要点**：提出NeuroSymActive框架，结合可微分神经符号推理与主动探索，以解决知识图谱问答中的多跳推理挑战。

**关键词**：知识图谱问答, 神经符号推理, 主动探索, 可微分推理, 多跳推理, 蒙特卡洛策略

## 3 点简述
- 核心问题：知识密集型查询需精确多跳推理，现有方法在效率与鲁棒性上不足。
- 方法要点：集成软统一符号模块、神经路径评估器和蒙特卡洛主动探索策略。
- 实验或效果：在标准基准上实现高准确率，同时减少图查询和模型调用次数。

## 摘要（原文）

> Large pretrained language models and neural reasoning systems have advanced many natural language tasks, yet they remain challenged by knowledge-intensive queries that require precise, structured multi-hop inference. Knowledge graphs provide a compact symbolic substrate for factual grounding, but integrating graph structure with neural models is nontrivial: naively embedding graph facts into prompts leads to inefficiency and fragility, while purely symbolic or search-heavy approaches can be costly in retrievals and lack gradient-based refinement. We introduce NeuroSymActive, a modular framework that combines a differentiable neural-symbolic reasoning layer with an active, value-guided exploration controller for Knowledge Graph Question Answering. The method couples soft-unification style symbolic modules with a neural path evaluator and a Monte-Carlo style exploration policy that prioritizes high-value path expansions. Empirical results on standard KGQA benchmarks show that NeuroSymActive attains strong answer accuracy while reducing the number of expensive graph lookups and model calls compared to common retrieval-augmented baselines.

