---
layout: default
title: APPO: Attention-guided Perception Policy Optimization for Video Reasoning
---

# APPO: Attention-guided Perception Policy Optimization for Video Reasoning
**arXiv**：[2602.23823v1](https://arxiv.org/abs/2602.23823) · [PDF](https://arxiv.org/pdf/2602.23823.pdf)  
**作者**：Henghui Du, Chang Zhou, Xi Chen, Di Hu  

**一句话要点**：提出APPO算法，通过注意力引导优化感知策略以低成本增强视频推理中的细粒度感知能力。

**关键词**：视频推理, 感知优化, 注意力机制, 令牌级奖励, 低成本训练, 细粒度感知

## 3 点简述
- 核心问题：视频推理过度依赖细粒度感知，而非专家级推理，且感知能力提升对性能影响更大。
- 方法要点：APPO利用令牌级密集奖励优化聚焦关键视频帧的感知令牌，无需昂贵细粒度标注。
- 实验或效果：在多种视频基准和模型规模上，APPO性能优于GRPO和DAPO，提升0.5%~4%。

## 摘要（原文）

> Complex video reasoning, actually, relies excessively on fine-grained perception rather than on expert (e.g., Ph.D, Science)-level reasoning. Through extensive empirical observation, we have recognized the critical impact of perception. In particular, when perception ability is almost fixed, enhancing reasoning from Qwen3-8B to OpenAI-o3 yields only 0.7% performance improvement. Conversely, even minimal change in perception model scale (from 7B to 32B) boosts performance by 1.4%, indicating enhancing perception, rather than reasoning, is more critical to improve performance. Therefore, exploring how to enhance perception ability through reasoning without the need for expensive fine-grained annotation information is worthwhile. To achieve this goal, we specially propose APPO, the Attention-guided Perception Policy Optimization algorithm that leverages token-level dense rewards to improve model's fine-grained perception. The core idea behind APPO is to optimize those tokens from different responses that primarily focus on the same crucial video frame (called intra-group perception tokens). Experimental results on diverse video benchmarks and models with different scales (3/7B) demonstrate APPO consistently outperforms GRPO and DAPO (0.5%~4%). We hope our work provides a promising approach to effectively enhance model's perception abilities through reasoning in a low-cost manner, serving diverse scenarios and demands.

