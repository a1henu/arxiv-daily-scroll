---
layout: default
title: Attention Grounded Enhancement for Visual Document Retrieval
---

# Attention Grounded Enhancement for Visual Document Retrieval
**arXiv**：[2511.13415v1](https://arxiv.org/abs/2511.13415) · [PDF](https://arxiv.org/pdf/2511.13415.pdf)  
**作者**：Wanqing Cui, Wei Huang, Yazhi Guo, Yibo Hu, Meiguang Jin, Junfeng Ma, Keping Bi  

**一句话要点**：提出AGREE框架以解决视觉文档检索中依赖表面线索的问题

**关键词**：视觉文档检索, 跨模态注意力, 局部监督, 检索增强, 多模态理解

## 3 点简述
- 核心问题：检索器依赖全局相关标签，难以捕捉隐式语义连接
- 方法要点：利用跨模态注意力作为局部监督，结合全局信号优化检索器
- 实验或效果：在ViDoRe V2基准上显著优于仅全局监督基线

## 摘要（原文）

> Visual document retrieval requires understanding heterogeneous and multi-modal content to satisfy information needs. Recent advances use screenshot-based document encoding with fine-grained late interaction, significantly improving retrieval performance. However, retrievers are still trained with coarse global relevance labels, without revealing which regions support the match. As a result, retrievers tend to rely on surface-level cues and struggle to capture implicit semantic connections, hindering their ability to handle non-extractive queries. To alleviate this problem, we propose a \textbf{A}ttention-\textbf{G}rounded \textbf{RE}triever \textbf{E}nhancement (AGREE) framework. AGREE leverages cross-modal attention from multimodal large language models as proxy local supervision to guide the identification of relevant document regions. During training, AGREE combines local signals with the global signals to jointly optimize the retriever, enabling it to learn not only whether documents match, but also which content drives relevance. Experiments on the challenging ViDoRe V2 benchmark show that AGREE significantly outperforms the global-supervision-only baseline. Quantitative and qualitative analyses further demonstrate that AGREE promotes deeper alignment between query terms and document regions, moving beyond surface-level matching toward more accurate and interpretable retrieval. Our code is available at: https://anonymous.4open.science/r/AGREE-2025.

