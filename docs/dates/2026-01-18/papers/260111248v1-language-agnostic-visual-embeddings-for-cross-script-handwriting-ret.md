---
layout: default
title: Language-Agnostic Visual Embeddings for Cross-Script Handwriting Retrieval
---

# Language-Agnostic Visual Embeddings for Cross-Script Handwriting Retrieval
**arXiv**：[2601.11248v1](https://arxiv.org/abs/2601.11248) · [PDF](https://arxiv.org/pdf/2601.11248.pdf)  
**作者**：Fangke Chen, Tianhao Dong, Sirry Chen, Guobin Zhang, Yishu Zhang, Yining Chen  

**一句话要点**：提出轻量级非对称双编码器框架，实现跨语言手写体检索

**关键词**：手写体检索, 跨语言检索, 视觉嵌入, 轻量级模型, 非对称编码器

## 3 点简述
- 核心问题：手写体检索面临书写风格差异大、跨语言语义鸿沟等挑战，现有大模型计算成本过高
- 方法要点：通过联合优化实例级对齐和类级语义一致性，学习语言无关的视觉嵌入表示
- 实验效果：在跨语言检索任务中超越28个基线模型，参数大幅减少但保持高精度

## 摘要（原文）

> Handwritten word retrieval is vital for digital archives but remains challenging due to large handwriting variability and cross-lingual semantic gaps. While large vision-language models offer potential solutions, their prohibitive computational costs hinder practical edge deployment. To address this, we propose a lightweight asymmetric dual-encoder framework that learns unified, style-invariant visual embeddings. By jointly optimizing instance-level alignment and class-level semantic consistency, our approach anchors visual embeddings to language-agnostic semantic prototypes, enforcing invariance across scripts and writing styles. Experiments show that our method outperforms 28 baselines and achieves state-of-the-art accuracy on within-language retrieval benchmarks. We further conduct explicit cross-lingual retrieval, where the query language differs from the target language, to validate the effectiveness of the learned cross-lingual representations. Achieving strong performance with only a fraction of the parameters required by existing models, our framework enables accurate and resource-efficient cross-script handwriting retrieval.

