---
layout: default
title: SurvKAN: A Fully Parametric Survival Model Based on Kolmogorov-Arnold Networks
---

# SurvKAN: A Fully Parametric Survival Model Based on Kolmogorov-Arnold Networks
**arXiv**：[2602.02179v1](https://arxiv.org/abs/2602.02179) · [PDF](https://arxiv.org/pdf/2602.02179.pdf)  
**作者**：Marina Mastroleo, Alberto Archetti, Federico Mastroleo, Matteo Matteucci  

**一句话要点**：提出SurvKAN，一种基于KAN的全参数生存模型，用于临床时间-事件预测，消除比例风险约束。

**关键词**：生存分析, Kolmogorov-Arnold网络, 全参数模型, 临床预测, 可解释性, 时间-事件预测

## 3 点简述
- 核心问题：传统生存模型如Cox依赖线性关系和比例风险假设，难以捕捉真实临床动态，而深度学习模型牺牲可解释性。
- 方法要点：SurvKAN将时间作为KAN的显式输入，直接预测对数风险函数，通过可学习单变量函数保持特征随时间影响的可解释性。
- 实验或效果：在标准生存基准测试中，SurvKAN在一致性和校准指标上达到竞争性或优于经典和先进基线，可解释性分析揭示临床相关模式。

## 摘要（原文）

> Accurate prediction of time-to-event outcomes is critical for clinical decision-making, treatment planning, and resource allocation in modern healthcare. While classical survival models such as Cox remain widely adopted in standard practice, they rely on restrictive assumptions, including linear covariate relationships and proportional hazards over time, that often fail to capture real-world clinical dynamics. Recent deep learning approaches like DeepSurv and DeepHit offer improved expressivity but sacrifice interpretability, limiting clinical adoption where trust and transparency are paramount. Hybrid models incorporating Kolmogorov-Arnold Networks (KANs), such as CoxKAN, have begun to address this trade-off but remain constrained by the semi-parametric Cox framework. In this work we introduce SurvKAN, a fully parametric, time-continuous survival model based on KAN architectures that eliminates the proportional hazards constraint. SurvKAN treats time as an explicit input to a KAN that directly predicts the log-hazard function, enabling end-to-end training on the full survival likelihood. Our architecture preserves interpretability through learnable univariate functions that indicate how individual features influence risk over time. Extensive experiments on standard survival benchmarks demonstrate that SurvKAN achieves competitive or superior performance compared to classical and state-of-the-art baselines across concordance and calibration metrics. Additionally, interpretability analyses reveal clinically meaningful patterns that align with medical domain knowledge.

