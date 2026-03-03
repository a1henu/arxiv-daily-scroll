---
layout: default
title: Reconstructing Content via Collaborative Attention to Improve Multimodal Embedding Quality
---

# Reconstructing Content via Collaborative Attention to Improve Multimodal Embedding Quality
**arXiv**：[2603.01471v1](https://arxiv.org/abs/2603.01471) · [PDF](https://arxiv.org/pdf/2603.01471.pdf)  
**作者**：Jiahan Chen, Da Li, Hengran Zhang, Yinqiong Cai, Lixin Su, Jiafeng Guo, Daiting Shi, Dawei Yin, Keping Bi  

**一句话要点**：提出基于协作注意力的内容重建预训练范式CoCoA，以优化多模态嵌入质量

**关键词**：多模态嵌入, 注意力机制, 预训练范式, 内容重建, 对比学习

## 3 点简述
- 现有MLLM的因果注意力范式难以形成全局紧凑表示，限制嵌入质量
- 通过重构注意力流并引入基于EOS的重建任务，将语义信息压缩至<EOS>标记
- 在MMEB-V1基准上验证，基于Qwen2-VL的CoCoA显著提升嵌入性能

## 摘要（原文）

> Multimodal embedding models, rooted in multimodal large language models (MLLMs), have yielded significant performance improvements across diverse tasks such as retrieval and classification. However, most existing approaches rely heavily on large-scale contrastive learning, with limited exploration of how the architectural and training paradigms of MLLMs affect embedding quality. While effective for generation, the causal attention and next-token prediction paradigm of MLLMs does not explicitly encourage the formation of globally compact representations, limiting their effectiveness as multimodal embedding backbones. To address this, we propose CoCoA, a Content reconstruction pre-training paradigm based on Collaborative Attention for multimodal embedding optimization. Specifically, we restructure the attention flow and introduce an EOS-based reconstruction task, encouraging the model to reconstruct input from the corresponding <EOS> embeddings. This drives the multimodal model to compress the semantic information of the input into the <EOS> token, laying the foundations for subsequent contrastive learning. Extensive experiments on MMEB-V1 demonstrate that CoCoA built upon Qwen2-VL and Qwen2.5-VL significantly improves embedding quality. Results validate that content reconstruction serves as an effective strategy to maximize the value of existing data, enabling multimodal embedding models generate compact and informative representations, raising their performance ceiling.

