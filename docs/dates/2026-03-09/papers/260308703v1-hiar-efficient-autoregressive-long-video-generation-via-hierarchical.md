---
layout: default
title: HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising
---

# HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising
**arXiv**：[2603.08703v1](https://arxiv.org/abs/2603.08703) · [PDF](https://arxiv.org/pdf/2603.08703.pdf)  
**作者**：Kai Zou, Dian Zheng, Hongbo Liu, Tiankai Hang, Bin Liu, Nenghai Yu  

**一句话要点**：提出HiAR框架，通过分层去噪解决自回归长视频生成中的质量退化问题。

**关键词**：长视频生成, 自回归扩散, 分层去噪, 错误传播缓解, 蒸馏训练, 时间一致性

## 3 点简述
- 核心问题：自回归扩散生成长视频时，基于高度去噪上下文导致错误传播和渐进质量下降。
- 方法要点：采用分层去噪，在相同噪声级别上条件化上下文，以保持时间一致性并减少错误累积。
- 实验或效果：在VBench上实现最佳总分和最低时间漂移，推理速度提升1.8倍。

## 摘要（原文）

> Autoregressive (AR) diffusion offers a promising framework for generating videos of theoretically infinite length. However, a major challenge is maintaining temporal continuity while preventing the progressive quality degradation caused by error accumulation. To ensure continuity, existing methods typically condition on highly denoised contexts; yet, this practice propagates prediction errors with high certainty, thereby exacerbating degradation. In this paper, we argue that a highly clean context is unnecessary. Drawing inspiration from bidirectional diffusion models, which denoise frames at a shared noise level while maintaining coherence, we propose that conditioning on context at the same noise level as the current block provides sufficient signal for temporal consistency while effectively mitigating error propagation. Building on this insight, we propose HiAR, a hierarchical denoising framework that reverses the conventional generation order: instead of completing each block sequentially, it performs causal generation across all blocks at every denoising step, so that each block is always conditioned on context at the same noise level. This hierarchy naturally admits pipelined parallel inference, yielding a 1.8 wall-clock speedup in our 4-step setting. We further observe that self-rollout distillation under this paradigm amplifies a low-motion shortcut inherent to the mode-seeking reverse-KL objective. To counteract this, we introduce a forward-KL regulariser in bidirectional-attention mode, which preserves motion diversity for causal inference without interfering with the distillation loss. On VBench (20s generation), HiAR achieves the best overall score and the lowest temporal drift among all compared methods.

