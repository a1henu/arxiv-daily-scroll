---
layout: default
title: Double Horizon Model-Based Policy Optimization
---

# Double Horizon Model-Based Policy Optimization
**arXiv**：[2512.15439v1](https://arxiv.org/abs/2512.15439) · [PDF](https://arxiv.org/pdf/2512.15439.pdf)  
**作者**：Akihiro Kubo, Paavo Parmas, Shin Ishii  

**一句话要点**：提出双视野模型策略优化以解决模型强化学习中轨迹长度选择的两难问题

**关键词**：模型强化学习, 轨迹长度选择, 分布偏移, 梯度稳定性, 连续控制, 双视野策略

## 3 点简述
- 模型强化学习中，长轨迹减少分布偏移但增加模型偏差，短轨迹降低梯度方差但可能加剧分布偏移，导致两个最优视野冲突。
- DHMBPO将轨迹生成分为长分布轨迹和短训练轨迹，前者提供在线状态样本缓解分布偏移，后者利用可微转换实现稳定梯度估计。
- 实验表明，该方法在连续控制基准上平衡分布偏移、模型偏差和梯度不稳定性，提升了样本效率和运行时间。

## 摘要（原文）

> Model-based reinforcement learning (MBRL) reduces the cost of real-environment sampling by generating synthetic trajectories (called rollouts) from a learned dynamics model. However, choosing the length of the rollouts poses two dilemmas: (1) Longer rollouts better preserve on-policy training but amplify model bias, indicating the need for an intermediate horizon to mitigate distribution shift (i.e., the gap between on-policy and past off-policy samples). (2) Moreover, a longer model rollout may reduce value estimation bias but raise the variance of policy gradients due to backpropagation through multiple steps, implying another intermediate horizon for stable gradient estimates. However, these two optimal horizons may differ. To resolve this conflict, we propose Double Horizon Model-Based Policy Optimization (DHMBPO), which divides the rollout procedure into a long "distribution rollout" (DR) and a short "training rollout" (TR). The DR generates on-policy state samples for mitigating distribution shift. In contrast, the short TR leverages differentiable transitions to offer accurate value gradient estimation with stable gradient updates, thereby requiring fewer updates and reducing overall runtime. We demonstrate that the double-horizon approach effectively balances distribution shift, model bias, and gradient instability, and surpasses existing MBRL methods on continuous-control benchmarks in terms of both sample efficiency and runtime.

