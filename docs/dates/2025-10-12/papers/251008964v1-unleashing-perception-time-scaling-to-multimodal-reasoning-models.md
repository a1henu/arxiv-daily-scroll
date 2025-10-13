---
layout: default
title: Unleashing Perception-Time Scaling to Multimodal Reasoning Models
---

# Unleashing Perception-Time Scaling to Multimodal Reasoning Models
**arXiv**：[2510.08964v1](https://arxiv.org/abs/2510.08964) · [PDF](https://arxiv.org/pdf/2510.08964.pdf)  
**作者**：Yifan Li, Zhenghao Chen, Ziheng Wu, Kun Zhou, Ruipu Luo, Can Zhang, Zhentao He, Yufei Zhan, Wayne Xin Zhao, Minghui Qiu  

**一句话要点**：提出感知时间缩放以提升多模态模型的视觉感知精度

**关键词**：感知时间缩放, 多模态推理, 视觉估计, 强化学习, 基准评估, 合成数据

## 3 点简述
- 核心问题：当前大视觉语言模型在视觉感知任务中精度有限，推理时间缩放效果不佳。
- 方法要点：引入感知时间缩放，分解复杂感知问题为可处理子问题，结合强化学习。
- 实验或效果：在DisTANCE基准上高精度性能从8.0%提升至64.7%，泛化能力强。

## 摘要（原文）

> Recent advances in inference-time scaling, particularly those leveraging
> reinforcement learning with verifiable rewards, have substantially enhanced the
> reasoning capabilities of Large Vision-Language Models (LVLMs). Inspired by
> this success, similar strategies have been applied to multimodal reasoning, yet
> their impact on visual perception remains unclear. To investigate this gap, we
> introduce DisTANCE, a perception-centric benchmark for visual estimation tasks.
> Evaluation results show that LVLMs exhibit limited estimation precision, and
> inference-time scaling offers only marginal gains. We attribute this to the
> fast perception paradigm of current LVLMs, where visual understanding is
> treated as a one-shot output without modeling the underlying perceptual
> process. To address this, we propose Perception-Time Scaling (PTS), a novel
> paradigm that encourages token-rich perception and decomposes complex
> perception problems into intermediate tractable sub-problems, thereby enabling
> perception to align with and benefit from inference-time scaling. Combined with
> reinforcement learning techniques, PTS significantly improves perception
> accuracy, raising high-precision performance on DisTANCE from 8.0% to 64.7%,
> and generalizes well to out-of-domain tasks. Surprisingly, even though PTS data
> are purely synthetic, combining them with math reasoning data yields consistent
> gains in both reasoning and real-world perception benchmarks. Further analysis
> reveals that PTS introduces more perception-related tokens and increases the
> model's attention to image tokens. Our code and data will be publicly released.

