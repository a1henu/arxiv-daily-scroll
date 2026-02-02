---
layout: default
title: OrLog: Resolving Complex Queries with LLMs and Probabilistic Reasoning
---

# OrLog: Resolving Complex Queries with LLMs and Probabilistic Reasoning
**arXiv**：[2601.23085v1](https://arxiv.org/abs/2601.23085) · [PDF](https://arxiv.org/pdf/2601.23085.pdf)  
**作者**：Mohanna Hoveyda, Jelle Piepenbrock, Arjen P de Vries, Maarten de Rijke, Faegheh Hasibi  

**一句话要点**：提出OrLog框架，结合LLM与概率推理解决复杂约束查询检索问题

**关键词**：神经符号检索, 概率推理, LLM应用, 查询约束处理, 信息检索

## 3 点简述
- 核心问题：现有检索系统忽略查询逻辑约束或推理不可靠，神经符号方法局限于形式逻辑
- 方法要点：OrLog解耦谓词级可能性估计与逻辑推理，LLM提供可能性分数，概率引擎计算查询满足后验概率
- 实验或效果：OrLog提升Top-rank精度，尤其在析取查询，效率高，平均每查询-实体对减少约90%令牌

## 摘要（原文）

> Resolving complex information needs that come with multiple constraints should consider enforcing the logical operators encoded in the query (i.e., conjunction, disjunction, negation) on the candidate answer set. Current retrieval systems either ignore these constraints in neural embeddings or approximate them in a generative reasoning process that can be inconsistent and unreliable. Although well-suited to structured reasoning, existing neuro-symbolic approaches remain confined to formal logic or mathematics problems as they often assume unambiguous queries and access to complete evidence, conditions rarely met in information retrieval. To bridge this gap, we introduce OrLog, a neuro-symbolic retrieval framework that decouples predicate-level plausibility estimation from logical reasoning: a large language model (LLM) provides plausibility scores for atomic predicates in one decoding-free forward pass, from which a probabilistic reasoning engine derives the posterior probability of query satisfaction. We evaluate OrLog across multiple backbone LLMs, varying levels of access to external knowledge, and a range of logical constraints, and compare it against base retrievers and LLM-as-reasoner methods. Provided with entity descriptions, OrLog can significantly boost top-rank precision compared to LLM reasoning with larger gains on disjunctive queries. OrLog is also more efficient, cutting mean tokens by $\sim$90\% per query-entity pair. These results demonstrate that generation-free predicate plausibility estimation combined with probabilistic reasoning enables constraint-aware retrieval that outperforms monolithic reasoning while using far fewer tokens.

