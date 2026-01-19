---
layout: default
title: FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling
---

# FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling
**arXiv**：[2601.11134v1](https://arxiv.org/abs/2601.11134) · [PDF](https://arxiv.org/pdf/2601.11134.pdf)  
**作者**：Sultan Amed, Tanmay Sen, Sayantan Banerjee  

**一句话要点**：提出联邦生存学习框架FSL-BDP，用于信用风险建模，结合贝叶斯差分隐私保护数据隐私。

**关键词**：联邦学习, 生存分析, 差分隐私, 信用风险建模, 数据隐私保护

## 3 点简述
- 核心问题：传统违约预测忽略违约时间，且集中训练违反数据保护法规。
- 方法要点：采用联邦学习框架，结合贝叶斯差分隐私，在不集中敏感数据下建模违约时间轨迹。
- 实验或效果：在三个真实数据集上，贝叶斯差分隐私在联邦设置中表现优于经典差分隐私，接近非隐私性能。

## 摘要（原文）

> Credit risk models are a critical decision-support tool for financial institutions, yet tightening data-protection rules (e.g., GDPR, CCPA) increasingly prohibit cross-border sharing of borrower data, even as these models benefit from cross-institution learning. Traditional default prediction suffers from two limitations: binary classification ignores default timing, treating early defaulters (high loss) equivalently to late defaulters (low loss), and centralized training violates emerging regulatory constraints. We propose a Federated Survival Learning framework with Bayesian Differential Privacy (FSL-BDP) that models time-to-default trajectories without centralizing sensitive data. The framework provides Bayesian (data-dependent) differential privacy (DP) guarantees while enabling institutions to jointly learn risk dynamics. Experiments on three real-world credit datasets (LendingClub, SBA, Bondora) show that federation fundamentally alters the relative effectiveness of privacy mechanisms. While classical DP performs better than Bayesian DP in centralized settings, the latter benefits substantially more from federation (+7.0\% vs +1.4\%), achieving near parity of non-private performance and outperforming classical DP in the majority of participating clients. This ranking reversal yields a key decision-support insight: privacy mechanism selection should be evaluated in the target deployment architecture, rather than centralized benchmarks. These findings provide actionable guidance for practitioners designing privacy-preserving decision support systems in regulated, multi-institutional environments.

