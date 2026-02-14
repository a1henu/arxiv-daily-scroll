---
layout: default
title: Statistical Parsing for Logical Information Retrieval
---

# Statistical Parsing for Logical Information Retrieval
**arXiv**：[2602.12170v1](https://arxiv.org/abs/2602.12170) · [PDF](https://arxiv.org/pdf/2602.12170.pdf)  
**作者**：Greg Coppola  

**一句话要点**：提出扩展量化布尔贝叶斯网络与类型化槽语法，结合大语言模型实现自然语言逻辑推理与解析

**关键词**：逻辑推理模型, 自然语言解析, 量化布尔贝叶斯网络, 类型化槽语法, 大语言模型集成, 形式语义学

## 3 点简述
- 核心问题：先前量化布尔贝叶斯网络缺乏否定/反向推理和自然语言解析器，限制了逻辑信息检索应用
- 方法要点：扩展网络支持否定因子和反向推理，引入类型化逻辑语言和槽语法，结合大语言模型进行预处理和消歧
- 实验或效果：推理引擎通过44/44测试案例，语法解析33/33正确，大语言模型消歧准确率95%，但直接解析性能低

## 摘要（原文）

> In previous work (Coppola, 2024) we introduced the Quantified Boolean Bayesian Network (QBBN), a logical graphical model that implements the forward fragment of natural deduction (Prawitz, 1965) as a probabilistic factor graph. That work left two gaps: no negation/backward reasoning, and no parser for natural language.
>   This paper addresses both gaps across inference, semantics, and syntax. For inference, we extend the QBBN with NEG factors enforcing P(x) + P(neg x) = 1, enabling contrapositive reasoning (modus tollens) via backward lambda messages, completing Prawitz's simple elimination rules. The engine handles 44/44 test cases spanning 22 reasoning patterns. For semantics, we present a typed logical language with role-labeled predicates, modal quantifiers, and three tiers of expressiveness following Prawitz: first-order quantification, propositions as arguments, and predicate quantification via lambda abstraction. For syntax, we present a typed slot grammar that deterministically compiles sentences to logical form (33/33 correct, zero ambiguity). LLMs handle disambiguation (95% PP attachment accuracy) but cannot produce structured parses directly (12.4% UAS), confirming grammars are necessary. The architecture: LLM preprocesses, grammar parses, LLM reranks, QBBN infers.
>   We argue this reconciles formal semantics with Sutton's "bitter lesson" (2019): LLMs eliminate the annotation bottleneck that killed formal NLP, serving as annotator while the QBBN serves as verifier. Code: https://github.com/gregorycoppola/world

