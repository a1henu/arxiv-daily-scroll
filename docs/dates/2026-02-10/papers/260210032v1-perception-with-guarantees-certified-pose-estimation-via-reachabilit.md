---
layout: default
title: Perception with Guarantees: Certified Pose Estimation via Reachability Analysis
---

# Perception with Guarantees: Certified Pose Estimation via Reachability Analysis
**arXiv**：[2602.10032v1](https://arxiv.org/abs/2602.10032) · [PDF](https://arxiv.org/pdf/2602.10032.pdf)  
**作者**：Tobias Ladner, Yasser Shoukry, Matthias Althoff  

**一句话要点**：提出基于可达性分析和形式化神经网络验证的认证姿态估计方法，以解决安全关键系统中仅凭相机图像和已知目标几何的3D姿态定位问题。

**关键词**：认证姿态估计, 可达性分析, 形式化神经网络验证, 安全关键系统, 3D姿态定位, 相机图像处理

## 3 点简述
- 核心问题：安全关键系统中姿态估计需保证最坏情况下的安全性，但现有方法依赖外部服务或提供粗略估计，缺乏形式化保证。
- 方法要点：利用可达性分析和形式化神经网络验证，从相机图像和已知目标几何中计算并形式化边界姿态，实现认证姿态估计。
- 实验或效果：在合成和真实世界实验中，该方法能高效且准确地定位智能体，验证了其有效性和实用性。

## 摘要（原文）

> Agents in cyber-physical systems are increasingly entrusted with safety-critical tasks. Ensuring safety of these agents often requires localizing the pose for subsequent actions. Pose estimates can, e.g., be obtained from various combinations of lidar sensors, cameras, and external services such as GPS. Crucially, in safety-critical domains, a rough estimate is insufficient to formally determine safety, i.e., guaranteeing safety even in the worst-case scenario, and external services might additionally not be trustworthy. We address this problem by presenting a certified pose estimation in 3D solely from a camera image and a well-known target geometry. This is realized by formally bounding the pose, which is computed by leveraging recent results from reachability analysis and formal neural network verification. Our experiments demonstrate that our approach efficiently and accurately localizes agents in both synthetic and real-world experiments.

