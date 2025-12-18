---
layout: default
title: The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems
---

# The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems
**arXiv**：[2512.15068v1](https://arxiv.org/abs/2512.15068) · [PDF](https://arxiv.org/pdf/2512.15068.pdf)  
**作者**：Debu Sinha  

**一句话要点**：应用保形预测量化RAG系统中基于嵌入的幻觉检测局限性，揭示语义幻觉问题。

**关键词**：检索增强生成, 幻觉检测, 保形预测, 语义相似性, 自然语言推理, 误报率

## 3 点简述
- 核心问题：RAG系统幻觉检测中，基于语义相似性和NLI的方法存在根本性局限，导致高误报率。
- 方法要点：采用保形预测提供有限样本覆盖保证，精确量化检测能力，使用约600个示例校准集。
- 实验或效果：在合成数据上实现94%覆盖率和0%误报率，但在真实基准上嵌入方法误报率高达50%-100%，GPT-4作为LLM法官仅7%误报率。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems remain susceptible to hallucinations despite grounding in retrieved evidence. Current detection methods rely on semantic similarity and natural language inference (NLI), but their fundamental limitations have not been rigorously characterized. We apply conformal prediction to hallucination detection, providing finite-sample coverage guarantees that enable precise quantification of detection capabilities. Using calibration sets of approximately 600 examples, we achieve 94% coverage with 0% false positive rate on synthetic hallucinations (Natural Questions). However, on three real hallucination benchmarks spanning multiple LLMs (GPT-4, ChatGPT, GPT-3, Llama-2, Mistral), embedding-based methods - including state-of-the-art OpenAI text-embedding-3-large and cross-encoder models - exhibit unacceptable false positive rates: 100% on HaluEval, 88% on RAGTruth, and 50% on WikiBio. Crucially, GPT-4 as an LLM judge achieves only 7% FPR (95% CI: [3.4%, 13.7%]) on the same data, proving the task is solvable through reasoning. We term this the "semantic illusion": semantically plausible hallucinations preserve similarity to source documents while introducing factual errors invisible to embeddings. This limitation persists across embedding architectures, LLM generators, and task types, suggesting embedding-based detection is insufficient for production RAG deployment.

