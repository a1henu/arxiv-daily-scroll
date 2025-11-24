---
layout: default
title: RynnVLA-002: A Unified Vision-Language-Action and World Model
---

# RynnVLA-002: A Unified Vision-Language-Action and World Model
**arXiv**：[2511.17502v1](https://arxiv.org/abs/2511.17502) · [PDF](https://arxiv.org/pdf/2511.17502.pdf)  
**作者**：Jun Cen, Siteng Huang, Yuqian Yuan, Hangjie Yuan, Chaohui Yu, Yuming Jiang, Jiayan Guo, Kehan Li, Hao Luo, Fan Wang, Xin Li, Deli Zhao, Hao Chen  

**一句话要点**：提出统一视觉-语言-动作与世界模型，以联合学习环境动态和动作规划。

**关键词**：视觉-语言-动作模型, 世界模型, 机器人任务, 联合学习, 环境动态预测

## 3 点简述
- 核心问题：如何统一视觉-语言-动作模型与世界模型，以增强环境理解和动作生成。
- 方法要点：世界模型预测未来图像状态，VLA模型生成动作，两者相互增强。
- 实验或效果：在LIBERO仿真中达97.4%成功率，真实世界任务成功率提升50%。

## 摘要（原文）

> We introduce RynnVLA-002, a unified Vision-Language-Action (VLA) and world model. The world model leverages action and visual inputs to predict future image states, learning the underlying physics of the environment to refine action generation. Conversely, the VLA model produces subsequent actions from image observations, enhancing visual understanding and supporting the world model's image generation. The unified framework of RynnVLA-002 enables joint learning of environmental dynamics and action planning. Our experiments show that RynnVLA-002 surpasses individual VLA and world models, demonstrating their mutual enhancement. We evaluate RynnVLA-002 in both simulation and real-world robot tasks. RynnVLA-002 achieves 97.4% success rate on the LIBERO simulation benchmark without pretraining, while in real-world LeRobot experiments, its integrated world model boosts the overall success rate by 50%.

