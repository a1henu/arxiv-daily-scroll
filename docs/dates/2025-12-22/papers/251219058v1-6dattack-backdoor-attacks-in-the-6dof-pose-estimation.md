---
layout: default
title: 6DAttack: Backdoor Attacks in the 6DoF Pose Estimation
---

# 6DAttack: Backdoor Attacks in the 6DoF Pose Estimation
**arXiv**：[2512.19058v1](https://arxiv.org/abs/2512.19058) · [PDF](https://arxiv.org/pdf/2512.19058.pdf)  
**作者**：Jihui Guo, Zongmin Zhang, Zhen Sun, Yuhao Yang, Jinlin Wu, Fu Zhang, Xinlei He  

**一句话要点**：提出6DAttack框架，利用3D物体触发器对6DoF姿态估计进行后门攻击。

**关键词**：6DoF姿态估计, 后门攻击, 3D触发器, 安全威胁, 深度学习安全

## 3 点简述
- 核心问题：6DoF姿态估计面临后门攻击威胁，现有2D方法不适用连续参数控制。
- 方法要点：使用3D物体触发器诱导可控错误姿态，同时保持正常行为。
- 实验效果：在多个数据集和模型上实现高攻击成功率，不影响清洁性能，防御无效。

## 摘要（原文）

> Deep learning advances have enabled accurate six-degree-of-freedom (6DoF) object pose estimation, widely used in robotics, AR/VR, and autonomous systems. However, backdoor attacks pose significant security risks. While most research focuses on 2D vision, 6DoF pose estimation remains largely unexplored. Unlike traditional backdoors that only change classes, 6DoF attacks must control continuous parameters like translation and rotation, rendering 2D methods inapplicable. We propose 6DAttack, a framework using 3D object triggers to induce controlled erroneous poses while maintaining normal behavior. Evaluations on PVNet, DenseFusion, and PoseDiffusion across LINEMOD, YCB-Video, and CO3D show high attack success rates (ASRs) without compromising clean performance. Backdoored models achieve up to 100% clean ADD accuracy and 100% ASR, with triggered samples reaching 97.70% ADD-P. Furthermore, a representative defense remains ineffective. Our findings reveal a serious, underexplored threat to 6DoF pose estimation.

