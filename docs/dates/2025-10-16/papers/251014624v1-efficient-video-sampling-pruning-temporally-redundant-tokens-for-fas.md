---
layout: default
title: Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference
---

# Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference
**arXiv**：[2510.14624v1](https://arxiv.org/abs/2510.14624) · [PDF](https://arxiv.org/pdf/2510.14624.pdf)  
**作者**：Natan Bagrov, Eugene Khvedchenia, Borys Tymchenko, Shay Aharon, Lior Kadoch, Tomer Keren, Ofri Masad, Yonatan Geifman, Ran Zilberstein, Tuomas Rintamaki, Matthieu Le, Andrew Tao  

**一句话要点**：提出高效视频采样方法以解决视频语言模型推理中的冗余令牌问题

**关键词**：视频语言模型, 令牌剪枝, 推理加速, 长视频处理, 高效采样

## 3 点简述
- 核心问题：视频语言模型处理长视频时令牌数量超出预算，导致上下文限制和延迟问题。
- 方法要点：通过识别并剪枝时间上静态的补丁来减少令牌冗余，无需架构修改或重训练。
- 实验或效果：应用后LLM首令牌时间减少高达4倍，准确率损失最小，提升效率-准确性权衡。

## 摘要（原文）

> Vision-language models (VLMs) have recently expanded from static image
> understanding to video reasoning, but their scalability is fundamentally
> limited by the quadratic cost of processing dense frame sequences. Long videos
> often exceed the token budget of modern language models, leading to severe
> context limitations and latency issues. We introduce Efficient Video Sampling
> (EVS), a simple, plug-and-play method for reducing token redundancy in videos
> by identifying and pruning temporally static patches -- spatial regions that
> remain unchanged across consecutive frames. EVS preserves positional identity,
> requires no architectural changes or retraining. We show that EVS substantially
> reduces token count while maintaining semantic fidelity, enabling faster
> inference and longer input sequences. Applied at inference time, EVS reduces
> large language model (LLM) time-to-first-token (TTFT) by up to 4x with minimal
> accuracy loss. When combined with an uptraining phase using stochastic pruning
> rates, EVS yields models that are robust to varying compression levels and
> retain full performance under aggressive pruning. Extensive experiments
> demonstrate that EVS consistently improves efficiency-accuracy trade-offs,
> unlocking scalable video-language understanding without sacrificing quality.

