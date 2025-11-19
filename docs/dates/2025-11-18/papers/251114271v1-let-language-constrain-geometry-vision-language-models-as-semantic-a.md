---
layout: default
title: Let Language Constrain Geometry: Vision-Language Models as Semantic and Spatial Critics for 3D Generation
---

# Let Language Constrain Geometry: Vision-Language Models as Semantic and Spatial Critics for 3D Generation
**arXiv**：[2511.14271v1](https://arxiv.org/abs/2511.14271) · [PDF](https://arxiv.org/pdf/2511.14271.pdf)  
**作者**：Weimin Bai, Yubo Li, Weijian Luo, Zeqiang Lai, Yequan Wang, Wenzheng Chen, He Sun  

**一句话要点**：提出VLM3D框架，利用视觉语言模型作为语义和空间批评器以改进文本到3D生成

**关键词**：文本到3D生成, 视觉语言模型, 语义对齐, 空间理解, 批评信号, 3D生成优化

## 3 点简述
- 核心问题：文本到3D生成模型存在语义对齐粗糙和空间理解不足的问题
- 方法要点：使用VLM的双查询批评信号评估语义保真度和几何一致性
- 实验或效果：在优化和前馈管道中显著提升性能，纠正空间错误

## 摘要（原文）

> Text-to-3D generation has advanced rapidly, yet state-of-the-art models, encompassing both optimization-based and feed-forward architectures, still face two fundamental limitations. First, they struggle with coarse semantic alignment, often failing to capture fine-grained prompt details. Second, they lack robust 3D spatial understanding, leading to geometric inconsistencies and catastrophic failures in part assembly and spatial relationships. To address these challenges, we propose VLM3D, a general framework that repurposes large vision-language models (VLMs) as powerful, differentiable semantic and spatial critics. Our core contribution is a dual-query critic signal derived from the VLM's Yes or No log-odds, which assesses both semantic fidelity and geometric coherence. We demonstrate the generality of this guidance signal across two distinct paradigms: (1) As a reward objective for optimization-based pipelines, VLM3D significantly outperforms existing methods on standard benchmarks. (2) As a test-time guidance module for feed-forward pipelines, it actively steers the iterative sampling process of SOTA native 3D models to correct severe spatial errors. VLM3D establishes a principled and generalizable path to inject the VLM's rich, language-grounded understanding of both semantics and space into diverse 3D generative pipelines.

