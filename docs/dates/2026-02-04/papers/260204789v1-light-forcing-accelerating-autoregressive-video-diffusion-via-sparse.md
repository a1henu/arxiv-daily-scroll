---
layout: default
title: Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention
---

# Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention
**arXiv**：[2602.04789v1](https://arxiv.org/abs/2602.04789) · [PDF](https://arxiv.org/pdf/2602.04789.pdf)  
**作者**：Chengtao Lv, Yumeng Shi, Yushi Huang, Ruihao Gong, Shen Ren, Wenya Wang  

**一句话要点**：提出Light Forcing稀疏注意力方法，以加速自回归视频扩散模型生成。

**关键词**：自回归视频生成, 稀疏注意力, 加速推理, 视频扩散模型, 高效部署

## 3 点简述
- 核心问题：现有稀疏注意力应用于自回归视频模型时，因孤立处理分块和未充分利用历史上下文，导致性能下降。
- 方法要点：引入分块感知增长机制，定量评估分块贡献以分配稀疏度；采用分层稀疏注意力，以粗到细方式捕获历史和局部上下文。
- 实验或效果：在VBench上达到84.5分，实现1.2~1.3倍端到端加速，结合量化后加速2.3倍，在RTX 5090 GPU上达19.7 FPS。

## 摘要（原文）

> Advanced autoregressive (AR) video generation models have improved visual fidelity and interactivity, but the quadratic complexity of attention remains a primary bottleneck for efficient deployment. While existing sparse attention solutions have shown promise on bidirectional models, we identify that applying these solutions to AR models leads to considerable performance degradation for two reasons: isolated consideration of chunk generation and insufficient utilization of past informative context. Motivated by these observations, we propose \textsc{Light Forcing}, the \textit{first} sparse attention solution tailored for AR video generation models. It incorporates a \textit{Chunk-Aware Growth} mechanism to quantitatively estimate the contribution of each chunk, which determines their sparsity allocation. This progressive sparsity increase strategy enables the current chunk to inherit prior knowledge in earlier chunks during generation. Additionally, we introduce a \textit{Hierarchical Sparse Attention} to capture informative historical and local context in a coarse-to-fine manner. Such two-level mask selection strategy (\ie, frame and block level) can adaptively handle diverse attention patterns. Extensive experiments demonstrate that our method outperforms existing sparse attention in quality (\eg, 84.5 on VBench) and efficiency (\eg, $1.2{\sim}1.3\times$ end-to-end speedup). Combined with FP8 quantization and LightVAE, \textsc{Light Forcing} further achieves a $2.3\times$ speedup and 19.7\,FPS on an RTX~5090 GPU. Code will be released at \href{https://github.com/chengtao-lv/LightForcing}{https://github.com/chengtao-lv/LightForcing}.

