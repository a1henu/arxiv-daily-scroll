---
layout: default
title: SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling
---

# SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling
**arXiv**：[2512.23162v1](https://arxiv.org/abs/2512.23162) · [PDF](https://arxiv.org/pdf/2512.23162.pdf)  
**作者**：Yufan He, Pengfei Guo, Mengya Xu, Zhaoshuo Li, Andriy Myronenko, Dillan Imans, Bingjie Liu, Dongren Yang, Mingxue Gu, Yongnan Ji, Yueming Jin, Ren Zhao, Baiyong Shen, Daguang Xu  

**一句话要点**：提出SurgWorld世界模型，通过生成合成手术视频和伪运动学数据，解决手术机器人数据稀缺问题。

**关键词**：手术机器人, 世界建模, 视频生成, 逆动力学模型, 视觉语言动作模型, 数据增强

## 3 点简述
- 核心问题：手术机器人缺乏带动作标签的视觉-动作配对数据，阻碍模仿学习和VLA模型训练。
- 方法要点：构建SATA数据集和SurgWorld世界模型，生成合成手术视频，并利用逆动力学模型推断伪运动学数据。
- 实验或效果：在真实手术机器人平台上，使用增强数据训练的VLA策略显著优于仅基于真实演示的模型。

## 摘要（原文）

> Data scarcity remains a fundamental barrier to achieving fully autonomous surgical robots. While large scale vision language action (VLA) models have shown impressive generalization in household and industrial manipulation by leveraging paired video action data from diverse domains, surgical robotics suffers from the paucity of datasets that include both visual observations and accurate robot kinematics. In contrast, vast corpora of surgical videos exist, but they lack corresponding action labels, preventing direct application of imitation learning or VLA training. In this work, we aim to alleviate this problem by learning policy models from SurgWorld, a world model designed for surgical physical AI. We curated the Surgical Action Text Alignment (SATA) dataset with detailed action description specifically for surgical robots. Then we built SurgeWorld based on the most advanced physical AI world model and SATA. It's able to generate diverse, generalizable and realistic surgery videos. We are also the first to use an inverse dynamics model to infer pseudokinematics from synthetic surgical videos, producing synthetic paired video action data. We demonstrate that a surgical VLA policy trained with these augmented data significantly outperforms models trained only on real demonstrations on a real surgical robot platform. Our approach offers a scalable path toward autonomous surgical skill acquisition by leveraging the abundance of unlabeled surgical video and generative world modeling, thus opening the door to generalizable and data efficient surgical robot policies.

