---
layout: default
title: ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation
---

# ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation
**arXiv**：[2601.08325v1](https://arxiv.org/abs/2601.08325) · [PDF](https://arxiv.org/pdf/2601.08325.pdf)  
**作者**：Zhenyang Liu, Yongchong Gu, Yikai Wang, Xiangyang Xue, Yanwei Fu  

**一句话要点**：提出ActiveVLA框架，通过主动感知提升机器人3D精细操作能力

**关键词**：机器人操作, 主动感知, 视觉-语言-动作模型, 3D精细操作, 视角选择

## 3 点简述
- 现有VLA方法依赖静态摄像头，缺乏自适应视角选择，限制长时程和精细操作性能
- ActiveVLA采用粗到精范式：先定位关键3D区域，再优化主动感知以选择最佳视角并提高分辨率
- 实验表明，ActiveVLA在三个仿真基准上优于现有方法，并能迁移到真实世界复杂环境

## 摘要（原文）

> Recent advances in robot manipulation have leveraged pre-trained vision-language models (VLMs) and explored integrating 3D spatial signals into these models for effective action prediction, giving rise to the promising vision-language-action (VLA) paradigm. However, most existing approaches overlook the importance of active perception: they typically rely on static, wrist-mounted cameras that provide an end-effector-centric viewpoint. As a result, these models are unable to adaptively select optimal viewpoints or resolutions during task execution, which significantly limits their performance in long-horizon tasks and fine-grained manipulation scenarios. To address these limitations, we propose ActiveVLA, a novel vision-language-action framework that empowers robots with active perception capabilities for high-precision, fine-grained manipulation. ActiveVLA adopts a coarse-to-fine paradigm, dividing the process into two stages: (1) Critical region localization. ActiveVLA projects 3D inputs onto multi-view 2D projections, identifies critical 3D regions, and supports dynamic spatial awareness. (2) Active perception optimization. Drawing on the localized critical regions, ActiveVLA uses an active view selection strategy to choose optimal viewpoints. These viewpoints aim to maximize amodal relevance and diversity while minimizing occlusions. Additionally, ActiveVLA applies a 3D zoom-in to improve resolution in key areas. Together, these steps enable finer-grained active perception for precise manipulation. Extensive experiments demonstrate that ActiveVLA achieves precise 3D manipulation and outperforms state-of-the-art baselines on three simulation benchmarks. Moreover, ActiveVLA transfers seamlessly to real-world scenarios, enabling robots to learn high-precision tasks in complex environments.

