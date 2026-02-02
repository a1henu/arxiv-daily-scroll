---
layout: default
title: Triage: Hierarchical Visual Budgeting for Efficient Video Reasoning in Vision-Language Models
---

# Triage: Hierarchical Visual Budgeting for Efficient Video Reasoning in Vision-Language Models
**arXiv**：[2601.22959v1](https://arxiv.org/abs/2601.22959) · [PDF](https://arxiv.org/pdf/2601.22959.pdf)  
**作者**：Anmin Wang, Nan Zhang, Wei Tao, Xiaoyang Qu, Guokuan Li, Jiguang Wan, Jianzong Wang  

**一句话要点**：提出Triage框架，通过分层视觉预算解决视频处理中的计算冗余问题。

**关键词**：视频推理, 视觉语言模型, 计算效率, 分层预算, 关键帧选择, 令牌分配

## 3 点简述
- 核心问题：视频处理中数据冗余导致长令牌序列，增加计算负担。
- 方法要点：训练免费框架，分帧级和令牌级预算，优先选择关键帧和核心令牌。
- 实验或效果：提升推理速度，减少内存占用，在多个基准上保持或超越性能。

## 摘要（原文）

> Vision-Language Models (VLMs) face significant computational challenges in video processing due to massive data redundancy, which creates prohibitively long token sequences. To address this, we introduce Triage, a training-free, plug-and-play framework that reframes video reasoning as a resource allocation problem via hierarchical visual budgeting. Its first stage, Frame-Level Budgeting, identifies keyframes by evaluating their visual dynamics and relevance, generating a strategic prior based on their importance scores. Guided by this prior, the second stage, Token-Level Budgeting, allocates tokens in two phases: it first secures high-relevance Core Tokens, followed by diverse Context Tokens selected with an efficient batched Maximal Marginal Relevance (MMR) algorithm. Extensive experiments demonstrate that Triage improves inference speed and reduces memory footprint, while maintaining or surpassing the performance of baselines and other methods on various video reasoning benchmarks.

