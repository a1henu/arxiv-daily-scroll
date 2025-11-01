---
layout: default
title: Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation
---

# Hybrid Consistency Policy: Decoupling Multi-Modal Diversity and Real-Time Efficiency in Robotic Manipulation
**arXiv**：[2510.26670v1](https://arxiv.org/abs/2510.26670) · [PDF](https://arxiv.org/pdf/2510.26670.pdf)  
**作者**：Qianyou Zhao, Yuliang Shen, Xuanran Zhai, Ce Hao, Duidi Wu, Jin Qi, Jie Hu, Qiaojun Yu  

**一句话要点**：提出混合一致性策略以解决机器人操作中多模态多样性与实时效率的权衡问题

**关键词**：机器人操作, 扩散模型, 一致性蒸馏, 多模态学习, 实时策略, 模仿学习

## 3 点简述
- 扩散模仿学习难以同时实现快速采样与强多模态行为
- 结合随机前缀与一致性跳跃，通过时间变化一致性蒸馏优化预测
- 在仿真与真实机器人中，以25步加一跳接近80步DDPM性能，显著降低延迟

## 摘要（原文）

> In visuomotor policy learning, diffusion-based imitation learning has become
> widely adopted for its ability to capture diverse behaviors. However,
> approaches built on ordinary and stochastic denoising processes struggle to
> jointly achieve fast sampling and strong multi-modality. To address these
> challenges, we propose the Hybrid Consistency Policy (HCP). HCP runs a short
> stochastic prefix up to an adaptive switch time, and then applies a one-step
> consistency jump to produce the final action. To align this one-jump
> generation, HCP performs time-varying consistency distillation that combines a
> trajectory-consistency objective to keep neighboring predictions coherent and a
> denoising-matching objective to improve local fidelity. In both simulation and
> on a real robot, HCP with 25 SDE steps plus one jump approaches the 80-step
> DDPM teacher in accuracy and mode coverage while significantly reducing
> latency. These results show that multi-modality does not require slow
> inference, and a switch time decouples mode retention from speed. It yields a
> practical accuracy efficiency trade-off for robot policies.

