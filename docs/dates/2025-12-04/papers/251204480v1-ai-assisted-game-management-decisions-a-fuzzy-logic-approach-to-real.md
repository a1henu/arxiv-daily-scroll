---
layout: default
title: AI-Assisted Game Management Decisions: A Fuzzy Logic Approach to Real-Time Substituitions
---

# AI-Assisted Game Management Decisions: A Fuzzy Logic Approach to Real-Time Substituitions
**arXiv**：[2512.04480v1](https://arxiv.org/abs/2512.04480) · [PDF](https://arxiv.org/pdf/2512.04480.pdf)  
**作者**：Pedro Passos  

**一句话要点**：提出基于模糊逻辑的决策支持系统，用于实时足球换人优化

**关键词**：模糊逻辑, 决策支持系统, 实时换人, 足球分析, PlayeRank指标

## 3 点简述
- 核心问题：传统足球换人决策依赖直觉或预测模型，存在偏见和透明度不足。
- 方法要点：采用模糊逻辑构建规则推理引擎，结合改进的PlayeRank指标和生理上下文变量。
- 实验或效果：通过2018世界杯案例验证，系统能识别高风险场景并匹配专家共识。

## 摘要（原文）

> In elite soccer, substitution decisions entail significant financial and sporting consequences yet remain heavily reliant on intuition or predictive models that merely mimic historical biases. This paper introduces a Fuzzy Logic based Decision Support System (DSS) designed for real time, prescriptive game management. Unlike traditional Machine Learning approaches that encounter a predictive ceiling by attempting to replicate human behavior, our system audits performance through an objective, rule based inference engine. We propose a methodological advancement by reformulating the PlayeRank metric into a Cumulative Mean with Role Aware Normalization, eliminating the play time exposure bias inherent in cumulative sum models to enable accurate intra match comparison. The system integrates this refined metric with physiological proxies (fatigue) and contextual variables (disciplinary risk modulated by tactical role) to calculate a dynamic Substitution Priority (P final). Validation via a case study of the 2018 FIFA World Cup match between Brazil and Belgium demonstrates the system's ecological validity: it not only aligned with expert consensus on executed substitutions (for example Gabriel Jesus) but, crucially, identified high risk scenarios ignored by human decision makers. Specifically, the model flagged the "FAGNER Paradox" - a maximum priority defensive risk - minutes before a critical yellow card, and detected the "Lukaku Paradox", where an isolated assist masked a severe drop in participation. These results confirm that Fuzzy Logic offers a transparent, explainable, and superior alternative to black box models for optimizing real time tactical decisions.

