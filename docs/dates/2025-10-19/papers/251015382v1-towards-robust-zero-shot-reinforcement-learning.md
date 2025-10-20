---
layout: default
title: Towards Robust Zero-Shot Reinforcement Learning
---

# Towards Robust Zero-Shot Reinforcement Learning
**arXiv**：[2510.15382v1](https://arxiv.org/abs/2510.15382) · [PDF](https://arxiv.org/pdf/2510.15382.pdf)  
**作者**：Kexin Zheng, Lauriane Teyssier, Yinan Zheng, Yu Luo, Xiayuan Zhan  

**一句话要点**：提出BREEZE以解决零样本强化学习中的表达性不足和分布外动作偏差问题

**关键词**：零样本强化学习, 行为正则化, 扩散模型, 表示学习, 离线强化学习

## 3 点简述
- 核心问题：零样本强化学习中FB方法表达性不足，分布外动作导致表示偏差和性能下降
- 方法要点：引入行为正则化稳定策略学习，使用任务条件扩散模型提取高质量多模态策略
- 实验或效果：在ExORL和D4RL Kitchen数据集上表现最佳或接近最佳，鲁棒性优于现有方法

## 摘要（原文）

> The recent development of zero-shot reinforcement learning (RL) has opened a
> new avenue for learning pre-trained generalist policies that can adapt to
> arbitrary new tasks in a zero-shot manner. While the popular Forward-Backward
> representations (FB) and related methods have shown promise in zero-shot RL, we
> empirically found that their modeling lacks expressivity and that extrapolation
> errors caused by out-of-distribution (OOD) actions during offline learning
> sometimes lead to biased representations, ultimately resulting in suboptimal
> performance. To address these issues, we propose Behavior-REgularizEd Zero-shot
> RL with Expressivity enhancement (BREEZE), an upgraded FB-based framework that
> simultaneously enhances learning stability, policy extraction capability, and
> representation learning quality. BREEZE introduces behavioral regularization in
> zero-shot RL policy learning, transforming policy optimization into a stable
> in-sample learning paradigm. Additionally, BREEZE extracts the policy using a
> task-conditioned diffusion model, enabling the generation of high-quality and
> multimodal action distributions in zero-shot RL settings. Moreover, BREEZE
> employs expressive attention-based architectures for representation modeling to
> capture the complex relationships between environmental dynamics. Extensive
> experiments on ExORL and D4RL Kitchen demonstrate that BREEZE achieves the best
> or near-the-best performance while exhibiting superior robustness compared to
> prior offline zero-shot RL methods. The official implementation is available
> at: https://github.com/Whiterrrrr/BREEZE.

