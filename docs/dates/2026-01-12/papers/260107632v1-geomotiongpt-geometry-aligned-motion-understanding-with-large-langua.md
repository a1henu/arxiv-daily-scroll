---
layout: default
title: GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models
---

# GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models
**arXiv**：[2601.07632v1](https://arxiv.org/abs/2601.07632) · [PDF](https://arxiv.org/pdf/2601.07632.pdf)  
**作者**：Zhankai Ye, Bofan Li, Yukai Jin, Shuoqiu Li, Wei Wang, Yanfu Zhang, Shangqian Gao, Xin Liu  

**一句话要点**：提出GeoMotionGPT框架，通过几何对齐提升大语言模型在运动理解中的推理能力。

**关键词**：运动理解, 几何对齐, 大语言模型, 正交正则化, 运动量化

## 3 点简述
- 现有方法将运动量化与语义嵌入学习解耦，导致运动空间几何与嵌入空间未对齐，影响推理精度。
- 采用正交化运动码本和LLM嵌入空间，通过稀疏投影和两阶段正则化实现几何对齐。
- 在HumanML3D数据集上实验，性能提升20%，验证几何对齐对运动推理的有效性。

## 摘要（原文）

> Discrete motion tokenization has recently enabled Large Language Models (LLMs) to serve as versatile backbones for motion understanding and motion-language reasoning. However, existing pipelines typically decouple motion quantization from semantic embedding learning, linking them solely via token IDs. This approach fails to effectively align the intrinsic geometry of the motion space with the embedding space, thereby hindering the LLM's capacity for nuanced motion reasoning. We argue that alignment is most effective when both modalities share a unified geometric basis. Therefore, instead of forcing the LLM to reconstruct the complex geometry among motion tokens from scratch, we present a novel framework that explicitly enforces orthogonality on both the motion codebook and the LLM embedding space, ensuring that their relational structures naturally mirror each other. Specifically, we employ a decoder-only quantizer with Gumbel-Softmax for differentiable training and balanced codebook usage. To bridge the modalities, we use a sparse projection that maps motion codes into the LLM embedding space while preserving orthogonality. Finally, a two-stage orthonormal regularization schedule enforces soft constraints during tokenizer training and LLM fine-tuning to maintain geometric alignment without hindering semantic adaptation. Extensive experiments on HumanML3D demonstrate that our framework achieves a 20% performance improvement over current state-of-the-art methods, validating that a unified geometric basis effectively empowers the LLM for nuanced motion reasoning.

