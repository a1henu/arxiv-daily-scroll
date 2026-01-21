---
layout: default
title: Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow
---

# Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow
**arXiv**：[2601.14243v1](https://arxiv.org/abs/2601.14243) · [PDF](https://arxiv.org/pdf/2601.14243.pdf)  
**作者**：Haocheng Xi, Charlie Ruan, Peiyuan Liao, Yujun Lin, Han Cai, Yilong Zhao, Shuo Yang, Kurt Keutzer, Song Han, Ligeng Zhu  

**一句话要点**：提出Jet-RL框架，通过统一训练与滚动的FP8精度流，解决强化学习中量化训练的不稳定性问题。

**关键词**：强化学习, FP8量化, 训练稳定性, 精度流统一, 计算效率

## 3 点简述
- 现有强化学习训练中，BF16训练加FP8滚动的策略因数值不匹配导致训练不稳定和精度崩溃。
- Jet-RL采用统一的FP8精度流，最小化数值差异，无需低效的步间校准。
- 实验显示，Jet-RL在滚动和训练阶段分别提速33%和41%，整体提速16%，且保持稳定收敛。

## 摘要（原文）

> Reinforcement learning (RL) is essential for enhancing the complex reasoning capabilities of large language models (LLMs). However, existing RL training pipelines are computationally inefficient and resource-intensive, with the rollout phase accounting for over 70% of total training time. Quantized RL training, particularly using FP8 precision, offers a promising approach to mitigating this bottleneck. A commonly adopted strategy applies FP8 precision during rollout while retaining BF16 precision for training. In this work, we present the first comprehensive study of FP8 RL training and demonstrate that the widely used BF16-training + FP8-rollout strategy suffers from severe training instability and catastrophic accuracy collapse under long-horizon rollouts and challenging tasks. Our analysis shows that these failures stem from the off-policy nature of the approach, which introduces substantial numerical mismatch between training and inference. Motivated by these observations, we propose Jet-RL, an FP8 RL training framework that enables robust and stable RL optimization. The key idea is to adopt a unified FP8 precision flow for both training and rollout, thereby minimizing numerical discrepancies and eliminating the need for inefficient inter-step calibration. Extensive experiments validate the effectiveness of Jet-RL: our method achieves up to 33% speedup in the rollout phase, up to 41% speedup in the training phase, and a 16% end-to-end speedup over BF16 training, while maintaining stable convergence across all settings and incurring negligible accuracy degradation.

