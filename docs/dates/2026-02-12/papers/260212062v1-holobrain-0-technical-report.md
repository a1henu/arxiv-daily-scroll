---
layout: default
title: HoloBrain-0 Technical Report
---

# HoloBrain-0 Technical Report
**arXiv**：[2602.12062v1](https://arxiv.org/abs/2602.12062) · [PDF](https://arxiv.org/pdf/2602.12062.pdf)  
**作者**：Xuewu Lin, Tianwei Lin, Yun Du, Hongyu Xie, Yiwei Jin, Jiawei Li, Shijie Wu, Qingze Wang, Mengdi Li, Mengao Zhao, Ziang Li, Chaodong Huang, Hongzhe Bi, Lichao Huang, Zhizhong Su  

**一句话要点**：提出HoloBrain-0 VLA框架，通过融入机器人先验增强3D空间推理，支持可靠机器人部署。

**关键词**：视觉-语言-动作框架, 机器人先验, 3D空间推理, 仿真基准, 开源生态系统, 设备部署

## 3 点简述
- 核心问题：基础模型研究与可靠机器人部署之间存在差距，需提升3D空间推理能力。
- 方法要点：设计VLA架构，显式融入机器人多视角相机参数和运动学描述（URDF）等先验。
- 实验或效果：在仿真基准和真实世界长时程操作任务中取得先进结果，0.2B参数变体支持低延迟设备部署。

## 摘要（原文）

> In this work, we introduce HoloBrain-0, a comprehensive Vision-Language-Action (VLA) framework that bridges the gap between foundation model research and reliable real-world robot deployment. The core of our system is a novel VLA architecture that explicitly incorporates robot embodiment priors, including multi-view camera parameters and kinematic descriptions (URDF), to enhance 3D spatial reasoning and support diverse embodiments. We validate this design through a scalable ``pre-train then post-train" paradigm, achieving state-of-the-art results on simulation benchmarks such as RoboTwin 2.0, LIBERO, and GenieSim, as well as strong results on challenging long-horizon real-world manipulation tasks. Notably, our efficient 0.2B-parameter variant rivals significantly larger baselines, enabling low-latency on-device deployment. To further accelerate research and practical adoption, we fully open-source the entire HoloBrain ecosystem, which includes: (1) powerful pre-trained VLA foundations; (2) post-trained checkpoints for multiple simulation suites and real-world tasks; and (3) RoboOrchard, a full-stack VLA infrastructure for data curation, model training and deployment. Together with standardized data collection protocols, this release provides the community with a complete, reproducible path toward high-performance robotic manipulation.

