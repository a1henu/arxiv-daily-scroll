---
layout: default
title: Masked Registration and Autoencoding of CT Images for Predictive Tibia Reconstruction
---

# Masked Registration and Autoencoding of CT Images for Predictive Tibia Reconstruction
**arXiv**：[2512.09525v1](https://arxiv.org/abs/2512.09525) · [PDF](https://arxiv.org/pdf/2512.09525.pdf)  
**作者**：Hongyou Zhou, Cederic Aßmann, Alaa Bejaoui, Heiko Tzschätzsch, Mark Heyland, Julian Zierke, Niklas Tuttle, Sebastian Hölzl, Timo Auer, David A. Back, Marc Toussaint  

**一句话要点**：提出结合掩码注册与自编码的CT图像方法，以预测胫骨重建目标

**关键词**：CT图像处理, 神经注册, 自编码器, 胫骨重建, 掩码输入, 手术规划

## 3 点简述
- 核心问题：复杂胫骨骨折手术规划中，难以想象健康骨对齐的3D结构。
- 方法要点：使用改进的空间变换网络进行CT注册，结合自编码器建模健康胫骨变异，并处理掩码输入。
- 实验或效果：通过掩码输入预测患者特异性健康骨结构，项目页面提供代码。

## 摘要（原文）

> Surgical planning for complex tibial fractures can be challenging for surgeons, as the 3D structure of the later desirable bone alignment may be diffi- cult to imagine. To assist in such planning, we address the challenge of predicting a patient-specific reconstruction target from a CT of the fractured tibia. Our ap- proach combines neural registration and autoencoder models. Specifically, we first train a modified spatial transformer network (STN) to register a raw CT to a standardized coordinate system of a jointly trained tibia prototype. Subsequently, various autoencoder (AE) architectures are trained to model healthy tibial varia- tions. Both the STN and AE models are further designed to be robust to masked input, allowing us to apply them to fractured CTs and decode to a prediction of the patient-specific healthy bone in standard coordinates. Our contributions include: i) a 3D-adapted STN for global spatial registration, ii) a comparative analysis of AEs for bone CT modeling, and iii) the extension of both to handle masked inputs for predictive generation of healthy bone structures. Project page: https://github.com/HongyouZhou/repair

