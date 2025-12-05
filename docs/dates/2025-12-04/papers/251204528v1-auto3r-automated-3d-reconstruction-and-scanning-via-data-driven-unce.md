---
layout: default
title: Auto3R: Automated 3D Reconstruction and Scanning via Data-driven Uncertainty Quantification
---

# Auto3R: Automated 3D Reconstruction and Scanning via Data-driven Uncertainty Quantification
**arXiv**：[2512.04528v1](https://arxiv.org/abs/2512.04528) · [PDF](https://arxiv.org/pdf/2512.04528.pdf)  
**作者**：Chentao Shen, Sizhe Zheng, Bingqian Wu, Yaohua Feng, Yuanchen Fei, Mingyu Mei, Hanwen Jiang, Xiangru Huang  

**一句话要点**：提出Auto3R以自动化3D扫描与重建，通过数据驱动的不确定性量化优化视角规划。

**关键词**：3D重建, 自动化扫描, 不确定性量化, 数据驱动模型, 机器人视觉, 数字资产生成

## 3 点简述
- 核心问题：传统高质量3D扫描依赖人工规划视角，自动化需求增长但面临非朗伯和镜面材质挑战。
- 方法要点：基于数据驱动的不确定性量化模型，在迭代重建中预测扫描视角的不确定性分布，无需真实几何和外观信息。
- 实验或效果：实验显示性能大幅超越现有方法，并在机器人臂上部署，有效数字化真实物体生成逼真数字资产。

## 摘要（原文）

> Traditional high-quality 3D scanning and reconstruction typically relies on human labor to plan the scanning procedure. With the rapid development of embodied systems such as drones and robots, there is a growing demand of performing accurate 3D scanning and reconstruction in an fully automated manner. We introduce Auto3R, a data-driven uncertainty quantification model that is designed to automate the 3D scanning and reconstruction of scenes and objects, including objects with non-lambertian and specular materials. Specifically, in a process of iterative 3D reconstruction and scanning, Auto3R can make efficient and accurate prediction of uncertainty distribution over potential scanning viewpoints, without knowing the ground truth geometry and appearance. Through extensive experiments, Auto3R achieves superior performance that outperforms the state-of-the-art methods by a large margin. We also deploy Auto3R on a robot arm equipped with a camera and demonstrate that Auto3R can be used to effectively digitize real-world 3D objects and delivers ready-to-use and photorealistic digital assets. Our homepage: https://tomatoma00.github.io/auto3r.github.io .

