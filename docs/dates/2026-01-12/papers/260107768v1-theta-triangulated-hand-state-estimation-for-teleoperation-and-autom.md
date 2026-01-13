---
layout: default
title: THETA: Triangulated Hand-State Estimation for Teleoperation and Automation in Robotic Hand Control
---

# THETA: Triangulated Hand-State Estimation for Teleoperation and Automation in Robotic Hand Control
**arXiv**：[2601.07768v1](https://arxiv.org/abs/2601.07768) · [PDF](https://arxiv.org/pdf/2601.07768.pdf)  
**作者**：Alex Huang, Akshay Karthik  

**一句话要点**：提出基于三摄像头三角测量的手部状态估计方法THETA，用于低成本机器人手遥操作与自动化控制。

**关键词**：手部状态估计, 三角测量跟踪, 低成本遥操作, 机器人手控制, 多视角分割, 关节角度分类

## 3 点简述
- 核心问题：机器人手遥操作依赖昂贵深度相机或传感器手套，成本高。
- 方法要点：使用三个网络摄像头三角化跟踪，估计手指相对关节角度，结合分割与分类模型。
- 实验或效果：在40种手势数据集上，分类准确率达97.18%，实时控制低成本机器人手DexHand。

## 摘要（原文）

> The teleoperation of robotic hands is limited by the high costs of depth cameras and sensor gloves, commonly used to estimate hand relative joint positions (XYZ). We present a novel, cost-effective approach using three webcams for triangulation-based tracking to approximate relative joint angles (theta) of human fingers. We also introduce a modified DexHand, a low-cost robotic hand from TheRobotStudio, to demonstrate THETA's real-time application. Data collection involved 40 distinct hand gestures using three 640x480p webcams arranged at 120-degree intervals, generating over 48,000 RGB images. Joint angles were manually determined by measuring midpoints of the MCP, PIP, and DIP finger joints. Captured RGB frames were processed using a DeepLabV3 segmentation model with a ResNet-50 backbone for multi-scale hand segmentation. The segmented images were then HSV-filtered and fed into THETA's architecture, consisting of a MobileNetV2-based CNN classifier optimized for hierarchical spatial feature extraction and a 9-channel input tensor encoding multi-perspective hand representations. The classification model maps segmented hand views into discrete joint angles, achieving 97.18% accuracy, 98.72% recall, F1 Score of 0.9274, and a precision of 0.8906. In real-time inference, THETA captures simultaneous frames, segments hand regions, filters them, and compiles a 9-channel tensor for classification. Joint-angle predictions are relayed via serial to an Arduino, enabling the DexHand to replicate hand movements. Future research will increase dataset diversity, integrate wrist tracking, and apply computer vision techniques such as OpenAI-Vision. THETA potentially ensures cost-effective, user-friendly teleoperation for medical, linguistic, and manufacturing applications.

