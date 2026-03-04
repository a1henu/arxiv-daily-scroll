---
layout: default
title: Improving Diffusion Planners by Self-Supervised Action Gating with Energies
---

# Improving Diffusion Planners by Self-Supervised Action Gating with Energies
**arXiv**：[2603.02650v1](https://arxiv.org/abs/2603.02650) · [PDF](https://arxiv.org/pdf/2603.02650.pdf)  
**作者**：Yuan Lu, Dongqi Han, Yansen Wang, Dongsheng Li  

**一句话要点**：提出SAGE方法以解决扩散规划器中动态不一致导致的执行脆弱问题

**关键词**：扩散规划器, 离线强化学习, 动态一致性, 推理时重排, 潜空间预测

## 3 点简述
- 扩散规划器在离线强化学习中可能因价值引导选择动态不一致轨迹而失败
- SAGE通过JEPA编码器和潜空间预测误差在推理时重排候选动作，结合可行性评分与价值估计
- 实验表明SAGE无需环境交互或策略重训练，提升了扩散规划器在多个基准上的性能和鲁棒性

## 摘要（原文）

> Diffusion planners are a strong approach for offline reinforcement learning, but they can fail when value-guided selection favours trajectories that score well yet are locally inconsistent with the environment dynamics, resulting in brittle execution. We propose Self-supervised Action Gating with Energies (SAGE), an inference-time re-ranking method that penalises dynamically inconsistent plans using a latent consistency signal. SAGE trains a Joint-Embedding Predictive Architecture (JEPA) encoder on offline state sequences and an action-conditioned latent predictor for short horizon transitions. At test time, SAGE assigns each sampled candidate an energy given by its latent prediction error and combines this feasibility score with value estimates to select actions. SAGE can integrate into existing diffusion planning pipelines that can sample trajectories and select actions via value scoring; it requires no environment rollouts and no policy re-training. Across locomotion, navigation, and manipulation benchmarks, SAGE improves the performance and robustness of diffusion planners.

