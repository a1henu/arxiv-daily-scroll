---
layout: default
title: Token Reduction via Local and Global Contexts Optimization for Efficient Video Large Language Models
---

# Token Reduction via Local and Global Contexts Optimization for Efficient Video Large Language Models
**arXiv**：[2603.01400v1](https://arxiv.org/abs/2603.01400) · [PDF](https://arxiv.org/pdf/2603.01400.pdf)  
**作者**：Jinlong Li, Liyuan Jiang, Haonan Zhang, Nicu Sebe  

**一句话要点**：提出AOT方法，通过局部全局最优传输优化视频大语言模型的令牌减少，提升效率。

**关键词**：视频大语言模型, 令牌减少, 最优传输, 时空效率, 无训练优化

## 3 点简述
- 核心问题：视频大语言模型因冗余视觉令牌导致效率低下，现有方法在时空减少和信息保留上不足。
- 方法要点：基于注意力引导建立帧内和帧间令牌锚点，利用最优传输聚合信息，实现无训练令牌减少。
- 实验或效果：在多个视频基准测试中取得竞争性性能，显著提升计算效率并保持时空保真度。

## 摘要（原文）

> Video Large Language Models (VLLMs) demonstrate strong video understanding but suffer from inefficiency due to redundant visual tokens. Existing pruning primary targets intra-frame spatial redundancy or prunes inside the LLM with shallow-layer overhead, yielding suboptimal spatiotemporal reduction and underutilizing long-context compressibility. All of them often discard subtle yet informative context from merged or pruned tokens. In this paper, we propose a new perspective that elaborates token \textbf{A}nchors within intra-frame and inter-frame to comprehensively aggregate the informative contexts via local-global \textbf{O}ptimal \textbf{T}ransport (\textbf{AOT}). Specifically, we first establish local- and global-aware token anchors within each frame under the attention guidance, which then optimal transport aggregates the informative contexts from pruned tokens, constructing intra-frame token anchors. Then, building on the temporal frame clips, the first frame within each clip will be considered as the keyframe anchors to ensemble similar information from consecutive frames through optimal transport, while keeping distinct tokens to represent temporal dynamics, leading to efficient token reduction in a training-free manner. Extensive evaluations show that our proposed AOT obtains competitive performances across various short- and long-video benchmarks on leading video LLMs, obtaining substantial computational efficiency while preserving temporal and visual fidelity. Project webpage: \href{https://tyroneli.github.io/AOT}{AOT}.

