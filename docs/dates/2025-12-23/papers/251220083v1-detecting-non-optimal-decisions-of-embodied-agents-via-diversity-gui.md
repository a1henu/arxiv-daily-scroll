---
layout: default
title: Detecting Non-Optimal Decisions of Embodied Agents via Diversity-Guided Metamorphic Testing
---

# Detecting Non-Optimal Decisions of Embodied Agents via Diversity-Guided Metamorphic Testing
**arXiv**：[2512.20083v1](https://arxiv.org/abs/2512.20083) · [PDF](https://arxiv.org/pdf/2512.20083.pdf)  
**作者**：Wenzhao Wu, Yahui Tang, Mingfei Cheng, Wenbing Tang, Yuan Zhou, Yang Liu  

**一句话要点**：提出NoD-DGMT框架，通过多样性引导的蜕变测试检测具身代理的非最优决策

**关键词**：具身代理, 非最优决策检测, 蜕变测试, 多样性引导, 任务规划, AI2-THOR模拟器

## 3 点简述
- 核心问题：具身代理在任务规划中可能产生非最优决策，导致资源浪费和性能下降
- 方法要点：设计四种蜕变关系捕获最优性属性，并采用多样性引导策略高效选择测试用例
- 实验或效果：在AI2-THOR模拟器上测试，平均违规检测率达31.9%，优于六个基线方法

## 摘要（原文）

> As embodied agents advance toward real-world deployment, ensuring optimal decisions becomes critical for resource-constrained applications. Current evaluation methods focus primarily on functional correctness, overlooking the non-functional optimality of generated plans. This gap can lead to significant performance degradation and resource waste. We identify and formalize the problem of Non-optimal Decisions (NoDs), where agents complete tasks successfully but inefficiently. We present NoD-DGMT, a systematic framework for detecting NoDs in embodied agent task planning via diversity-guided metamorphic testing. Our key insight is that optimal planners should exhibit invariant behavioral properties under specific transformations. We design four novel metamorphic relations capturing fundamental optimality properties: position detour suboptimality, action optimality completeness, condition refinement monotonicity, and scene perturbation invariance. To maximize detection efficiency, we introduce a diversity-guided selection strategy that actively selects test cases exploring different violation categories, avoiding redundant evaluations while ensuring comprehensive diversity coverage. Extensive experiments on the AI2-THOR simulator with four state-of-the-art planning models demonstrate that NoD-DGMT achieves violation detection rates of 31.9% on average, with our diversity-guided filter improving rates by 4.3% and diversity scores by 3.3 on average. NoD-DGMT significantly outperforms six baseline methods, with 16.8% relative improvement over the best baseline, and demonstrates consistent superiority across different model architectures and task complexities.

