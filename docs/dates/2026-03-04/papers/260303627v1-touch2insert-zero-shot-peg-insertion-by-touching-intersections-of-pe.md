---
layout: default
title: Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole
---

# Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole
**arXiv**：[2603.03627v1](https://arxiv.org/abs/2603.03627) · [PDF](https://arxiv.org/pdf/2603.03627.pdf)  
**作者**：Masaru Yajima, Yuma Shin, Rei Kawakami, Asako Kanezaki, Kei Ota  

**一句话要点**：提出Touch2Insert框架，利用触觉感知实现零样本任意形状插接，解决工业连接器插入中的精度与泛化挑战。

**关键词**：触觉感知, 零样本学习, 机器人插接, 几何重建, 位姿估计

## 3 点简述
- 核心问题：工业连接器插入需亚毫米精度，视觉方法易受遮挡限制，学习策略泛化性差。
- 方法要点：基于高分辨率触觉图像重建截面几何，通过配准估计孔相对位姿，无需任务特定训练。
- 实验或效果：仿真中位姿估计达亚毫米精度，真实机器人平均成功率86.7%，验证了鲁棒性与泛化性。

## 摘要（原文）

> Reliable insertion of industrial connectors remains a central challenge in robotics, requiring sub-millimeter precision under uncertainty and often without full visual access. Vision-based approaches struggle with occlusion and limited generalization, while learning-based policies frequently fail to transfer to unseen geometries. To address these limitations, we leverage tactile sensing, which captures local surface geometry at the point of contact and thus provides reliable information even under occlusion and across novel connector shapes. Building on this capability, we present \emph{Touch2Insert}, a tactile-based framework for arbitrary peg insertion. Our method reconstructs cross-sectional geometry from high-resolution tactile images and estimates the relative pose of the hole with respect to the peg in a zero-shot manner. By aligning reconstructed shapes through registration, the framework enables insertion from a single contact without task-specific training. To evaluate its performance, we conducted experiments with three diverse connectors in both simulation and real-robot settings. The results indicate that Touch2Insert achieved sub-millimeter pose estimation accuracy for all connectors in simulation, and attained an average success rate of 86.7\% on the real robot, thereby confirming the robustness and generalizability of tactile sensing for real-world robotic connector insertion.

