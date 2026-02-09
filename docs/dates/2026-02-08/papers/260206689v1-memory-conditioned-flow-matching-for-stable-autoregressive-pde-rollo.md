---
layout: default
title: Memory-Conditioned Flow-Matching for Stable Autoregressive PDE Rollouts
---

# Memory-Conditioned Flow-Matching for Stable Autoregressive PDE Rollouts
**arXiv**：[2602.06689v1](https://arxiv.org/abs/2602.06689) · [PDF](https://arxiv.org/pdf/2602.06689.pdf)  
**作者**：Victor Armegioiu  

**一句话要点**：提出记忆条件流匹配以稳定自回归PDE长时推演，解决粗到细尺度下的漂移问题。

**关键词**：自回归PDE求解, 流匹配生成, 记忆条件模型, 长时推演稳定性, 多尺度模拟, Wasserstein稳定性

## 3 点简述
- 自回归PDE求解器在长时推演中易漂移，源于无记忆闭包的结构限制。
- 引入记忆条件扩散/流匹配，通过在线状态注入降噪过程，减少传输需求。
- 实验显示在可压缩流和多尺度混合中，提升精度和稳定性，改善频谱与统计保真度。

## 摘要（原文）

> Autoregressive generative PDE solvers can be accurate one step ahead yet drift over long rollouts, especially in coarse-to-fine regimes where each step must regenerate unresolved fine scales. This is the regime of diffusion and flow-matching generators: although their internal dynamics are Markovian, rollout stability is governed by per-step \emph{conditional law} errors. Using the Mori--Zwanzig projection formalism, we show that eliminating unresolved variables yields an exact resolved evolution with a Markov term, a memory term, and an orthogonal forcing, exposing a structural limitation of memoryless closures. Motivated by this, we introduce memory-conditioned diffusion/flow-matching with a compact online state injected into denoising via latent features. Via disintegration, memory induces a structured conditional tail prior for unresolved scales and reduces the transport needed to populate missing frequencies. We prove Wasserstein stability of the resulting conditional kernel. We then derive discrete Grönwall rollout bounds that separate memory approximation from conditional generation error. Experiments on compressible flows with shocks and multiscale mixing show improved accuracy and markedly more stable long-horizon rollouts, with better fine-scale spectral and statistical fidelity.

