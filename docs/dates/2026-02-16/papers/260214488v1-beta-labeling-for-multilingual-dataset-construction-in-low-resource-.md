---
layout: default
title: BETA-Labeling for Multilingual Dataset Construction in Low-Resource IR
---

# BETA-Labeling for Multilingual Dataset Construction in Low-Resource IR
**arXiv**：[2602.14488v1](https://arxiv.org/abs/2602.14488) · [PDF](https://arxiv.org/pdf/2602.14488.pdf)  
**作者**：Md. Najib Hasan, Mst. Jannatun Ferdous Rain, Fyad Mohammed, Nazmul Siddique  

**一句话要点**：提出BETA标注框架构建低资源语言IR数据集，并评估跨语言数据集重用的可靠性

**关键词**：低资源信息检索, 多语言数据集构建, 大语言模型标注, 跨语言数据集重用, 机器翻译评估

## 3 点简述
- 低资源语言IR受限于高质量标注数据稀缺，手动标注成本高且难以扩展
- 采用多LLM标注器结合上下文对齐、一致性检查和多数同意，辅以人工评估提升标签质量
- 通过机器翻译实验揭示跨语言数据集重用存在语义保留差异和语言依赖偏差，影响可靠性

## 摘要（原文）

> IR in low-resource languages remains limited by the scarcity of high-quality, task-specific annotated datasets. Manual annotation is expensive and difficult to scale, while using large language models (LLMs) as automated annotators introduces concerns about label reliability, bias, and evaluation validity. This work presents a Bangla IR dataset constructed using a BETA-labeling framework involving multiple LLM annotators from diverse model families. The framework incorporates contextual alignment, consistency checks, and majority agreement, followed by human evaluation to verify label quality. Beyond dataset creation, we examine whether IR datasets from other low-resource languages can be effectively reused through one-hop machine translation. Using LLM-based translation across multiple language pairs, we experimented on meaning preservation and task validity between source and translated datasets. Our experiment reveal substantial variation across languages, reflecting language-dependent biases and inconsistent semantic preservation that directly affect the reliability of cross-lingual dataset reuse. Overall, this study highlights both the potential and limitations of LLM-assisted dataset creation for low-resource IR. It provides empirical evidence of the risks associated with cross-lingual dataset reuse and offers practical guidance for constructing more reliable benchmarks and evaluation pipelines in low-resource language settings.

