---
layout: default
title: REFA: Real-time Egocentric Facial Animations for Virtual Reality
---

# REFA: Real-time Egocentric Facial Animations for Virtual Reality
**arXiv**：[2601.03507v1](https://arxiv.org/abs/2601.03507) · [PDF](https://arxiv.org/pdf/2601.03507.pdf)  
**作者**：Qiang Zhang, Tong Xiao, Haroun Habeeb, Larissa Laich, Sofien Bouaziz, Patrick Snape, Wenjing Zhang, Matthew Cioffi, Peizhao Zhang, Pavel Pidlypenskyi, Winnie Lin, Luming Ma, Mengjiao Wang, Kunpeng Li, Chengjiang Long, Steven Song, Martin Prazak, Alexander Sjoholm, Ajinkya Deogade, Jaebong Lee, Julio Delgado Mangas, Amaury Aubel  

**一句话要点**：提出REFA系统，通过头戴式红外摄像头实时追踪面部表情，驱动虚拟角色表情，无需繁琐校准。

**关键词**：实时面部动画, 虚拟现实, 蒸馏训练, 可微分渲染, 红外摄像头, 表情追踪

## 3 点简述
- 核心问题：虚拟现实中实时、非侵入式面部表情追踪，以增强虚拟环境中的沟通与表达。
- 方法要点：基于蒸馏方法训练机器学习模型，利用合成与真实图像等多源异构数据，结合可微分渲染管道自动提取标签。
- 实验或效果：收集18k多样本数据集，系统在视频会议、游戏等应用中实现准确表情驱动，提升用户体验。

## 摘要（原文）

> We present a novel system for real-time tracking of facial expressions using egocentric views captured from a set of infrared cameras embedded in a virtual reality (VR) headset. Our technology facilitates any user to accurately drive the facial expressions of virtual characters in a non-intrusive manner and without the need of a lengthy calibration step. At the core of our system is a distillation based approach to train a machine learning model on heterogeneous data and labels coming form multiple sources, \eg synthetic and real images. As part of our dataset, we collected 18k diverse subjects using a lightweight capture setup consisting of a mobile phone and a custom VR headset with extra cameras. To process this data, we developed a robust differentiable rendering pipeline enabling us to automatically extract facial expression labels. Our system opens up new avenues for communication and expression in virtual environments, with applications in video conferencing, gaming, entertainment, and remote collaboration.

