---
layout: default
title: R3ST: A Synthetic 3D Dataset With Realistic Trajectories
---

# R3ST: A Synthetic 3D Dataset With Realistic Trajectories
**arXiv**：[2512.16784v1](https://arxiv.org/abs/2512.16784) · [PDF](https://arxiv.org/pdf/2512.16784.pdf)  
**作者**：Simone Teglia, Claudia Melis Tonti, Francesco Pro, Leonardo Russo, Andrea Alfarano, Leonardo Pentassuglia, Irene Amerini  

**一句话要点**：提出R3ST合成数据集，通过集成真实轨迹解决合成数据中车辆运动不真实的问题。

**关键词**：合成数据集, 车辆轨迹预测, 3D环境生成, 真实轨迹集成, 交通分析

## 3 点简述
- 核心问题：现有合成数据集缺乏真实车辆运动轨迹，影响交通分析模型训练。
- 方法要点：构建合成3D环境，集成来自SinD无人机数据集的人类驾驶真实轨迹。
- 实验或效果：提供精确多模态标注和真实轨迹，推动车辆轨迹预测研究。

## 摘要（原文）

> Datasets are essential to train and evaluate computer vision models used for traffic analysis and to enhance road safety. Existing real datasets fit real-world scenarios, capturing authentic road object behaviors, however, they typically lack precise ground-truth annotations. In contrast, synthetic datasets play a crucial role, allowing for the annotation of a large number of frames without additional costs or extra time. However, a general drawback of synthetic datasets is the lack of realistic vehicle motion, since trajectories are generated using AI models or rule-based systems. In this work, we introduce R3ST (Realistic 3D Synthetic Trajectories), a synthetic dataset that overcomes this limitation by generating a synthetic 3D environment and integrating real-world trajectories derived from SinD, a bird's-eye-view dataset recorded from drone footage. The proposed dataset closes the gap between synthetic data and realistic trajectories, advancing the research in trajectory forecasting of road vehicles, offering both accurate multimodal ground-truth annotations and authentic human-driven vehicle trajectories.

