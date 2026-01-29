---
layout: default
title: Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching
---

# Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching
**arXiv**：[2601.20332v1](https://arxiv.org/abs/2601.20332) · [PDF](https://arxiv.org/pdf/2601.20332.pdf)  
**作者**：Fengrui Zuo, Zhiwei Ke, Yiming Liu, Wenqi Lou, Chao Wang, Xvehai Zhou  

**一句话要点**：提出Window-Diffusion方法，通过窗口化令牌剪枝与缓存加速扩散语言模型推理

**关键词**：扩散语言模型, 推理加速, 令牌剪枝, 缓存机制, 窗口化计算

## 3 点简述
- 扩散语言模型推理存在全序列注意力冗余计算问题，块状扩散方法需重训练且更新顺序受限
- 基于令牌级分析，提出窗口化方法：在线计算活跃令牌、缓存缓冲令牌、剪枝远场令牌，限制计算窗口
- 在LLaDA和Dream模型上实验，匹配计算预算下实现最高99倍推理加速，生成性能基本保持

## 摘要（原文）

> Diffusion language models (DLMs) generate text through iterative denoising, but inference requires full-sequence attention at every iteration, resulting in substantial redundant computation on masked tokens. Block-wise diffusion can reduce this cost, yet it typically relies on retraining and constrained update orders, limiting its direct applicability to pretrained DLMs. Our token-level analysis reveals pronounced structural locality in DLM inference. Decoding is driven by a small set of prefix-localized active tokens; the influence of distant undecoded context diminishes rapidly, and decoded tokens exhibit stage-wise temporal stability, enabling reuse of intermediate representations except for a brief post-decode transient. Motivated by these observations, we propose \textbf{\placeholder}\footnote{The source code is available at https://github.com/vhicrgit/Window-Diffusion.}, a window-based token pruning and caching method for inference. We maintain a local computation window that slides rightward as denoising progresses, and partition undecoded tokens into: (i) \textit{active tokens} that are computed online, (ii) \textit{buffer tokens} whose KV states are cached and periodically refreshed, and (iii) \textit{far-field tokens} that are pruned outside the window. Computation is restricted to active and buffer tokens within the window, while far-field tokens are omitted at each stage. Experiments on LLaDA and Dream show that, under matched compute budgets, our method achieves up to $99\times$ inference speedup while largely preserving generation performance.

