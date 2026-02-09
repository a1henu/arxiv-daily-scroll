---
layout: default
title: Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels
---

# Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels
**arXiv**：[2602.06382v1](https://arxiv.org/abs/2602.06382) · [PDF](https://arxiv.org/pdf/2602.06382.pdf)  
**作者**：Wandong Sun, Yongbo Su, Leoric Huang, Alex Zhang, Dwyane Wei, Mu San, Daniel Tian, Ellie Cao, Finn Yan, Ethan Xie, Zongwu Xie  

**一句话要点**：提出端到端框架以解决基于视觉的人形机器人运动中的模拟到现实差距和多样化地形适应问题。

**关键词**：人形机器人运动, 端到端学习, 模拟到现实迁移, 深度传感器模拟, 行为蒸馏, 地形适应

## 3 点简述
- 核心问题：模拟到现实差距导致感知噪声，多样化地形训练存在目标冲突。
- 方法要点：开发高保真深度传感器模拟，结合视觉感知行为蒸馏和多判别器学习。
- 实验或效果：在配备不同立体深度相机的人形平台上验证，实现跨环境稳健性能。

## 摘要（原文）

> Achieving robust vision-based humanoid locomotion remains challenging due to two fundamental issues: the sim-to-real gap introduces significant perception noise that degrades performance on fine-grained tasks, and training a unified policy across diverse terrains is hindered by conflicting learning objectives. To address these challenges, we present an end-to-end framework for vision-driven humanoid locomotion. For robust sim-to-real transfer, we develop a high-fidelity depth sensor simulation that captures stereo matching artifacts and calibration uncertainties inherent in real-world sensing. We further propose a vision-aware behavior distillation approach that combines latent space alignment with noise-invariant auxiliary tasks, enabling effective knowledge transfer from privileged height maps to noisy depth observations. For versatile terrain adaptation, we introduce terrain-specific reward shaping integrated with multi-critic and multi-discriminator learning, where dedicated networks capture the distinct dynamics and motion priors of each terrain type. We validate our approach on two humanoid platforms equipped with different stereo depth cameras. The resulting policy demonstrates robust performance across diverse environments, seamlessly handling extreme challenges such as high platforms and wide gaps, as well as fine-grained tasks including bidirectional long-term staircase traversal.

