---
layout: default
title: Canonical Intermediate Representation for LLM-based optimization problem formulation and code generation
---

# Canonical Intermediate Representation for LLM-based optimization problem formulation and code generation
**arXiv**：[2602.02029v1](https://arxiv.org/abs/2602.02029) · [PDF](https://arxiv.org/pdf/2602.02029.pdf)  
**作者**：Zhongyuan Lyu, Shuoyu Hu, Lujie Liu, Hongxia Yang, Ming LI  

**一句话要点**：提出规范中间表示以解决基于LLM的优化问题建模与代码生成中复合约束和建模范式难题

**关键词**：优化问题建模, 规范中间表示, 多智能体框架, 规则到约束推理, LLM代码生成, 操作研究

## 3 点简述
- 核心问题：LLM在从自然语言描述自动构建优化模型时，难以处理复杂操作规则的复合约束和合适建模范式。
- 方法要点：引入规范中间表示，通过约束原型和候选建模范式编码操作规则语义，解耦规则逻辑与数学实例化。
- 实验或效果：在新建基准上达到47.2%准确率，在现有基准上接近GPT-5等专有模型性能，并通过反思机制进一步提升结果。

## 摘要（原文）

> Automatically formulating optimization models from natural language descriptions is a growing focus in operations research, yet current LLM-based approaches struggle with the composite constraints and appropriate modeling paradigms required by complex operational rules. To address this, we introduce the Canonical Intermediate Representation (CIR): a schema that LLMs explicitly generate between problem descriptions and optimization models. CIR encodes the semantics of operational rules through constraint archetypes and candidate modeling paradigms, thereby decoupling rule logic from its mathematical instantiation. Upon a newly generated CIR knowledge base, we develop the rule-to-constraint (R2C) framework, a multi-agent pipeline that parses problem texts, synthesizes CIR implementations by retrieving domain knowledge, and instantiates optimization models. To systematically evaluate rule-to-constraint reasoning, we test R2C on our newly constructed benchmark featuring rich operational rules, and benchmarks from prior work. Extensive experiments show that R2C achieves state-of-the-art accuracy on the proposed benchmark (47.2% Accuracy Rate). On established benchmarks from the literature, R2C delivers highly competitive results, approaching the performance of proprietary models (e.g., GPT-5). Moreover, with a reflection mechanism, R2C achieves further gains and sets new best-reported results on some benchmarks.

