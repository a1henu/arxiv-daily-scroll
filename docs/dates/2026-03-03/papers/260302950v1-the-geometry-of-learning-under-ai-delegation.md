---
layout: default
title: The Geometry of Learning Under AI Delegation
---

# The Geometry of Learning Under AI Delegation
**arXiv**：[2603.02950v1](https://arxiv.org/abs/2603.02950) · [PDF](https://arxiv.org/pdf/2603.02950.pdf)  
**作者**：Lingxiao Huang, Nisheeth K. Vishnoi  

**一句话要点**：提出耦合动力学模型以分析AI委托下人类技能演变的几何稳定性

**关键词**：AI委托, 技能演化, 动力学系统, 稳定性分析, 长期性能

## 3 点简述
- 核心问题：AI从工具转向协作者时，人类技能如何随时间变化
- 方法要点：建模人类技能与AI委托的联合演化，基于优化任务误差的单一指标
- 实验或效果：揭示AI使用可导致稳定低技能均衡，短期性能提升但长期性能损失

## 摘要（原文）

> As AI systems shift from tools to collaborators, a central question is how the skills of humans relying on them change over time. We study this question mathematically by modeling the joint evolution of human skill and AI delegation as a coupled dynamical system. In our model, delegation adapts to relative performance, while skill improves through use and decays under non-use; crucially, both updates arise from optimizing a single performance metric measuring expected task error. Despite this local alignment, adaptive AI use fundamentally alters the global stability structure of human skill acquisition. Beyond the high-skill equilibrium of human-only learning, the system admits a *stable* low-skill equilibrium corresponding to persistent reliance, separated by a sharp basin boundary that makes early decisions effectively irreversible under the induced dynamics. We further show that AI assistance can strictly improve short-run performance while inducing persistent long-run performance loss relative to the no-AI baseline, driven by a negative feedback between delegation and practice. We characterize how AI quality deforms the basin boundary and show that these effects are robust to noise and asymmetric trust updates. Our results identify stability, not incentives or misalignment, as the central mechanism by which AI assistance can undermine long-run human performance and skill.

