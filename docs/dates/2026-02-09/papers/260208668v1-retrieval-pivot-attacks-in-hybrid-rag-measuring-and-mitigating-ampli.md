---
layout: default
title: Retrieval Pivot Attacks in Hybrid RAG: Measuring and Mitigating Amplified Leakage from Vector Seeds to Graph Expansion
---

# Retrieval Pivot Attacks in Hybrid RAG: Measuring and Mitigating Amplified Leakage from Vector Seeds to Graph Expansion
**arXiv**：[2602.08668v1](https://arxiv.org/abs/2602.08668) · [PDF](https://arxiv.org/pdf/2602.08668.pdf)  
**作者**：Scott Thornton  

**一句话要点**：提出检索枢纽攻击风险度量与缓解方法，以解决混合RAG中向量种子到图扩展的跨租户数据泄露问题。

**关键词**：混合检索增强生成, 跨租户数据泄露, 检索枢纽攻击, 知识图扩展, 向量相似性搜索, 授权边界

## 3 点简述
- 核心问题：混合RAG组合向量检索与知识图扩展时，通过实体链接形成检索枢纽，导致跨租户数据泄露。
- 方法要点：形式化检索枢纽风险，引入Leakage@k等指标量化泄露，提出在图扩展边界实施授权以消除泄露。
- 实验或效果：在合成企业语料和Enron邮件语料中，未防御混合管道风险高达0.95，边界授权后风险降至近零。

## 摘要（原文）

> Hybrid Retrieval-Augmented Generation (RAG) pipelines combine vector similarity search with knowledge graph expansion for multi-hop reasoning. We show that this composition introduces a distinct security failure mode: a vector-retrieved "seed" chunk can pivot via entity links into sensitive graph neighborhoods, causing cross-tenant data leakage that does not occur in vector-only retrieval. We formalize this risk as Retrieval Pivot Risk (RPR) and introduce companion metrics Leakage@k, Amplification Factor, and Pivot Depth (PD) to quantify leakage magnitude and traversal structure.
>   We present seven Retrieval Pivot Attacks that exploit the vector-to-graph boundary and show that adversarial injection is not required: naturally shared entities create cross-tenant pivot paths organically. Across a synthetic multi-tenant enterprise corpus and the Enron email corpus, the undefended hybrid pipeline exhibits high pivot risk (RPR up to 0.95) with multiple unauthorized items returned per query. Leakage consistently appears at PD=2, which we attribute to the bipartite chunk-entity topology and formalize as a proposition.
>   We then show that enforcing authorization at a single location, the graph expansion boundary, eliminates measured leakage (RPR near 0) across both corpora, all attack variants, and label forgery rates up to 10 percent, with minimal overhead. Our results indicate the root cause is boundary enforcement, not inherently complex defenses: two individually secure retrieval components can compose into an insecure system unless authorization is re-checked at the transition point.

