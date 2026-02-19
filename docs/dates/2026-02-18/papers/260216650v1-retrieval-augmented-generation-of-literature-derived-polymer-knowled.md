---
layout: default
title: Retrieval Augmented Generation of Literature-derived Polymer Knowledge: The Example of a Biodegradable Polymer Expert System
---

# Retrieval Augmented Generation of Literature-derived Polymer Knowledge: The Example of a Biodegradable Polymer Expert System
**arXiv**：[2602.16650v1](https://arxiv.org/abs/2602.16650) · [PDF](https://arxiv.org/pdf/2602.16650.pdf)  
**作者**：Sonakshi Gupta, Akhlak Mahmood, Wei Xiong, Rampi Ramprasad  

**一句话要点**：提出基于检索增强生成的聚合物知识系统，结合向量与图方法提升文献分析能力。

**关键词**：检索增强生成, 聚合物知识图谱, 文献分析, 向量检索, 图检索, 材料科学助手

## 3 点简述
- 聚合物文献知识分散且术语不一致，难以系统检索与推理。
- 开发向量检索与图检索两种方法，构建段落嵌入和结构化知识图谱。
- 实验显示图方法精度高、可解释性强，向量方法召回广，专家验证有效。

## 摘要（原文）

> Polymer literature contains a large and growing body of experimental knowledge, yet much of it is buried in unstructured text and inconsistent terminology, making systematic retrieval and reasoning difficult. Existing tools typically extract narrow, study-specific facts in isolation, failing to preserve the cross-study context required to answer broader scientific questions. Retrieval-augmented generation (RAG) offers a promising way to overcome this limitation by combining large language models (LLMs) with external retrieval, but its effectiveness depends strongly on how domain knowledge is represented. In this work, we develop two retrieval pipelines: a dense semantic vector-based approach (VectorRAG) and a graph-based approach (GraphRAG). Using over 1,000 polyhydroxyalkanoate (PHA) papers, we construct context-preserving paragraph embeddings and a canonicalized structured knowledge graph supporting entity disambiguation and multi-hop reasoning. We evaluate these pipelines through standard retrieval metrics, comparisons with general state-of-the-art systems such as GPT and Gemini, and qualitative validation by a domain chemist. The results show that GraphRAG achieves higher precision and interpretability, while VectorRAG provides broader recall, highlighting complementary trade-offs. Expert validation further confirms that the tailored pipelines, particularly GraphRAG, produce well-grounded, citation-reliable responses with strong domain relevance. By grounding every statement in evidence, these systems enable researchers to navigate the literature, compare findings across studies, and uncover patterns that are difficult to extract manually. More broadly, this work establishes a practical framework for building materials science assistants using curated corpora and retrieval design, reducing reliance on proprietary models while enabling trustworthy literature analysis at scale.

