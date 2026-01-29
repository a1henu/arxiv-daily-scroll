---
layout: default
title: Context-Augmented Code Generation Using Programming Knowledge Graphs
---

# Context-Augmented Code Generation Using Programming Knowledge Graphs
**arXiv**：[2601.20810v1](https://arxiv.org/abs/2601.20810) · [PDF](https://arxiv.org/pdf/2601.20810.pdf)  
**作者**：Shahd Seddik, Fahd Seddik, Iman Saberi, Fatemeh Fard, Minh Hieu Huynh, Patanamon Thongtanunam  

**一句话要点**：提出编程知识图谱方法以增强代码生成中的检索精度和减少幻觉

**关键词**：代码生成, 检索增强生成, 编程知识图谱, 幻觉缓解, 细粒度检索

## 3 点简述
- 核心问题：LLMs在复杂代码生成中检索不精准且易产生幻觉
- 方法要点：使用编程知识图谱进行语义表示和细粒度检索，结合树剪枝和重排序机制
- 实验或效果：在HumanEval和MBPP上提升pass@1准确率最高20%，优于基线34%

## 摘要（原文）

> Large Language Models (LLMs) excel at code generation but struggle with complex problems. Retrieval-Augmented Generation (RAG) mitigates this issue by integrating external knowledge, yet retrieval models often miss relevant context, and generation models hallucinate with irrelevant data. We propose Programming Knowledge Graph (PKG) for semantic representation and fine-grained retrieval of code and text. Our approach enhances retrieval precision through tree pruning and mitigates hallucinations via a re-ranking mechanism that integrates non-RAG solutions. Structuring external data into finer-grained nodes improves retrieval granularity. Evaluations on HumanEval and MBPP show up to 20% pass@1 accuracy gains and a 34% improvement over baselines on MBPP. Our findings demonstrate that our proposed PKG approach along with re-ranker effectively address complex problems while maintaining minimal negative impact on solutions that are already correct without RAG. The replication package is published at https://github.com/iamshahd/ProgrammingKnowledgeGraph

