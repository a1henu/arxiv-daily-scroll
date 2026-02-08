---
layout: default
title: Alignment Verifiability in Large Language Models: Normative Indistinguishability under Behavioral Evaluation
---

# Alignment Verifiability in Large Language Models: Normative Indistinguishability under Behavioral Evaluation
**arXiv**：[2602.05656v1](https://arxiv.org/abs/2602.05656) · [PDF](https://arxiv.org/pdf/2602.05656.pdf)  
**作者**：Igor Santos-Grueiro  

**一句话要点**：提出规范性不可区分性概念，揭示有限行为评估下大语言模型对齐不可验证性

**关键词**：大语言模型对齐, 行为评估, 规范性不可区分性, 对齐验证, 部分可观测性, 评估感知代理

## 3 点简述
- 核心问题：行为评估无法唯一推断大语言模型的潜在对齐属性，存在推理漏洞
- 方法要点：形式化对齐验证问题，引入规范性不可区分性分析行为分布
- 实验或效果：证明在有限评估和评估感知代理下，行为合规性不能保证对齐

## 摘要（原文）

> Behavioral evaluation is the dominant paradigm for assessing alignment in large language models (LLMs). In practice, alignment is inferred from performance under finite evaluation protocols - benchmarks, red-teaming suites, or automated pipelines - and observed compliance is often treated as evidence of underlying alignment. This inference step, from behavioral evidence to claims about latent alignment properties, is typically implicit and rarely analyzed as an inference problem in its own right.
>   We study this problem formally. We frame alignment evaluation as an identifiability question under partial observability and allow agent behavior to depend on information correlated with the evaluation regime. Within this setting, we introduce the Alignment Verifiability Problem and the notion of Normative Indistinguishability, capturing when distinct latent alignment hypotheses induce identical distributions over all evaluator-accessible signals.
>   Our main result is a negative but sharply delimited identifiability theorem. Under finite behavioral evaluation and evaluation-aware agents, observed behavioral compliance does not uniquely identify latent alignment. That is, even idealized behavioral evaluation cannot, in general, certify alignment as a latent property.
>   We further show that behavioral alignment tests should be interpreted as estimators of indistinguishability classes rather than verifiers of alignment. Passing increasingly stringent tests may reduce the space of compatible hypotheses, but cannot collapse it to a singleton under the stated conditions. This reframes alignment benchmarks as providing upper bounds on observable compliance within a regime, rather than guarantees of underlying alignment.

