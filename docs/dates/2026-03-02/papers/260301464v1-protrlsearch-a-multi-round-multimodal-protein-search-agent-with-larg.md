---
layout: default
title: ProtRLSearch: A Multi-Round Multimodal Protein Search Agent with Large Language Models Trained via Reinforcement Learning
---

# ProtRLSearch: A Multi-Round Multimodal Protein Search Agent with Large Language Models Trained via Reinforcement Learning
**arXiv**：[2603.01464v1](https://arxiv.org/abs/2603.01464) · [PDF](https://arxiv.org/pdf/2603.01464.pdf)  
**作者**：Congying Liu, Taihao Li, Ming Huang, Xingyuan Wei, Peipei Liu, Yiqing Shen, Yanxu Mao, Tiehan Cui  

**一句话要点**：提出ProtRLSearch，一种基于强化学习的多轮多模态蛋白质搜索代理，以解决医疗场景中蛋白质序列约束下的推理任务。

**关键词**：蛋白质搜索代理, 多模态输入, 强化学习训练, 多轮搜索, 蛋白质序列分析, 医疗推理

## 3 点简述
- 核心问题：现有蛋白质搜索代理多为单轮文本搜索，缺乏序列模态输入和搜索过程约束，导致推理偏差难以纠正。
- 方法要点：采用多轮多模态输入（蛋白质序列和文本），结合多维奖励的强化学习训练，提升搜索决策质量。
- 实验或效果：构建ProtMCQs基准（3000道多选题），评估模型在蛋白质查询任务中整合序列与文本信息的能力。

## 摘要（原文）

> Protein analysis tasks arising in healthcare settings often require accurate reasoning under protein sequence constraints, involving tasks such as functional interpretation of disease-related variants, protein-level analysis for clinical research, and similar scenarios. To address such tasks, search agents are introduced to search protein-related information, providing support for disease-related variant analysis and protein function reasoning in protein-centric inference. However, such search agents are mostly limited to single-round, text-only modality search, which prevents the protein sequence modality from being incorporated as a multimodal input into the search decision-making process. Meanwhile, their reliance on reinforcement learning (RL) supervision that focuses solely on the final answer results in a lack of search process constraints, making deviations in keyword selection and reasoning directions difficult to identify and correct in a timely manner. To address these limitations, we propose ProtRLSearch, a multi-round protein search agent trained with multi-dimensional reward based RL, which jointly leverages protein sequence and text as multimodal inputs during real-time search to produce high quality reports. To evaluate the ability of models to integrate protein sequence information and text-based multimodal inputs in realistic protein query settings, we construct ProtMCQs, a benchmark of 3,000 multiple choice questions (MCQs) organized into three difficulty levels. The benchmark evaluates protein query tasks that range from sequence constrained reasoning about protein function and phenotype changes to comprehensive protein reasoning that integrates multi-dimensional sequence features with signal pathways and regulatory networks.

