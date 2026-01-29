---
layout: default
title: ProFlow: Zero-Shot Physics-Consistent Sampling via Proximal Flow Guidance
---

# ProFlow: Zero-Shot Physics-Consistent Sampling via Proximal Flow Guidance
**arXiv**：[2601.20227v1](https://arxiv.org/abs/2601.20227) · [PDF](https://arxiv.org/pdf/2601.20227.pdf)  
**作者**：Zichao Yu, Ming Li, Wenyi Zhang, Difan Zou, Weiguo Gao  

**一句话要点**：提出ProFlow框架，通过近端流引导实现零样本物理一致采样，解决稀疏观测下物理场推断的约束问题。

**关键词**：物理场推断, 零样本采样, 近端流引导, 偏微分方程约束, 生成模型先验, 稀疏观测

## 3 点简述
- 核心问题：从稀疏观测推断物理场时，需严格满足偏微分方程，现有方法难以在不破坏生成先验下强制硬约束。
- 方法要点：采用两步交替方案，包括终端优化步和插值步，通过近端最小化实现物理与观测一致性。
- 实验或效果：在多种方程上验证，ProFlow在物理一致性、观测保真度和分布统计准确性上优于现有基线。

## 摘要（原文）

> Inferring physical fields from sparse observations while strictly satisfying partial differential equations (PDEs) is a fundamental challenge in computational physics. Recently, deep generative models offer powerful data-driven priors for such inverse problems, yet existing methods struggle to enforce hard physical constraints without costly retraining or disrupting the learned generative prior. Consequently, there is a critical need for a sampling mechanism that can reconcile strict physical consistency and observational fidelity with the statistical structure of the pre-trained prior. To this end, we present ProFlow, a proximal guidance framework for zero-shot physics-consistent sampling, defined as inferring solutions from sparse observations using a fixed generative prior without task-specific retraining. The algorithm employs a rigorous two-step scheme that alternates between: (\romannumeral1) a terminal optimization step, which projects the flow prediction onto the intersection of the physically and observationally consistent sets via proximal minimization; and (\romannumeral2) an interpolation step, which maps the refined state back to the generative trajectory to maintain consistency with the learned flow probability path. This procedure admits a Bayesian interpretation as a sequence of local maximum a posteriori (MAP) updates. Comprehensive benchmarks on Poisson, Helmholtz, Darcy, and viscous Burgers' equations demonstrate that ProFlow achieves superior physical and observational consistency, as well as more accurate distributional statistics, compared to state-of-the-art diffusion- and flow-based baselines.

