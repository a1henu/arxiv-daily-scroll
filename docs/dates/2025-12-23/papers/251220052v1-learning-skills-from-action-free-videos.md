---
layout: default
title: Learning Skills from Action-Free Videos
---

# Learning Skills from Action-Free Videos
**arXiv**：[2512.20052v1](https://arxiv.org/abs/2512.20052) · [PDF](https://arxiv.org/pdf/2512.20052.pdf)  
**作者**：Hung-Chieh Fang, Kuo-Han Hung, Chu-Rong Chen, Po-Jung Chou, Chun-Kai Yang, Po-Chen Ko, Yu-Chiang Wang, Yueh-Hua Wu, Min-Hung Chen, Shao-Hua Sun  

**一句话要点**：提出基于光流的技能抽象框架，从无动作视频中学习技能以提升机器人规划能力。

**关键词**：技能学习, 光流表示, 机器人规划, 无动作视频, 潜在技能空间

## 3 点简述
- 核心问题：现有视频生成模型难以转化为低级动作，而潜在动作模型缺乏高级规划能力。
- 方法要点：通过光流中间表示学习潜在技能空间，对齐视频动态与机器人动作。
- 实验或效果：在多项任务和长时程设置中一致提升性能，验证从原始视觉数据获取和组合技能的能力。

## 摘要（原文）

> Learning from videos offers a promising path toward generalist robots by providing rich visual and temporal priors beyond what real robot datasets contain. While existing video generative models produce impressive visual predictions, they are difficult to translate into low-level actions. Conversely, latent-action models better align videos with actions, but they typically operate at the single-step level and lack high-level planning capabilities. We bridge this gap by introducing Skill Abstraction from Optical Flow (SOF), a framework that learns latent skills from large collections of action-free videos. Our key idea is to learn a latent skill space through an intermediate representation based on optical flow that captures motion information aligned with both video dynamics and robot actions. By learning skills in this flow-based latent space, SOF enables high-level planning over video-derived skills and allows for easier translation of these skills into actions. Experiments show that our approach consistently improves performance in both multitask and long-horizon settings, demonstrating the ability to acquire and compose skills directly from raw visual data.

