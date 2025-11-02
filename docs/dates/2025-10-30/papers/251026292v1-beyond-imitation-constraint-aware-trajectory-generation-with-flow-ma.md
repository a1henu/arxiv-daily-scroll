---
layout: default
title: Beyond Imitation: Constraint-Aware Trajectory Generation with Flow Matching For End-to-End Autonomous Driving
---

# Beyond Imitation: Constraint-Aware Trajectory Generation with Flow Matching For End-to-End Autonomous Driving
**arXiv**：[2510.26292v1](https://arxiv.org/abs/2510.26292) · [PDF](https://arxiv.org/pdf/2510.26292.pdf)  
**作者**：Lin Liu, Guanyi Yu, Ziying Song, Junqiao Li, Caiyan Jia, Feiyang Jia, Peiliang Wu, Yandan Luo  

**一句话要点**：提出约束感知轨迹生成框架CATG，以解决端到端自动驾驶中的模式崩溃和约束整合问题。

**关键词**：自动驾驶规划, 轨迹生成, 流匹配, 约束整合, 模式崩溃缓解

## 3 点简述
- 核心问题：模仿学习方法易发生模式崩溃，生成式方法难以直接整合安全与物理约束。
- 方法要点：利用约束流匹配，在生成过程中直接施加约束，并参数化驾驶攻击性。
- 实验或效果：在NavSim v2挑战中获第二名，EPDMS得分51.31，获创新奖。

## 摘要（原文）

> Planning is a critical component of end-to-end autonomous driving. However,
> prevailing imitation learning methods often suffer from mode collapse, failing
> to produce diverse trajectory hypotheses. Meanwhile, existing generative
> approaches struggle to incorporate crucial safety and physical constraints
> directly into the generative process, necessitating an additional optimization
> stage to refine their outputs. To address these limitations, we propose CATG, a
> novel planning framework that leverages Constrained Flow Matching. Concretely,
> CATG explicitly models the flow matching process, which inherently mitigates
> mode collapse and allows for flexible guidance from various conditioning
> signals. Our primary contribution is the novel imposition of explicit
> constraints directly within the flow matching process, ensuring that the
> generated trajectories adhere to vital safety and kinematic rules. Secondly,
> CATG parameterizes driving aggressiveness as a control signal during
> generation, enabling precise manipulation of trajectory style. Notably, on the
> NavSim v2 challenge, CATG achieved 2nd place with an EPDMS score of 51.31 and
> was honored with the Innovation Award.

