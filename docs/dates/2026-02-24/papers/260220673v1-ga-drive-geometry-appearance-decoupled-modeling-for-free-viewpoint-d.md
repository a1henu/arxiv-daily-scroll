---
layout: default
title: GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio
---

# GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio
**arXiv**：[2602.20673v1](https://arxiv.org/abs/2602.20673) · [PDF](https://arxiv.org/pdf/2602.20673.pdf)  
**作者**：Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  

**一句话要点**：提出GA-Drive框架，通过几何-外观解耦与扩散生成实现自由视点驾驶场景模拟。

**关键词**：驾驶场景生成, 几何-外观解耦, 扩散模型, 自由视点模拟, 自动驾驶仿真

## 3 点简述
- 核心问题：自由视点、可编辑、高保真驾驶模拟器对自动驾驶系统训练与评估至关重要。
- 方法要点：基于几何信息合成伪视图，再通过视频扩散模型生成真实感视图，实现几何与外观解耦。
- 实验或效果：在NTA-IoU、NTL-IoU和FID指标上显著优于现有方法，支持外观编辑。

## 摘要（原文）

> A free-viewpoint, editable, and high-fidelity driving simulator is crucial for training and evaluating end-to-end autonomous driving systems. In this paper, we present GA-Drive, a novel simulation framework capable of generating camera views along user-specified novel trajectories through Geometry-Appearance Decoupling and Diffusion-Based Generation. Given a set of images captured along a recorded trajectory and the corresponding scene geometry, GA-Drive synthesizes novel pseudo-views using geometry information. These pseudo-views are then transformed into photorealistic views using a trained video diffusion model. In this way, we decouple the geometry and appearance of scenes. An advantage of such decoupling is its support for appearance editing via state-of-the-art video-to-video editing techniques, while preserving the underlying geometry, enabling consistent edits across both original and novel trajectories. Extensive experiments demonstrate that GA-Drive substantially outperforms existing methods in terms of NTA-IoU, NTL-IoU, and FID scores.

