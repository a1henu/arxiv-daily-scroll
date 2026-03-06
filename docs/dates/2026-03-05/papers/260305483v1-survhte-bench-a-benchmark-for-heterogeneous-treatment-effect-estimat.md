---
layout: default
title: SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis
---

# SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis
**arXiv**：[2603.05483v1](https://arxiv.org/abs/2603.05483) · [PDF](https://arxiv.org/pdf/2603.05483.pdf)  
**作者**：Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss, George H. Chen  

**一句话要点**：提出SurvHTE-Bench基准，用于评估生存分析中异质处理效应估计方法。

**关键词**：生存分析, 异质处理效应, 基准测试, 因果推断, 删失数据

## 3 点简述
- 核心问题：生存分析中异质处理效应估计因删失、反事实缺失和复杂识别假设而面临挑战。
- 方法要点：基准包含合成、半合成和真实数据集，系统比较现有方法在不同条件下的性能。
- 实验或效果：首次在多样设置下提供严格比较，支持公平、可复现和可扩展的评估。

## 摘要（原文）

> Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragmented and inconsistent. We introduce SurvHTE-Bench, the first comprehensive benchmark for HTE estimation with censored outcomes. The benchmark spans (i) a modular suite of synthetic datasets with known ground truth, systematically varying causal assumptions and survival dynamics, (ii) semi-synthetic datasets that pair real-world covariates with simulated treatments and outcomes, and (iii) real-world datasets from a twin study (with known ground truth) and from an HIV clinical trial. Across synthetic, semi-synthetic, and real-world settings, we provide the first rigorous comparison of survival HTE methods under diverse conditions and realistic assumption violations. SurvHTE-Bench establishes a foundation for fair, reproducible, and extensible evaluation of causal survival methods. The data and code of our benchmark are available at: https://github.com/Shahriarnz14/SurvHTE-Bench .

