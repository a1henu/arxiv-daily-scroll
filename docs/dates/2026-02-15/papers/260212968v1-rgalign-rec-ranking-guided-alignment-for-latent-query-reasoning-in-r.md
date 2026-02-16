---
layout: default
title: RGAlign-Rec: Ranking-Guided Alignment for Latent Query Reasoning in Recommendation Systems
---

# RGAlign-Rec: Ranking-Guided Alignment for Latent Query Reasoning in Recommendation Systems
**arXiv**：[2602.12968v1](https://arxiv.org/abs/2602.12968) · [PDF](https://arxiv.org/pdf/2602.12968.pdf)  
**作者**：Junhua Liu, Yang Jihao, Cheng Chang, Kunrong LI, Bin Fu, Kwan Hui Lim  

**一句话要点**：提出RGAlign-Rec框架，通过排序引导对齐解决推荐系统中语义推理与排序目标不匹配问题。

**关键词**：推荐系统, 语义推理, 排序对齐, LLM应用, 主动推荐

## 3 点简述
- 核心问题：用户特征与知识库语义意图的差距，以及LLM输出与排序任务目标的不对齐。
- 方法要点：结合LLM语义推理器和查询增强排序模型，采用多阶段排序引导对齐训练范式。
- 实验或效果：在工业数据集上提升GAUC和召回率，在线测试显示CTR显著改善。

## 摘要（原文）

> Proactive intent prediction is a critical capability in modern e-commerce chatbots, enabling "zero-query" recommendations by anticipating user needs from behavioral and contextual signals. However, existing industrial systems face two fundamental challenges: (1) the semantic gap between discrete user features and the semantic intents within the chatbot's Knowledge Base, and (2) the objective misalignment between general-purpose LLM outputs and task-specific ranking utilities. To address these issues, we propose RGAlign-Rec, a closed-loop alignment framework that integrates an LLM-based semantic reasoner with a Query-Enhanced (QE) ranking model. We also introduce Ranking-Guided Alignment (RGA), a multi-stage training paradigm that utilizes downstream ranking signals as feedback to refine the LLM's latent reasoning. Extensive experiments on a large-scale industrial dataset from Shopee demonstrate that RGAlign-Rec achieves a 0.12% gain in GAUC, leading to a significant 3.52% relative reduction in error rate, and a 0.56% improvement in Recall@3. Online A/B testing further validates the cumulative effectiveness of our framework: the Query-Enhanced model (QE-Rec) initially yields a 0.98% improvement in CTR, while the subsequent Ranking-Guided Alignment stage contributes an additional 0.13% gain. These results indicate that ranking-aware alignment effectively synchronizes semantic reasoning with ranking objectives, significantly enhancing both prediction accuracy and service quality in real-world proactive recommendation systems.

