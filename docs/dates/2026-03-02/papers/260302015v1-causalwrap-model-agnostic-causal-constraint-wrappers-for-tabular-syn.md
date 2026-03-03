---
layout: default
title: CausalWrap: Model-Agnostic Causal Constraint Wrappers for Tabular Synthetic Data
---

# CausalWrap: Model-Agnostic Causal Constraint Wrappers for Tabular Synthetic Data
**arXiv**：[2603.02015v1](https://arxiv.org/abs/2603.02015) · [PDF](https://arxiv.org/pdf/2603.02015.pdf)  
**作者**：Amir Asiaee, Zhuohui J. Liang, Chao Yan  

**一句话要点**：提出CausalWrap以增强表格合成数据在因果推理中的结构保真度

**关键词**：表格合成数据, 因果推理, 模型无关包装器, 结构保真度, 后处理校正

## 3 点简述
- 表格合成数据生成器通常仅匹配观测分布，导致因果分析和分布外推理的结构关系保留不足。
- CausalWrap是一种模型无关的包装器，通过注入部分因果知识，对基础生成器样本进行轻量级后处理校正。
- 在模拟、半合成和真实世界数据集上验证，CausalWrap显著提升因果保真度，同时保持常规效用。

## 摘要（原文）

> Tabular synthetic data generators are typically trained to match observational distributions, which can yield high conventional utility (e.g., column correlations, predictive accuracy) yet poor preservation of structural relations relevant to causal analysis and out-of-distribution (OOD) reasoning. When the downstream use of synthetic data involves causal reasoning -- estimating treatment effects, evaluating policies, or testing mediation pathways -- merely matching the observational distribution is insufficient: structural fidelity and treatment-mechanism preservation become essential. We propose CausalWrap (CW), a model-agnostic wrapper that injects partial causal knowledge (PCK) -- trusted edges, forbidden edges, and qualitative/monotonic constraints -- into any pretrained base generator (GAN, VAE, or diffusion model), without requiring access to its internals. CW learns a lightweight, differentiable post-hoc correction map applied to samples from the base generator, optimized with causal penalty terms under an augmented-Lagrangian schedule. We provide theoretical results connecting penalty-based optimization to constraint satisfaction and relating approximate factorization to joint distributional control. We validate CW on simulated structural causal models (SCMs) with known ground-truth interventions, semi-synthetic causal benchmarks (IHDP and an ACIC-style suite), and a real-world ICU cohort (MIMIC-IV) with expert-elicited partial graphs. CW improves causal fidelity across diverse base generators -- e.g., reducing average treatment effect (ATE) error by up to 63% on ACIC and lifting ATE agreement from 0.00 to 0.38 on the intensive care unit (ICU) cohort -- while largely retaining conventional utility.

