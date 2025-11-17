---
layout: default
title: 6D Strawberry Pose Estimation: Real-time and Edge AI Solutions Using Purely Synthetic Training Data
---

# 6D Strawberry Pose Estimation: Real-time and Edge AI Solutions Using Purely Synthetic Training Data
**arXiv**：[2511.11307v1](https://arxiv.org/abs/2511.11307) · [PDF](https://arxiv.org/pdf/2511.11307.pdf)  
**作者**：Saptarshi Neil Sinha, Julius Kühn, Mika Silvan Goschke, Michael Weinmann  

**一句话要点**：提出基于纯合成数据的草莓6D姿态估计方法，用于农业自动化采摘。

**关键词**：6D姿态估计, 合成数据训练, 农业机器人, YOLOX算法, 边缘AI

## 3 点简述
- 核心问题：农业自动化中草莓采摘面临高成本和劳动力短缺，需精确姿态估计。
- 方法要点：使用YOLOX-6D-Pose算法和Blender流程生成逼真合成数据训练模型。
- 实验或效果：在RTX 3090和Jetson Orin Nano上实现高精度，适合边缘部署。

## 摘要（原文）

> Automated and selective harvesting of fruits has become an important area of research, particularly due to challenges such as high costs and a shortage of seasonal labor in advanced economies. This paper focuses on 6D pose estimation of strawberries using purely synthetic data generated through a procedural pipeline for photorealistic rendering. We employ the YOLOX-6D-Pose algorithm, a single-shot approach that leverages the YOLOX backbone, known for its balance between speed and accuracy, and its support for edge inference. To address the lacking availability of training data, we introduce a robust and flexible pipeline for generating synthetic strawberry data from various 3D models via a procedural Blender pipeline, where we focus on enhancing the realism of the synthesized data in comparison to previous work to make it a valuable resource for training pose estimation algorithms. Quantitative evaluations indicate that our models achieve comparable accuracy on both the NVIDIA RTX 3090 and Jetson Orin Nano across several ADD-S metrics, with the RTX 3090 demonstrating superior processing speed. However, the Jetson Orin Nano is particularly suited for resource-constrained environments, making it an excellent choice for deployment in agricultural robotics. Qualitative assessments further confirm the model's performance, demonstrating its capability to accurately infer the poses of ripe and partially ripe strawberries, while facing challenges in detecting unripe specimens. This suggests opportunities for future improvements, especially in enhancing detection capabilities for unripe strawberries (if desired) by exploring variations in color. Furthermore, the methodology presented could be adapted easily for other fruits such as apples, peaches, and plums, thereby expanding its applicability and impact in the field of agricultural automation.

