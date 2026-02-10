---
layout: default
title: Automatic In-Domain Exemplar Construction and LLM-Based Refinement of Multi-LLM Expansions for Query Expansion
---

# Automatic In-Domain Exemplar Construction and LLM-Based Refinement of Multi-LLM Expansions for Query Expansion
**arXiv**：[2602.08917v1](https://arxiv.org/abs/2602.08917) · [PDF](https://arxiv.org/pdf/2602.08917.pdf)  
**作者**：Minghan Li, Ercong Nie, Siqi Zhao, Tongna Chen, Huiping Huang, Guodong Zhou  

**一句话要点**：提出自动构建领域内示例池与多LLM集成精炼框架，以解决查询扩展中的领域适应性问题。

**关键词**：查询扩展, 大型语言模型, 领域适应, 示例选择, 模型集成, 无监督学习

## 3 点简述
- 核心问题：查询扩展依赖手工提示或单一LLM，难以适应领域变化且扩展性差。
- 方法要点：自动构建领域内示例池，通过聚类选择多样化示例，并集成两个异构LLM生成扩展后由精炼LLM整合。
- 实验或效果：在多个数据集上显著优于基线方法，提供无监督、可复现的解决方案。

## 摘要（原文）

> Query expansion with large language models is promising but often relies on hand-crafted prompts, manually chosen exemplars, or a single LLM, making it non-scalable and sensitive to domain shift. We present an automated, domain-adaptive QE framework that builds in-domain exemplar pools by harvesting pseudo-relevant passages using a BM25-MonoT5 pipeline. A training-free cluster-based strategy selects diverse demonstrations, yielding strong and stable in-context QE without supervision. To further exploit model complementarity, we introduce a two-LLM ensemble in which two heterogeneous LLMs independently generate expansions and a refinement LLM consolidates them into one coherent expansion. Across TREC DL20, DBPedia, and SciFact, the refined ensemble delivers consistent and statistically significant gains over BM25, Rocchio, zero-shot, and fixed few-shot baselines. The framework offers a reproducible testbed for exemplar selection and multi-LLM generation, and a practical, label-free solution for real-world QE.

