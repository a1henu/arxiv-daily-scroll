---
layout: default
title: TimeSearch-R: Adaptive Temporal Search for Long-Form Video Understanding via Self-Verification Reinforcement Learning
---

# TimeSearch-R: Adaptive Temporal Search for Long-Form Video Understanding via Self-Verification Reinforcement Learning
**arXiv**：[2511.05489v1](https://arxiv.org/abs/2511.05489) · [PDF](https://arxiv.org/pdf/2511.05489.pdf)  
**作者**：Junwen Pan, Qizhe Zhang, Rui Zhang, Ming Lu, Xin Wan, Yuan Zhang, Chang Liu, Qi She  

**一句话要点**：提出TimeSearch-R以通过自验证强化学习优化长视频时序搜索

**关键词**：时序搜索, 长视频理解, 强化学习, 自验证, 视频推理, 端到端优化

## 3 点简述
- 核心问题：现有时序搜索方法依赖手工过程，缺乏端到端优化，导致搜索不完整和推理不一致。
- 方法要点：引入GRPO-CSV，通过自验证机制检查搜索帧的充分性，提升视频推理的完整性。
- 实验效果：在多个基准测试中显著提升性能，如LongVideoBench上超越Qwen2.5-VL和Video-R1。

## 摘要（原文）

> Temporal search aims to identify a minimal set of relevant frames from tens
> of thousands based on a given query, serving as a foundation for accurate
> long-form video understanding. Existing works attempt to progressively narrow
> the search space. However, these approaches typically rely on a hand-crafted
> search process, lacking end-to-end optimization for learning optimal search
> strategies. In this paper, we propose TimeSearch-R, which reformulates temporal
> search as interleaved text-video thinking, seamlessly integrating searching
> video clips into the reasoning process through reinforcement learning (RL).
> However, applying RL training methods, such as Group Relative Policy
> Optimization (GRPO), to video reasoning can result in unsupervised intermediate
> search decisions. This leads to insufficient exploration of the video content
> and inconsistent logical reasoning. To address these issues, we introduce GRPO
> with Completeness Self-Verification (GRPO-CSV), which gathers searched video
> frames from the interleaved reasoning process and utilizes the same policy
> model to verify the adequacy of searched frames, thereby improving the
> completeness of video reasoning. Additionally, we construct datasets
> specifically designed for the SFT cold-start and RL training of GRPO-CSV,
> filtering out samples with weak temporal dependencies to enhance task
> difficulty and improve temporal search capabilities. Extensive experiments
> demonstrate that TimeSearch-R achieves significant improvements on temporal
> search benchmarks such as Haystack-LVBench and Haystack-Ego4D, as well as
> long-form video understanding benchmarks like VideoMME and MLVU. Notably,
> TimeSearch-R establishes a new state-of-the-art on LongVideoBench with 4.1%
> improvement over the base model Qwen2.5-VL and 2.0% over the advanced video
> reasoning model Video-R1. Our code is available at
> https://github.com/Time-Search/TimeSearch-R.

