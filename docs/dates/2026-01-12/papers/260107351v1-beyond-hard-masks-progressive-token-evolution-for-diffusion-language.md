---
layout: default
title: Beyond Hard Masks: Progressive Token Evolution for Diffusion Language Models
---

# Beyond Hard Masks: Progressive Token Evolution for Diffusion Language Models
**arXiv**：[2601.07351v1](https://arxiv.org/abs/2601.07351) · [PDF](https://arxiv.org/pdf/2601.07351.pdf)  
**作者**：Linhao Zhong, Linyu Wu, Bozhen Fang, Tianjian Feng, Chenchen Jing, Wen Wang, Jiaheng Zhang, Hao Chen, Chunhua Shen  

**一句话要点**：提出EvoToken-DLM，通过软令牌演化替代硬掩码，以改进扩散语言模型的解码可修订性。

**关键词**：扩散语言模型, 软令牌演化, 连续轨迹监督, 解码可修订性, 并行解码

## 3 点简述
- 核心问题：扩散语言模型依赖硬二进制掩码和离散令牌分配，限制早期决策修订和中间概率表示利用。
- 方法要点：引入演化软令牌分布，支持从掩码状态到离散输出的渐进过渡，并采用连续轨迹监督对齐训练目标。
- 实验或效果：在多个基准测试中，EvoToken-DLM表现优于现有扩散和掩码语言模型基线。

## 摘要（原文）

> Diffusion Language Models (DLMs) offer a promising alternative for language modeling by enabling parallel decoding through iterative refinement. However, most DLMs rely on hard binary masking and discrete token assignments, which hinder the revision of early decisions and underutilize intermediate probabilistic representations. In this paper, we propose EvoToken-DLM, a novel diffusion-based language modeling approach that replaces hard binary masks with evolving soft token distributions. EvoToken-DLM enables a progressive transition from masked states to discrete outputs, supporting revisable decoding. To effectively support this evolution, we introduce continuous trajectory supervision, which aligns training objectives with iterative probabilistic updates. Extensive experiments across multiple benchmarks show that EvoToken-DLM consistently achieves superior performance, outperforming strong diffusion-based and masked DLM baselines. Project webpage: https://aim-uofa.github.io/EvoTokenDLM.

