---
layout: default
title: MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training
---

# MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training
**arXiv**：[2512.15411v1](https://arxiv.org/abs/2512.15411) · [PDF](https://arxiv.org/pdf/2512.15411.pdf)  
**作者**：Zhenhan Yin, Xuanhan Wang, Jiahao Jiang, Kaiyuan Deng, Pengqi Chen, Shuangle Li, Chong Liu, Xing Xu, ingkuan Song, Lianli Gao, Heng Tao Shen  

**一句话要点**：提出MiVLA模型，通过人机互模仿预训练增强视觉-语言-动作模型的泛化能力

**关键词**：视觉-语言-动作模型, 人机互模仿, 泛化能力, 机器人控制, 预训练方法

## 3 点简述
- 核心问题：现有视觉-语言-动作模型因视角、外观和形态不匹配导致泛化能力受限
- 方法要点：利用人手机械臂行为相似性，通过双向动作空间对齐进行互模仿预训练
- 实验或效果：在仿真和真实机器人任务中，MiVLA相比先进模型提升25%和14%性能

## 摘要（原文）

> While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

