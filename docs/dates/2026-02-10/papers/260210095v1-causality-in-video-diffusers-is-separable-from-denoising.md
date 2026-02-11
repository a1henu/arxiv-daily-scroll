---
layout: default
title: Causality in Video Diffusers is Separable from Denoising
---

# Causality in Video Diffusers is Separable from Denoising
**arXiv**：[2602.10095v1](https://arxiv.org/abs/2602.10095) · [PDF](https://arxiv.org/pdf/2602.10095.pdf)  
**作者**：Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  

**一句话要点**：提出可分离因果扩散架构，将视频生成中的因果推理与去噪过程解耦，提升效率与质量。

**关键词**：因果扩散模型, 视频生成, 可分离架构, 因果推理, 去噪过程, 效率优化

## 3 点简述
- 当前因果扩散模型将时间推理与迭代去噪纠缠，导致计算冗余和效率低下。
- 通过分析自回归视频扩散模型，发现早期层特征相似、深层层注意力稀疏，提出分离因果推理与帧渲染。
- 实验表明，新架构在合成和真实基准上匹配或超越基线质量，同时显著提高吞吐量和延迟。

## 摘要（原文）

> Causality -- referring to temporal, uni-directional cause-effect relationships between components -- underlies many complex generative processes, including videos, language, and robot trajectories. Current causal diffusion models entangle temporal reasoning with iterative denoising, applying causal attention across all layers, at every denoising step, and over the entire context. In this paper, we show that the causal reasoning in these models is separable from the multi-step denoising process. Through systematic probing of autoregressive video diffusers, we uncover two key regularities: (1) early layers produce highly similar features across denoising steps, indicating redundant computation along the diffusion trajectory; and (2) deeper layers exhibit sparse cross-frame attention and primarily perform intra-frame rendering. Motivated by these findings, we introduce Separable Causal Diffusion (SCD), a new architecture that explicitly decouples once-per-frame temporal reasoning, via a causal transformer encoder, from multi-step frame-wise rendering, via a lightweight diffusion decoder. Extensive experiments on both pretraining and post-training tasks across synthetic and real benchmarks show that SCD significantly improves throughput and per-frame latency while matching or surpassing the generation quality of strong causal diffusion baselines.

