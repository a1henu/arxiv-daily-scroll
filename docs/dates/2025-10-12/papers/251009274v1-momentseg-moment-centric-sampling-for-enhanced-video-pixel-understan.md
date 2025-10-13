---
layout: default
title: MomentSeg: Moment-Centric Sampling for Enhanced Video Pixel Understanding
---

# MomentSeg: Moment-Centric Sampling for Enhanced Video Pixel Understanding
**arXiv**：[2510.09274v1](https://arxiv.org/abs/2510.09274) · [PDF](https://arxiv.org/pdf/2510.09274.pdf)  
**作者**：Ming Dai, Sen Yang, Boqiang Duan, Wankou Yang, Jingdong Wang  

**一句话要点**：提出MomentSeg框架，通过关键时刻采样优化视频像素理解，解决RefVOS中的时序推理问题。

**关键词**：视频对象分割, 时序句子定位, 关键时刻采样, 双向锚点传播, 语言引导分割

## 3 点简述
- 核心问题：现有RefVOS采样策略忽略时序线索或增加系统复杂性。
- 方法要点：联合优化TSG和RefVOS，使用FIND令牌识别关键时刻。
- 实验或效果：未知，但代码和模型将开源。

## 摘要（原文）

> Referring Video Object Segmentation (RefVOS) seeks to segment target objects
> in videos guided by natural language descriptions, demanding both temporal
> reasoning and fine-grained visual comprehension. Existing sampling strategies
> for LLM-based approaches typically rely on either handcrafted heuristics or
> external keyframe models. The former often overlooks essential temporal cues,
> while the latter increases system complexity. To address this, we propose a
> unified framework that jointly optimizes Temporal Sentence Grounding (TSG) and
> RefVOS, naturally incorporating key moment grounding capability. During
> training, we introduce a novel TSG paradigm that employs a dedicated
> \texttt{[FIND]} token for key moment identification through temporal token
> similarity matching, thereby avoiding the need for external timestamp
> encodings. For inference, we design a Moment-Centric Sampling (MCS) strategy
> that densely samples informative moments while sparsely sampling non-essential
> frames, preserving both motion details and global context. To further enhance
> tracking stability, we develop Bidirectional Anchor-updated Propagation (BAP),
> which leverages the most relevant moment as start point for high-quality mask
> initialization and dynamically updates at sampled points to mitigate
> accumulated errors. Code and model will be available at:
> https://github.com/Dmmm1997/MomentSeg

