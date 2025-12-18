---
layout: default
title: mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs
---

# mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs
**arXiv**：[2512.15692v1](https://arxiv.org/abs/2512.15692) · [PDF](https://arxiv.org/pdf/2512.15692.pdf)  
**作者**：Jonas Pai, Liam Achenbach, Victoriano Montesinos, Benedek Forrai, Oier Mees, Elvis Nava  

**一句话要点**：提出视频-动作模型以解决机器人控制中视觉-语言-动作模型对物理动态理解不足的问题

**关键词**：视频-动作模型, 机器人控制, 逆动力学模型, 流匹配, 物理动态理解, 样本效率

## 3 点简述
- 核心问题：现有视觉-语言-动作模型依赖静态网络数据预训练，缺乏物理因果理解，需大量专家数据补偿。
- 方法要点：引入视频-动作模型，结合预训练视频模型和流匹配动作解码器，作为逆动力学模型生成机器人动作。
- 实验或效果：在模拟和真实机器人任务中实现最优性能，样本效率提升10倍，收敛速度加快2倍。

## 摘要（原文）

> Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce \model, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

