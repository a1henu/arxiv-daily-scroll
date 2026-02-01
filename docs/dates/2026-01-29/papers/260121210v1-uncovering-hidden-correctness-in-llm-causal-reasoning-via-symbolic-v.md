---
layout: default
title: Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification
---

# Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification
**arXiv**：[2601.21210v1](https://arxiv.org/abs/2601.21210) · [PDF](https://arxiv.org/pdf/2601.21210.pdf)  
**作者**：Paul He, Yinya Huang, Mrinmaya Sachan, Zhijing Jin  

**一句话要点**：提出DoVerifier符号验证器以解决LLM因果推理评估中语义正确性缺失的问题

**关键词**：因果推理, 符号验证, do-calculus, LLM评估, 语义正确性

## 3 点简述
- 当前LLM因果推理评估依赖字符串匹配，无法捕捉形式语义有效性
- DoVerifier基于do-calculus和概率论规则，验证因果表达式是否可从给定因果图推导
- 在合成数据和因果QA基准上，DoVerifier更准确地评估语义正确性，提供更严谨的评估方式

## 摘要（原文）

> Large language models (LLMs) are increasingly being applied to tasks that involve causal reasoning. However, current benchmarks often rely on string matching or surface-level metrics that do not capture whether the output of a model is formally valid under the semantics of causal reasoning. To address this, we propose DoVerifier, a simple symbolic verifier that checks whether LLM-generated causal expressions are derivable from a given causal graph using rules from do-calculus and probability theory. This allows us to recover correct answers to causal queries that would otherwise be marked incorrect due to superficial differences in their causal semantics. Our evaluations on synthetic data and causal QA benchmarks show that DoVerifier more accurately captures semantic correctness of causal reasoning traces, offering a more rigorous and informative way to evaluate LLMs on causal reasoning.

