---
layout: default
title: \textsc{NaVIDA}: Vision-Language Navigation with Inverse Dynamics Augmentation
---

# \textsc{NaVIDA}: Vision-Language Navigation with Inverse Dynamics Augmentation
**arXiv**：[2601.18188v1](https://arxiv.org/abs/2601.18188) · [PDF](https://arxiv.org/pdf/2601.18188.pdf)  
**作者**：Weiye Zhu, Zekai Zhang, Xiangchen Wang, Hewei Pan, Teng Wang, Tiantian Geng, Rongtao Xu, Feng Zheng  

**一句话要点**：提出NaVIDA框架，通过逆动力学增强解决视觉语言导航中视觉-动作因果建模不足的问题。

**关键词**：视觉语言导航, 逆动力学增强, 分层动作分块, 因果建模, 机器人导航

## 3 点简述
- 核心问题：现有方法缺乏视觉变化与动作的因果建模，导致行为不稳定和泛化能力弱。
- 方法要点：引入基于块的逆动力学监督和分层概率动作分块，学习视觉-动作因果关系并扩展规划范围。
- 实验或效果：在导航性能上优于现有方法，参数更少（3B vs. 8B），并在真实机器人评估中验证有效性。

## 摘要（原文）

> Vision-and-Language Navigation (VLN) requires agents to interpret natural language instructions and act coherently in visually rich environments. However, most existing methods rely on reactive state-action mappings without explicitly modeling how actions causally transform subsequent visual observations. Lacking such vision-action causality, agents cannot anticipate the visual changes induced by its own actions, leading to unstable behaviors, weak generalization, and cumulative error along trajectory. To address these issues, we introduce \textsc{NaVIDA} (\textbf{Nav}igation with \textbf{I}nverse \textbf{D}ynamics \textbf{A}ugmentation), a unified VLN framework that couples policy learning with action-grounded visual dynamics and adaptive execution. \textsc{NaVIDA} augments training with chunk-based inverse-dynamics supervision to learn causal relationship between visual changes and corresponding actions. To structure this supervision and extend the effective planning range, \textsc{NaVIDA} employs hierarchical probabilistic action chunking (HPAC), which organizes trajectories into multi-step chunks and provides discriminative, longer-range visual-change cues. To further curb error accumulation and stabilize behavior at inference, an entropy-guided mechanism adaptively sets the execution horizon of action chunks. Extensive experiments show that \textsc{NaVIDA} achieves superior navigation performance compared to state-of-the-art methods with fewer parameters (3B vs. 8B). Real-world robot evaluations further validate the practical feasibility and effectiveness of our approach. Code and data will be available upon acceptance.

