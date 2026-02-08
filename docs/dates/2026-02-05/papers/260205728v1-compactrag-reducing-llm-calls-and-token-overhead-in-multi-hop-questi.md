---
layout: default
title: CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering
---

# CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering
**arXiv**：[2602.05728v1](https://arxiv.org/abs/2602.05728) · [PDF](https://arxiv.org/pdf/2602.05728.pdf)  
**作者**：Hao Yang, Zhiyu Yang, Xupeng Zhang, Wei Wei, Yunjie Zhang, Lin Yang  

**一句话要点**：提出CompactRAG以减少多跳问答中的LLM调用和令牌开销

**关键词**：检索增强生成, 多跳问答, 知识库构建, 令牌优化, 实体一致性

## 3 点简述
- 现有RAG系统在多跳问答中效率低，因逐步检索推理导致重复LLM调用和高令牌消耗
- 离线阶段将语料转换为原子QA知识库，在线阶段通过查询分解和密集检索减少LLM调用
- 在HotpotQA等数据集上验证，在保持准确性的同时显著降低令牌消耗

## 摘要（原文）

> Retrieval-augmented generation (RAG) has become a key paradigm for knowledge-intensive question answering. However, existing multi-hop RAG systems remain inefficient, as they alternate between retrieval and reasoning at each step, resulting in repeated LLM calls, high token consumption, and unstable entity grounding across hops. We propose CompactRAG, a simple yet effective framework that decouples offline corpus restructuring from online reasoning.
>   In the offline stage, an LLM reads the corpus once and converts it into an atomic QA knowledge base, which represents knowledge as minimal, fine-grained question-answer pairs. In the online stage, complex queries are decomposed and carefully rewritten to preserve entity consistency, and are resolved through dense retrieval followed by RoBERTa-based answer extraction. Notably, during inference, the LLM is invoked only twice in total - once for sub-question decomposition and once for final answer synthesis - regardless of the number of reasoning hops.
>   Experiments on HotpotQA, 2WikiMultiHopQA, and MuSiQue demonstrate that CompactRAG achieves competitive accuracy while substantially reducing token consumption compared to iterative RAG baselines, highlighting a cost-efficient and practical approach to multi-hop reasoning over large knowledge corpora. The implementation is available at GitHub.

