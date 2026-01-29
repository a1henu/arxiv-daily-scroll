---
layout: default
title: Fair Recourse for All: Ensuring Individual and Group Fairness in Counterfactual Explanations
---

# Fair Recourse for All: Ensuring Individual and Group Fairness in Counterfactual Explanations
**arXiv**：[2601.20449v1](https://arxiv.org/abs/2601.20449) · [PDF](https://arxiv.org/pdf/2601.20449.pdf)  
**作者**：Fatima Ezzeddine, Obaida Ammar, Silvia Giordano, Omran Ayoub  

**一句话要点**：提出基于强化学习的公平反事实解释方法，确保个体与群体公平性

**关键词**：反事实解释, 公平性, 强化学习, 可解释人工智能, 个体公平, 群体公平

## 3 点简述
- 核心问题：反事实解释需兼顾个体相似性与跨保护群体的公平性，现有方法常正交处理
- 方法要点：定义个体、群体及混合公平性，采用模型无关的强化学习优化生成公平反事实
- 实验或效果：在三个基准数据集上验证，有效平衡公平性与解释质量，量化不同公平层级的成本

## 摘要（原文）

> Explainable Artificial Intelligence (XAI) is becoming increasingly essential for enhancing the transparency of machine learning (ML) models. Among the various XAI techniques, counterfactual explanations (CFs) hold a pivotal role due to their ability to illustrate how changes in input features can alter an ML model's decision, thereby offering actionable recourse to users. Ensuring that individuals with comparable attributes and those belonging to different protected groups (e.g., demographic) receive similar and actionable recourse options is essential for trustworthy and fair decision-making. In this work, we address this challenge directly by focusing on the generation of fair CFs. Specifically, we start by defining and formulating fairness at: 1) individual fairness, ensuring that similar individuals receive similar CFs, 2) group fairness, ensuring equitable CFs across different protected groups and 3) hybrid fairness, which accounts for both individual and broader group-level fairness. We formulate the problem as an optimization task and propose a novel model-agnostic, reinforcement learning based approach to generate CFs that satisfy fairness constraints at both the individual and group levels, two objectives that are usually treated as orthogonal. As fairness metrics, we extend existing metrics commonly used for auditing ML models, such as equal choice of recourse and equal effectiveness across individuals and groups. We evaluate our approach on three benchmark datasets, showing that it effectively ensures individual and group fairness while preserving the quality of the generated CFs in terms of proximity and plausibility, and quantify the cost of fairness in the different levels separately. Our work opens a broader discussion on hybrid fairness and its role and implications for XAI and beyond CFs.

