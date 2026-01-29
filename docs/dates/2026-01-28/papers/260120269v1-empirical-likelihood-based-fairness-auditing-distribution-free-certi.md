---
layout: default
title: Empirical Likelihood-Based Fairness Auditing: Distribution-Free Certification and Flagging
---

# Empirical Likelihood-Based Fairness Auditing: Distribution-Free Certification and Flagging
**arXiv**：[2601.20269v1](https://arxiv.org/abs/2601.20269) · [PDF](https://arxiv.org/pdf/2601.20269.pdf)  
**作者**：Jie Tang, Chuanlong Xie, Xianli Zeng, Lixing Zhu  

**一句话要点**：提出基于经验似然的公平性审计框架，用于无分布假设的认证与偏差群体识别

**关键词**：公平性审计, 经验似然, 非参数推断, 算法偏差, 统计认证, 子群体发现

## 3 点简述
- 核心问题：机器学习模型在敏感子群体间存在系统性性能差异，现有审计方法受限于分布假设或计算开销
- 方法要点：采用非参数经验似然方法构建稳健统计量，基于渐近卡方分布进行推断，无需数据分布假设
- 实验或效果：在COMPAS数据集上验证，优于自助法，覆盖率更接近名义水平，计算延迟大幅降低

## 摘要（原文）

> Machine learning models in high-stakes applications, such as recidivism prediction and automated personnel selection, often exhibit systematic performance disparities across sensitive subpopulations, raising critical concerns regarding algorithmic bias. Fairness auditing addresses these risks through two primary functions: certification, which verifies adherence to fairness constraints; and flagging, which isolates specific demographic groups experiencing disparate treatment. However, existing auditing techniques are frequently limited by restrictive distributional assumptions or prohibitive computational overhead. We propose a novel empirical likelihood-based (EL) framework that constructs robust statistical measures for model performance disparities. Unlike traditional methods, our approach is non-parametric; the proposed disparity statistics follow asymptotically chi-square or mixed chi-square distributions, ensuring valid inference without assuming underlying data distributions. This framework uses a constrained optimization profile that admits stable numerical solutions, facilitating both large-scale certification and efficient subpopulation discovery. Empirically, the EL methods outperform bootstrap-based approaches, yielding coverage rates closer to nominal levels while reducing computational latency by several orders of magnitude. We demonstrate the practical utility of this framework on the COMPAS dataset, where it successfully flags intersectional biases, specifically identifying a significantly higher positive prediction rate for African-American males under 25 and a systemic under-prediction for Caucasian females relative to the population mean.

