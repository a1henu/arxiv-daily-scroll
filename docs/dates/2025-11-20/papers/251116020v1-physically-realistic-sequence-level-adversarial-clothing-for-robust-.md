---
layout: default
title: Physically Realistic Sequence-Level Adversarial Clothing for Robust Human-Detection Evasion
---

# Physically Realistic Sequence-Level Adversarial Clothing for Robust Human-Detection Evasion
**arXiv**：[2511.16020v1](https://arxiv.org/abs/2511.16020) · [PDF](https://arxiv.org/pdf/2511.16020.pdf)  
**作者**：Dingkun Zhou, Patrick P. K. Chan, Hengxu Wu, Shikang Zheng, Ruiqi Huang, Yuanjie Zhao  

**一句话要点**：提出序列级优化框架以生成可打印对抗纹理，实现长视频中人体检测的稳定规避

**关键词**：人体检测规避, 序列级对抗攻击, 可打印纹理, 物理模拟, UV空间优化, 跨模型迁移

## 3 点简述
- 核心问题：现有可穿戴攻击方法在长视频中因运动、姿态变化和衣物变形而难以维持隐蔽性
- 方法要点：采用UV空间映射、调色板参数化和物理模拟，优化控制点以最小化检测置信度
- 实验或效果：在数字和物理环境中实现强隐蔽性、高鲁棒性和跨模型可迁移性

## 摘要（原文）

> Deep neural networks used for human detection are highly vulnerable to adversarial manipulation, creating safety and privacy risks in real surveillance environments. Wearable attacks offer a realistic threat model, yet existing approaches usually optimize textures frame by frame and therefore fail to maintain concealment across long video sequences with motion, pose changes, and garment deformation. In this work, a sequence-level optimization framework is introduced to generate natural, printable adversarial textures for shirts, trousers, and hats that remain effective throughout entire walking videos in both digital and physical settings. Product images are first mapped to UV space and converted into a compact palette and control-point parameterization, with ICC locking to keep all colors printable. A physically based human-garment pipeline is then employed to simulate motion, multi-angle camera viewpoints, cloth dynamics, and illumination variation. An expectation-over-transformation objective with temporal weighting is used to optimize the control points so that detection confidence is minimized across whole sequences. Extensive experiments demonstrate strong and stable concealment, high robustness to viewpoint changes, and superior cross-model transferability. Physical garments produced with sublimation printing achieve reliable suppression under indoor and outdoor recordings, confirming real-world feasibility.

