---
layout: default
title: Radiometrically Consistent Gaussian Surfels for Inverse Rendering
---

# Radiometrically Consistent Gaussian Surfels for Inverse Rendering
**arXiv**：[2603.01491v1](https://arxiv.org/abs/2603.01491) · [PDF](https://arxiv.org/pdf/2603.01491.pdf)  
**作者**：Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  

**一句话要点**：提出RadioGS框架，通过辐射一致性约束解决高斯溅射中逆渲染的间接光照建模问题。

**关键词**：逆渲染, 高斯溅射, 辐射一致性, 间接光照建模, 高斯面元, 快速重光照

## 3 点简述
- 核心问题：现有高斯溅射方法在逆渲染中难以准确解耦材质属性，特别是间接光照建模缺乏未观测视角的监督。
- 方法要点：引入辐射一致性约束，最小化高斯基元学习辐射与物理渲染辐射的残差，提供未观测视角的监督，并基于高斯面元和2D高斯光线追踪高效集成。
- 实验或效果：在现有逆渲染基准测试中优于其他高斯方法，保持计算效率，支持快速重光照（<10ms渲染成本）。

## 摘要（原文）

> Inverse rendering with Gaussian Splatting has advanced rapidly, but accurately disentangling material properties from complex global illumination effects, particularly indirect illumination, remains a major challenge. Existing methods often query indirect radiance from Gaussian primitives pre-trained for novel-view synthesis. However, these pre-trained Gaussian primitives are supervised only towards limited training viewpoints, thus lack supervision for modeling indirect radiances from unobserved views. To address this issue, we introduce radiometric consistency, a novel physically-based constraint that provides supervision towards unobserved views by minimizing the residual between each Gaussian primitive's learned radiance and its physically-based rendered counterpart. Minimizing the residual for unobserved views establishes a self-correcting feedback loop that provides supervision from both physically-based rendering and novel-view synthesis, enabling accurate modeling of inter-reflection. We then propose Radiometrically Consistent Gaussian Surfels (RadioGS), an inverse rendering framework built upon our principle by efficiently integrating radiometric consistency by utilizing Gaussian surfels and 2D Gaussian ray tracing. We further propose a finetuning-based relighting strategy that adapts Gaussian surfel radiances to new illuminations within minutes, achieving low rendering cost (<10ms). Extensive experiments on existing inverse rendering benchmarks show that RadioGS outperforms existing Gaussian-based methods in inverse rendering, while retaining the computational efficiency.

