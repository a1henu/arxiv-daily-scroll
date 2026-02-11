---
layout: default
title: EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration
---

# EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration
**arXiv**：[2602.10106v1](https://arxiv.org/abs/2602.10106) · [PDF](https://arxiv.org/pdf/2602.10106.pdf)  
**作者**：Modi Shi, Shijia Peng, Jin Chen, Haoran Jiang, Yinghui Li, Di Huang, Ping Luo, Hongyang Li, Li Chen  

**一句话要点**：提出EgoHumanoid框架，利用人类第一人称演示与少量机器人数据协同训练，实现人形机器人在真实环境中的移动操作。

**关键词**：人形机器人移动操作, 第一人称演示, 视点对齐, 动作对齐, 真实世界实验, 数据收集系统

## 3 点简述
- 核心问题：人形机器人移动操作数据稀缺，人类演示与机器人形态差异大，难以直接应用。
- 方法要点：通过视点对齐和动作对齐，桥接人类与机器人间的形态和视角差异，构建可扩展的人类数据收集系统。
- 实验或效果：在真实世界实验中，结合人类数据比仅用机器人数据性能提升51%，尤其在未见环境中表现突出。

## 摘要（原文）

> Human demonstrations offer rich environmental diversity and scale naturally, making them an appealing alternative to robot teleoperation. While this paradigm has advanced robot-arm manipulation, its potential for the more challenging, data-hungry problem of humanoid loco-manipulation remains largely unexplored. We present EgoHumanoid, the first framework to co-train a vision-language-action policy using abundant egocentric human demonstrations together with a limited amount of robot data, enabling humanoids to perform loco-manipulation across diverse real-world environments. To bridge the embodiment gap between humans and robots, including discrepancies in physical morphology and viewpoint, we introduce a systematic alignment pipeline spanning from hardware design to data processing. A portable system for scalable human data collection is developed, and we establish practical collection protocols to improve transferability. At the core of our human-to-humanoid alignment pipeline lies two key components. The view alignment reduces visual domain discrepancies caused by camera height and perspective variation. The action alignment maps human motions into a unified, kinematically feasible action space for humanoid control. Extensive real-world experiments demonstrate that incorporating robot-free egocentric data significantly outperforms robot-only baselines by 51\%, particularly in unseen environments. Our analysis further reveals which behaviors transfer effectively and the potential for scaling human data.

