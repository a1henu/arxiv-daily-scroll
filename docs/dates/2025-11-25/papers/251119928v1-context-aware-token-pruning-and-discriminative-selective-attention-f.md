---
layout: default
title: Context-Aware Token Pruning and Discriminative Selective Attention for Transformer Tracking
---

# Context-Aware Token Pruning and Discriminative Selective Attention for Transformer Tracking
**arXiv**：[2511.19928v1](https://arxiv.org/abs/2511.19928) · [PDF](https://arxiv.org/pdf/2511.19928.pdf)  
**作者**：Janani Kugarajeevan, Thanikasalam Kokul, Amirthalingam Ramanan, Subha Fernando  

**一句话要点**：提出CPDATrack以解决Transformer跟踪中背景和干扰物干扰问题

**关键词**：Transformer跟踪, 令牌剪枝, 选择性注意力, 背景抑制, 干扰物处理

## 3 点简述
- 核心问题：背景和干扰物令牌削弱跟踪器判别能力，现有剪枝方法易丢失目标上下文信息
- 方法要点：集成可学习模块剪枝背景令牌，并采用判别性选择性注意力机制
- 实验或效果：在GOT-10k等基准上达到SOTA，平均重叠率达75.1%

## 摘要（原文）

> One-stream Transformer-based trackers have demonstrated remarkable performance by concatenating template and search region tokens, thereby enabling joint attention across all tokens. However, enabling an excessive proportion of background search tokens to attend to the target template tokens weakens the tracker's discriminative capability. Several token pruning methods have been proposed to mitigate background interference; however, they often remove tokens near the target, leading to the loss of essential contextual information and degraded tracking performance. Moreover, the presence of distractors within the search tokens further reduces the tracker's ability to accurately identify the target. To address these limitations, we propose CPDATrack, a novel tracking framework designed to suppress interference from background and distractor tokens while enhancing computational efficiency. First, a learnable module is integrated between two designated encoder layers to estimate the probability of each search token being associated with the target. Based on these estimates, less-informative background tokens are pruned from the search region while preserving the contextual cues surrounding the target. To further suppress background interference, a discriminative selective attention mechanism is employed that fully blocks search-to-template attention in the early layers. In the subsequent encoder layers, high-probability target tokens are selectively extracted from a localized region to attend to the template tokens, thereby reducing the influence of background and distractor tokens. The proposed CPDATrack achieves state-of-the-art performance across multiple benchmarks, particularly on GOT-10k, where it attains an average overlap of 75.1 percent.

