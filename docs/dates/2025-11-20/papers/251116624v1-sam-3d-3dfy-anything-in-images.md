---
layout: default
title: SAM 3D: 3Dfy Anything in Images
---

# SAM 3D: 3Dfy Anything in Images
**arXiv**：[2511.16624v1](https://arxiv.org/abs/2511.16624) · [PDF](https://arxiv.org/pdf/2511.16624.pdf)  
**作者**：SAM 3D Team, Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang, Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, Aohan Lin, Jiawei Liu, Ziqi Ma, Anushka Sagar, Bowen Song, Xiaodong Wang, Jianing Yang, Bowen Zhang, Piotr Dollár, Georgia Gkioxari, Matt Feiszli, Jitendra Malik  

**一句话要点**：提出SAM 3D模型，从单张图像生成3D对象重建，适用于自然场景。

**关键词**：3D对象重建, 单图像生成, 视觉基础数据, 多阶段训练, 自然场景处理

## 3 点简述
- 核心问题：从单张图像重建3D对象，处理遮挡和场景杂乱。
- 方法要点：结合人工和模型标注，大规模数据训练，多阶段框架。
- 实验或效果：人类偏好测试中胜率至少5:1，优于近期工作。

## 摘要（原文）

> We present SAM 3D, a generative model for visually grounded 3D object reconstruction, predicting geometry, texture, and layout from a single image. SAM 3D excels in natural images, where occlusion and scene clutter are common and visual recognition cues from context play a larger role. We achieve this with a human- and model-in-the-loop pipeline for annotating object shape, texture, and pose, providing visually grounded 3D reconstruction data at unprecedented scale. We learn from this data in a modern, multi-stage training framework that combines synthetic pretraining with real-world alignment, breaking the 3D "data barrier". We obtain significant gains over recent work, with at least a 5:1 win rate in human preference tests on real-world objects and scenes. We will release our code and model weights, an online demo, and a new challenging benchmark for in-the-wild 3D object reconstruction.

