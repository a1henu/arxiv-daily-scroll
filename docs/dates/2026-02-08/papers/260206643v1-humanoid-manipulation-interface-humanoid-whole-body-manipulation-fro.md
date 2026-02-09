---
layout: default
title: Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations
---

# Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations
**arXiv**：[2602.06643v1](https://arxiv.org/abs/2602.06643) · [PDF](https://arxiv.org/pdf/2602.06643.pdf)  
**作者**：Ruiqian Nai, Boyuan Zheng, Junming Zhao, Haodong Zhu, Sicong Dai, Zunhao Chen, Yihang Hu, Yingdong Hu, Tong Zhang, Chuan Wen, Yang Gao  

**一句话要点**：提出Humanoid Manipulation Interface，通过便携硬件采集人体运动数据，学习人形机器人全身操控技能。

**关键词**：人形机器人操控, 全身运动学习, 数据采集框架, 分层学习管道, 机器人技能迁移

## 3 点简述
- 当前人形机器人全身操控方法依赖遥操作或视觉模拟到真实强化学习，存在硬件限制和奖励工程复杂问题。
- HuMI框架使用便携硬件采集人体全身运动数据，驱动分层学习管道，将人类动作转化为灵巧可行的人形机器人技能。
- 在五个全身任务实验中，HuMI数据采集效率比遥操作提高3倍，在未见环境中达到70%成功率。

## 摘要（原文）

> Current approaches for humanoid whole-body manipulation, primarily relying on teleoperation or visual sim-to-real reinforcement learning, are hindered by hardware logistics and complex reward engineering. Consequently, demonstrated autonomous skills remain limited and are typically restricted to controlled environments. In this paper, we present the Humanoid Manipulation Interface (HuMI), a portable and efficient framework for learning diverse whole-body manipulation tasks across various environments. HuMI enables robot-free data collection by capturing rich whole-body motion using portable hardware. This data drives a hierarchical learning pipeline that translates human motions into dexterous and feasible humanoid skills. Extensive experiments across five whole-body tasks--including kneeling, squatting, tossing, walking, and bimanual manipulation--demonstrate that HuMI achieves a 3x increase in data collection efficiency compared to teleoperation and attains a 70% success rate in unseen environments.

