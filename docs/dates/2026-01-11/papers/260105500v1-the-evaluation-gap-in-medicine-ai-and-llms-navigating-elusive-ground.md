---
layout: default
title: The Evaluation Gap in Medicine, AI and LLMs: Navigating Elusive Ground Truth & Uncertainty via a Probabilistic Paradigm
---

# The Evaluation Gap in Medicine, AI and LLMs: Navigating Elusive Ground Truth & Uncertainty via a Probabilistic Paradigm
**arXiv**：[2601.05500v1](https://arxiv.org/abs/2601.05500) · [PDF](https://arxiv.org/pdf/2601.05500.pdf)  
**作者**：Aparna Elangovan, Lei Xu, Mahsa Elyasi, Ismail Akdulum, Mehmet Aksakal, Enes Gurun, Brian Hur, Saab Mansour, Ravid Shwartz Ziv, Karin Verspoor, Dan Roth  

**一句话要点**：提出概率范式以解决医学AI评估中因真值不确定性导致的误导性结论

**关键词**：医学AI评估, 真值不确定性, 概率范式, 期望准确率, 分层评估, 专家性能估计

## 3 点简述
- 核心问题：医学AI评估忽略真值答案的不确定性，可能导致非专家与专家性能相似的错误结论
- 方法要点：引入概率范式，定义期望准确率和期望F1来估计专家在真值变异性下的得分
- 实验或效果：建议按真值答案概率分层评估，当总体性能低于80%时分层尤为关键

## 摘要（原文）

> Benchmarking the relative capabilities of AI systems, including Large Language Models (LLMs) and Vision Models, typically ignores the impact of uncertainty in the underlying ground truth answers from experts. This ambiguity is particularly consequential in medicine where uncertainty is pervasive. In this paper, we introduce a probabilistic paradigm to theoretically explain how high certainty in ground truth answers is almost always necessary for even an expert to achieve high scores, whereas in datasets with high variation in ground truth answers there may be little difference between a random labeller and an expert. Therefore, ignoring uncertainty in ground truth evaluation data can result in the misleading conclusion that a non-expert has similar performance to that of an expert. Using the probabilistic paradigm, we thus bring forth the concepts of expected accuracy and expected F1 to estimate the score an expert human or system can achieve given ground truth answer variability.
>   Our work leads to the recommendation that when establishing the capability of a system, results should be stratified by probability of the ground truth answer, typically measured by the agreement rate of ground truth experts. Stratification becomes critical when the overall performance drops below a threshold of 80%. Under stratified evaluation, performance comparison becomes more reliable in high certainty bins, mitigating the effect of the key confounding factor -- uncertainty.

