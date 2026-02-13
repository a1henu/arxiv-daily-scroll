---
layout: default
title: dVoting: Fast Voting for dLLMs
---

# dVoting: Fast Voting for dLLMs
**arXiv**：[2602.12153v1](https://arxiv.org/abs/2602.12153) · [PDF](https://arxiv.org/pdf/2602.12153.pdf)  
**作者**：Sicheng Feng, Zigeng Chen, Xinyin Ma, Gongfan Fang, Xinchao Wang  

**一句话要点**：提出dVoting以提升扩散大语言模型的推理能力，通过快速投票技术实现无训练性能增强

**关键词**：扩散大语言模型, 投票技术, 并行解码, 推理增强, 无训练优化

## 3 点简述
- 核心问题：扩散大语言模型在并行解码时，少数不确定令牌影响整体性能，需高效优化方法
- 方法要点：利用dLLMs任意位置生成能力，通过采样、一致性分析、投票再生迭代精炼不确定令牌
- 实验或效果：在GSM8K、MATH500、ARC-C、MMLU等基准上性能提升3.16%-14.84%，计算开销可接受

## 摘要（原文）

> Diffusion Large Language Models (dLLMs) represent a new paradigm beyond autoregressive modeling, offering competitive performance while naturally enabling a flexible decoding process. Specifically, dLLMs can generate tokens at arbitrary positions in parallel, endowing them with significant potential for parallel test-time scaling, which was previously constrained by severe inefficiency in autoregressive modeling. In this work, we introduce dVoting, a fast voting technique that boosts reasoning capability without training, with only an acceptable extra computational overhead. dVoting is motivated by the observation that, across multiple samples for the same prompt, token predictions remain largely consistent, whereas performance is determined by a small subset of tokens exhibiting cross-sample variability. Leveraging the arbitrary-position generation capability of dLLMs, dVoting performs iterative refinement by sampling, identifying uncertain tokens via consistency analysis, regenerating them through voting, and repeating this process until convergence. Extensive evaluations demonstrate that dVoting consistently improves performance across various benchmarks. It achieves gains of 6.22%-7.66% on GSM8K, 4.40%-7.20% on MATH500, 3.16%-14.84% on ARC-C, and 4.83%-5.74% on MMLU. Our code is available at https://github.com/fscdc/dVoting

