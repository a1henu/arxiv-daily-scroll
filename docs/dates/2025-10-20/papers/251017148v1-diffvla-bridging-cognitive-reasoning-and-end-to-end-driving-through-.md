---
layout: default
title: DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment
---

# DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment
**arXiv**：[2510.17148v1](https://arxiv.org/abs/2510.17148) · [PDF](https://arxiv.org/pdf/2510.17148.pdf)  
**作者**：Yu Gao, Yiru Wang, Anqing Jiang, Heng Yuwen, Wang Shuo, Sun Hao, Wang Jijun  

**一句话要点**：提出DiffVLA++框架，通过度量引导对齐桥接认知推理与端到端驾驶

**关键词**：自动驾驶, 视觉语言动作模型, 端到端规划, 度量引导对齐, 轨迹生成

## 3 点简述
- 核心问题：端到端驾驶模型泛化能力差，VLA模型物理可行性不足
- 方法要点：结合VLA模块生成语义轨迹与E2E模块确保物理可行性
- 实验效果：在ICCV 2025挑战中EPDMS达49.12，提升驾驶性能

## 摘要（原文）

> Conventional end-to-end (E2E) driving models are effective at generating
> physically plausible trajectories, but often fail to generalize to long-tail
> scenarios due to the lack of essential world knowledge to understand and reason
> about surrounding environments. In contrast, Vision-Language-Action (VLA)
> models leverage world knowledge to handle challenging cases, but their limited
> 3D reasoning capability can lead to physically infeasible actions. In this work
> we introduce DiffVLA++, an enhanced autonomous driving framework that
> explicitly bridges cognitive reasoning and E2E planning through metric-guided
> alignment. First, we build a VLA module directly generating semantically
> grounded driving trajectories. Second, we design an E2E module with a dense
> trajectory vocabulary that ensures physical feasibility. Third, and most
> critically, we introduce a metric-guided trajectory scorer that guides and
> aligns the outputs of the VLA and E2E modules, thereby integrating their
> complementary strengths. The experiment on the ICCV 2025 Autonomous Grand
> Challenge leaderboard shows that DiffVLA++ achieves EPDMS of 49.12.

