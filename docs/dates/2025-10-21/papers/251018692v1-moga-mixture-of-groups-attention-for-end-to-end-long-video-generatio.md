---
layout: default
title: MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation
---

# MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation
**arXiv**：[2510.18692v1](https://arxiv.org/abs/2510.18692) · [PDF](https://arxiv.org/pdf/2510.18692.pdf)  
**作者**：Weinan Jia, Yuning Lu, Mengqi Huang, Hualiang Wang, Binyuan Huang, Nan Chen, Mu Liu, Jidong Jiang, Zhendong Mao  

**一句话要点**：提出MoGA稀疏注意力机制以解决长视频生成中注意力计算效率低的问题

**关键词**：长视频生成, 稀疏注意力, 扩散变换器, 令牌路由, 端到端训练

## 3 点简述
- 核心问题：扩散变换器在长视频生成中，全注意力计算随序列长度呈二次方增长，效率低下。
- 方法要点：使用轻量级可学习令牌路由器实现语义感知路由，避免块状估计，提升长程交互。
- 实验或效果：模型能端到端生成长达分钟级、多镜头、480p视频，验证了方法的有效性。

## 摘要（原文）

> Long video generation with Diffusion Transformers (DiTs) is bottlenecked by
> the quadratic scaling of full attention with sequence length. Since attention
> is highly redundant, outputs are dominated by a small subset of query-key
> pairs. Existing sparse methods rely on blockwise coarse estimation, whose
> accuracy-efficiency trade-offs are constrained by block size. This paper
> introduces Mixture-of-Groups Attention (MoGA), an efficient sparse attention
> that uses a lightweight, learnable token router to precisely match tokens
> without blockwise estimation. Through semantic-aware routing, MoGA enables
> effective long-range interactions. As a kernel-free method, MoGA integrates
> seamlessly with modern attention stacks, including FlashAttention and sequence
> parallelism. Building on MoGA, we develop an efficient long video generation
> model that end-to-end produces minute-level, multi-shot, 480p videos at 24 fps,
> with a context length of approximately 580k. Comprehensive experiments on
> various video generation tasks validate the effectiveness of our approach.

