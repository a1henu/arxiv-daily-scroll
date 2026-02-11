---
layout: default
title: Causal Identification in Multi-Task Demand Learning with Confounding
---

# Causal Identification in Multi-Task Demand Learning with Confounding
**arXiv**：[2602.09969v1](https://arxiv.org/abs/2602.09969) · [PDF](https://arxiv.org/pdf/2602.09969.pdf)  
**作者**：Varun Gupta, Vijay Kamble  

**一句话要点**：提出决策条件掩码结果元学习以解决多任务需求学习中的内生性混淆问题

**关键词**：多任务学习, 因果识别, 内生性, 需求估计, 元学习, 零售定价

## 3 点简述
- 研究多任务需求学习中的内生性混淆，历史价格与未观测需求因素相关导致因果识别失败
- 提出DCMOML框架，通过设计元学习器信息集，在价格自适应限制下实现因果参数的条件均值识别
- 为小样本、内生价格的大规模需求估计提供理论保证，支持数据驱动定价模型部署

## 摘要（原文）

> We study a canonical multi-task demand learning problem motivated by retail pricing, in which a firm seeks to estimate heterogeneous linear price-response functions across a large collection of decision contexts. Each context is characterized by rich observable covariates yet typically exhibits only limited historical price variation, motivating the use of multi-task learning to borrow strength across tasks. A central challenge in this setting is endogeneity: historical prices are chosen by managers or algorithms and may be arbitrarily correlated with unobserved, task-level demand determinants. Under such confounding by latent fundamentals, commonly used approaches, such as pooled regression and meta-learning, fail to identify causal price effects.
>   We propose a new estimation framework that achieves causal identification despite arbitrary dependence between prices and latent task structure. Our approach, Decision-Conditioned Masked-Outcome Meta-Learning (DCMOML), involves carefully designing the information set of a meta-learner to leverage cross-task heterogeneity while accounting for endogenous decision histories. Under a mild restriction on price adaptivity in each task, we establish that this method identifies the conditional mean of the task-specific causal parameters given the designed information set. Our results provide guarantees for large-scale demand estimation with endogenous prices and small per-task samples, offering a principled foundation for deploying causal, data-driven pricing models in operational environments.

