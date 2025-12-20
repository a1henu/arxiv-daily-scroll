---
layout: default
title: GinSign: Grounding Natural Language Into System Signatures for Temporal Logic Translation
---

# GinSign: Grounding Natural Language Into System Signatures for Temporal Logic Translation
**arXiv**：[2512.16770v1](https://arxiv.org/abs/2512.16770) · [PDF](https://arxiv.org/pdf/2512.16770.pdf)  
**作者**：William English, Chase Walker, Dominic Simon, Rickard Ewetz  

**一句话要点**：提出GinSign框架，通过系统签名将自然语言接地到时序逻辑翻译，提升自主系统规范准确性。

**关键词**：自然语言到时序逻辑翻译, 系统签名接地, 分层分类模型, 自主系统验证, 逻辑等价性评估

## 3 点简述
- 现有NL到TL翻译框架依赖准确原子接地或接地精度低，导致语义不等价。
- GinSign引入分层接地模型，将NL跨度映射到系统签名，分解为结构化分类任务。
- 实验显示框架支持下游模型检查，接地逻辑等价分数达95.5%，优于SOTA 1.4倍。

## 摘要（原文）

> Natural language (NL) to temporal logic (TL) translation enables engineers to specify, verify, and enforce system behaviors without manually crafting formal specifications-an essential capability for building trustworthy autonomous systems. While existing NL-to-TL translation frameworks have demonstrated encouraging initial results, these systems either explicitly assume access to accurate atom grounding or suffer from low grounded translation accuracy. In this paper, we propose a framework for Grounding Natural Language Into System Signatures for Temporal Logic translation called GinSign. The framework introduces a grounding model that learns the abstract task of mapping NL spans onto a given system signature: given a lifted NL specification and a system signature $\mathcal{S}$, the classifier must assign each lifted atomic proposition to an element of the set of signature-defined atoms $\mathcal{P}$. We decompose the grounding task hierarchically -- first predicting predicate labels, then selecting the appropriately typed constant arguments. Decomposing this task from a free-form generation problem into a structured classification problem permits the use of smaller masked language models and eliminates the reliance on expensive LLMs. Experiments across multiple domains show that frameworks which omit grounding tend to produce syntactically correct lifted LTL that is semantically nonequivalent to grounded target expressions, whereas our framework supports downstream model checking and achieves grounded logical-equivalence scores of $95.5\%$, a $1.4\times$ improvement over SOTA.

