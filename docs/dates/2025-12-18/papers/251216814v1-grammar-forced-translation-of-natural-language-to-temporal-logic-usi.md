---
layout: default
title: Grammar-Forced Translation of Natural Language to Temporal Logic using LLMs
---

# Grammar-Forced Translation of Natural Language to Temporal Logic using LLMs
**arXiv**：[2512.16814v1](https://arxiv.org/abs/2512.16814) · [PDF](https://arxiv.org/pdf/2512.16814.pdf)  
**作者**：William English, Dominic Simon, Sumit Kumar Jha, Rickard Ewetz  

**一句话要点**：提出语法强制翻译框架以提升自然语言到时序逻辑的翻译准确率

**关键词**：自然语言到时序逻辑翻译, 语法强制翻译, 解空间缩减, 小样本学习, 机器人通信

## 3 点简述
- 核心问题：现有方法在原子命题提升、共指消解和小样本学习方面存在困难
- 方法要点：通过限制每一步有效输出词汇来降低翻译复杂度，利用问题特性减少解空间
- 实验或效果：在CW、GLTL和Navi基准上，端到端翻译准确率平均提升5.49%，域外翻译提升14.06%

## 摘要（原文）

> Translating natural language (NL) into a formal language such as temporal logic (TL) is integral for human communication with robots and autonomous systems. State-of-the-art approaches decompose the task into a lifting of atomic propositions (APs) phase and a translation phase. However, existing methods struggle with accurate lifting, the existence of co-references, and learning from limited data. In this paper, we propose a framework for NL to TL translation called Grammar Forced Translation (GraFT). The framework is based on the observation that previous work solves both the lifting and translation steps by letting a language model iteratively predict tokens from its full vocabulary. In contrast, GraFT reduces the complexity of both tasks by restricting the set of valid output tokens from the full vocabulary to only a handful in each step. The solution space reduction is obtained by exploiting the unique properties of each problem. We also provide a theoretical justification for why the solution space reduction leads to more efficient learning. We evaluate the effectiveness of GraFT using the CW, GLTL, and Navi benchmarks. Compared with state-of-the-art translation approaches, it can be observed that GraFT the end-to-end translation accuracy by 5.49% and out-of-domain translation accuracy by 14.06% on average.

