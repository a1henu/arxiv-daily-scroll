---
layout: default
title: Decomposing Physician Disagreement in HealthBench
---

# Decomposing Physician Disagreement in HealthBench
**arXiv**：[2602.22758v1](https://arxiv.org/abs/2602.22758) · [PDF](https://arxiv.org/pdf/2602.22758.pdf)  
**作者**：Satya Borgohain, Roy Mariathas  

**一句话要点**：分解HealthBench中医生分歧以揭示医疗AI评估的结构性限制与可改进方向

**关键词**：医疗AI评估, 医生分歧分解, 方差分析, 不确定性分类, 评估设计改进

## 3 点简述
- 核心问题：分析医疗AI评估数据集HealthBench中医生标签分歧的来源与可解释性。
- 方法要点：通过方差分解、统计检验和不确定性分类，量化分歧的贡献因素。
- 实验或效果：发现81.8%分歧为案例级残差，可减少不确定性（如信息缺失）能显著增加分歧几率，但解释方差有限。

## 摘要（原文）

> We decompose physician disagreement in the HealthBench medical AI evaluation dataset to understand where variance resides and what observable features can explain it. Rubric identity accounts for 15.8% of met/not-met label variance but only 3.6-6.9% of disagreement variance; physician identity accounts for just 2.4%. The dominant 81.8% case-level residual is not reduced by HealthBench's metadata labels (z = -0.22, p = 0.83), normative rubric language (pseudo R^2 = 1.2%), medical specialty (0/300 Tukey pairs significant), surface-feature triage (AUC = 0.58), or embeddings (AUC = 0.485). Disagreement follows an inverted-U with completion quality (AUC = 0.689), confirming physicians agree on clearly good or bad outputs but split on borderline cases. Physician-validated uncertainty categories reveal that reducible uncertainty (missing context, ambiguous phrasing) more than doubles disagreement odds (OR = 2.55, p < 10^(-24)), while irreducible uncertainty (genuine medical ambiguity) has no effect (OR = 1.01, p = 0.90), though even the former explains only ~3% of total variance. The agreement ceiling in medical AI evaluation is thus largely structural, but the reducible/irreducible dissociation suggests that closing information gaps in evaluation scenarios could lower disagreement where inherent clinical ambiguity does not, pointing toward actionable evaluation design improvements.

