---
layout: default
title: Self-MedRAG: a Self-Reflective Hybrid Retrieval-Augmented Generation Framework for Reliable Medical Question Answering
---

# Self-MedRAG: a Self-Reflective Hybrid Retrieval-Augmented Generation Framework for Reliable Medical Question Answering
**arXiv**：[2601.04531v1](https://arxiv.org/abs/2601.04531) · [PDF](https://arxiv.org/pdf/2601.04531.pdf)  
**作者**：Jessica Ryan, Alexander I. Gumilang, Robert Wiliam, Derwin Suhartono  

**一句话要点**：提出Self-MedRAG框架，通过混合检索与自反思循环提升医疗问答的可靠性。

**关键词**：医疗问答, 检索增强生成, 混合检索, 自反思机制, 临床推理, 自然语言推理

## 3 点简述
- 核心问题：LLMs在医疗问答中易产生幻觉，传统RAG难以处理复杂推理查询。
- 方法要点：结合稀疏与密集检索，并引入自反思模块迭代验证答案证据。
- 实验或效果：在MedQA和PubMedQA上显著提升准确率，减少无依据主张。

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated significant potential in medical Question Answering (QA), yet they remain prone to hallucinations and ungrounded reasoning, limiting their reliability in high-stakes clinical scenarios. While Retrieval-Augmented Generation (RAG) mitigates these issues by incorporating external knowledge, conventional single-shot retrieval often fails to resolve complex biomedical queries requiring multi-step inference. To address this, we propose Self-MedRAG, a self-reflective hybrid framework designed to mimic the iterative hypothesis-verification process of clinical reasoning. Self-MedRAG integrates a hybrid retrieval strategy, combining sparse (BM25) and dense (Contriever) retrievers via Reciprocal Rank Fusion (RRF) to maximize evidence coverage. It employs a generator to produce answers with supporting rationales, which are then assessed by a lightweight self-reflection module using Natural Language Inference (NLI) or LLM-based verification. If the rationale lacks sufficient evidentiary support, the system autonomously reformulates the query and iterates to refine the context. We evaluated Self-MedRAG on the MedQA and PubMedQA benchmarks. The results demonstrate that our hybrid retrieval approach significantly outperforms single-retriever baselines. Furthermore, the inclusion of the self-reflective loop yielded substantial gains, increasing accuracy on MedQA from 80.00% to 83.33% and on PubMedQA from 69.10% to 79.82%. These findings confirm that integrating hybrid retrieval with iterative, evidence-based self-reflection effectively reduces unsupported claims and enhances the clinical reliability of LLM-based systems.

