---
layout: default
title: Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale
---

# Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale
**arXiv**：[2601.20276v1](https://arxiv.org/abs/2601.20276) · [PDF](https://arxiv.org/pdf/2601.20276.pdf)  
**作者**：Tianwei Lin, Zuyi Zhou, Xinda Zhao, Chenke Wang, Xiaohong Li, Yu Chen, Chuanrui Hu, Jian Pei, Yafeng Deng  

**一句话要点**：提出EverMemBench-S基准以评估长上下文LLM在语义干扰下的证据访问与使用能力

**关键词**：长上下文评估, 语义干扰, 证据访问, 检索增强生成, 基准测试, 大语言模型

## 3 点简述
- 核心问题：现有NIAH评估仅测量良性跨度定位，忽略语义干扰下的证据访问瓶颈
- 方法要点：构建326M令牌MemoryBank，包含碰撞测试的近误硬负例和人工验证的金证据集
- 实验或效果：在从64K到326M令牌的语料阶梯上，系统在语义干扰下证据访问性能显著下降

## 摘要（原文）

> Long-context LLM agents must access the right evidence from large environments and use it faithfully. However, the popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization. The needle is near-unique, and the haystack is largely irrelevant. We introduce EverMemBench-S (EMB-S), an adversarial NIAH-style benchmark built on a 326M-token MemoryBank. While the full MemoryBank spans 326M tokens for retrieval-based (RAG) evaluation, we evaluate native long-context models only at scales that fit within each model's context window (up to 1M tokens in this work) to ensure a fair comparison. EMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification. We also propose a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting. This enables consistent diagnosis for both native long-context prompting and retrieval pipelines. Across a reference-corpus ladder from domain-isolated 64K contexts to a globally shared 326M-token environment, we observe a clear reality gap. Systems that saturate benign NIAH degrade sharply in evidence access under semantic interference. These results indicate that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.

