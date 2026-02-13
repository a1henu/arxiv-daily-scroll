---
layout: default
title: Statistical Parsing for Logical Information Retrieval
---

# Statistical Parsing for Logical Information Retrieval
**arXiv**：[2602.12170v1](https://arxiv.org/abs/2602.12170) · [PDF](https://arxiv.org/pdf/2602.12170.pdf)  
**作者**：Greg Coppola  

**一句话要点**：提出带否定扩展的量化布尔贝叶斯网络与类型槽语法，以结合LLM实现逻辑信息检索

**关键词**：逻辑图形模型, 自然语言解析, 概率推理, 形式语义学, 大语言模型集成

## 3 点简述
- 扩展QBBN模型，引入NEG因子支持否定与逆向推理，完成Prawitz简单消除规则
- 设计类型逻辑语言与槽语法，实现句子到逻辑形式的确定性编译，LLM辅助消歧
- 架构整合LLM预处理与重排序，QBBN推理验证，在44个测试案例中全正确

## 摘要（原文）

> In previous work (Coppola, 2024) we introduced the Quantified Boolean Bayesian Network (QBBN), a logical graphical model that implements the forward fragment of natural deduction (Prawitz, 1965) as a probabilistic factor graph. That work left two gaps: no negation/backward reasoning, and no parser for natural language.
>   This paper addresses both gaps across inference, semantics, and syntax. For inference, we extend the QBBN with NEG factors enforcing P(x) + P(neg x) = 1, enabling contrapositive reasoning (modus tollens) via backward lambda messages, completing Prawitz's simple elimination rules. The engine handles 44/44 test cases spanning 22 reasoning patterns. For semantics, we present a typed logical language with role-labeled predicates, modal quantifiers, and three tiers of expressiveness following Prawitz: first-order quantification, propositions as arguments, and predicate quantification via lambda abstraction. For syntax, we present a typed slot grammar that deterministically compiles sentences to logical form (33/33 correct, zero ambiguity). LLMs handle disambiguation (95% PP attachment accuracy) but cannot produce structured parses directly (12.4% UAS), confirming grammars are necessary. The architecture: LLM preprocesses, grammar parses, LLM reranks, QBBN infers.
>   We argue this reconciles formal semantics with Sutton's "bitter lesson" (2019): LLMs eliminate the annotation bottleneck that killed formal NLP, serving as annotator while the QBBN serves as verifier. Code: https://github.com/gregorycoppola/world

