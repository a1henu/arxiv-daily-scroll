---
layout: default
title: Feasibility Preservation under Monotone Retrieval Truncation
---

# Feasibility Preservation under Monotone Retrieval Truncation
**arXiv**：[2601.15241v1](https://arxiv.org/abs/2601.15241) · [PDF](https://arxiv.org/pdf/2601.15241.pdf)  
**作者**：Sean Plummer  

**一句话要点**：提出单调截断下的可行性保持理论，以解决检索截断导致的结构性失败问题。

**关键词**：检索截断, 可行性保持, 单调截断, 有限可证性, 查询类生成, 结构性失败

## 3 点简述
- 核心问题：检索截断可能阻止兼容证据共现，导致基于相关性的评估未捕获的失败。
- 方法要点：形式化检索为候选证据序列，证明单调截断保证个体查询的有限可证性。
- 实验或效果：展示非单调截断、非有限生成查询类和纯槽位覆盖下的尖锐反例。

## 摘要（原文）

> Retrieval-based systems approximate access to a corpus by exposing only a truncated subset of available evidence. Even when relevant information exists in the corpus, truncation can prevent compatible evidence from co-occurring, leading to failures that are not captured by relevance-based evaluation. This paper studies retrieval from a structural perspective, modeling query answering as a feasibility problem under truncation.
>   We formalize retrieval as a sequence of candidate evidence sets and characterize conditions under which feasibility in the limit implies feasibility at finite retrieval depth. We show that monotone truncation suffices to guarantee finite witnessability for individual queries. For classes of queries, we identify finite generation of witness certificates as the additional condition required to obtain a uniform retrieval bound, and we show that this condition is necessary. We further exhibit sharp counterexamples demonstrating failure under non-monotone truncation, non-finitely-generated query classes, and purely slotwise coverage.
>   Together, these results isolate feasibility preservation as a correctness criterion for retrieval independent of relevance scoring or optimization, and clarify structural limitations inherent to truncation-based retrieval.

