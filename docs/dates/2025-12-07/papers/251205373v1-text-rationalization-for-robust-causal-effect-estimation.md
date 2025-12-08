---
layout: default
title: Text Rationalization for Robust Causal Effect Estimation
---

# Text Rationalization for Robust Causal Effect Estimation
**arXiv**：[2512.05373v1](https://arxiv.org/abs/2512.05373) · [PDF](https://arxiv.org/pdf/2512.05373.pdf)  
**作者**：Lijinghua Zhang, Hengrui Cai  

**一句话要点**：提出混淆感知令牌合理化框架，以解决文本数据在因果效应估计中的正性假设违反问题。

**关键词**：因果推断, 文本数据, 正性假设, 令牌选择, 混淆调整, MIMIC-III

## 3 点简述
- 核心问题：高维文本特征导致正性假设违反，引发倾向得分极端化和估计方差膨胀。
- 方法要点：通过残差独立性诊断选择稀疏必要令牌子集，保留混淆信息以保障无混淆性。
- 实验或效果：在合成数据和MIMIC-III数据库实验中，相比基线方法，提供更准确、稳定和可解释的估计。

## 摘要（原文）

> Recent advances in natural language processing have enabled the increasing use of text data in causal inference, particularly for adjusting confounding factors in treatment effect estimation. Although high-dimensional text can encode rich contextual information, it also poses unique challenges for causal identification and estimation. In particular, the positivity assumption, which requires sufficient treatment overlap across confounder values, is often violated at the observational level, when massive text is represented in feature spaces. Redundant or spurious textual features inflate dimensionality, producing extreme propensity scores, unstable weights, and inflated variance in effect estimates. We address these challenges with Confounding-Aware Token Rationalization (CATR), a framework that selects a sparse necessary subset of tokens using a residual-independence diagnostic designed to preserve confounding information sufficient for unconfoundedness. By discarding irrelevant texts while retaining key signals, CATR mitigates observational-level positivity violations and stabilizes downstream causal effect estimators. Experiments on synthetic data and a real-world study using the MIMIC-III database demonstrate that CATR yields more accurate, stable, and interpretable causal effect estimates than existing baselines.

