---
layout: default
title: Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming
---

# Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming
**arXiv**：[2601.02060v1](https://arxiv.org/abs/2601.02060) · [PDF](https://arxiv.org/pdf/2601.02060.pdf)  
**作者**：Nguyet-Anh H. Lang, Eric Lang, Thanh Le-Cong, Bach Le, Quyet-Thang Huynh  

**一句话要点**：提出FPEval框架以评估大语言模型在函数式编程中的代码生成能力

**关键词**：函数式编程, 代码生成, 大语言模型评估, 静态分析, 编程基准

## 3 点简述
- 核心问题：大语言模型在函数式编程语言中的代码生成能力缺乏全面评估
- 方法要点：基于FPBench构建包含721个任务的基准，结合测试验证和静态分析进行综合评估
- 实验或效果：模型性能随升级提升，但在纯函数式语言中错误率更高，且常生成非惯用代码

## 摘要（原文）

> Functional programming provides strong foundations for developing reliable and secure software systems, yet its adoption remains not widespread due to the steep learning curve. Recent advances in Large Language Models (LLMs) for code generation present new opportunities to lower these barriers. However, extensive evaluations of LLMs largely focus on imperative programming languages, and their capabilities in functional programming languages (FP) remain underexplored. To address this gap, we introduce FPEval, a holistic evaluation framework built on FPBench, a new benchmark of 721 programming tasks across three difficulty levels on three mainstream FP languages: Haskell, Ocaml and Scala. FPEval provides compehensive evaluation infrastructures with both test validations with comprehensive test suites and static analysis tools to assess both functional correctness and code style and maintainability. Using this framework, we evaluate state-of-the-art LLMs, including GPT-3.5, GPT-4o, and GPT-5, for code generation in functional programming languages and Java as an imperative baseline. Our results demonstrate that LLM performance in functional programming improves substantially with model advancement; however, error rates remain significantly higher in purely functional languages (Haskell and OCaml) than in hybrid (Scala) or imperative (Java) languages. Moreover, LLMs frequently generate non-idiomatic functional code that follows imperative patterns, raising concerns about code style and long-term maintainability. Finally, we show that LLMs can partially self-repair both correctness and quality issues when provided with static analysis feedback and hand-crafted instructions for common types of issues.

