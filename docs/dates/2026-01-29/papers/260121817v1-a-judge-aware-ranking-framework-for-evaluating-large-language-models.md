---
layout: default
title: A Judge-Aware Ranking Framework for Evaluating Large Language Models without Ground Truth
---

# A Judge-Aware Ranking Framework for Evaluating Large Language Models without Ground Truth
**arXiv**：[2601.21817v1](https://arxiv.org/abs/2601.21817) · [PDF](https://arxiv.org/pdf/2601.21817.pdf)  
**作者**：Mingyuan Xu, Xinzi Tan, Jiawei Wu, Doudou Zhou  

**一句话要点**：提出法官感知排名框架，通过联合估计模型质量和法官可靠性，解决无真值标签下大语言模型评估的偏差问题。

**关键词**：大语言模型评估, 无真值标签排名, 法官可靠性建模, Bradley-Terry-Luce扩展, 不确定性量化, 成对比较

## 3 点简述
- 核心问题：LLM-as-a-judge评估中，法官LLM可靠性差异大，导致排名偏差和不确定性估计误导。
- 方法要点：扩展Bradley-Terry-Luce模型，引入法官特异性判别参数，从成对比较中联合估计潜在模型质量和法官可靠性。
- 实验或效果：在多个基准和新数据集上，提高与人类偏好一致性，数据效率优于未加权基线，并提供校准的不确定性量化。

## 摘要（原文）

> Evaluating large language models (LLMs) on open-ended tasks without ground-truth labels is increasingly done via the LLM-as-a-judge paradigm. A critical but under-modeled issue is that judge LLMs differ substantially in reliability; treating all judges equally can yield biased leaderboards and misleading uncertainty estimates. More data can make evaluation more confidently wrong under misspecified aggregation. We propose a judge-aware ranking framework that extends the Bradley-Terry-Luce model by introducing judge-specific discrimination parameters, jointly estimating latent model quality and judge reliability from pairwise comparisons without reference labels. We establish identifiability up to natural normalizations and prove consistency and asymptotic normality of the maximum likelihood estimator, enabling confidence intervals for score differences and rank comparisons. Across multiple public benchmarks and a newly collected dataset, our method improves agreement with human preferences, achieves higher data efficiency than unweighted baselines, and produces calibrated uncertainty quantification for LLM rankings.

