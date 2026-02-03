---
layout: default
title: SafePred: A Predictive Guardrail for Computer-Using Agents via World Models
---

# SafePred: A Predictive Guardrail for Computer-Using Agents via World Models
**arXiv**：[2602.01725v1](https://arxiv.org/abs/2602.01725) · [PDF](https://arxiv.org/pdf/2602.01725.pdf)  
**作者**：Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang  

**一句话要点**：提出SafePred预测护栏框架，通过世界模型对齐未来风险与当前决策，以解决计算机使用代理的长时风险问题。

**关键词**：计算机使用代理, 预测护栏, 世界模型, 风险预测, 决策优化, 安全策略

## 3 点简述
- 核心问题：现有反应式护栏无法预防长时风险，如延迟性高风险后果。
- 方法要点：基于安全策略和世界模型预测短时与长时风险，并通过干预和重规划优化决策。
- 实验或效果：实验显示显著减少高风险行为，安全性能超97.6%，任务效用提升达21.4%。

## 摘要（原文）

> With the widespread deployment of Computer-using Agents (CUAs) in complex real-world environments, prevalent long-term risks often lead to severe and irreversible consequences. Most existing guardrails for CUAs adopt a reactive approach, constraining agent behavior only within the current observation space. While these guardrails can prevent immediate short-term risks (e.g., clicking on a phishing link), they cannot proactively avoid long-term risks: seemingly reasonable actions can lead to high-risk consequences that emerge with a delay (e.g., cleaning logs leads to future audits being untraceable), which reactive guardrails cannot identify within the current observation space. To address these limitations, we propose a predictive guardrail approach, with the core idea of aligning predicted future risks with current decisions. Based on this approach, we present SafePred, a predictive guardrail framework for CUAs that establishes a risk-to-decision loop to ensure safe agent behavior. SafePred supports two key abilities: (1) Short- and long-term risk prediction: by using safety policies as the basis for risk prediction, SafePred leverages the prediction capability of the world model to generate semantic representations of both short-term and long-term risks, thereby identifying and pruning actions that lead to high-risk states; (2) Decision optimization: translating predicted risks into actionable safe decision guidances through step-level interventions and task-level re-planning. Extensive experiments show that SafePred significantly reduces high-risk behaviors, achieving over 97.6% safety performance and improving task utility by up to 21.4% compared with reactive baselines.

