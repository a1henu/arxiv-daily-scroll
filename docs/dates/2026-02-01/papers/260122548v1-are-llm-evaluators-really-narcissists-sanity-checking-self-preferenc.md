---
layout: default
title: Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations
---

# Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations
**arXiv**：[2601.22548v1](https://arxiv.org/abs/2601.22548) · [PDF](https://arxiv.org/pdf/2601.22548.pdf)  
**作者**：Dani Roytburg, Matthew Bozoukov, Matthew Nguyen, Mackenzie Puig-Hall, Narmeen Oozeer  

**一句话要点**：提出评估者质量基线以解决LLM自偏好评估中的方法混淆问题

**关键词**：大语言模型评估, 自偏好偏差, 评估者质量基线, 方法混淆, 评估完整性, 噪声数据消除

## 3 点简述
- 核心问题：LLM作为评估者时自偏好偏差难以与实验混淆因素分离，影响评估完整性
- 方法要点：引入评估者质量基线，通过比较评估者错误投票给自身与错误投票给他人的概率来解耦自偏好信号
- 实验或效果：在37,448个查询上测试，仅51%的初始发现保持统计显著性，减少测量误差达89.6%

## 摘要（原文）

> Recent research has shown that large language models (LLM) favor own outputs when acting as judges, undermining the integrity of automated post-training and evaluation workflows. However, it is difficult to disentangle which evaluation biases are explained by narcissism versus general experimental confounds, distorting measurements of self-preference bias. We discover a core methodological confound which could reduce measurement error by 89.6%. Specifically, LLM evaluators may deliver self-preferring verdicts when the judge responds to queries which they completed incorrectly themselves; this would be true regardless of whether one of their responses is their own. To decouple self-preference signals from noisy outputs on hard problems, we introduce an Evaluator Quality Baseline, which compares the probability that a judge incorrectly votes for itself against the probability that it votes for an incorrect response from another model. Evaluating this simple baseline on 37,448 queries, only 51% of initial findings retain statistical significance. Finally, we turn towards characterizing the entropy of "easy" versus "hard" evaluation votes from LLM judges. Our corrective baseline enables future research on self-preference by eliminating noisy data from potential solutions. More widely, this work contributes to the growing body of work on cataloging and isolating judge-bias effects.

