---
layout: default
title: HyPerNav: Hybrid Perception for Object-Oriented Navigation in Unknown Environment
---

# HyPerNav: Hybrid Perception for Object-Oriented Navigation in Unknown Environment
**arXiv**：[2510.22917v1](https://arxiv.org/abs/2510.22917) · [PDF](https://arxiv.org/pdf/2510.22917.pdf)  
**作者**：Zecheng Yin, Hao Zhao, Zhen Li  

**一句话要点**：提出HyPerNav方法，利用视觉语言模型融合局部与全局感知，提升未知环境中目标导向导航性能。

**关键词**：目标导向导航, 视觉语言模型, 混合感知, 未知环境导航, RGB-D传感器, 俯视图融合

## 3 点简述
- 核心问题：未知环境中目标导向导航依赖单一感知源，缺乏局部与全局信息融合。
- 方法要点：结合视觉语言模型，同时处理RGB-D传感器局部观测和实时俯视图全局上下文。
- 实验或效果：在仿真和真实世界测试中，性能优于基线，消融研究验证混合感知有效性。

## 摘要（原文）

> Objective-oriented navigation(ObjNav) enables robot to navigate to target
> object directly and autonomously in an unknown environment. Effective
> perception in navigation in unknown environment is critical for autonomous
> robots. While egocentric observations from RGB-D sensors provide abundant local
> information, real-time top-down maps offer valuable global context for ObjNav.
> Nevertheless, the majority of existing studies focus on a single source, seldom
> integrating these two complementary perceptual modalities, despite the fact
> that humans naturally attend to both. With the rapid advancement of
> Vision-Language Models(VLMs), we propose Hybrid Perception Navigation
> (HyPerNav), leveraging VLMs' strong reasoning and vision-language understanding
> capabilities to jointly perceive both local and global information to enhance
> the effectiveness and intelligence of navigation in unknown environments. In
> both massive simulation evaluation and real-world validation, our methods
> achieved state-of-the-art performance against popular baselines. Benefiting
> from hybrid perception approach, our method captures richer cues and finds the
> objects more effectively, by simultaneously leveraging information
> understanding from egocentric observations and the top-down map. Our ablation
> study further proved that either of the hybrid perception contributes to the
> navigation performance.

