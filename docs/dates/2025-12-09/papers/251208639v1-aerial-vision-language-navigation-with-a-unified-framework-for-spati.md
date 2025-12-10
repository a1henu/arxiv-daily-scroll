---
layout: default
title: Aerial Vision-Language Navigation with a Unified Framework for Spatial, Temporal and Embodied Reasoning
---

# Aerial Vision-Language Navigation with a Unified Framework for Spatial, Temporal and Embodied Reasoning
**arXiv**：[2512.08639v1](https://arxiv.org/abs/2512.08639) · [PDF](https://arxiv.org/pdf/2512.08639.pdf)  
**作者**：Huilin Xu, Zhuoyang Liu, Yixiang Luomei, Feng Xu  

**一句话要点**：提出统一框架，仅用单目RGB和语言指令实现无人机视觉语言导航，优化空间、时间和具身推理。

**关键词**：视觉语言导航, 无人机导航, 多任务学习, 单目视觉, 具身推理, 关键帧选择

## 3 点简述
- 核心问题：现有方法依赖全景、深度或里程计，增加成本和复杂性，阻碍轻量无人机部署。
- 方法要点：将导航建模为下一个令牌预测，通过提示引导多任务学习联合优化感知、推理和动作预测。
- 实验或效果：在Aerial VLN基准上验证，单目RGB设置下性能优于现有RGB基线，接近全景RGB-D方法。

## 摘要（原文）

> Aerial Vision-and-Language Navigation (VLN) aims to enable unmanned aerial vehicles (UAVs) to interpret natural language instructions and navigate complex urban environments using onboard visual observation. This task holds promise for real-world applications such as low-altitude inspection, search-and-rescue, and autonomous aerial delivery. Existing methods often rely on panoramic images, depth inputs, or odometry to support spatial reasoning and action planning. These requirements increase system cost and integration complexity, thus hindering practical deployment for lightweight UAVs. We present a unified aerial VLN framework that operates solely on egocentric monocular RGB observations and natural language instructions. The model formulates navigation as a next-token prediction problem, jointly optimizing spatial perception, trajectory reasoning, and action prediction through prompt-guided multi-task learning. Moreover, we propose a keyframe selection strategy to reduce visual redundancy by retaining semantically informative frames, along with an action merging and label reweighting mechanism that mitigates long-tailed supervision imbalance and facilitates stable multi-task co-training. Extensive experiments on the Aerial VLN benchmark validate the effectiveness of our method. Under the challenging monocular RGB-only setting, our model achieves strong results across both seen and unseen environments. It significantly outperforms existing RGB-only baselines and narrows the performance gap with state-of-the-art panoramic RGB-D counterparts. Comprehensive ablation studies further demonstrate the contribution of our task design and architectural choices.

