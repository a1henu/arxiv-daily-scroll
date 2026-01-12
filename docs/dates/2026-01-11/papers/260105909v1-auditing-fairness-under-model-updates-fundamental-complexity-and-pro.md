---
layout: default
title: Auditing Fairness under Model Updates: Fundamental Complexity and Property-Preserving Updates
---

# Auditing Fairness under Model Updates: Fundamental Complexity and Property-Preserving Updates
**arXiv**：[2601.05909v1](https://arxiv.org/abs/2601.05909) · [PDF](https://arxiv.org/pdf/2601.05909.pdf)  
**作者**：Ayoub Ajarra, Debabrota Basu  

**一句话要点**：提出基于经验属性优化的PAC审计框架，以应对模型更新下的公平性审计复杂性

**关键词**：公平性审计, 模型更新, PAC学习, 统计均等性, SP维度, 经验属性优化

## 3 点简述
- 研究模型自适应更新下群体公平性审计的根本复杂性，关注属性保持的更新策略
- 提出基于EPO神谕的通用PAC审计框架，引入SP维度量化可允许战略更新的复杂度
- 为统计均等性建立分布无关审计界限，并扩展至预测误差和鲁棒风险等其他审计目标

## 摘要（原文）

> As machine learning models become increasingly embedded in societal infrastructure, auditing them for bias is of growing importance. However, in real-world deployments, auditing is complicated by the fact that model owners may adaptively update their models in response to changing environments, such as financial markets. These updates can alter the underlying model class while preserving certain properties of interest, raising fundamental questions about what can be reliably audited under such shifts.
>   In this work, we study group fairness auditing under arbitrary updates. We consider general shifts that modify the pre-audit model class while maintaining invariance of the audited property. Our goals are two-fold: (i) to characterize the information complexity of allowable updates, by identifying which strategic changes preserve the property under audit; and (ii) to efficiently estimate auditing properties, such as group fairness, using a minimal number of labeled samples.
>   We propose a generic framework for PAC auditing based on an Empirical Property Optimization (EPO) oracle. For statistical parity, we establish distribution-free auditing bounds characterized by the SP dimension, a novel combinatorial measure that captures the complexity of admissible strategic updates. Finally, we demonstrate that our framework naturally extends to other auditing objectives, including prediction error and robust risk.

