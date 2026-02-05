---
layout: default
title: Reshaping Action Error Distributions for Reliable Vision-Language-Action Models
---

# Reshaping Action Error Distributions for Reliable Vision-Language-Action Models
**arXiv**：[2602.04228v1](https://arxiv.org/abs/2602.04228) · [PDF](https://arxiv.org/pdf/2602.04228.pdf)  
**作者**：Shuanghao Bai, Dakai Wang, Cheng Chi, Wanqi Zhou, Jing Lyu, Xiaoguang Zhao, Pengwei Wang, Zhongyuan Wang, Lei Xing, Shanghang Zhang, Badong Chen  

**一句话要点**：提出基于最小误差熵的目标函数以提升连续动作视觉-语言-动作模型的鲁棒性

**关键词**：视觉-语言-动作模型, 连续动作回归, 最小误差熵, 机器人操作, 鲁棒性训练, 信息理论

## 3 点简述
- 核心问题：传统均方误差在连续动作回归中施加强点约束，可能限制模型泛化能力。
- 方法要点：引入最小误差熵及其加权变体，结合均方误差重塑动作误差分布。
- 实验效果：在标准、少样本和噪声设置下，多基准测试显示成功率与鲁棒性一致提升。

## 摘要（原文）

> In robotic manipulation, vision-language-action (VLA) models have emerged as a promising paradigm for learning generalizable and scalable robot policies. Most existing VLA frameworks rely on standard supervised objectives, typically cross-entropy for discrete actions and mean squared error (MSE) for continuous action regression, which impose strong pointwise constraints on individual predictions. In this work, we focus on continuous-action VLA models and move beyond conventional MSE-based regression by reshaping action error distributions during training. Drawing on information-theoretic principles, we introduce Minimum Error Entropy (MEE) into modern VLA architectures and propose a trajectory-level MEE objective, together with two weighted variants, combined with MSE for continuous-action VLA training. We evaluate our approaches across standard, few-shot, and noisy settings on multiple representative VLA architectures, using simulation benchmarks such as LIBERO and SimplerEnv as well as real-world robotic manipulation tasks. Experimental results demonstrate consistent improvements in success rates and robustness across these settings. Under imbalanced data regimes, the gains persist within a well-characterized operating range, while incurring negligible additional training cost and no impact on inference efficiency. We further provide theoretical analyses that explain why MEE-based supervision is effective and characterize its practical range. Project Page: https://cognition2actionlab.github.io/VLA-TMEE.github.io/

