---
layout: default
title: Causal Learning Should Embrace the Wisdom of the Crowd
---

# Causal Learning Should Embrace the Wisdom of the Crowd
**arXiv**：[2603.02678v1](https://arxiv.org/abs/2603.02678) · [PDF](https://arxiv.org/pdf/2603.02678.pdf)  
**作者**：Ryan Feng Lin, Yuantao Wei, Huiling Liao, Xiaoning Qian, Shuai Huang  

**一句话要点**：提出集成众包与LLM的分布式框架以解决因果图学习中的知识碎片化问题

**关键词**：因果发现, 有向无环图学习, 众包平台, 专家知识聚合, 大语言模型模拟, 分布式决策

## 3 点简述
- 核心问题：从观测数据学习因果图面临组合爆炸和模糊性，个体知识不完整
- 方法要点：整合众包平台、交互式知识获取、专家意见建模与LLM模拟，合成分布式决策
- 实验或效果：未知，论文旨在推动新研究前沿，未报告具体实验

## 摘要（原文）

> Learning causal structures typically represented by directed acyclic graphs (DAGs) from observational data is notoriously challenging due to the combinatorial explosion of possible graphs and inherent ambiguities in observations. This paper argues that causal learning is now ready for the emergence of a new paradigm supported by rapidly advancing technologies, fulfilling the long-standing vision of leveraging human causal knowledge. This paradigm integrates scalable crowdsourcing platforms for data collection, interactive knowledge elicitation for expert opinion modeling, robust aggregation techniques for expert reconciliation, and large language model (LLM)-based simulation for augmenting AI-driven information acquisition. In this paper, we focus on DAG learning for causal discovery and frame the problem as a distributed decision-making task, recognizing that each participant (human expert or LLM agent) possesses fragmented and imperfect knowledge about different subsets of the variables of interest in the causal graph. By proposing a systematic framework to synthesize these insights, we aim to enable the recovery of a global causal structure unachievable by any individual agent alone.We advocate for a new research frontier and outline a comprehensive framework for new research thrusts that range from eliciting, modeling, aggregating, and optimizing human causal knowledge contributions.

