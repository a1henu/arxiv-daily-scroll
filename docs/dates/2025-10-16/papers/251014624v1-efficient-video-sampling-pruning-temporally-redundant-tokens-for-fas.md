---
layout: default
title: Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference
---

# Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference
**arXiv**：[2510.14624v1](https://arxiv.org/abs/2510.14624) · [PDF](https://arxiv.org/pdf/2510.14624.pdf)  
**作者**：Natan Bagrov, Eugene Khvedchenia, Borys Tymchenko, Shay Aharon, Lior Kadoch, Tomer Keren, Ofri Masad, Yonatan Geifman, Ran Zilberstein, Tuomas Rintamaki, Matthieu Le, Andrew Tao  

**一句话要点**：提出高效视频采样方法，通过剪枝时间冗余令牌加速视觉语言模型推理

**关键词**：视频语言模型, 令牌剪枝, 推理加速, 时间冗余, 高效采样

## 3 点简述
- 核心问题：视频处理中密集帧序列导致二次计算成本，限制模型可扩展性和延迟
- 方法要点：识别并剪枝时间静态补丁，无需架构修改或重训练，保持位置身份
- 实验或效果：推理时应用可减少令牌数，TTFT降低达4倍，精度损失最小

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

