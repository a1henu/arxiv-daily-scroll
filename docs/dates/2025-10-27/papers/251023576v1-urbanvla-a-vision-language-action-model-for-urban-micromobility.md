---
layout: default
title: UrbanVLA: A Vision-Language-Action Model for Urban Micromobility
---

# UrbanVLA: A Vision-Language-Action Model for Urban Micromobility
**arXiv**：[2510.23576v1](https://arxiv.org/abs/2510.23576) · [PDF](https://arxiv.org/pdf/2510.23576.pdf)  
**作者**：Anqi Li, Zhiyong Wang, Jiazhao Zhang, Minghan Li, Yunpeng Qi, Zhibo Chen, Zhizheng Zhang, He Wang  

**一句话要点**：提出UrbanVLA模型以解决城市微移动中的长距离导航问题

**关键词**：城市微移动导航, 视觉-语言-动作模型, 两阶段训练, 路径-视觉对齐, 强化微调, 大规模环境导航

## 3 点简述
- 核心问题：城市微移动在动态、非结构化环境中实现可靠长距离导航的挑战
- 方法要点：采用两阶段训练，结合监督和强化微调，对齐路径点与视觉观察
- 实验或效果：在MetaUrban上超越基线55%，实现大规模城市环境的可靠导航

## 摘要（原文）

> Urban micromobility applications, such as delivery robots, demand reliable
> navigation across large-scale urban environments while following long-horizon
> route instructions. This task is particularly challenging due to the dynamic
> and unstructured nature of real-world city areas, yet most existing navigation
> methods remain tailored to short-scale and controllable scenarios. Effective
> urban micromobility requires two complementary levels of navigation skills:
> low-level capabilities such as point-goal reaching and obstacle avoidance, and
> high-level capabilities, such as route-visual alignment. To this end, we
> propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework
> designed for scalable urban navigation. Our method explicitly aligns noisy
> route waypoints with visual observations during execution, and subsequently
> plans trajectories to drive the robot. To enable UrbanVLA to master both levels
> of navigation, we employ a two-stage training pipeline. The process begins with
> Supervised Fine-Tuning (SFT) using simulated environments and trajectories
> parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on
> a mixture of simulation and real-world data, which enhances the model's safety
> and adaptability in real-world settings. Experiments demonstrate that UrbanVLA
> surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban.
> Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both
> scalability to large-scale urban environments and robustness against real-world
> uncertainties.

