---
layout: default
title: NavDreamer: Video Models as Zero-Shot 3D Navigators
---

# NavDreamer: Video Models as Zero-Shot 3D Navigators
**arXiv**：[2602.09765v1](https://arxiv.org/abs/2602.09765) · [PDF](https://arxiv.org/pdf/2602.09765.pdf)  
**作者**：Xijie Huang, Weiqi Gai, Tianyue Wu, Congyu Wang, Zhiyang Liu, Xin Zhou, Yuze Wu, Fei Gao  

**一句话要点**：提出NavDreamer，利用视频模型作为零样本3D导航器，通过生成视频规划解决导航数据稀缺和静态表示问题。

**关键词**：零样本导航, 视频生成模型, 时空动态建模, 逆动力学解码, 导航基准测试

## 3 点简述
- 核心问题：现有视觉-语言-动作模型在导航中面临数据稀缺、静态表示无法捕捉时空动态和物理规律的局限。
- 方法要点：基于视频框架，利用生成视频模型作为语言指令与导航轨迹的通用接口，结合采样优化和逆动力学模型解码可执行路径。
- 实验或效果：在综合基准测试中展示了对新对象和未见环境的鲁棒零样本泛化能力，验证视频规划适用于导航高层决策。

## 摘要（原文）

> Previous Vision-Language-Action models face critical limitations in navigation: scarce, diverse data from labor-intensive collection and static representations that fail to capture temporal dynamics and physical laws. We propose NavDreamer, a video-based framework for 3D navigation that leverages generative video models as a universal interface between language instructions and navigation trajectories. Our main hypothesis is that video's ability to encode spatiotemporal information and physical dynamics, combined with internet-scale availability, enables strong zero-shot generalization in navigation. To mitigate the stochasticity of generative predictions, we introduce a sampling-based optimization method that utilizes a VLM for trajectory scoring and selection. An inverse dynamics model is employed to decode executable waypoints from generated video plans for navigation. To systematically evaluate this paradigm in several video model backbones, we introduce a comprehensive benchmark covering object navigation, precise navigation, spatial grounding, language control, and scene reasoning. Extensive experiments demonstrate robust generalization across novel objects and unseen environments, with ablation studies revealing that navigation's high-level decision-making nature makes it particularly suited for video-based planning.

