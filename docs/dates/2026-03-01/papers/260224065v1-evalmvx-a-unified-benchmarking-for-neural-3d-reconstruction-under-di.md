---
layout: default
title: EvalMVX: A Unified Benchmarking for Neural 3D Reconstruction under Diverse Multiview Setups
---

# EvalMVX: A Unified Benchmarking for Neural 3D Reconstruction under Diverse Multiview Setups
**arXiv**：[2602.24065v1](https://arxiv.org/abs/2602.24065) · [PDF](https://arxiv.org/pdf/2602.24065.pdf)  
**作者**：Zaiyan Yang, Jieji Ren, Xiangyi Wang, zonglin li, Xu Cao, Heng Guo, Zhanyu Ma, Boxin Shi  

**一句话要点**：提出EvalMVX数据集以统一评估多视图3D重建方法在不同光照和几何细节下的性能

**关键词**：多视图3D重建, 数据集基准, 神经表面重建, 光度立体, 偏振形状重建, 真实世界评估

## 3 点简述
- 核心问题：现有数据集主要基于RGB输入评估多视图立体视觉，缺乏对多视图光度立体和多视图偏振形状重建的定量比较
- 方法要点：构建包含25个物体、8500张图像的真实世界数据集，涵盖20个视角和17种光照条件，提供对齐的真实3D网格
- 实验或效果：评估13种近期方法，记录最佳性能，识别在不同几何细节和反射类型下的开放问题

## 摘要（原文）

> Recent advancements in neural surface reconstruction have significantly enhanced 3D reconstruction. However, current real world datasets mainly focus on benchmarking multiview stereo (MVS) based on RGB inputs. Multiview photometric stereo (MVPS) and multiview shape from polarization (MVSfP), though indispensable on high-fidelity surface reconstruction and sparse inputs, have not been quantitatively assessed together with MVS. To determine the working range of different MVX (MVS, MVSfP, and MVPS) techniques, we propose EvalMVX, a real-world dataset containing $25$ objects, each captured with a polarized camera under $20$ varying views and $17$ light conditions including OLAT and natural illumination, leading to $8,500$ images. Each object includes aligned ground-truth 3D mesh, facilitating quantitative benchmarking of MVX methods simultaneously. Based on our EvalMVX, we evaluate $13$ MVX methods published in recent years, record the best-performing methods, and identify open problems under diverse geometric details and reflectance types. We hope EvalMVX and the benchmarking results can inspire future research on multiview 3D reconstruction.

