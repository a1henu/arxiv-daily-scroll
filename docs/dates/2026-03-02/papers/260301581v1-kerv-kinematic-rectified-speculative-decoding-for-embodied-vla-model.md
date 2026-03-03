---
layout: default
title: KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models
---

# KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models
**arXiv**：[2603.01581v1](https://arxiv.org/abs/2603.01581) · [PDF](https://arxiv.org/pdf/2603.01581.pdf)  
**作者**：Zihao Zheng, Zhihao Mao, Maoliang Li, Jiayu Chen, Xinhao Sun, Zhaobo Zhang, Donggang Cao, Hong Mei, Xiang Chen  

**一句话要点**：提出KERV框架，结合运动学预测优化视觉-语言-动作模型的推测解码，以提升推理速度

**关键词**：视觉-语言-动作模型, 推测解码, 运动学预测, 卡尔曼滤波器, 机器人控制, 推理加速

## 3 点简述
- 核心问题：视觉-语言-动作模型推理慢，推测解码中重推理成本高且阈值调整难
- 方法要点：使用基于运动学的卡尔曼滤波器预测动作补偿错误，避免重推理；动态调整接受阈值
- 实验或效果：在多样任务中实现27%~37%加速，成功率几乎无损失

## 摘要（原文）

> Vision-Language-Action (VLA) models build a token-domain robot control paradigm, yet suffer from low speed. Speculative Decoding (SD) is an optimization strategy that can boost inference speed. Two key issues emerge when integrating VLA and SD: first, SD relies on re-inference to address token errors, which is computationally expensive; second, to mitigate token errors, the acceptance threshold in SD requires careful adjustment. Existing works fail to address the above two issues effectively. Meanwhile, as the bridge between AI and the physical world, existing embodied intelligence has overlooked the application of robotic kinematics. To address these issues, we innovatively combine token-domain VLA models with kinematic-domain prediction for SD, proposing a kinematic-rectified SD framework named KERV. We employ a kinematics-based Kalman Filter to predict actions and compensate for SD errors, avoiding costly re-inference. Moreover, we design a kinematics-based adjustment strategy to dynamically rectify the acceptance threshold, addressing the difficulty of threshold determination. Experimental results across diverse tasks and environments demonstrate that KERV achieves 27%~37% acceleration with nearly no Success Rate loss.

