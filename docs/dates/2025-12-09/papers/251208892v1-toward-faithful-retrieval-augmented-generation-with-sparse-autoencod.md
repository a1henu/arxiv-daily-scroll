---
layout: default
title: Toward Faithful Retrieval-Augmented Generation with Sparse Autoencoders
---

# Toward Faithful Retrieval-Augmented Generation with Sparse Autoencoders
**arXiv**：[2512.08892v1](https://arxiv.org/abs/2512.08892) · [PDF](https://arxiv.org/pdf/2512.08892.pdf)  
**作者**：Guangzhi Xiong, Zhenghao He, Bohan Liu, Sanchit Sinha, Aidong Zhang  

**一句话要点**：提出RAGLens，基于稀疏自编码器检测检索增强生成中的不忠实输出。

**关键词**：检索增强生成, 稀疏自编码器, 幻觉检测, 可解释性, 轻量级检测器

## 3 点简述
- 核心问题：检索增强生成存在不忠实输出，现有检测方法依赖大量标注数据或高推理成本。
- 方法要点：利用稀疏自编码器解耦内部激活，通过信息特征选择和加性建模构建轻量级检测器。
- 实验或效果：RAGLens检测性能优于现有方法，提供可解释理由，并揭示幻觉信号分布新见解。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs) by grounding outputs in retrieved evidence, but faithfulness failures, where generations contradict or extend beyond the provided sources, remain a critical challenge. Existing hallucination detection methods for RAG often rely either on large-scale detector training, which requires substantial annotated data, or on querying external LLM judges, which leads to high inference costs. Although some approaches attempt to leverage internal representations of LLMs for hallucination detection, their accuracy remains limited. Motivated by recent advances in mechanistic interpretability, we employ sparse autoencoders (SAEs) to disentangle internal activations, successfully identifying features that are specifically triggered during RAG hallucinations. Building on a systematic pipeline of information-based feature selection and additive feature modeling, we introduce RAGLens, a lightweight hallucination detector that accurately flags unfaithful RAG outputs using LLM internal representations. RAGLens not only achieves superior detection performance compared to existing methods, but also provides interpretable rationales for its decisions, enabling effective post-hoc mitigation of unfaithful RAG. Finally, we justify our design choices and reveal new insights into the distribution of hallucination-related signals within LLMs. The code is available at https://github.com/Teddy-XiongGZ/RAGLens.

