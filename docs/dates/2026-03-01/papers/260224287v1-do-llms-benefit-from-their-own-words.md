---
layout: default
title: Do LLMs Benefit From Their Own Words?
---

# Do LLMs Benefit From Their Own Words?
**arXiv**：[2602.24287v1](https://arxiv.org/abs/2602.24287) · [PDF](https://arxiv.org/pdf/2602.24287.pdf)  
**作者**：Jenny Y. Huang, Leshem Choshen, Ramon Astudillo, Tamara Broderick, Jacob Andreas  

**一句话要点**：提出选择性省略助手历史的方法，以提升多轮对话响应质量并减少内存消耗。

**关键词**：多轮对话, 上下文管理, 大语言模型, 提示工程, 内存优化

## 3 点简述
- 核心问题：大语言模型在多轮对话中是否受益于自身先前响应的条件化。
- 方法要点：比较全上下文提示与仅用户轮提示，并设计上下文过滤方法选择性省略助手侧历史。
- 实验或效果：发现省略助手历史不影响多数轮次质量，可减少上下文长度达10倍，并改善错误传播。

## 摘要（原文）

> Multi-turn interactions with large language models typically retain the assistant's own past responses in the conversation history. In this work, we revisit this design choice by asking whether large language models benefit from conditioning on their own prior responses. Using in-the-wild, multi-turn conversations, we compare standard (full-context) prompting with a user-turn-only prompting approach that omits all previous assistant responses, across three open reasoning models and one state-of-the-art model. To our surprise, we find that removing prior assistant responses does not affect response quality on a large fraction of turns. Omitting assistant-side history can reduce cumulative context lengths by up to 10x. To explain this result, we find that multi-turn conversations consist of a substantial proportion (36.4%) of self-contained prompts, and that many follow-up prompts provide sufficient instruction to be answered using only the current user turn and prior user turns. When analyzing cases where user-turn-only prompting substantially outperforms full context, we identify instances of context pollution, in which models over-condition on their previous responses, introducing errors, hallucinations, or stylistic artifacts that propagate across turns. Motivated by these findings, we design a context-filtering approach that selectively omits assistant-side context. Our findings suggest that selectively omitting assistant history can improve response quality while reducing memory consumption.

