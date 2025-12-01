---
layout: default
title: RobotSeg: A Model and Dataset for Segmenting Robots in Image and Video
---

# RobotSeg: A Model and Dataset for Segmenting Robots in Image and Video
**arXiv**：[2511.22950v1](https://arxiv.org/abs/2511.22950) · [PDF](https://arxiv.org/pdf/2511.22950.pdf)  
**作者**：Haiyang Mei, Qiming Huang, Hai Ci, Mike Zheng Shou  

**一句话要点**：提出RobotSeg模型与VRS数据集，以解决机器人分割中的结构复杂性和标注效率问题。

**关键词**：机器人分割, 基础模型, 视频数据集, 结构感知, 自动提示, 高效标注

## 3 点简述
- 核心问题：机器人分割因形态多样、结构复杂和快速变化而具挑战性。
- 方法要点：基于SAM 2改进，引入结构增强记忆关联器、机器人提示生成器和高效标注训练策略。
- 实验或效果：在图像和视频上实现最先进性能，构建包含2.8k视频的数据集。

## 摘要（原文）

> Accurate robot segmentation is a fundamental capability for robotic perception. It enables precise visual servoing for VLA systems, scalable robot-centric data augmentation, accurate real-to-sim transfer, and reliable safety monitoring in dynamic human-robot environments. Despite the strong capabilities of modern segmentation models, surprisingly it remains challenging to segment robots. This is due to robot embodiment diversity, appearance ambiguity, structural complexity, and rapid shape changes. Embracing these challenges, we introduce RobotSeg, a foundation model for robot segmentation in image and video. RobotSeg is built upon the versatile SAM 2 foundation model but addresses its three limitations for robot segmentation, namely the lack of adaptation to articulated robots, reliance on manual prompts, and the need for per-frame training mask annotations, by introducing a structure-enhanced memory associator, a robot prompt generator, and a label-efficient training strategy. These innovations collectively enable a structure-aware, automatic, and label-efficient solution. We further construct the video robot segmentation (VRS) dataset comprising over 2.8k videos (138k frames) with diverse robot embodiments and environments. Extensive experiments demonstrate that RobotSeg achieves state-of-the-art performance on both images and videos, establishing a strong foundation for future advances in robot perception.

