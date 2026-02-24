---
layout: default
title: DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces
---

# DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces
**arXiv**：[2602.19565v1](https://arxiv.org/abs/2602.19565) · [PDF](https://arxiv.org/pdf/2602.19565.pdf)  
**作者**：Li Zhang, Mingyu Mei, Ailing Wang, Xianhui Meng, Yan Zhong, Xinyuan Song, Liu Liu, Rujing Wang, Zaixing He, Cewu Lu  

**一句话要点**：提出DICArt框架，通过离散扩散过程解决类别级铰接物体姿态估计中的搜索空间大和运动学约束问题。

**关键词**：铰接物体姿态估计, 离散扩散模型, 运动学约束, 类别级6D姿态估计, 生成建模

## 3 点简述
- 现有方法在连续空间中回归姿态，面临搜索空间大和运动学约束难以整合的挑战。
- DICArt将姿态估计建模为条件离散扩散过程，使用灵活流决策器和分层运动学耦合策略。
- 在合成和真实数据集上验证，DICArt表现出优越性能和鲁棒性。

## 摘要（原文）

> Articulated object pose estimation is a core task in embodied AI. Existing methods typically regress poses in a continuous space, but often struggle with 1) navigating a large, complex search space and 2) failing to incorporate intrinsic kinematic constraints. In this work, we introduce DICArt (DIsCrete Diffusion for Articulation Pose Estimation), a novel framework that formulates pose estimation as a conditional discrete diffusion process. Instead of operating in a continuous domain, DICArt progressively denoises a noisy pose representation through a learned reverse diffusion procedure to recover the GT pose. To improve modeling fidelity, we propose a flexible flow decider that dynamically determines whether each token should be denoised or reset, effectively balancing the real and noise distributions during diffusion. Additionally, we incorporate a hierarchical kinematic coupling strategy, estimating the pose of each rigid part hierarchically to respect the object's kinematic structure. We validate DICArt on both synthetic and real-world datasets. Experimental results demonstrate its superior performance and robustness. By integrating discrete generative modeling with structural priors, DICArt offers a new paradigm for reliable category-level 6D pose estimation in complex environments.

