---
layout: default
title: HarvestFlex: Strawberry Harvesting via Vision-Language-Action Policy Adaptation in the Wild
---

# HarvestFlex: Strawberry Harvesting via Vision-Language-Action Policy Adaptation in the Wild
**arXiv**：[2603.05982v1](https://arxiv.org/abs/2603.05982) · [PDF](https://arxiv.org/pdf/2603.05982.pdf)  
**作者**：Ziyang Zhao, Shuheng Wang, Zhonghua Miao, Ya Xiong  

**一句话要点**：提出基于视觉-语言-动作策略迁移的草莓采摘系统，在真实温室中实现闭环采摘。

**关键词**：视觉-语言-动作策略, 草莓采摘, 温室机器人, 策略迁移, 闭环系统, RGB传感

## 3 点简述
- 核心问题：在遮挡和镜面反射下，将VLA策略迁移到非结构化温室草莓采摘任务。
- 方法要点：使用三视图RGB传感和端到端闭环系统，避免深度云和显式几何校准。
- 实验效果：通过全微调pi_0.5模型，在50次试验中达到74.0%成功率，采摘时间32.6秒/个。

## 摘要（原文）

> This work presents the first study on transferring vision-language-action (VLA) policies to real greenhouse tabletop strawberry harvesting, a long-horizon, unstructured task challenged by occlusion and specular reflections. We built an end-to-end closed-loop system on the HarvestFlex platform using three-view RGB sensing (two fixed scene views plus a wrist-mounted view) and intentionally avoided depth clouds and explicit geometric calibration. We collected 3.71 h of VR teleoperated demonstrations (227 episodes) and fine-tuned pi_0, pi_0.5, and WALL-OSS with full fine-tuning and LoRA. Under a unified 50 trials real-greenhouse protocol and metrics spanning completion, pi_0.5 with full fine-tuning achieved success rate of 74.0% with 32.6 s/pick and damage rate of 4.1%. Asynchronous inference-control decoupling further improved performance over synchronous deployment. Results showed non-trivial closed-loop picking with fewer than four hours of real data, while remaining limited by close-range observability loss and contact-dynamics mismatch. A demonstration video is available at: https://youtu.be/bN8ZowZKPMI.

