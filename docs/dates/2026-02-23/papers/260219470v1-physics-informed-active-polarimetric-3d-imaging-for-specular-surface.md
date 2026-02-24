---
layout: default
title: Physics-informed Active Polarimetric 3D Imaging for Specular Surfaces
---

# Physics-informed Active Polarimetric 3D Imaging for Specular Surfaces
**arXiv**：[2602.19470v1](https://arxiv.org/abs/2602.19470) · [PDF](https://arxiv.org/pdf/2602.19470.pdf)  
**作者**：Jiazhang Wang, Hyelim Yang, Tianyi Wang, Florian Willomitzer  

**一句话要点**：提出物理信息深度学习框架，用于单次拍摄复杂镜面表面的3D成像。

**关键词**：镜面表面成像, 偏振3D成像, 物理信息深度学习, 单次拍摄测量, 表面法线估计

## 3 点简述
- 核心问题：镜面表面3D成像在动态环境中难以实现快速准确测量，现有方法存在多拍依赖或精度限制。
- 方法要点：结合偏振线索和结构光照，通过双编码器架构处理非线性耦合，直接推断表面法线。
- 实验或效果：实现单次拍摄下的准确鲁棒法线估计，推理速度快，适用于复杂镜面表面。

## 摘要（原文）

> 3D imaging of specular surfaces remains challenging in real-world scenarios, such as in-line inspection or hand-held scanning, requiring fast and accurate measurement of complex geometries. Optical metrology techniques such as deflectometry achieve high accuracy but typically rely on multi-shot acquisition, making them unsuitable for dynamic environments. Fourier-based single-shot approaches alleviate this constraint, yet their performance deteriorates when measuring surfaces with high spatial frequency structure or large curvature. Alternatively, polarimetric 3D imaging in computer vision operates in a single-shot fashion and exhibits robustness to geometric complexity. However, its accuracy is fundamentally limited by the orthographic imaging assumption. In this paper, we propose a physics-informed deep learning framework for single-shot 3D imaging of complex specular surfaces. Polarization cues provide orientation priors that assist in interpreting geometric information encoded by structured illumination. These complementary cues are processed through a dual-encoder architecture with mutual feature modulation, allowing the network to resolve their nonlinear coupling and directly infer surface normals. The proposed method achieves accurate and robust normal estimation in single-shot with fast inference, enabling practical 3D imaging of complex specular surfaces.

