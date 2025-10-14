---
layout: default
title: Scaling Language-Centric Omnimodal Representation Learning
---

# Scaling Language-Centric Omnimodal Representation Learning
**arXiv**：[2510.11693v1](https://arxiv.org/abs/2510.11693) · [PDF](https://arxiv.org/pdf/2510.11693.pdf)  
**作者**：Chenghao Xiao, Hou Pong Chan, Hao Zhang, Weiwen Xu, Mahani Aljunied, Yu Rong  

**一句话要点**：提出语言中心全模态嵌入框架以增强多模态表示学习

**关键词**：多模态表示学习, 语言中心嵌入, 对比学习, 生成预训练, 跨模态对齐, 缩放定律

## 3 点简述
- 核心问题：基于MLLM的多模态嵌入方法优势原因未明，需探索隐式跨模态对齐机制。
- 方法要点：利用生成预训练中的隐式对齐，结合对比学习轻量化优化表示空间。
- 实验或效果：在多种基准测试中实现SOTA，验证生成-表示缩放定律的有效性。

## 摘要（原文）

> Recent multimodal embedding approaches leveraging multimodal large language
> models (MLLMs) fine-tuned with contrastive learning (CL) have shown promising
> results, yet the underlying reasons behind their superiority remain
> underexplored. This work argues that a crucial advantage of MLLM-based
> approaches stems from implicit cross-modal alignment achieved during generative
> pretraining, where the language decoder learns to exploit multimodal signals
> within a shared representation space for generating unimodal outputs. Through
> analysis of anisotropy and kernel similarity structure, we empirically confirm
> that latent alignment emerges within MLLM representations, allowing CL to serve
> as a lightweight refinement stage. Leveraging this insight, we propose a
> Language-Centric Omnimodal Embedding framework, termed LCO-Emb. Extensive
> experiments across diverse backbones and benchmarks demonstrate its
> effectiveness, achieving state-of-the-art performance across modalities.
> Furthermore, we identify a Generation-Representation Scaling Law (GRSL),
> showing that the representational capabilities gained through contrastive
> refinement scales positively with the MLLM's generative capabilities. This
> suggests that improving generative abilities evolves as an effective paradigm
> for enhancing representation quality. We provide a theoretical explanation of
> GRSL, which formally links the MLLM's generative quality to the upper bound on
> its representation performance, and validate it on a challenging, low-resource
> visual-document retrieval task, showing that continual generative pretraining
> before CL can further enhance the potential of a model's embedding
> capabilities. Codes, models, and resources are available at
> https://github.com/LCO-Embedding/LCO-Embedding.

