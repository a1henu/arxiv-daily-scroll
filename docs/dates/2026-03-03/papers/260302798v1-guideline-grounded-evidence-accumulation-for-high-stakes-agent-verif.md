---
layout: default
title: Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification
---

# Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification
**arXiv**：[2603.02798v1](https://arxiv.org/abs/2603.02798) · [PDF](https://arxiv.org/pdf/2603.02798.pdf)  
**作者**：Yichi Zhang, Nabeel Seedat, Yinpeng Dong, Peng Cui, Jun Zhu, Mihaela van de Schaar  

**一句话要点**：提出GLEAN框架，通过指南证据积累实现高风险代理决策的可靠验证

**关键词**：代理验证, 指南证据积累, 贝叶斯校准, 临床诊断, 高风险决策, 不确定性触发

## 3 点简述
- 核心问题：LLM代理在高风险决策中缺乏可靠验证，现有方法因领域知识不足和校准有限而表现不佳。
- 方法要点：GLEAN将专家协议转化为轨迹感知的校准正确性信号，评估步骤对齐并聚合多指南评级为代理特征，使用贝叶斯逻辑回归校准为概率。
- 实验或效果：在MIMIC-IV数据集的三疾病临床诊断中，AUROC提升12%，Brier分数降低50%，专家研究认可其实用性。

## 摘要（原文）

> As LLM-powered agents have been used for high-stakes decision-making, such as clinical diagnosis, it becomes critical to develop reliable verification of their decisions to facilitate trustworthy deployment. Yet, existing verifiers usually underperform owing to a lack of domain knowledge and limited calibration. To address this, we establish GLEAN, an agent verification framework with Guideline-grounded Evidence Accumulation that compiles expert-curated protocols into trajectory-informed, well-calibrated correctness signals. GLEAN evaluates the step-wise alignment with domain guidelines and aggregates multi-guideline ratings into surrogate features, which are accumulated along the trajectory and calibrated into correctness probabilities using Bayesian logistic regression. Moreover, the estimated uncertainty triggers active verification, which selectively collects additional evidence for uncertain cases via expanding guideline coverage and performing differential checks. We empirically validate GLEAN with agentic clinical diagnosis across three diseases from the MIMIC-IV dataset, surpassing the best baseline by 12% in AUROC and 50% in Brier score reduction, which confirms the effectiveness in both discrimination and calibration. In addition, the expert study with clinicians recognizes GLEAN's utility in practice.

