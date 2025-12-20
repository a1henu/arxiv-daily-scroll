---
layout: default
title: GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation
---

# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation
**arXiv**：[2512.16811v1](https://arxiv.org/abs/2512.16811) · [PDF](https://arxiv.org/pdf/2512.16811.pdf)  
**作者**：Jingjing Qian, Boyao Han, Chen Shi, Lei Xiao, Long Yang, Shaoshuai Shi, Li Jiang  

**一句话要点**：提出GeoPredict框架，通过预测运动学和3D几何先验增强VLA模型，以解决精确3D操作任务中的不可靠性问题。

**关键词**：视觉-语言-动作模型, 3D几何预测, 机器人操作, 运动学先验, 高斯几何, 轨迹预测

## 3 点简述
- 核心问题：现有VLA模型在机器人操作中多为反应式和2D中心化，在需要精确3D推理的任务中不可靠。
- 方法要点：引入轨迹级模块预测机器人手臂的3D关键点轨迹，以及预测性3D高斯几何模块沿轨迹预测工作空间几何。
- 实验或效果：在RoboCasa Human-50、LIBERO和真实世界任务中，GeoPredict优于基线，尤其在几何密集和空间要求高的场景。

## 摘要（原文）

> Vision-Language-Action (VLA) models achieve strong generalization in robotic manipulation but remain largely reactive and 2D-centric, making them unreliable in tasks that require precise 3D reasoning. We propose GeoPredict, a geometry-aware VLA framework that augments a continuous-action policy with predictive kinematic and geometric priors. GeoPredict introduces a trajectory-level module that encodes motion history and predicts multi-step 3D keypoint trajectories of robot arms, and a predictive 3D Gaussian geometry module that forecasts workspace geometry with track-guided refinement along future keypoint trajectories. These predictive modules serve exclusively as training-time supervision through depth-based rendering, while inference requires only lightweight additional query tokens without invoking any 3D decoding. Experiments on RoboCasa Human-50, LIBERO, and real-world manipulation tasks show that GeoPredict consistently outperforms strong VLA baselines, especially in geometry-intensive and spatially demanding scenarios.

