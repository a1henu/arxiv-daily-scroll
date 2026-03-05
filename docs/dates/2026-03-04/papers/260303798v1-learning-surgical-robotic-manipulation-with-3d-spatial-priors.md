---
layout: default
title: Learning Surgical Robotic Manipulation with 3D Spatial Priors
---

# Learning Surgical Robotic Manipulation with 3D Spatial Priors
**arXiv**：[2603.03798v1](https://arxiv.org/abs/2603.03798) · [PDF](https://arxiv.org/pdf/2603.03798.pdf)  
**作者**：Yu Sheng, Lidian Wang, Xiaomeng Chu, Jiajun Deng, Min Cheng, Yanyong Zhang, Bei Hua, Houqiang Li, Jianmin Ji  

**一句话要点**：提出Spatial Surgical Transformer，通过端到端视觉运动策略解决手术机器人3D空间感知问题。

**关键词**：手术机器人, 3D空间感知, 端到端策略, 几何Transformer, 数据集构建, 真实机器人实验

## 3 点简述
- 核心问题：现有方法存在多阶段误差累积或临床干扰，缺乏高效3D空间感知。
- 方法要点：构建Surgical3D数据集，微调几何Transformer提取3D表示，通过MSFC对齐动作空间。
- 实验或效果：真实机器人实验在打结和器官解剖任务中实现先进性能和强空间泛化。

## 摘要（原文）

> Achieving 3D spatial awareness is crucial for surgical robotic manipulation, where precise and delicate operations are required. Existing methods either explicitly reconstruct the surgical scene prior to manipulation, or enhance multi-view features by adding wrist-mounted cameras to supplement the default stereo endoscopes. However, both paradigms suffer from notable limitations: the former easily leads to error accumulation and prevents end-to-end optimization due to its multi-stage nature, while the latter is rarely adopted in clinical practice since wrist-mounted cameras can interfere with the motion of surgical robot arms. In this work, we introduce the Spatial Surgical Transformer (SST), an end-to-end visuomotor policy that empowers surgical robots with 3D spatial awareness by directly exploring 3D spatial cues embedded in endoscopic images. First, we build Surgical3D, a large-scale photorealistic dataset containing 30K stereo endoscopic image pairs with accurate 3D geometry, addressing the scarcity of 3D data in surgical scenes. Based on Surgical3D, we finetune a powerful geometric transformer to extract robust 3D latent representations from stereo endoscopes images. These representations are then seamlessly aligned with the robot's action space via a lightweight multi-level spatial feature connector (MSFC), all within an endoscope-centric coordinate frame. Extensive real-robot experiments demonstrate that SST achieves state-of-the-art performance and strong spatial generalization on complex surgical tasks such as knot tying and ex-vivo organ dissection, representing a significant step toward practical clinical deployment. The dataset and code will be released.

