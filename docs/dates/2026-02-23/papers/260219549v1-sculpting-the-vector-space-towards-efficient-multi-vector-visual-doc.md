---
layout: default
title: Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework
---

# Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework
**arXiv**：[2602.19549v1](https://arxiv.org/abs/2602.19549) · [PDF](https://arxiv.org/pdf/2602.19549.pdf)  
**作者**：Yibo Yan, Mingdong Ou, Yi Cao, Xin Zou, Jiahao Huo, Shuliang Liu, James Kwok, Xuming Hu  

**一句话要点**：提出Prune-then-Merge框架以解决视觉文档检索中多向量范式效率与性能的权衡问题

**关键词**：视觉文档检索, 多向量范式, 自适应剪枝, 分层合并, 压缩效率, 特征保真度

## 3 点简述
- 核心问题：多向量范式在视觉文档检索中性能优越但开销巨大，现有剪枝与合并方法在压缩率和特征保真度间难以平衡
- 方法要点：采用自适应剪枝阶段过滤低信息补丁，再通过分层合并阶段压缩预过滤嵌入集，避免噪声导致的特征稀释
- 实验或效果：在29个VDR数据集上验证，框架优于现有方法，显著扩展近无损压缩范围并在高压缩比下保持稳健性能

## 摘要（原文）

> Visual Document Retrieval (VDR), which aims to retrieve relevant pages within vast corpora of visually-rich documents, is of significance in current multimodal retrieval applications. The state-of-the-art multi-vector paradigm excels in performance but suffers from prohibitive overhead, a problem that current efficiency methods like pruning and merging address imperfectly, creating a difficult trade-off between compression rate and feature fidelity. To overcome this dilemma, we introduce Prune-then-Merge, a novel two-stage framework that synergizes these complementary approaches. Our method first employs an adaptive pruning stage to filter out low-information patches, creating a refined, high-signal set of embeddings. Subsequently, a hierarchical merging stage compresses this pre-filtered set, effectively summarizing semantic content without the noise-induced feature dilution seen in single-stage methods. Extensive experiments on 29 VDR datasets demonstrate that our framework consistently outperforms existing methods, significantly extending the near-lossless compression range and providing robust performance at high compression ratios.

