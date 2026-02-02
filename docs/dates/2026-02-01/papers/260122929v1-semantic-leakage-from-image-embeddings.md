---
layout: default
title: Semantic Leakage from Image Embeddings
---

# Semantic Leakage from Image Embeddings
**arXiv**：[2601.22929v1](https://arxiv.org/abs/2601.22929) · [PDF](https://arxiv.org/pdf/2601.22929.pdf)  
**作者**：Yiyi Chen, Qiongkai Xu, Desmond Eliott, Qiongxiu Li, Johannes Bjerva  

**一句话要点**：提出SLImE框架揭示图像嵌入的语义泄漏，挑战其隐私安全假设。

**关键词**：图像嵌入, 语义泄漏, 隐私安全, 嵌入对齐, 轻量级推理, 语义检索

## 3 点简述
- 核心问题：图像嵌入在压缩后仍可能泄露语义信息，无需精确重建原图。
- 方法要点：基于对齐嵌入保留的局部语义邻域，设计轻量级推理框架SLImE。
- 实验或效果：在多种嵌入模型中验证语义信息恢复，暴露隐私脆弱性。

## 摘要（原文）

> Image embeddings are generally assumed to pose limited privacy risk. We challenge this assumption by formalizing semantic leakage as the ability to recover semantic structures from compressed image embeddings. Surprisingly, we show that semantic leakage does not require exact reconstruction of the original image. Preserving local semantic neighborhoods under embedding alignment is sufficient to expose the intrinsic vulnerability of image embeddings. Crucially, this preserved neighborhood structure allows semantic information to propagate through a sequence of lossy mappings. Based on this conjecture, we propose Semantic Leakage from Image Embeddings (SLImE), a lightweight inference framework that reveals semantic information from standalone compressed image embeddings, incorporating a locally trained semantic retriever with off-the-shelf models, without training task-specific decoders. We thoroughly validate each step of the framework empirically, from aligned embeddings to retrieved tags, symbolic representations, and grammatical and coherent descriptions. We evaluate SLImE across a range of open and closed embedding models, including GEMINI, COHERE, NOMIC, and CLIP, and demonstrate consistent recovery of semantic information across diverse inference tasks. Our results reveal a fundamental vulnerability in image embeddings, whereby the preservation of semantic neighborhoods under alignment enables semantic leakage, highlighting challenges for privacy preservation.1

