---
layout: default
title: Multimodal Latent Reasoning via Hierarchical Visual Cues Injection
---

# Multimodal Latent Reasoning via Hierarchical Visual Cues Injection
**arXiv**：[2602.05359v1](https://arxiv.org/abs/2602.05359) · [PDF](https://arxiv.org/pdf/2602.05359.pdf)  
**作者**：Yiming Zhang, Qiangyu Yan, Borui Jiang, Kai Han  

**一句话要点**：提出HIVE框架，通过分层视觉线索注入实现多模态潜在推理，以提升复杂场景理解。

**关键词**：多模态大语言模型, 潜在推理, 分层视觉线索, Transformer扩展, 场景理解, 测试时间缩放

## 3 点简述
- 核心问题：现有MLLMs推理依赖快速思维或显式语言链，易导致低效、冗长和幻觉。
- 方法要点：递归扩展Transformer块，在潜在空间中迭代推理，并注入从全局到细粒度的分层视觉线索。
- 实验或效果：评估显示结合视觉知识时测试时间缩放有效，分层信息显著增强复杂场景理解能力。

## 摘要（原文）

> The advancement of multimodal large language models (MLLMs) has enabled impressive perception capabilities. However, their reasoning process often remains a "fast thinking" paradigm, reliant on end-to-end generation or explicit, language-centric chains of thought (CoT), which can be inefficient, verbose, and prone to hallucination. This work posits that robust reasoning should evolve within a latent space, integrating multimodal signals seamlessly. We propose multimodal latent reasoning via HIerarchical Visual cuEs injection (\emph{HIVE}), a novel framework that instills deliberate, "slow thinking" without depending on superficial textual rationales. Our method recursively extends transformer blocks, creating an internal loop for iterative reasoning refinement. Crucially, it injectively grounds this process with hierarchical visual cues from global scene context to fine-grained regional details directly into the model's latent representations. This enables the model to perform grounded, multi-step inference entirely in the aligned latent space. Extensive evaluations demonstrate that test-time scaling is effective when incorporating vision knowledge, and that integrating hierarchical information significantly enhances the model's understanding of complex scenes.

