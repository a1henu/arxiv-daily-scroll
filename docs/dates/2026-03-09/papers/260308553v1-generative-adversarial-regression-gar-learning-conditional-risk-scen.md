---
layout: default
title: Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios
---

# Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios
**arXiv**：[2603.08553v1](https://arxiv.org/abs/2603.08553) · [PDF](https://arxiv.org/pdf/2603.08553.pdf)  
**作者**：Saeed Asadi, Jonathan Yu-Meng Li  

**一句话要点**：提出生成对抗回归框架，通过生成器学习条件风险场景以对齐下游风险目标。

**关键词**：生成对抗回归, 条件风险学习, 极小极大优化, 风险场景生成, 可引出函数

## 3 点简述
- 核心问题：如何生成条件风险场景以匹配可引出函数（如分位数、期望分位数）的风险目标。
- 方法要点：采用极小极大公式，训练生成器使策略诱导风险与真实数据一致，确保跨策略鲁棒性。
- 实验或效果：在S&P 500数据上，GAR优于无条件、计量经济学和直接预测基线，保持风险稳定。

## 摘要（原文）

> We propose Generative Adversarial Regression (GAR), a framework for learning conditional risk scenarios through generators aligned with downstream risk objectives. GAR builds on a regression characterization of conditional risk for elicitable functionals, including quantiles, expectiles, and jointly elicitable pairs. We extend this principle from point prediction to generative modeling by training generators whose policy-induced risk matches that of real data under the same context. To ensure robustness across all policies, GAR adopts a minimax formulation in which an adversarial policy identifies worst-case discrepancies in risk evaluation while the generator adapts to eliminate them. This structure preserves alignment with the risk functional across a broad class of policies rather than a fixed, pre-specified set. We illustrate GAR through a tail-risk instantiation based on jointly elicitable $(\mathrm{VaR}, \mathrm{ES})$ objectives. Experiments on S\&P 500 data show that GAR produces scenarios that better preserve downstream risk than unconditional, econometric, and direct predictive baselines while remaining stable under adversarially selected policies.

