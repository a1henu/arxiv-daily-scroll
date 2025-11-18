---
layout: default
title: OpenRoboCare: A Multimodal Multi-Task Expert Demonstration Dataset for Robot Caregiving
---

# OpenRoboCare: A Multimodal Multi-Task Expert Demonstration Dataset for Robot Caregiving
**arXiv**：[2511.13707v1](https://arxiv.org/abs/2511.13707) · [PDF](https://arxiv.org/pdf/2511.13707.pdf)  
**作者**：Xiaoyu Liang, Ziang Liu, Kelvin Lin, Edward Gu, Ruolin Ye, Tam Nguyen, Cynthia Hsu, Zhanxin Wu, Xiaoman Yang, Christy Sum Yu Cheung, Harold Soh, Katherine Dimitropoulou, Tapomayukh Bhattacharjee  

**一句话要点**：提出OpenRoboCare多模态数据集以解决机器人照护中缺乏专家示范数据的问题

**关键词**：机器人照护, 多模态数据集, 专家示范, 日常活动任务, 物理人机交互, 感知挑战

## 3 点简述
- 核心问题：机器人照护任务缺乏大规模、多样化的专家示范数据集，影响物理人机交互的感知与规划。
- 方法要点：收集21名职业治疗师执行15项日常活动任务的多模态数据，包括RGB-D视频、姿态跟踪等五种模态。
- 实验或效果：评估显示数据集对现有机器人感知和人类活动识别方法构成挑战，提升辅助机器人安全性。

## 摘要（原文）

> We present OpenRoboCare, a multimodal dataset for robot caregiving, capturing expert occupational therapist demonstrations of Activities of Daily Living (ADLs). Caregiving tasks involve complex physical human-robot interactions, requiring precise perception under occlusions, safe physical contact, and long-horizon planning. While recent advances in robot learning from demonstrations have shown promise, there is a lack of a large-scale, diverse, and expert-driven dataset that captures real-world caregiving routines. To address this gap, we collect data from 21 occupational therapists performing 15 ADL tasks on two manikins. The dataset spans five modalities: RGB-D video, pose tracking, eye-gaze tracking, task and action annotations, and tactile sensing, providing rich multimodal insights into caregiver movement, attention, force application, and task execution strategies. We further analyze expert caregiving principles and strategies, offering insights to improve robot efficiency and task feasibility. Additionally, our evaluations demonstrate that OpenRoboCare presents challenges for state-of-the-art robot perception and human activity recognition methods, both critical for developing safe and adaptive assistive robots, highlighting the value of our contribution. See our website for additional visualizations: https://emprise.cs.cornell.edu/robo-care/.

