---
layout: default
title: ErrEval: Error-Aware Evaluation for Question Generation through Explicit Diagnostics
---

# ErrEval: Error-Aware Evaluation for Question Generation through Explicit Diagnostics
**arXiv**：[2601.10406v1](https://arxiv.org/abs/2601.10406) · [PDF](https://arxiv.org/pdf/2601.10406.pdf)  
**作者**：Weiping Fu, Bifan Wei, Jingyi Hao, Yushun Zhang, Jian Zhang, Jiaxin Wang, Bo Li, Yu He, Lingling Zhang, Jun Liu  

**一句话要点**：提出ErrEval框架，通过显式错误诊断增强自动问题生成的评估准确性。

**关键词**：自动问题生成, 错误诊断, 评估框架, 大语言模型评估, 质量评估

## 3 点简述
- 核心问题：现有自动问题生成评估方法忽视关键缺陷，导致质量高估。
- 方法要点：ErrEval采用两阶段评估，先错误识别再引导评分，结合轻量错误标识器。
- 实验或效果：在三个基准测试中验证有效性，提升与人类判断的一致性并缓解高估问题。

## 摘要（原文）

> Automatic Question Generation (QG) often produces outputs with critical defects, such as factual hallucinations and answer mismatches. However, existing evaluation methods, including LLM-based evaluators, mainly adopt a black-box and holistic paradigm without explicit error modeling, leading to the neglect of such defects and overestimation of question quality. To address this issue, we propose ErrEval, a flexible and Error-aware Evaluation framework that enhances QG evaluation through explicit error diagnostics. Specifically, ErrEval reformulates evaluation as a two-stage process of error diagnosis followed by informed scoring. At the first stage, a lightweight plug-and-play Error Identifier detects and categorizes common errors across structural, linguistic, and content-related aspects. These diagnostic signals are then incorporated as explicit evidence to guide LLM evaluators toward more fine-grained and grounded judgments. Extensive experiments on three benchmarks demonstrate the effectiveness of ErrEval, showing that incorporating explicit diagnostics improves alignment with human judgments. Further analyses confirm that ErrEval effectively mitigates the overestimation of low-quality questions.

