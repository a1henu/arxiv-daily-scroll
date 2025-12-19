---
layout: default
title: In-Context Algebra
---

# In-Context Algebra
**arXiv**：[2512.16902v1](https://arxiv.org/abs/2512.16902) · [PDF](https://arxiv.org/pdf/2512.16902.pdf)  
**作者**：Eric Todd, Jannik Brinkmann, Rohit Gandikota, David Bau  

**一句话要点**：提出上下文代数任务以研究Transformer在变量符号不固定时的推理机制

**关键词**：Transformer推理, 上下文学习, 代数群, 符号机制, 因果测试, 泛化能力

## 3 点简述
- 核心问题：Transformer在符号含义随序列变化的代数任务中如何学习推理机制
- 方法要点：设计新任务，符号与代数群元素的映射在序列间变化，并创建因果测试验证假设机制
- 实验或效果：模型达到近完美准确率，泛化至未见代数群，识别出三种一致学习机制

## 摘要（原文）

> We investigate the mechanisms that arise when transformers are trained to solve arithmetic on sequences where tokens are variables whose meaning is determined only through their interactions. While prior work has found that transformers develop geometric embeddings that mirror algebraic structure, those previous findings emerge from settings where arithmetic-valued tokens have fixed meanings. We devise a new task in which the assignment of symbols to specific algebraic group elements varies from one sequence to another. Despite this challenging setup, transformers achieve near-perfect accuracy on the task and even generalize to unseen algebraic groups. We develop targeted data distributions to create causal tests of a set of hypothesized mechanisms, and we isolate three mechanisms models consistently learn: commutative copying where a dedicated head copies answers, identity element recognition that distinguishes identity-containing facts, and closure-based cancellation that tracks group membership to constrain valid answers. Complementary to the geometric representations found in fixed-symbol settings, our findings show that models develop symbolic reasoning mechanisms when trained to reason in-context with variables whose meanings are not fixed.

