---
layout: default
title: AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models
---

# AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models
**arXiv**：[2602.06825v1](https://arxiv.org/abs/2602.06825) · [PDF](https://arxiv.org/pdf/2602.06825.pdf)  
**作者**：Yuming Li, Qingyu Li, Chengyu Bai, Xiangyang Luo, Zeyue Xue, Wenyu Qin, Meng Wang, Yikai Wang, Shanghang Zhang  

**一句话要点**：提出自适应熵引导策略优化以提升扩散模型对齐效率

**关键词**：扩散模型对齐, 策略优化, 注意力熵, 自适应采样, 强化学习从人类反馈

## 3 点简述
- 核心问题：GRPO等方法采样策略低效，忽视样本学习价值和关键探索时刻的动态变化
- 方法要点：利用注意力熵作为双重信号代理，全局动态分配预算，局部引导关键时间步探索
- 实验或效果：在文本到图像生成任务中加速收敛并实现更优对齐性能

## 摘要（原文）

> Reinforcement learning from human feedback (RLHF) shows promise for aligning diffusion and flow models, yet policy optimization methods such as GRPO suffer from inefficient and static sampling strategies. These methods treat all prompts and denoising steps uniformly, ignoring substantial variations in sample learning value as well as the dynamic nature of critical exploration moments.
>   To address this issue, we conduct a detailed analysis of the internal attention dynamics during GRPO training and uncover a key insight: attention entropy can serve as a powerful dual-signal proxy. First, across different samples, the relative change in attention entropy (ΔEntropy), which reflects the divergence between the current policy and the base policy, acts as a robust indicator of sample learning value. Second, during the denoising process, the peaks of absolute attention entropy (Entropy(t)), which quantify attention dispersion, effectively identify critical timesteps where high-value exploration occurs.
>   Building on this observation, we propose Adaptive Entropy-Guided Policy Optimization (AEGPO), a novel dual-signal, dual-level adaptive optimization strategy. At the global level, AEGPO uses ΔEntropy to dynamically allocate rollout budgets, prioritizing prompts with higher learning value. At the local level, it exploits the peaks of Entropy(t) to guide exploration selectively at critical high-dispersion timesteps rather than uniformly across all denoising steps.
>   By focusing computation on the most informative samples and the most critical moments, AEGPO enables more efficient and effective policy optimization. Experiments on text-to-image generation tasks demonstrate that AEGPO significantly accelerates convergence and achieves superior alignment performance compared to standard GRPO variants.

