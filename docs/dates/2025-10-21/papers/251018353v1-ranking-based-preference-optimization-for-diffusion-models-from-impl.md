---
layout: default
title: Ranking-based Preference Optimization for Diffusion Models from Implicit User Feedback
---

# Ranking-based Preference Optimization for Diffusion Models from Implicit User Feedback
**arXiv**：[2510.18353v1](https://arxiv.org/abs/2510.18353) · [PDF](https://arxiv.org/pdf/2510.18353.pdf)  
**作者**：Yi-Lun Wu, Bo-Kai Ruan, Chiang Tseng, Hong-Han Shuai  

**一句话要点**：提出Diffusion-DRO框架，通过排名优化解决扩散模型偏好学习中的非线性估计和离线数据限制问题。

**关键词**：扩散模型, 偏好优化, 逆强化学习, 排名学习, 去噪训练, 离线在线数据融合

## 3 点简述
- 核心问题：现有DPO方法在估计图像概率时因sigmoid函数非线性和离线数据集多样性不足而受限。
- 方法要点：基于逆强化学习，将偏好学习转化为排名问题，简化训练目标为去噪形式。
- 实验或效果：在挑战性和未见提示下，生成质量优于基线，定量指标和用户研究均显示改进。

## 摘要（原文）

> Direct preference optimization (DPO) methods have shown strong potential in
> aligning text-to-image diffusion models with human preferences by training on
> paired comparisons. These methods improve training stability by avoiding the
> REINFORCE algorithm but still struggle with challenges such as accurately
> estimating image probabilities due to the non-linear nature of the sigmoid
> function and the limited diversity of offline datasets. In this paper, we
> introduce Diffusion Denoising Ranking Optimization (Diffusion-DRO), a new
> preference learning framework grounded in inverse reinforcement learning.
> Diffusion-DRO removes the dependency on a reward model by casting preference
> learning as a ranking problem, thereby simplifying the training objective into
> a denoising formulation and overcoming the non-linear estimation issues found
> in prior methods. Moreover, Diffusion-DRO uniquely integrates offline expert
> demonstrations with online policy-generated negative samples, enabling it to
> effectively capture human preferences while addressing the limitations of
> offline data. Comprehensive experiments show that Diffusion-DRO delivers
> improved generation quality across a range of challenging and unseen prompts,
> outperforming state-of-the-art baselines in both both quantitative metrics and
> user studies. Our source code and pre-trained models are available at
> https://github.com/basiclab/DiffusionDRO.

