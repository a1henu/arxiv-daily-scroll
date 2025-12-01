---
layout: default
title: Resolving Evidence Sparsity: Agentic Context Engineering for Long-Document Understanding
---

# Resolving Evidence Sparsity: Agentic Context Engineering for Long-Document Understanding
**arXiv**：[2511.22850v1](https://arxiv.org/abs/2511.22850) · [PDF](https://arxiv.org/pdf/2511.22850.pdf)  
**作者**：Keliang Liu, Zizhi Chen, Mingcheng Li, Jingqun Tang, Dingkang Yang, Lihua Zhang  

**一句话要点**：提出SLEUTH多智能体框架以解决长文档理解中的证据稀疏问题

**关键词**：长文档理解, 多智能体框架, 证据稀疏, 视觉语言模型, 检索增强生成, 分层精炼

## 3 点简述
- 核心问题：长文档中线索分散且冗余，影响视觉语言模型性能
- 方法要点：采用粗到细流程，协调检索器和四个智能体进行证据筛选与推理
- 实验或效果：在多个基准测试中实现SOTA，消融研究验证模块有效性

## 摘要（原文）

> Document understanding is a long standing practical task. Vision Language Models (VLMs) have gradually become a primary approach in this domain, demonstrating effective performance on single page tasks. However, their effectiveness diminishes when handling long documents. In such scenarios, clues are often scattered across multiple pages and modalities, and redundancy from lengthy inputs can impair the models judgment. While retrieval augmented generation mitigates this issue by filtering for question relevant content, the retrieved results still contain substantial redundancy. To address these limitations, we propose SLEUTH, a multi agent framework. Concretely, SLEUTH orchestrates a retriever and four collaborative agents in a coarse to fine process. The framework identifies key textual and visual clues within the retrieved pages, filters for salient visual evidence such as tables and charts, and analyzes the query to devise a reasoning strategy. It ultimately synthesizes a distilled, evidence dense multimodal context to generate the final prediction. SLEUTH is model agnostic and scalable. When paired with advanced VLM backbones, it consistently improves performance on multiple long document benchmarks, achieving state of the art results. Ablation studies verify each modules effectiveness and confirm the benefits of our hierarchical refinement paradigm.

