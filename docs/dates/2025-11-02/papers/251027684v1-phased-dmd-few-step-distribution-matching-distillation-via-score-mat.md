---
layout: default
title: Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals
---

# Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals
**arXiv**：[2510.27684v1](https://arxiv.org/abs/2510.27684) · [PDF](https://arxiv.org/pdf/2510.27684.pdf)  
**作者**：Xiangyu Fan, Zesong Qiu, Zhuguanyu Wu, Fanzhou Wang, Zhiqian Lin, Tianxiang Ren, Dahua Lin, Ruihao Gong, Lei Yang  

**一句话要点**：提出Phased DMD多步蒸馏框架，通过子区间分数匹配解决复杂生成任务中的模型容量限制问题。

**关键词**：分布匹配蒸馏, 多步蒸馏, 分数匹配, 模型容量, 生成多样性, SNR子区间

## 3 点简述
- 核心问题：一步蒸馏模型在复杂生成任务中性能不足，多步蒸馏存在内存和计算效率问题。
- 方法要点：将SNR范围划分为子区间，结合MoE进行渐进分布匹配和分数匹配。
- 实验效果：在图像和视频生成模型蒸馏中，优于DMD，保持输出多样性和关键生成能力。

## 摘要（原文）

> Distribution Matching Distillation (DMD) distills score-based generative
> models into efficient one-step generators, without requiring a one-to-one
> correspondence with the sampling trajectories of their teachers. However,
> limited model capacity causes one-step distilled models underperform on complex
> generative tasks, e.g., synthesizing intricate object motions in text-to-video
> generation. Directly extending DMD to multi-step distillation increases memory
> usage and computational depth, leading to instability and reduced efficiency.
> While prior works propose stochastic gradient truncation as a potential
> solution, we observe that it substantially reduces the generation diversity of
> multi-step distilled models, bringing it down to the level of their one-step
> counterparts. To address these limitations, we propose Phased DMD, a multi-step
> distillation framework that bridges the idea of phase-wise distillation with
> Mixture-of-Experts (MoE), reducing learning difficulty while enhancing model
> capacity. Phased DMD is built upon two key ideas: progressive distribution
> matching and score matching within subintervals. First, our model divides the
> SNR range into subintervals, progressively refining the model to higher SNR
> levels, to better capture complex distributions. Next, to ensure the training
> objective within each subinterval is accurate, we have conducted rigorous
> mathematical derivations. We validate Phased DMD by distilling state-of-the-art
> image and video generation models, including Qwen-Image (20B parameters) and
> Wan2.2 (28B parameters). Experimental results demonstrate that Phased DMD
> preserves output diversity better than DMD while retaining key generative
> capabilities. We will release our code and models.

