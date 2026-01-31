---
layout: default
title: Within-Model vs Between-Prompt Variability in Large Language Models for Creative Tasks
---

# Within-Model vs Between-Prompt Variability in Large Language Models for Creative Tasks
**arXiv**：[2601.21339v1](https://arxiv.org/abs/2601.21339) · [PDF](https://arxiv.org/pdf/2601.21339.pdf)  
**作者**：Jennifer Haase, Jana Gonnermann-Müller, Paul H. P. Hanel, Nicolas Leins, Thomas Kosch, Jan Mendling, Sebastian Pokutta  

**一句话要点**：评估大语言模型在创意任务中提示、模型选择和随机性对输出变异的影响

**关键词**：大语言模型, 输出变异分析, 创意任务评估, 提示工程, 采样随机性

## 3 点简述
- 核心问题：探究LLM输出变异中提示、模型选择和采样随机性的相对贡献
- 方法要点：在12个LLM上使用10个创意提示，每个提示采样100次，共12,000个样本
- 实验或效果：输出质量（原创性）变异主要由提示和模型选择解释，输出数量（流畅性）变异主要由模型选择和模型内变异主导

## 摘要（原文）

> How much of LLM output variance is explained by prompts versus model choice versus stochasticity through sampling? We answer this by evaluating 12 LLMs on 10 creativity prompts with 100 samples each (N = 12,000). For output quality (originality), prompts explain 36.43% of variance, comparable to model choice (40.94%). But for output quantity (fluency), model choice (51.25%) and within-LLM variance (33.70%) dominate, with prompts explaining only 4.22%. Prompts are powerful levers for steering output quality, but given the substantial within-LLM variance (10-34%), single-sample evaluations risk conflating sampling noise with genuine prompt or model effects.

