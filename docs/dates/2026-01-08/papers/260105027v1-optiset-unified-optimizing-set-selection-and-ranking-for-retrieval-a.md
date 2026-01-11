---
layout: default
title: OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation
---

# OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation
**arXiv**：[2601.05027v1](https://arxiv.org/abs/2601.05027) · [PDF](https://arxiv.org/pdf/2601.05027.pdf)  
**作者**：Yi Jiang, Sendong Zhao, Jianbo Li, Bairui Hu, Yanrui Du, Haochun Wang, Bing Qin  

**一句话要点**：提出OptiSet框架，通过统一优化集合选择与排序，解决检索增强生成中的冗余与组合增益问题。

**关键词**：检索增强生成, 集合选择, 集合排序, 自合成策略, 组合优化, 证据冗余

## 3 点简述
- 核心问题：现有方法基于静态选择top-k段落，忽略段落间组合增益并引入冗余。
- 方法要点：采用“扩展-精炼”范式，通过多视角扩展和重选形成紧凑证据集，并设计自合成策略评估效用变化。
- 实验或效果：实验表明OptiSet在复杂组合问题上提升性能，使生成更高效，代码已开源。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) improves generation quality by incorporating evidence retrieved from large external corpora. However, most existing methods rely on statically selecting top-k passages based on individual relevance, which fails to exploit combinatorial gains among passages and often introduces substantial redundancy. To address this limitation, we propose OptiSet, a set-centric framework that unifies set selection and set-level ranking for RAG. OptiSet adopts an "Expand-then-Refine" paradigm: it first expands a query into multiple perspectives to enable a diverse candidate pool and then refines the candidate pool via re-selection to form a compact evidence set. We then devise a self-synthesis strategy without strong LLM supervision to derive preference labels from the set conditional utility changes of the generator, thereby identifying complementary and redundant evidence. Finally, we introduce a set-list wise training strategy that jointly optimizes set selection and set-level ranking, enabling the model to favor compact, high-gain evidence sets. Extensive experiments demonstrate that OptiSet improves performance on complex combinatorial problems and makes generation more efficient. The source code is publicly available.

