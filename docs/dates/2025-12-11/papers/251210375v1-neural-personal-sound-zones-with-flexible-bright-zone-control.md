---
layout: default
title: Neural personal sound zones with flexible bright zone control
---

# Neural personal sound zones with flexible bright zone control
**arXiv**：[2512.10375v1](https://arxiv.org/abs/2512.10375) · [PDF](https://arxiv.org/pdf/2512.10375.pdf)  
**作者**：Wenye Zhu, Jun Tang, Xiaofei Li  

**一句话要点**：提出基于3D卷积神经网络的个人声区系统，实现灵活控制点网格与替代重建目标

**关键词**：个人声区, 3D卷积神经网络, 声场控制, 灵活控制点, 虚拟现实, 声学信号处理

## 3 点简述
- 传统个人声区系统需固定接收阵列测量重建目标，不便且成本高
- 方法使用3D CNN，以虚拟目标场景为输入，输出个人声区预滤波器
- 实验表明，单次训练即可处理灵活控制点网格的多种重建目标

## 摘要（原文）

> Personal sound zone (PSZ) reproduction system, which attempts to create distinct virtual acoustic scenes for different listeners at their respective positions within the same spatial area using one loudspeaker array, is a fundamental technology in the application of virtual reality. For practical applications, the reconstruction targets must be measured on the same fixed receiver array used to record the local room impulse responses (RIRs) from the loudspeaker array to the control points in each PSZ, which makes the system inconvenient and costly for real-world use. In this paper, a 3D convolutional neural network (CNN) designed for PSZ reproduction with flexible control microphone grid and alternative reproduction target is presented, utilizing the virtual target scene as inputs and the PSZ pre-filters as output. Experimental results of the proposed method are compared with the traditional method, demonstrating that the proposed method is able to handle varied reproduction targets on flexible control point grid using only one training session. Furthermore, the proposed method also demonstrates the capability to learn global spatial information from sparse sampling points distributed in PSZs.

