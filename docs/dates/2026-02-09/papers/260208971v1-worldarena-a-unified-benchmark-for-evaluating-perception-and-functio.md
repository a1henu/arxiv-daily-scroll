---
layout: default
title: WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models
---

# WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models
**arXiv**：[2602.08971v1](https://arxiv.org/abs/2602.08971) · [PDF](https://arxiv.org/pdf/2602.08971.pdf)  
**作者**：Yu Shang, Zhuohang Li, Yiding Ma, Weikang Su, Xin Jin, Ziyou Wang, Xin Zhang, Yinzhou Tang, Chen Gao, Wei Wu, Xihui Liu, Dhruv Shah, Zhaoxiang Zhang, Zhibo Chen, Jun Zhu, Yonghong Tian, Tat-Seng Chua, Wenwu Zhu, Yong Li  

**一句话要点**：提出WorldArena统一基准以评估具身世界模型的感知与功能效用

**关键词**：具身世界模型, 统一基准, 感知评估, 功能效用, EWMScore, 公开排行榜

## 3 点简述
- 当前评估具身世界模型时，主要关注感知保真度，忽视其在决策任务中的功能效用。
- WorldArena通过视频感知质量和具身任务功能两个维度，结合16个指标和主观人类评估进行系统评估。
- 实验揭示感知与功能间存在显著差距，高视觉质量不一定对应强任务能力，并发布公开排行榜。

## 摘要（原文）

> While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental dynamics through action-conditioned prediction, their evaluation remains fragmented. Current evaluation of embodied world models has largely focused on perceptual fidelity (e.g., video generation quality), overlooking the functional utility of these models in downstream decision-making tasks. In this work, we introduce WorldArena, a unified benchmark designed to systematically evaluate embodied world models across both perceptual and functional dimensions. WorldArena assesses models through three dimensions: video perception quality, measured with 16 metrics across six sub-dimensions; embodied task functionality, which evaluates world models as data engines, policy evaluators, and action planners integrating with subjective human evaluation. Furthermore, we propose EWMScore, a holistic metric integrating multi-dimensional performance into a single interpretable index. Through extensive experiments on 14 representative models, we reveal a significant perception-functionality gap, showing that high visual quality does not necessarily translate into strong embodied task capability. WorldArena benchmark with the public leaderboard is released at https://worldarena.ai, providing a framework for tracking progress toward truly functional world models in embodied AI.

