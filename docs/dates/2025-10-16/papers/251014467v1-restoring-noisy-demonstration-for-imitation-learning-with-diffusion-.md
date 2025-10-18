---
layout: default
title: Restoring Noisy Demonstration for Imitation Learning With Diffusion Models
---

# Restoring Noisy Demonstration for Imitation Learning With Diffusion Models
**arXiv**：[2510.14467v1](https://arxiv.org/abs/2510.14467) · [PDF](https://arxiv.org/pdf/2510.14467.pdf)  
**作者**：Shang-Fu Chen, Co Yong, Shao-Hua Sun  

**一句话要点**：提出过滤-恢复框架以解决模仿学习中噪声专家演示问题

**关键词**：模仿学习, 噪声演示, 扩散模型, 机器人操作, 离线学习

## 3 点简述
- 核心问题：专家演示常含噪声，影响模仿学习性能
- 方法要点：先过滤干净样本，再用条件扩散模型恢复噪声样本
- 实验效果：在机器人操作和运动任务中优于现有方法，验证鲁棒性

## 摘要（原文）

> Imitation learning (IL) aims to learn a policy from expert demonstrations and
> has been applied to various applications. By learning from the expert policy,
> IL methods do not require environmental interactions or reward signals.
> However, most existing imitation learning algorithms assume perfect expert
> demonstrations, but expert demonstrations often contain imperfections caused by
> errors from human experts or sensor/control system inaccuracies. To address the
> above problems, this work proposes a filter-and-restore framework to best
> leverage expert demonstrations with inherent noise. Our proposed method first
> filters clean samples from the demonstrations and then learns conditional
> diffusion models to recover the noisy ones. We evaluate our proposed framework
> and existing methods in various domains, including robot arm manipulation,
> dexterous manipulation, and locomotion. The experiment results show that our
> proposed framework consistently outperforms existing methods across all the
> tasks. Ablation studies further validate the effectiveness of each component
> and demonstrate the framework's robustness to different noise types and levels.
> These results confirm the practical applicability of our framework to noisy
> offline demonstration data.

