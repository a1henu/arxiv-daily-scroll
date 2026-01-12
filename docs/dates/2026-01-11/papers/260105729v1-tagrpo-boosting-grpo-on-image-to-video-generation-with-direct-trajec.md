---
layout: default
title: TAGRPO: Boosting GRPO on Image-to-Video Generation with Direct Trajectory Alignment
---

# TAGRPO: Boosting GRPO on Image-to-Video Generation with Direct Trajectory Alignment
**arXiv**：[2601.05729v1](https://arxiv.org/abs/2601.05729) · [PDF](https://arxiv.org/pdf/2601.05729.pdf)  
**作者**：Jin Wang, Jianxiang Lu, Guangzheng Xu, Comi Chen, Haoyu Yang, Linqing Wang, Peng Chen, Mingtao Chen, Zhichao Hu, Longhuang Wu, Shuai Shao, Qinglin Lu, Ping Luo  

**一句话要点**：提出TAGRPO框架以提升图像到视频生成中GRPO的性能，通过直接轨迹对齐实现优化。

**关键词**：图像到视频生成, 强化学习优化, 轨迹对齐, 对比学习, 后训练框架

## 3 点简述
- 核心问题：现有GRPO方法在图像到视频生成中奖励提升不一致，效果有限。
- 方法要点：基于相同初始噪声的生成视频提供优化指导，在中间潜在空间应用GRPO损失，直接对齐高奖励轨迹并远离低奖励轨迹。
- 实验或效果：相比DanceGRPO，TAGRPO在图像到视频生成上取得显著改进，同时引入记忆库增强多样性和降低计算开销。

## 摘要（原文）

> Recent studies have demonstrated the efficacy of integrating Group Relative Policy Optimization (GRPO) into flow matching models, particularly for text-to-image and text-to-video generation. However, we find that directly applying these techniques to image-to-video (I2V) models often fails to yield consistent reward improvements. To address this limitation, we present TAGRPO, a robust post-training framework for I2V models inspired by contrastive learning. Our approach is grounded in the observation that rollout videos generated from identical initial noise provide superior guidance for optimization. Leveraging this insight, we propose a novel GRPO loss applied to intermediate latents, encouraging direct alignment with high-reward trajectories while maximizing distance from low-reward counterparts. Furthermore, we introduce a memory bank for rollout videos to enhance diversity and reduce computational overhead. Despite its simplicity, TAGRPO achieves significant improvements over DanceGRPO in I2V generation.

