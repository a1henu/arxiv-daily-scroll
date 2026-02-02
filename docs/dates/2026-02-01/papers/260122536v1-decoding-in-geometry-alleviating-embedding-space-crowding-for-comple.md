---
layout: default
title: Decoding in Geometry: Alleviating Embedding-Space Crowding for Complex Reasoning
---

# Decoding in Geometry: Alleviating Embedding-Space Crowding for Complex Reasoning
**arXiv**：[2601.22536v1](https://arxiv.org/abs/2601.22536) · [PDF](https://arxiv.org/pdf/2601.22536.pdf)  
**作者**：Yixin Yang, Qingxiu Dong, Zhifang Sui  

**一句话要点**：提出CraEG解码方法以缓解嵌入空间拥挤，提升大语言模型复杂推理性能

**关键词**：嵌入空间拥挤, 几何引导解码, 大语言模型推理, 采样策略, 数学问题求解

## 3 点简述
- 核心问题：嵌入空间拥挤现象导致解码时概率集中在几何邻近的令牌上，影响推理质量
- 方法要点：CraEG通过几何引导重加权，训练免费、单次解码，兼容标准采样策略
- 实验或效果：在多个模型和基准测试中，生成性能提升，鲁棒性和多样性指标改善

## 摘要（原文）

> Sampling-based decoding underlies complex reasoning in large language models (LLMs), where decoding strategies critically shape model behavior. Temperature- and truncation-based methods reshape the next-token distribution through global probability reweighting or thresholding to balance the quality-diversity tradeoff. However, they operate solely on token probabilities, ignoring fine-grained relationships among tokens in the embedding space. We uncover a novel phenomenon, embedding-space crowding, where the next-token distribution concentrates its probability mass on geometrically close tokens in the embedding space. We quantify crowding at multiple granularities and find a statistical association with reasoning success in mathematical problem solving. Motivated by this finding, we propose CraEG, a plug-and-play sampling method that mitigates crowding through geometry-guided reweighting. CraEG is training-free, single-pass, and compatible with standard sampling strategies. Experiments on multiple models and benchmarks demonstrate improved generation performance, with gains in robustness and diversity metrics.

