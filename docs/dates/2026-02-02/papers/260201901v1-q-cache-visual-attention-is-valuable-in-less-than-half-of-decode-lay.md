---
layout: default
title: Q Cache: Visual Attention is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model
---

# Q Cache: Visual Attention is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model
**arXiv**：[2602.01901v1](https://arxiv.org/abs/2602.01901) · [PDF](https://arxiv.org/pdf/2602.01901.pdf)  
**作者**：Jiedong Zhuang, Lu Lu, Ming Dai, Rui Hu, Jian Chen, Qiang Liu, Haoji Hu  

**一句话要点**：提出Q Cache与Lazy Attention以减少多模态大语言模型解码层冗余计算

**关键词**：多模态大语言模型, 注意力机制优化, KV缓存压缩, 推理加速, 视觉令牌冗余

## 3 点简述
- 核心问题：视觉编码器产生冗余视觉令牌，导致高推理成本和KV缓存瓶颈
- 方法要点：基于注意力机制相似性，设计跨层共享查询的Lazy Attention机制
- 实验或效果：在多个基准测试中，KV缓存减少超35%，吞吐量提升1.5倍，性能损失约1%

## 摘要（原文）

> Multimodal large language models (MLLMs) are plagued by exorbitant inference costs attributable to the profusion of visual tokens within the vision encoder. The redundant visual tokens engenders a substantial computational load and key-value (KV) cache footprint bottleneck. Existing approaches focus on token-wise optimization, leveraging diverse intricate token pruning techniques to eliminate non-crucial visual tokens. Nevertheless, these methods often unavoidably undermine the integrity of the KV cache, resulting in failures in long-text generation tasks. To this end, we conduct an in-depth investigation towards the attention mechanism of the model from a new perspective, and discern that attention within more than half of all decode layers are semantic similar. Upon this finding, we contend that the attention in certain layers can be streamlined by inheriting the attention from their preceding layers. Consequently, we propose Lazy Attention, an efficient attention mechanism that enables cross-layer sharing of similar attention patterns. It ingeniously reduces layer-wise redundant computation in attention. In Lazy Attention, we develop a novel layer-shared cache, Q Cache, tailored for MLLMs, which facilitates the reuse of queries across adjacent layers. In particular, Q Cache is lightweight and fully compatible with existing inference frameworks, including Flash Attention and KV cache. Additionally, our method is highly flexible as it is orthogonal to existing token-wise techniques and can be deployed independently or combined with token pruning approaches. Empirical evaluations on multiple benchmarks demonstrate that our method can reduce KV cache usage by over 35% and achieve 1.5x throughput improvement, while sacrificing only approximately 1% of performance on various MLLMs. Compared with SOTA token-wise methods, our technique achieves superior accuracy preservation.

