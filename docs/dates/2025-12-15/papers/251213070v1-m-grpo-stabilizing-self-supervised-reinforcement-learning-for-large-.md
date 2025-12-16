---
layout: default
title: M-GRPO: Stabilizing Self-Supervised Reinforcement Learning for Large Language Models with Momentum-Anchored Policy Optimization
---

# M-GRPO: Stabilizing Self-Supervised Reinforcement Learning for Large Language Models with Momentum-Anchored Policy Optimization
**arXiv**：[2512.13070v1](https://arxiv.org/abs/2512.13070) · [PDF](https://arxiv.org/pdf/2512.13070.pdf)  
**作者**：Bizhe Bai, Hongming Wu, Peng Ye, Tao Chen  

**一句话要点**：提出M-GRPO与IQR过滤以稳定大语言模型的自监督强化学习训练

**关键词**：自监督强化学习, 大语言模型, 策略优化, 训练稳定性, 推理能力

## 3 点简述
- 现有自监督强化学习方法在长时训练中易发生策略崩溃，性能急剧下降
- M-GRPO利用动量模型提供稳定训练目标，IQR过滤动态剪枝低熵轨迹以保持策略多样性
- 实验表明该方法提升训练稳定性并在多个推理基准上达到先进性能

## 摘要（原文）

> Self-supervised reinforcement learning (RL) presents a promising approach for enhancing the reasoning capabilities of Large Language Models (LLMs) without reliance on expensive human-annotated data. However, we find that existing methods suffer from a critical failure mode under long-horizon training: a "policy collapse" where performance precipitously degrades. We diagnose this instability and demonstrate that simply scaling the number of rollouts -- a common strategy to improve performance -- only delays, but does not prevent, this collapse. To counteract this instability, we first introduce M-GRPO (Momentum-Anchored Group Relative Policy Optimization), a framework that leverages a slowly evolving momentum model to provide a stable training target. In addition, we identify that this process is often accompanied by a rapid collapse in policy entropy, resulting in a prematurely confident and suboptimal policy. To specifically address this issue, we propose a second contribution: an adaptive filtering method based on the interquartile range (IQR) that dynamically prunes low-entropy trajectories, preserving essential policy diversity. Our extensive experiments on multiple reasoning benchmarks demonstrate that M-GRPO stabilizes the training process while the IQR filter prevents premature convergence. The combination of these two innovations leads to superior training stability and state-of-the-art performance.

