---
layout: default
title: BenchOverflow: Measuring Overflow in Large Language Models via Plain-Text Prompts
---

# BenchOverflow: Measuring Overflow in Large Language Models via Plain-Text Prompts
**arXiv**：[2601.08490v1](https://arxiv.org/abs/2601.08490) · [PDF](https://arxiv.org/pdf/2601.08490.pdf)  
**作者**：Erin Feiglin, Nir Hutnik, Raz Lapid  

**一句话要点**：提出BenchOverflow基准以评估大语言模型在普通文本提示下的输出溢出问题

**关键词**：大语言模型, 输出溢出, 基准测试, 长度控制, 成本优化, 可持续性

## 3 点简述
- 核心问题：大语言模型在普通交互中产生过度输出，增加成本、延迟和环境负担
- 方法要点：设计九种非对抗性文本提示策略，通过标准化协议量化输出长度分布
- 实验或效果：评估九种模型，发现输出长度右移和重尾，轻量缓解措施有效降低溢出风险

## 摘要（原文）

> We investigate a failure mode of large language models (LLMs) in which plain-text prompts elicit excessive outputs, a phenomenon we term Overflow. Unlike jailbreaks or prompt injection, Overflow arises under ordinary interaction settings and can lead to elevated serving cost, latency, and cross-user performance degradation, particularly when scaled across many requests. Beyond usability, the stakes are economic and environmental: unnecessary tokens increase per-request cost and energy consumption, compounding into substantial operational spend and carbon footprint at scale. Moreover, Overflow represents a practical vector for compute amplification and service degradation in shared environments. We introduce BenchOverflow, a model-agnostic benchmark of nine plain-text prompting strategies that amplify output volume without adversarial suffixes or policy circumvention. Using a standardized protocol with a fixed budget of 5000 new tokens, we evaluate nine open- and closed-source models and observe pronounced rightward shifts and heavy tails in length distributions. Cap-saturation rates (CSR@1k/3k/5k) and empirical cumulative distribution functions (ECDFs) quantify tail risk; within-prompt variance and cross-model correlations show that Overflow is broadly reproducible yet heterogeneous across families and attack vectors. A lightweight mitigation-a fixed conciseness reminder-attenuates right tails and lowers CSR for all strategies across the majority of models. Our findings position length control as a measurable reliability, cost, and sustainability concern rather than a stylistic quirk. By enabling standardized comparison of length-control robustness across models, BenchOverflow provides a practical basis for selecting deployments that minimize resource waste and operating expense, and for evaluating defenses that curb compute amplification without eroding task performance.

