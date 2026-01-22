---
layout: default
title: Knowledge Restoration-driven Prompt Optimization: Unlocking LLM Potential for Open-Domain Relational Triplet Extraction
---

# Knowledge Restoration-driven Prompt Optimization: Unlocking LLM Potential for Open-Domain Relational Triplet Extraction
**arXiv**：[2601.15037v1](https://arxiv.org/abs/2601.15037) · [PDF](https://arxiv.org/pdf/2601.15037.pdf)  
**作者**：Xiaonan Jing, Gongqing Wu, Xingrui Zhuo, Lang Sun, Jiapu Wang  

**一句话要点**：提出知识重构驱动的提示优化框架，以提升大语言模型在开放域关系三元组抽取中的性能。

**关键词**：开放域关系三元组抽取, 大语言模型, 提示优化, 知识重构, 自评估机制, 关系规范化

## 3 点简述
- 核心问题：现有方法依赖静态启发式提示，缺乏反思机制，易受语义模糊影响，导致错误抽取模式固化。
- 方法要点：设计基于知识重构的自评估机制，提供内在反馈信号；提出基于文本梯度的提示优化器，迭代优化提示以指导大语言模型。
- 实验或效果：在三个数据集上实验显示，KRPO在抽取F1分数上显著优于强基线。

## 摘要（原文）

> Open-domain Relational Triplet Extraction (ORTE) is the foundation for mining structured knowledge without predefined schemas. Despite the impressive in-context learning capabilities of Large Language Models (LLMs), existing methods are hindered by their reliance on static, heuristic-driven prompting strategies. Due to the lack of reflection mechanisms required to internalize erroneous signals, these methods exhibit vulnerability in semantic ambiguity, often making erroneous extraction patterns permanent. To address this bottleneck, we propose a Knowledge Reconstruction-driven Prompt Optimization (KRPO) framework to assist LLMs in continuously improving their extraction capabilities for complex ORTE task flows. Specifically, we design a self-evaluation mechanism based on knowledge restoration, which provides intrinsic feedback signals by projecting structured triplets into semantic consistency scores. Subsequently, we propose a prompt optimizer based on a textual gradient that can internalize historical experiences to iteratively optimize prompts, which can better guide LLMs to handle subsequent extraction tasks. Furthermore, to alleviate relation redundancy, we design a relation canonicalization memory that collects representative relations and provides semantically distinct schemas for the triplets. Extensive experiments across three datasets show that KRPO significantly outperforms strong baselines in the extraction F1 score.

