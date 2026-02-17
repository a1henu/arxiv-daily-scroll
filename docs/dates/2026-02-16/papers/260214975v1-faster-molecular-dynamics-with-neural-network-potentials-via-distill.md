---
layout: default
title: Faster Molecular Dynamics with Neural Network Potentials via Distilled Multiple Time-Stepping and Non-Conservative Forces
---

# Faster Molecular Dynamics with Neural Network Potentials via Distilled Multiple Time-Stepping and Non-Conservative Forces
**arXiv**：[2602.14975v1](https://arxiv.org/abs/2602.14975) · [PDF](https://arxiv.org/pdf/2602.14975.pdf)  
**作者**：Nicolaï Gouraud, Côme Cattin, Thomas Plé, Olivier Adjoua, Louis Lagardère, Jean-Philip Piquemal  

**一句话要点**：提出DMTS-NC方法，通过蒸馏多时间步与非保守力加速分子动力学模拟

**关键词**：分子动力学模拟, 神经网络势能, 蒸馏训练, 多时间步算法, 非保守力

## 3 点简述
- 核心问题：分子动力学模拟中，高精度保守势能计算耗时，影响效率。
- 方法要点：使用蒸馏架构生成非保守力，结合双级RESPA算法，保持物理先验如旋转等变性。
- 实验或效果：相比保守版本更稳定高效，速度提升15-30%，无需微调，适用于任何神经网络势能。

## 摘要（原文）

> Following our previous work (J. Phys. Chem. Lett., 2026, 17, 5, 1288-1295), we propose the DMTS-NC approach, a distilled multi-time-step (DMTS) strategy using non conservative (NC) forces to further accelerate atomistic molecular dynamics simulations using foundation neural network models. There, a dual-level reversible reference system propagator algorithm (RESPA) formalism couples a target accurate conservative potential to a simplified distilled representation optimized for the production of non-conservative forces. Despite being non-conservative, the distilled architecture is designed to enforce key physical priors, such as equivariance under rotation and cancellation of atomic force components. These choices facilitate the distillation process and therefore improve drastically the robustness of simulation, significantly limiting the "holes" in the simpler potential, thus achieving excellent agreement with the forces data. Overall, the DMTS-NC scheme is found to be more stable and efficient than its conservative counterpart with additional speedups reaching 15-30% over DMTS. Requiring no finetuning steps, it is easier to implement and can be pushed to the limit of the systems physical resonances to maintain accuracy while providing maximum efficiency. As for DMTS, DMTS-NC is applicable to any neural network potential.

