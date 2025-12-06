---
layout: default
title: BulletTime: Decoupled Control of Time and Camera Pose for Video Generation
---

# BulletTime: Decoupled Control of Time and Camera Pose for Video Generation
**arXiv**：[2512.05076v1](https://arxiv.org/abs/2512.05076) · [PDF](https://arxiv.org/pdf/2512.05076.pdf)  
**作者**：Yiming Wang, Qihang Zhang, Shengqu Cai, Tong Wu, Jan Ackermann, Zhengfei Kuang, Yang Zheng, Frano Rajič, Siyu Tang, Gordon Wetzstein  

**一句话要点**：提出BulletTime框架以解耦场景动态与相机位姿，实现视频生成的4D可控性。

**关键词**：视频生成, 扩散模型, 4D控制, 相机位姿解耦, 时空可控性

## 3 点简述
- 现有视频扩散模型耦合场景动态与相机运动，限制时空控制精度。
- 通过4D位置编码和自适应归一化，将世界时间序列和相机轨迹作为条件输入。
- 实验显示模型在多样时序和相机轨迹下实现稳健4D控制，生成质量高且优于先前工作。

## 摘要（原文）

> Emerging video diffusion models achieve high visual fidelity but fundamentally couple scene dynamics with camera motion, limiting their ability to provide precise spatial and temporal control. We introduce a 4D-controllable video diffusion framework that explicitly decouples scene dynamics from camera pose, enabling fine-grained manipulation of both scene dynamics and camera viewpoint. Our framework takes continuous world-time sequences and camera trajectories as conditioning inputs, injecting them into the video diffusion model through a 4D positional encoding in the attention layer and adaptive normalizations for feature modulation. To train this model, we curate a unique dataset in which temporal and camera variations are independently parameterized; this dataset will be made public. Experiments show that our model achieves robust real-world 4D control across diverse timing patterns and camera trajectories, while preserving high generation quality and outperforming prior work in controllability. See our website for video results: https://19reborn.github.io/Bullet4D/

