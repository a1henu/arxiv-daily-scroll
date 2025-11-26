---
layout: default
title: Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout
---

# Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout
**arXiv**：[2511.20649v1](https://arxiv.org/abs/2511.20649) · [PDF](https://arxiv.org/pdf/2511.20649.pdf)  
**作者**：Hidir Yesiltepe, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Pinar Yanardag  

**一句话要点**：提出∞-RoPE框架以解决自回归视频扩散模型的有限时长、控制迟缓和无法实现场景切换问题

**关键词**：无限视频生成, 自回归模型, 位置编码, 动作控制, 场景切换, 推理时优化

## 3 点简述
- 核心问题：自回归视频扩散模型受限于3D-RoPE的有限时长、长视频中动作控制响应慢，以及无法实现场景切换
- 方法要点：通过Block-Relativistic RoPE、KV Flush和RoPE Cut组件，实现无限时长生成、即时动作控制和场景切换
- 实验或效果：在VBench评分中持续超越先前自回归模型，验证了无限时长、可控和电影化视频生成能力

## 摘要（原文）

> Current autoregressive video diffusion models are constrained by three core bottlenecks: (i) the finite temporal horizon imposed by the base model's 3D Rotary Positional Embedding (3D-RoPE), (ii) slow prompt responsiveness in maintaining fine-grained action control during long-form rollouts, and (iii) the inability to realize discontinuous cinematic transitions within a single generation stream. We introduce $\infty$-RoPE, a unified inference-time framework that addresses all three limitations through three interconnected components: Block-Relativistic RoPE, KV Flush, and RoPE Cut. Block-Relativistic RoPE reformulates temporal encoding as a moving local reference frame, where each newly generated latent block is rotated relative to the base model's maximum frame horizon while earlier blocks are rotated backward to preserve relative temporal geometry. This relativistic formulation eliminates fixed temporal positions, enabling continuous video generation far beyond the base positional limits. To obtain fine-grained action control without re-encoding, KV Flush renews the KV cache by retaining only two latent frames, the global sink and the last generated latent frame, thereby ensuring immediate prompt responsiveness. Finally, RoPE Cut introduces controlled discontinuities in temporal RoPE coordinates, enabling multi-cut scene transitions within a single continuous rollout. Together, these components establish $\infty$-RoPE as a training-free foundation for infinite-horizon, controllable, and cinematic video diffusion. Comprehensive experiments show that $\infty$-RoPE consistently surpasses previous autoregressive models in overall VBench scores.

