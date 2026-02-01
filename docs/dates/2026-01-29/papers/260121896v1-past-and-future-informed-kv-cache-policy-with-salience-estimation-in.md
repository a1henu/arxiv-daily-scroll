---
layout: default
title: Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion
---

# Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion
**arXiv**：[2601.21896v1](https://arxiv.org/abs/2601.21896) · [PDF](https://arxiv.org/pdf/2601.21896.pdf)  
**作者**：Hanmo Chen, Chenghao Xu, Xu Yang, Xuan Chen, Cheng Deng  

**一句话要点**：提出PaFu-KV策略，通过显著性估计优化KV缓存，以提升自回归视频扩散的长时生成质量与效率。

**关键词**：自回归视频生成, KV缓存优化, 显著性估计, 蒸馏训练, 长时视频合成, 推理加速

## 3 点简述
- 现有自回归视频生成方法依赖启发式KV缓存策略，忽略令牌重要性差异，导致关键信息丢失和冗余缓存累积。
- PaFu-KV引入轻量级显著性估计头，基于双向教师蒸馏估计令牌显著性，动态保留重要令牌并丢弃无关令牌。
- 实验表明，该方法在保持高保真视频生成质量的同时，减少KV缓存容量和内存占用，加速推理过程。

## 摘要（原文）

> Video generation is pivotal to digital media creation, and recent advances in autoregressive video generation have markedly enhanced the efficiency of real-time video synthesis. However, existing approaches generally rely on heuristic KV Cache policies, which ignore differences in token importance in long-term video generation. This leads to the loss of critical spatiotemporal information and the accumulation of redundant, invalid cache, thereby degrading video generation quality and efficiency. To address this limitation, we first observe that token contributions to video generation are highly time-heterogeneous and accordingly propose a novel Past- and Future-Informed KV Cache Policy (PaFu-KV). Specifically, PaFu-KV introduces a lightweight Salience Estimation Head distilled from a bidirectional teacher to estimate salience scores, allowing the KV cache to retain informative tokens while discarding less relevant ones. This policy yields a better quality-efficiency trade-off by shrinking KV cache capacity and reducing memory footprint at inference time. Extensive experiments on benchmarks demonstrate that our method preserves high-fidelity video generation quality while enables accelerated inference, thereby enabling more efficient long-horizon video generation. Our code will be released upon paper acceptance.

