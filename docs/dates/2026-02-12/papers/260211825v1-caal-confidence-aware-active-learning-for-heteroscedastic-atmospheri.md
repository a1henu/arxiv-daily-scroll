---
layout: default
title: CAAL: Confidence-Aware Active Learning for Heteroscedastic Atmospheric Regression
---

# CAAL: Confidence-Aware Active Learning for Heteroscedastic Atmospheric Regression
**arXiv**：[2602.11825v1](https://arxiv.org/abs/2602.11825) · [PDF](https://arxiv.org/pdf/2602.11825.pdf)  
**作者**：Fei Jiang, Jiyang Xia, Junjie Yu, Mingfei Sun, Hugh Coe, David Topping, Dantong Liu, Zhenhui Jessie Li, Zhonghua Zheng  

**一句话要点**：提出置信感知主动学习框架CAAL，以解决异方差大气回归中样本选择效率低的问题

**关键词**：主动学习, 异方差回归, 不确定性估计, 大气科学, 样本选择, 置信感知

## 3 点简述
- 核心问题：大气粒子属性标注成本高，异方差噪声导致传统主动学习浪费预算于噪声主导区域
- 方法要点：通过解耦不确定性训练目标稳定估计，并设计置信感知获取函数动态加权认知不确定性
- 实验或效果：在粒子解析模拟和真实观测中，CAAL优于标准主动学习基线，提升数据库扩展效率

## 摘要（原文）

> Quantifying the impacts of air pollution on health and climate relies on key atmospheric particle properties such as toxicity and hygroscopicity. However, these properties typically require complex observational techniques or expensive particle-resolved numerical simulations, limiting the availability of labeled data. We therefore estimate these hard-to-measure particle properties from routinely available observations (e.g., air pollutant concentrations and meteorological conditions). Because routine observations only indirectly reflect particle composition and structure, the mapping from routine observations to particle properties is noisy and input-dependent, yielding a heteroscedastic regression setting. With a limited and costly labeling budget, the central challenge is to select which samples to measure or simulate. While active learning is a natural approach, most acquisition strategies rely on predictive uncertainty. Under heteroscedastic noise, this signal conflates reducible epistemic uncertainty with irreducible aleatoric uncertainty, causing limited budgets to be wasted in noise-dominated regions. To address this challenge, we propose a confidence-aware active learning framework (CAAL) for efficient and robust sample selection in heteroscedastic settings. CAAL consists of two components: a decoupled uncertainty-aware training objective that separately optimises the predictive mean and noise level to stabilise uncertainty estimation, and a confidence-aware acquisition function that dynamically weights epistemic uncertainty using predicted aleatoric uncertainty as a reliability signal. Experiments on particle-resolved numerical simulations and real atmospheric observations show that CAAL consistently outperforms standard AL baselines. The proposed framework provides a practical and general solution for the efficient expansion of high-cost atmospheric particle property databases.

