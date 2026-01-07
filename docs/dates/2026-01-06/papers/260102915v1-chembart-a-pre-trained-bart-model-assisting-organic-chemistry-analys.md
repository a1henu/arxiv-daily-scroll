---
layout: default
title: ChemBART: A Pre-trained BART Model Assisting Organic Chemistry Analysis
---

# ChemBART: A Pre-trained BART Model Assisting Organic Chemistry Analysis
**arXiv**：[2601.02915v1](https://arxiv.org/abs/2601.02915) · [PDF](https://arxiv.org/pdf/2601.02915.pdf)  
**作者**：Kenan Li, Yijian Zhang, Jin Wang, Haipeng Gan, Zeying Sun, Xiaoguang Lei, Hao Dong  

**一句话要点**：提出ChemBART预训练模型，基于化学反应统一处理多任务有机化学分析

**关键词**：有机化学分析, 预训练语言模型, 多任务学习, 合成路线设计, SMILES表示, 强化学习集成

## 3 点简述
- 核心问题：现有LLM在化学中多针对单任务，如前体预测，缺乏统一模型处理多任务合成规划。
- 方法要点：基于SMILES预训练BART模型，通过掩码填充任务学习反应表达，支持前体/试剂生成、温度-产率回归等下游任务。
- 实验或效果：模型设计的多步合成路线在湿实验验证中缩短路径，产率比文献基准提高约30%。

## 摘要（原文）

> Recent advances in large language models (LLMs) have demonstrated transformative potential across diverse fields. While LLMs have been applied to molecular simplified molecular input line entry system (SMILES) in computer-aided synthesis planning (CASP), existing methodologies typically address single tasks, such as precursor prediction. We introduce ChemBART, a SMILES-based LLM pre-trained on chemical reactions, which enables a unified model for multiple downstream chemical tasks--achieving the paradigm of "one model, one pre-training, multiple tasks." By leveraging outputs from a mask-filling pre-training task on reaction expressions, ChemBART effectively solves a variety of chemical problems, including precursor/reagent generation, temperature-yield regression, molecular property classification, and optimizing the policy and value functions within a reinforcement learning framework, integrated with Monte Carlo tree search for multi-step synthesis route design. Unlike single-molecule pre-trained LLMs constrained to specific applications, ChemBART addresses broader chemical challenges and integrates them for comprehensive synthesis planning. Crucially, ChemBART-designed multi-step synthesis routes and reaction conditions directly inspired wet-lab validation, which confirmed shorter pathways with ~30% yield improvement over literature benchmarks. Our work validates the power of reaction-focused pre-training and showcases the broad utility of ChemBART in advancing the complete synthesis planning cycle.

