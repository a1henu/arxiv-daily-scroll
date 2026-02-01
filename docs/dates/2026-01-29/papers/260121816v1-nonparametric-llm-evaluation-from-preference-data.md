---
layout: default
title: Nonparametric LLM Evaluation from Preference Data
---

# Nonparametric LLM Evaluation from Preference Data
**arXiv**：[2601.21816v1](https://arxiv.org/abs/2601.21816) · [PDF](https://arxiv.org/pdf/2601.21816.pdf)  
**作者**：Dennis Frauen, Athiya Deviyani, Mihaela van der Schaar, Stefan Feuerriegel  

**一句话要点**：提出非参数框架DMLEval，基于偏好数据评估大语言模型，支持灵活机器学习与不确定性量化。

**关键词**：大语言模型评估, 偏好数据, 非参数统计, 去偏机器学习, 排名模型, 不确定性量化

## 3 点简述
- 核心问题：现有方法依赖参数假设或缺乏不确定性量化，难以从偏好数据高效评估LLM。
- 方法要点：引入广义平均排名分数（GARS），结合去偏机器学习（DML）进行非参数估计与排名。
- 实验或效果：理论证明与合成/真实数据集验证，支持LLM-as-a-judge并优化数据收集策略。

## 摘要（原文）

> Evaluating the performance of large language models (LLMs) from human preference data is crucial for obtaining LLM leaderboards. However, many existing approaches either rely on restrictive parametric assumptions or lack valid uncertainty quantification when flexible machine learning methods are used. In this paper, we propose a nonparametric statistical framework, DMLEval, for comparing and ranking LLMs from preference data using debiased machine learning (DML). For this, we introduce generalized average ranking scores (GARS), which generalize commonly used ranking models, including the Bradley-Terry model or PageRank/ Rank centrality, with complex human responses such as ties. DMLEval comes with the following advantages: (i) It produces statistically efficient estimates of GARS ranking scores. (ii) It naturally allows the incorporation of black-box machine learning methods for estimation. (iii) It can be combined with pre-trained LLM evaluators (e.g., using LLM-as-a-judge). (iv) It suggests optimal policies for collecting preference data under budget constraints. We demonstrate these advantages both theoretically and empirically using both synthetic and real-world preference datasets. In summary, our framework provides practitioners with powerful, state-of-the-art methods for comparing or ranking LLMs.

