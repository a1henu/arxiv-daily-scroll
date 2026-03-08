---
layout: default
title: Direct Contact-Tolerant Motion Planning With Vision Language Models
---

# Direct Contact-Tolerant Motion Planning With Vision Language Models
**arXiv**：[2603.05017v1](https://arxiv.org/abs/2603.05017) · [PDF](https://arxiv.org/pdf/2603.05017.pdf)  
**作者**：He Li, Jian Sun, Chengyang Li, Guoliang Li, Qiyu Ruan, Shuai Wang, Chengzhong Xu  

**一句话要点**：提出直接接触容忍运动规划器，集成视觉语言模型于点云感知与导航，以解决杂乱环境中机器人接触容忍导航的适应性问题。

**关键词**：接触容忍运动规划, 视觉语言模型, 点云感知, 机器人导航, 优化控制

## 3 点简述
- 核心问题：现有接触容忍运动规划方法依赖间接空间表示，导致不准确且难以适应环境不确定性。
- 方法要点：设计VLM点云分割器进行接触容忍推理，并基于此构建感知到控制的优化问题，通过深度神经网络求解。
- 实验或效果：在仿真和真实机器人上验证，DCT在杂乱环境中实现鲁棒高效导航，优于基线方法。

## 摘要（原文）

> Navigation in cluttered environments often requires robots to tolerate contact with movable or deformable objects to maintain efficiency. Existing contact-tolerant motion planning (CTMP) methods rely on indirect spatial representations (e.g., prebuilt map, obstacle set), resulting in inaccuracies and a lack of adaptiveness to environmental uncertainties. To address this issue, we propose a direct contact-tolerant (DCT) planner, which integrates vision-language models (VLMs) into direct point perception and navigation, including two key components. The first one is VLM point cloud partitioner (VPP), which performs contact-tolerance reasoning in image space using VLM, caches inference masks, propagates them across frames using odometry, and projects them onto the current scan to generate a contact-aware point cloud. The second innovation is VPP guided navigation (VGN), which formulates CTMP as a perception-to-control optimization problem under direct contact-aware point cloud constraints, which is further solved by a specialized deep neural network (DNN). We implement DCT in Isaac Sim and a real car-like robot, demonstrating that DCT achieves robust and efficient navigation in cluttered environments with movable obstacles, outperforming representative baselines across diverse metrics. The code is available at: https://github.com/ChrisLeeUM/DCT.

