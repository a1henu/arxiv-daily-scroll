---
layout: default
title: Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs
---

# Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs
**arXiv**：[2601.10257v1](https://arxiv.org/abs/2601.10257) · [PDF](https://arxiv.org/pdf/2601.10257.pdf)  
**作者**：Nan Li, Bo Kang, Tijl De Bie  

**一句话要点**：提出诊断框架以分离输入语言与推理语言对LLMs跨语言道德对齐的影响

**关键词**：跨语言道德对齐, 诊断框架, 道德基础理论, 语言效应分解, LLMs评估, 上下文依赖性

## 3 点简述
- 核心问题：LLMs在不同语言中判断道德困境时，差异源于输入语言还是推理语言？
- 方法要点：通过匹配与不匹配条件分离两因素，结合道德基础理论解释判断变化。
- 实验或效果：应用于13个LLMs，显示推理语言效应方差是输入语言的两倍，检测到标准评估遗漏的上下文依赖性。

## 摘要（原文）

> When LLMs judge moral dilemmas, do they reach different conclusions in different languages, and if so, why? Two factors could drive such differences: the language of the dilemma itself, or the language in which the model reasons. Standard evaluation conflates these by testing only matched conditions (e.g., English dilemma with English reasoning). We introduce a methodology that separately manipulates each factor, covering also mismatched conditions (e.g., English dilemma with Chinese reasoning), enabling decomposition of their contributions. To study \emph{what} changes, we propose an approach to interpret the moral judgments in terms of Moral Foundations Theory. As a side result, we identify evidence for splitting the Authority dimension into a family-related and an institutional dimension. Applying this methodology to English-Chinese moral judgment with 13 LLMs, we demonstrate its diagnostic power: (1) the framework isolates reasoning-language effects as contributing twice the variance of input-language effects; (2) it detects context-dependency in nearly half of models that standard evaluation misses; and (3) a diagnostic taxonomy translates these patterns into deployment guidance. We release our code and datasets at https://anonymous.4open.science/r/CrossCulturalMoralJudgement.

