---
layout: default
title: Clinical Knowledge Graph Construction and Evaluation with Multi-LLMs via Retrieval-Augmented Generation
---

# Clinical Knowledge Graph Construction and Evaluation with Multi-LLMs via Retrieval-Augmented Generation
**arXiv**：[2601.01844v1](https://arxiv.org/abs/2601.01844) · [PDF](https://arxiv.org/pdf/2601.01844.pdf)  
**作者**：Udiptaman Das, Krishnasai B. Atmakuri, Duy Ho, Chi Lee, Yugyung Lee  

**一句话要点**：提出基于多智能体提示和检索增强生成的临床知识图谱构建与评估框架，以解决肿瘤学中无结构化文本的准确性和一致性挑战。

**关键词**：临床知识图谱, 检索增强生成, 多智能体提示, 肿瘤学, 本体对齐, 无监督评估

## 3 点简述
- 核心问题：现有方法依赖结构化输入，在肿瘤学中缺乏对事实准确性和语义一致性的鲁棒验证。
- 方法要点：采用多智能体提示和模式约束的检索增强生成策略，集成实体提取、不确定性评分、模式生成和共识验证。
- 实验或效果：在PDAC和BRCA肿瘤队列中，无需黄金标准标注，实现了精度、相关性和本体合规性的提升。

## 摘要（原文）

> Large language models (LLMs) offer new opportunities for constructing knowledge graphs (KGs) from unstructured clinical narratives. However, existing approaches often rely on structured inputs and lack robust validation of factual accuracy and semantic consistency, limitations that are especially problematic in oncology. We introduce an end-to-end framework for clinical KG construction and evaluation directly from free text using multi-agent prompting and a schema-constrained Retrieval-Augmented Generation (KG-RAG) strategy. Our pipeline integrates (1) prompt-driven entity, attribute, and relation extraction; (2) entropy-based uncertainty scoring; (3) ontology-aligned RDF/OWL schema generation; and (4) multi-LLM consensus validation for hallucination detection and semantic refinement. Beyond static graph construction, the framework supports continuous refinement and self-supervised evaluation, enabling iterative improvement of graph quality. Applied to two oncology cohorts (PDAC and BRCA), our method produces interpretable, SPARQL-compatible, and clinically grounded knowledge graphs without relying on gold-standard annotations. Experimental results demonstrate consistent gains in precision, relevance, and ontology compliance over baseline methods.

