---
layout: default
title: Direct Contact-Tolerant Motion Planning With Vision Language Models
---

# Direct Contact-Tolerant Motion Planning With Vision Language Models
**arXiv**：[2603.05017v1](https://arxiv.org/abs/2603.05017) · [PDF](https://arxiv.org/pdf/2603.05017.pdf)  
**作者**：He Li, Jian Sun, Chengyang Li, Guoliang Li, Qiyu Ruan, Shuai Wang, Chengzhong Xu  

**一句话要点**：提出直接接触容忍运动规划器，集成视觉语言模型以在杂乱环境中实现高效导航。

**关键词**：接触容忍运动规划, 视觉语言模型, 点云分割, 机器人导航, 感知到控制优化

## 3 点简述
- 现有接触容忍规划方法依赖间接空间表示，导致不准确且适应性差。
- 方法集成VLM进行点云分割和导航优化，直接处理接触感知点云。
- 在仿真和真实机器人实验中，优于基线方法，实现鲁棒高效导航。

## 摘要（原文）

> Navigation in cluttered environments often requires robots to tolerate contact with movable or deformable objects to maintain efficiency. Existing contact-tolerant motion planning (CTMP) methods rely on indirect spatial representations (e.g., prebuilt map, obstacle set), resulting in inaccuracies and a lack of adaptiveness to environmental uncertainties. To address this issue, we propose a direct contact-tolerant (DCT) planner, which integrates vision-language models (VLMs) into direct point perception and navigation, including two key components. The first one is VLM point cloud partitioner (VPP), which performs contact-tolerance reasoning in image space using VLM, caches inference masks, propagates them across frames using odometry, and projects them onto the current scan to generate a contact-aware point cloud. The second innovation is VPP guided navigation (VGN), which formulates CTMP as a perception-to-control optimization problem under direct contact-aware point cloud constraints, which is further solved by a specialized deep neural network (DNN). We implement DCT in Isaac Sim and a real car-like robot, demonstrating that DCT achieves robust and efficient navigation in cluttered environments with movable obstacles, outperforming representative baselines across diverse metrics. The code is available at: https://github.com/ChrisLeeUM/DCT.

