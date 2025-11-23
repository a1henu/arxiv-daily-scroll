---
layout: default
title: Reasoning Guided Embeddings: Leveraging MLLM Reasoning for Improved Multimodal Retrieval
---

# Reasoning Guided Embeddings: Leveraging MLLM Reasoning for Improved Multimodal Retrieval
**arXiv**：[2511.16150v1](https://arxiv.org/abs/2511.16150) · [PDF](https://arxiv.org/pdf/2511.16150.pdf)  
**作者**：Chunxu Liu, Jiyuan Yang, Ruopeng Gao, Yuhan Zhu, Feng Zhu, Rui Zhao, Limin Wang  

**一句话要点**：提出推理引导嵌入方法，利用MLLM推理提升多模态检索性能

**关键词**：多模态检索, 推理引导嵌入, MLLM应用, 对比训练, 嵌入质量提升

## 3 点简述
- 现有方法忽视MLLM的生成推理能力，影响多模态嵌入质量
- 结合结构化推理生成与对比训练，增强嵌入中的上下文推理信号
- 在MMEB基准上，多模态检索性能提升4.9%，验证推理有效性

## 摘要（原文）

> Multimodal embeddings are widely used in downstream tasks such as multimodal retrieval, enabling alignment of interleaved modalities in a shared representation space. While recent studies show that Multimodal Large Language Models (MLLMs) can serve as strong embedding extractors, existing approaches treat embedding extraction as a direct encoding step, overlooking the fact that MLLMs possess the generative capability for reasoning that could be leveraged to enhance representation quality. In this work, we explore how to explicitly incorporate reasoning into the embedding process. To this end, we propose Reasoning Guided Embeddings (RGE), which preserves the generative rationale process of MLLMs and couples it with contrastive training. Our method first enables the model to perform structured rationale generation conditioned on the instruction, and then extracts representations after reasoning has unfolded. This simple design enhances the context-conditional inference signals within the embedding, leading to improved multimodal representation quality. Experiments on the MMEB benchmark show that reasoning-guided conditioning improves multimodal retrieval performance by 4.9% over the non-reasoning baseline, confirming that explicit reasoning can effectively enhance embedding quality.

