---
layout: default
title: Conformal Tradeoffs: Guarantees Beyond Coverage
---

# Conformal Tradeoffs: Guarantees Beyond Coverage
**arXiv**：[2602.18045v1](https://arxiv.org/abs/2602.18045) · [PDF](https://arxiv.org/pdf/2602.18045.pdf)  
**作者**：Petrus H. Zwart  

**一句话要点**：提出超越覆盖率的保形预测操作认证框架，解决部署中承诺与延迟的权衡问题。

**关键词**：保形预测, 操作认证, 有限样本保证, 部署权衡, 校准审计, 毒性预测

## 3 点简述
- 核心问题：保形预测部署需平衡覆盖率、承诺频率和错误暴露等操作量，边际覆盖率不足。
- 方法要点：开发小样本Beta校正和校准-审计两阶段设计，提供有限窗口操作量认证。
- 实验或效果：在Tox21毒性预测和水溶性筛选数据集上演示操作菜单和不确定性包络。

## 摘要（原文）

> Deployed conformal predictors are long-lived decision infrastructure operating over finite operational windows. The real-world question is not only ``Does the true label lie in the prediction set at the target rate?'' (marginal coverage), but ``How often does the system commit versus defer? What error exposure does it induce when it acts? How do these rates trade off?'' Marginal coverage does not determine these deployment-facing quantities: the same calibrated thresholds can yield different operational profiles depending on score geometry. We provide a framework for operational certification and planning beyond coverage with three contributions. (1) Small-Sample Beta Correction (SSBC): we invert the exact finite-sample Beta/rank law for split conformal to map a user request $(α^\star,δ)$ to a calibrated grid point with PAC-style semantics, yielding explicit finite-window coverage guarantees. (2) Calibrate-and-Audit: since no distribution-free pivot exists for rates beyond coverage, we introduce a two-stage design in which an independent audit set produces a reusable region -- label table and certified finite-window envelopes (Binomial/Beta-Binomial) for operational quantities -- commitment frequency, deferral, decisive error exposure, and commit purity -- via linear projection. (3) Geometric characterization: we describe feasibility constraints, regime boundaries (hedging vs.\ rejection), and cost-coherence conditions induced by a fixed conformal partition, explaining why operational rates are coupled and how calibration navigates their trade-offs. The output is an auditable operational menu: for a fixed scoring model, we trace attainable operational profiles across calibration settings and attach finite-window uncertainty envelopes. We demonstrate the approach on Tox21 toxicity prediction (12 endpoints) and aqueous solubility screening using AquaSolDB.

