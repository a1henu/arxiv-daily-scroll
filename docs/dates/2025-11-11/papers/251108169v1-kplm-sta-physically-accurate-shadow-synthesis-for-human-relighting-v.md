---
layout: default
title: KPLM-STA: Physically-Accurate Shadow Synthesis for Human Relighting via Keypoint-Based Light Modeling
---

# KPLM-STA: Physically-Accurate Shadow Synthesis for Human Relighting via Keypoint-Based Light Modeling
**arXiv**：[2511.08169v1](https://arxiv.org/abs/2511.08169) · [PDF](https://arxiv.org/pdf/2511.08169.pdf)  
**作者**：Xinhui Yin, Qifei Li, Yilin Guo, Hongxia Xie, Xiaoli Zhang  

**一句话要点**：提出KPLM-STA框架以解决图像合成中人体阴影生成的真实性与几何精度问题

**关键词**：阴影合成, 关键点建模, 几何算法, 图像重光照, 人体姿态处理

## 3 点简述
- 核心问题：现有方法在图像合成中难以生成外观真实且几何精确的阴影，尤其在复杂人体姿态下。
- 方法要点：使用关键点线性模型和阴影三角算法，实现物理准确的阴影投影和几何计算。
- 实验或效果：在阴影真实度基准测试中达到最优性能，并泛化到多方向重光照场景。

## 摘要（原文）

> Image composition aims to seamlessly integrate a foreground object into a background, where generating realistic and geometrically accurate shadows remains a persistent challenge. While recent diffusion-based methods have outperformed GAN-based approaches, existing techniques, such as the diffusion-based relighting framework IC-Light, still fall short in producing shadows with both high appearance realism and geometric precision, especially in composite images. To address these limitations, we propose a novel shadow generation framework based on a Keypoints Linear Model (KPLM) and a Shadow Triangle Algorithm (STA). KPLM models articulated human bodies using nine keypoints and one bounding block, enabling physically plausible shadow projection and dynamic shading across joints, thereby enhancing visual realism. STA further improves geometric accuracy by computing shadow angles, lengths, and spatial positions through explicit geometric formulations. Extensive experiments demonstrate that our method achieves state-of-the-art performance on shadow realism benchmarks, particularly under complex human poses, and generalizes effectively to multi-directional relighting scenarios such as those supported by IC-Light.

