---
layout: default
title: SuperOcc: Toward Cohesive Temporal Modeling for Superquadric-based Occupancy Prediction
---

# SuperOcc: Toward Cohesive Temporal Modeling for Superquadric-based Occupancy Prediction
**arXiv**：[2601.15644v1](https://arxiv.org/abs/2601.15644) · [PDF](https://arxiv.org/pdf/2601.15644.pdf)  
**作者**：Zichen Yu, Quanli Liu, Wei Wang, Liyong Zhang, Xiaoguang Zhao  

**一句话要点**：提出SuperOcc框架，通过结合时间建模与多超二次曲面解码，提升自动驾驶中稀疏3D占用预测的性能与效率。

**关键词**：3D占用预测, 超二次曲面表示, 时间建模, 自动驾驶, 稀疏场景表示, 几何表达性

## 3 点简述
- 核心问题：现有超二次曲面方法在时间建模不足、查询稀疏性与几何表达性权衡、超二次曲面到体素映射效率低。
- 方法要点：结合视图中心与对象中心时间线索，采用多超二次曲面解码增强表达性，设计高效映射方案。
- 实验或效果：在SurroundOcc和Occ3D基准上实现先进性能，保持高效性，代码已开源。

## 摘要（原文）

> 3D occupancy prediction plays a pivotal role in the realm of autonomous driving, as it provides a comprehensive understanding of the driving environment. Most existing methods construct dense scene representations for occupancy prediction, overlooking the inherent sparsity of real-world driving scenes. Recently, 3D superquadric representation has emerged as a promising sparse alternative to dense scene representations due to the strong geometric expressiveness of superquadrics. However, existing superquadric frameworks still suffer from insufficient temporal modeling, a challenging trade-off between query sparsity and geometric expressiveness, and inefficient superquadric-to-voxel splatting. To address these issues, we propose SuperOcc, a novel framework for superquadric-based 3D occupancy prediction. SuperOcc incorporates three key designs: (1) a cohesive temporal modeling mechanism to simultaneously exploit view-centric and object-centric temporal cues; (2) a multi-superquadric decoding strategy to enhance geometric expressiveness without sacrificing query sparsity; and (3) an efficient superquadric-to-voxel splatting scheme to improve computational efficiency. Extensive experiments on the SurroundOcc and Occ3D benchmarks demonstrate that SuperOcc achieves state-of-the-art performance while maintaining superior efficiency. The code is available at https://github.com/Yzichen/SuperOcc.

