---
layout: default
title: DeepEra: A Deep Evidence Reranking Agent for Scientific Retrieval-Augmented Generated Question Answering
---

# DeepEra: A Deep Evidence Reranking Agent for Scientific Retrieval-Augmented Generated Question Answering
**arXiv**：[2601.16478v1](https://arxiv.org/abs/2601.16478) · [PDF](https://arxiv.org/pdf/2601.16478.pdf)  
**作者**：Haotian Chen, Qingqing Long, Siyu Pu, Xiao Luo, Wei Ju, Meng Xiao, Yuanchun Zhou, Jianghua Zhao, Xuezhi Wang  

**一句话要点**：提出DeepEra深度证据重排代理，以解决科学检索增强生成问答中语义相似但逻辑无关的挑战。

**关键词**：科学问答, 检索增强生成, 证据重排, 逻辑无关性, 逐步推理, 数据集构建

## 3 点简述
- 核心问题：现有检索重排方法易受语义相似但逻辑无关段落影响，降低事实可靠性并加剧幻觉。
- 方法要点：集成逐步推理，超越表层语义，更精确评估候选段落。
- 实验或效果：构建SciRAG-SSLI数据集，全面评估显示优于领先重排器的检索性能。

## 摘要（原文）

> With the rapid growth of scientific literature, scientific question answering (SciQA) has become increasingly critical for exploring and utilizing scientific knowledge. Retrieval-Augmented Generation (RAG) enhances LLMs by incorporating knowledge from external sources, thereby providing credible evidence for scientific question answering. But existing retrieval and reranking methods remain vulnerable to passages that are semantically similar but logically irrelevant, often reducing factual reliability and amplifying hallucinations.To address this challenge, we propose a Deep Evidence Reranking Agent (DeepEra) that integrates step-by-step reasoning, enabling more precise evaluation of candidate passages beyond surface-level semantics. To support systematic evaluation, we construct SciRAG-SSLI (Scientific RAG - Semantically Similar but Logically Irrelevant), a large-scale dataset comprising about 300K SciQA instances across 10 subjects, constructed from 10M scientific corpus. The dataset combines naturally retrieved contexts with systematically generated distractors to test logical robustness and factual grounding. Comprehensive evaluations confirm that our approach achieves superior retrieval performance compared to leading rerankers. To our knowledge, this work is the first to comprehensively study and empirically validate innegligible SSLI issues in two-stage RAG frameworks.

