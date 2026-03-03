---
layout: default
title: Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search
---

# Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search
**arXiv**：[2603.01692v1](https://arxiv.org/abs/2603.01692) · [PDF](https://arxiv.org/pdf/2603.01692.pdf)  
**作者**：Yifei Zhang, Xu Yang, Xiao Yang, Bowen Xian, Qizheng Li, Shikai Fang, Jingyuan Li, Jian Wang, Mingrui Xu, Weiqing Liu, Jiang Bian  

**一句话要点**：提出Gome代理，将梯度优化应用于机器学习工程，以提升LLM代理效率。

**关键词**：机器学习工程代理, 梯度优化, LLM推理, 树搜索, 分布式优化, 封闭世界评估

## 3 点简述
- 核心问题：基于LLM的机器学习工程代理依赖树搜索，效率低且不随推理能力提升而优化。
- 方法要点：Gome通过结构化诊断推理映射梯度计算，结合成功记忆和多轨迹执行实现分布式优化。
- 实验或效果：在封闭世界协议下，Gome在MLE-Bench上以12小时单V100预算达到35.1%任意奖牌率，显示梯度优化随模型推理能力增强而优势扩大。

## 摘要（原文）

> LLM-based agents for machine learning engineering (MLE) predominantly rely on tree search, a form of gradient-free optimization that uses scalar validation scores to rank candidates. As LLM reasoning capabilities improve, exhaustive enumeration becomes increasingly inefficient compared to directed updates, analogous to how accurate gradients enable efficient descent over random search. We introduce \textsc{Gome}, an MLE agent that operationalizes gradient-based optimization. \textsc{Gome} maps structured diagnostic reasoning to gradient computation, success memory to momentum, and multi-trace execution to distributed optimization. Under a closed-world protocol that isolates architectural effects from external knowledge, \textsc{Gome} achieves a state-of-the-art 35.1\% any-medal rate on MLE-Bench with a restricted 12-hour budget on a single V100 GPU. Scaling experiments across 10 models reveal a critical crossover: with weaker models, tree search retains advantages by compensating for unreliable reasoning through exhaustive exploration; as reasoning capability strengthens, gradient-based optimization progressively outperforms, with the gap widening at frontier-tier models. Given the rapid advancement of reasoning-oriented LLMs, this positions gradient-based optimization as an increasingly favorable paradigm. We release our codebase and GPT-5 traces.

