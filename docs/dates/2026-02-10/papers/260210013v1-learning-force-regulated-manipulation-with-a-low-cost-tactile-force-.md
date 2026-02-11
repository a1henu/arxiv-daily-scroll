---
layout: default
title: Learning Force-Regulated Manipulation with a Low-Cost Tactile-Force-Controlled Gripper
---

# Learning Force-Regulated Manipulation with a Low-Cost Tactile-Force-Controlled Gripper
**arXiv**：[2602.10013v1](https://arxiv.org/abs/2602.10013) · [PDF](https://arxiv.org/pdf/2602.10013.pdf)  
**作者**：Xuhui Kang, Tongxuan Tian, Sung-Wook Lee, Binghao Huang, Yunzhu Li, Yen-Ling Kuo  

**一句话要点**：提出低成本的触觉-力控夹爪与RETAF框架，以解决机器人对日常力敏感物体的精确力控操作问题。

**关键词**：力控操作, 触觉反馈, 低成本夹爪, 机器人抓取, 策略学习

## 3 点简述
- 核心问题：商用夹爪成本高或最小力大，难以用于日常力敏感物体的力控策略学习。
- 方法要点：设计低成本TF-Gripper夹爪，并开发RETAF框架，通过高频触觉反馈解耦力控与姿态预测。
- 实验或效果：在五个真实任务中，RETAF优于基线，显著提升抓取稳定性和任务性能。

## 摘要（原文）

> Successfully manipulating many everyday objects, such as potato chips, requires precise force regulation. Failure to modulate force can lead to task failure or irreversible damage to the objects. Humans can precisely achieve this by adapting force from tactile feedback, even within a short period of physical contact. We aim to give robots this capability. However, commercial grippers exhibit high cost or high minimum force, making them unsuitable for studying force-controlled policy learning with everyday force-sensitive objects. We introduce TF-Gripper, a low-cost (~$150) force-controlled parallel-jaw gripper that integrates tactile sensing as feedback. It has an effective force range of 0.45-45N and is compatible with different robot arms. Additionally, we designed a teleoperation device paired with TF-Gripper to record human-applied grasping forces. While standard low-frequency policies can be trained on this data, they struggle with the reactive, contact-dependent nature of force regulation. To overcome this, we propose RETAF (REactive Tactile Adaptation of Force), a framework that decouples grasping force control from arm pose prediction. RETAF regulates force at high frequency using wrist images and tactile feedback, while a base policy predicts end-effector pose and gripper open/close action. We evaluate TF-Gripper and RETAF across five real-world tasks requiring precise force regulation. Results show that compared to position control, direct force control significantly improves grasp stability and task performance. We further show that tactile feedback is essential for force regulation, and that RETAF consistently outperforms baselines and can be integrated with various base policies. We hope this work opens a path for scaling the learning of force-controlled policies in robotic manipulation. Project page: https://force-gripper.github.io .

