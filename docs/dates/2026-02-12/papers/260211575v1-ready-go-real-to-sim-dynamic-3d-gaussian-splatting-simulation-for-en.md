---
layout: default
title: ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles
---

# ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles
**arXiv**：[2602.11575v1](https://arxiv.org/abs/2602.11575) · [PDF](https://arxiv.org/pdf/2602.11575.pdf)  
**作者**：Seungyeon Yoo, Youngseok Jang, Dabin Kim, Youngsoo Han, Seungwoo Jung, H. Jin Kim  

**一句话要点**：提出ReaDy-Go以解决动态环境中视觉导航的仿真到现实差距问题

**关键词**：视觉导航, 3D高斯溅射, 仿真到现实, 动态环境, 数据集生成, 策略学习

## 3 点简述
- 视觉导航模型在动态环境中因仿真到现实差距和定制化训练困难而表现不佳
- ReaDy-Go结合静态3D高斯溅射场景与动态人体障碍，生成逼真动态导航数据集
- 在仿真和真实实验中优于基线，展示出泛化潜力

## 摘要（原文）

> Visual navigation models often struggle in real-world dynamic environments due to limited robustness to the sim-to-real gap and the difficulty of training policies tailored to target deployment environments (e.g., households, restaurants, and factories). Although real-to-sim navigation simulation using 3D Gaussian Splatting (GS) can mitigate this gap, prior works have assumed only static scenes or unrealistic dynamic obstacles, despite the importance of safe navigation in dynamic environments. To address these issues, we propose ReaDy-Go, a novel real-to-sim simulation pipeline that synthesizes photorealistic dynamic scenarios for target environments. ReaDy-Go generates photorealistic navigation datasets for dynamic environments by combining a reconstructed static GS scene with dynamic human GS obstacles, and trains policies robust to both the sim-to-real gap and moving obstacles. The pipeline consists of three components: (1) a dynamic GS simulator that integrates scene GS with a human animation module, enabling the insertion of animatable human GS avatars and the synthesis of plausible human motions from 2D trajectories, (2) navigation dataset generation for dynamic environments that leverages the simulator, a robot expert planner designed for dynamic GS representations, and a human planner, and (3) policy learning using the generated datasets. ReaDy-Go outperforms baselines across target environments in both simulation and real-world experiments, demonstrating improved navigation performance even after sim-to-real transfer and in the presence of moving obstacles. Moreover, zero-shot sim-to-real deployment in an unseen environment indicates its generalization potential. Project page: https://syeon-yoo.github.io/ready-go-site/.

