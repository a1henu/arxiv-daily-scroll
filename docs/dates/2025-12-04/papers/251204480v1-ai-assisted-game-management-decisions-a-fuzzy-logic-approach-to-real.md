---
layout: default
title: AI-Assisted Game Management Decisions: A Fuzzy Logic Approach to Real-Time Substituitions
---

# AI-Assisted Game Management Decisions: A Fuzzy Logic Approach to Real-Time Substituitions
**arXiv**：[2512.04480v1](https://arxiv.org/abs/2512.04480) · [PDF](https://arxiv.org/pdf/2512.04480.pdf)  
**作者**：Pedro Passos  

**一句话要点**：提出基于模糊逻辑的决策支持系统，用于实时足球换人优化，以解决传统模型依赖历史偏差的问题。

**关键词**：模糊逻辑决策支持系统, 实时换人优化, PlayeRank指标改进, 足球战术分析, 可解释人工智能

## 3 点简述
- 核心问题：精英足球换人决策依赖直觉或预测模型，易受历史偏差影响，缺乏实时客观指导。
- 方法要点：采用模糊逻辑构建规则推理引擎，结合改进的PlayeRank指标、生理疲劳和上下文变量，计算动态换人优先级。
- 实验或效果：通过2018年世界杯案例验证，系统与专家共识一致，并识别出人类决策忽略的高风险场景，如FAGNER和Lukaku悖论。

## 摘要（原文）

> In elite soccer, substitution decisions entail significant financial and sporting consequences yet remain heavily reliant on intuition or predictive models that merely mimic historical biases. This paper introduces a Fuzzy Logic based Decision Support System (DSS) designed for real time, prescriptive game management. Unlike traditional Machine Learning approaches that encounter a predictive ceiling by attempting to replicate human behavior, our system audits performance through an objective, rule based inference engine. We propose a methodological advancement by reformulating the PlayeRank metric into a Cumulative Mean with Role Aware Normalization, eliminating the play time exposure bias inherent in cumulative sum models to enable accurate intra match comparison. The system integrates this refined metric with physiological proxies (fatigue) and contextual variables (disciplinary risk modulated by tactical role) to calculate a dynamic Substitution Priority (P final). Validation via a case study of the 2018 FIFA World Cup match between Brazil and Belgium demonstrates the system's ecological validity: it not only aligned with expert consensus on executed substitutions (for example Gabriel Jesus) but, crucially, identified high risk scenarios ignored by human decision makers. Specifically, the model flagged the "FAGNER Paradox" - a maximum priority defensive risk - minutes before a critical yellow card, and detected the "Lukaku Paradox", where an isolated assist masked a severe drop in participation. These results confirm that Fuzzy Logic offers a transparent, explainable, and superior alternative to black box models for optimizing real time tactical decisions.

