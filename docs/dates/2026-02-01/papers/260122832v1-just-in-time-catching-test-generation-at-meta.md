---
layout: default
title: Just-in-Time Catching Test Generation at Meta
---

# Just-in-Time Catching Test Generation at Meta
**arXiv**：[2601.22832v1](https://arxiv.org/abs/2601.22832) · [PDF](https://arxiv.org/pdf/2601.22832.pdf)  
**作者**：Matthew Becker, Yifei Chen, Nicholas Cochran, Pouyan Ghasemi, Abhishek Gulati, Mark Harman, Zachary Haluza, Mehrdad Honarkhah, Herve Robert, Jiacheng Liu, Weini Liu, Sreeja Thummala, Xiaoning Yang, Rui Xin, Sophie Zeng  

**一句话要点**：提出即时捕获测试生成方法，以减少大规模后端系统中的错误并降低误报负担。

**关键词**：即时测试生成, 代码变更感知, 误报减少, 大规模系统, LLM评估, 工业应用

## 3 点简述
- 核心问题：传统硬化测试在生成时通过，无法在代码提交前捕获错误，且误报会增加开发负担。
- 方法要点：采用代码变更感知方法生成捕获测试，结合基于规则和LLM的评估器来减少误报。
- 实验或效果：分析22,126个测试，捕获候选生成提升4倍，误报评估减少70%人工审核，确认8个真阳性防止严重故障。

## 摘要（原文）

> We report on Just-in-Time catching test generation at Meta, designed to prevent bugs in large scale backend systems of hundreds of millions of line of code. Unlike traditional hardening tests, which pass at generation time, catching tests are meant to fail, surfacing bugs before code lands. The primary challenge is to reduce development drag from false positive test failures. Analyzing 22,126 generated tests, we show code-change-aware methods improve candidate catch generation 4x over hardening tests and 20x over coincidentally failing tests. To address false positives, we use rule-based and LLM-based assessors. These assessors reduce human review load by 70%. Inferential statistical analysis showed that human-accepted code changes are assessed to have significantly more false positives, while human-rejected changes have significantly more true positives. We reported 41 candidate catches to engineers; 8 were confirmed to be true positives, 4 of which would have led to serious failures had they remained uncaught. Overall, our results show that Just-in-Time catching is scalable, industrially applicable, and that it prevents serious failures from reaching production.

