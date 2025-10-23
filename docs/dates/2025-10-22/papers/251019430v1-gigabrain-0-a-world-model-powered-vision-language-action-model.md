---
layout: default
title: GigaBrain-0: A World Model-Powered Vision-Language-Action Model
---

# GigaBrain-0: A World Model-Powered Vision-Language-Action Model
**arXiv**：[2510.19430v1](https://arxiv.org/abs/2510.19430) · [PDF](https://arxiv.org/pdf/2510.19430.pdf)  
**作者**：GigaBrain Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jie Li, Jiagang Zhu, Lv Feng, Peng Li, Qiuping Deng, Runqi Ouyang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yang Wang, Yifan Li, Yilong Li, Yiran Ding, Yuan Xu, Yun Ye, Yukun Zhou, Zhehao Dong, Zhenan Wang, Zhichao Liu, Zheng Zhu  

**一句话要点**：提出GigaBrain-0，利用世界模型生成数据以解决机器人视觉-语言-动作模型数据收集难题

**关键词**：视觉-语言-动作模型, 世界模型数据生成, RGBD输入建模, 具身链式思维, 机器人泛化, 轻量级变体

## 3 点简述
- 核心问题：大规模真实机器人数据收集成本高，限制视觉-语言-动作模型的泛化能力。
- 方法要点：通过世界模型生成多样化数据，减少对真实数据的依赖，并引入RGBD输入和具身链式思维监督。
- 实验或效果：在灵巧、长视界和移动操作任务中实现优越泛化，包括外观、物体放置和视角变化。

## 摘要（原文）

> Training Vision-Language-Action (VLA) models for generalist robots typically
> requires large-scale real-world robot data, which is expensive and
> time-consuming to collect. The inefficiency of physical data collection
> severely limits the scalability, and generalization capacity of current VLA
> systems. To address this challenge, we introduce GigaBrain-0, a novel VLA
> foundation model empowered by world model-generated data (e.g., video
> generation, real2real transfer, human transfer, view transfer, sim2real
> transfer data). By leveraging world models to generate diverse data at scale,
> GigaBrain-0 significantly reduces reliance on real robot data while improving
> cross-task generalization. Our approach further improves policy robustness
> through RGBD input modeling and embodied Chain-of-Thought (CoT) supervision,
> enabling the model to reason about spatial geometry, object states, and
> long-horizon dependencies during task execution. This leads to substantial
> gains in real-world performance on dexterous, long-horizon, and mobile
> manipulation tasks. Extensive experiments demonstrate that GigaBrain-0 achieves
> superior generalization across variations in appearances (e.g., textures,
> colors), object placements, and camera viewpoints. Additionally, we present
> GigaBrain-0-Small, an optimized lightweight variant designed to run efficiently
> on devices such as the NVIDIA Jetson AGX Orin.

