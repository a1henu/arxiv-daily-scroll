---
layout: default
title: The Paradox of Robustness: Decoupling Rule-Based Logic from Affective Noise in High-Stakes Decision-Making
---

# The Paradox of Robustness: Decoupling Rule-Based Logic from Affective Noise in High-Stakes Decision-Making
**arXiv**：[2601.21439v1](https://arxiv.org/abs/2601.21439) · [PDF](https://arxiv.org/pdf/2601.21439.pdf)  
**作者**：Jon Chun, Katherine Elkins  

**一句话要点**：揭示指令调优大语言模型在高风险决策中逻辑稳定性与情感噪声解耦的稳健性悖论

**关键词**：稳健性悖论, 情感框架效应, 高风险决策, 指令调优模型, 叙事诱导偏见, 逻辑约束满足

## 3 点简述
- 核心问题：大语言模型在提示扰动下脆弱，但在规则约束决策中对情感框架效应的稳健性未知
- 方法要点：通过控制扰动框架在医疗、法律、金融领域量化模型与人类对叙事操纵的抵抗差异
- 实验或效果：模型对情感偏见的效应量近零，比人类稳健110-300倍，显示逻辑约束满足与说服性叙事解耦

## 摘要（原文）

> While Large Language Models (LLMs) are widely documented to be sensitive to minor prompt perturbations and prone to sycophantic alignment with user biases, their robustness in consequential, rule-bound decision-making remains under-explored. In this work, we uncover a striking "Paradox of Robustness": despite their known lexical brittleness, instruction-tuned LLMs exhibit a behavioral and near-total invariance to emotional framing effects. Using a novel controlled perturbation framework across three high-stakes domains (healthcare, law, and finance), we quantify a robustness gap where LLMs demonstrate 110-300 times greater resistance to narrative manipulation than human subjects. Specifically, we find a near-zero effect size for models (Cohen's h = 0.003) compared to the substantial biases observed in humans (Cohen's h in [0.3, 0.8]). This result is highly counterintuitive and suggests the mechanisms driving sycophancy and prompt sensitivity do not necessarily translate to a failure in logical constraint satisfaction. We show that this invariance persists across models with diverse training paradigms. Our findings show that while LLMs may be "brittle" to how a query is formatted, they are remarkably "stable" against why a decision should be biased. Our findings establish that instruction-tuned models can decouple logical rule-adherence from persuasive narratives, offering a source of decision stability that complements, and even potentially de-biases, human judgment in institutional contexts. We release the 162-scenario benchmark, code, and data to facilitate the rigorous evaluation of narrative-induced bias and robustness on GitHub.com.

