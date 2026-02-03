---
layout: default
title: Efficient Epistemic Uncertainty Estimation for Large Language Models via Knowledge Distillation
---

# Efficient Epistemic Uncertainty Estimation for Large Language Models via Knowledge Distillation
**arXiv**：[2602.01956v1](https://arxiv.org/abs/2602.01956) · [PDF](https://arxiv.org/pdf/2602.01956.pdf)  
**作者**：Seonghyeon Park, Jewon Yeom, Jaewon Sok, Jeongjae Park, Heejun Kim, Taesup Kim  

**一句话要点**：提出基于知识蒸馏的高效大语言模型认知不确定性估计框架，以降低幻觉风险。

**关键词**：大语言模型, 认知不确定性估计, 知识蒸馏, 幻觉检测, 高效推理

## 3 点简述
- 核心问题：大语言模型认知不确定性估计计算成本高，难以在安全关键任务中部署。
- 方法要点：利用小规模草稿模型通过Jensen-Shannon和KL散度近似不确定性，结合在线随机蒸馏和数据多样化策略提升效率与准确性。
- 实验或效果：在GSM8K上降低估计误差达37%，幻觉检测性能媲美高成本方法，推理开销可忽略。

## 摘要（原文）

> Quantifying uncertainty in Large Language Models (LLMs) is essential for mitigating hallucinations and enabling risk-aware deployment in safety-critical tasks. However, estimating Epistemic Uncertainty(EU) via Deep Ensembles is computationally prohibitive at the scale of modern models. We propose a framework that leverages the small draft models to efficiently estimate token-level EU, bypassing the need for full-scale ensembling. Theoretically grounded in a Bias-Variance Decomposition, our approach approximates EU via Jensen-Shannon divergence among drafts (variance proxy) and KL divergence between the draft mixture and the target (bias proxy). To further ensure accuracy without significant overhead, we introduce Online Stochastic Distillation (OSD) to efficiently approximate target aggregation and the Data-Diverse Drafts (DDD) strategy to enhance draft diversity for better target approximation. Extensive experiments on GSM8K demonstrate that our method reduces the estimation error (RMSE) by up to 37% compared to baselines. Crucially, our approach achieves Hallucination Detection performance competitive with heavy perturbation-based methods like TokUR while incurring negligible inference costs, offering a practical solution for uncertainty-aware LLM deployment.

