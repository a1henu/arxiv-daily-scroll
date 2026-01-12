---
layout: default
title: Orient Anything V2: Unifying Orientation and Rotation Understanding
---

# Orient Anything V2: Unifying Orientation and Rotation Understanding
**arXiv**：[2601.05573v1](https://arxiv.org/abs/2601.05573) · [PDF](https://arxiv.org/pdf/2601.05573.pdf)  
**作者**：Zehan Wang, Ziang Zhang, Jiayang Xu, Jialei Wang, Tianyu Pang, Chao Du, HengShuang Zhao, Zhou Zhao  

**一句话要点**：提出Orient Anything V2以统一理解单图或双图中的物体3D朝向与旋转

**关键词**：3D朝向估计, 旋转对称性建模, 零样本泛化, 多帧架构, 生成模型合成

## 3 点简述
- 核心问题：处理物体多样旋转对称性并直接估计相对旋转，扩展朝向理解能力
- 方法要点：通过生成模型合成3D资产、模型在环标注系统、对称感知分布拟合目标及多帧架构
- 实验或效果：在11个基准上实现零样本朝向估计、6DoF姿态估计和对称识别的先进性能

## 摘要（原文）

> This work presents Orient Anything V2, an enhanced foundation model for unified understanding of object 3D orientation and rotation from single or paired images. Building upon Orient Anything V1, which defines orientation via a single unique front face, V2 extends this capability to handle objects with diverse rotational symmetries and directly estimate relative rotations. These improvements are enabled by four key innovations: 1) Scalable 3D assets synthesized by generative models, ensuring broad category coverage and balanced data distribution; 2) An efficient, model-in-the-loop annotation system that robustly identifies 0 to N valid front faces for each object; 3) A symmetry-aware, periodic distribution fitting objective that captures all plausible front-facing orientations, effectively modeling object rotational symmetry; 4) A multi-frame architecture that directly predicts relative object rotations. Extensive experiments show that Orient Anything V2 achieves state-of-the-art zero-shot performance on orientation estimation, 6DoF pose estimation, and object symmetry recognition across 11 widely used benchmarks. The model demonstrates strong generalization, significantly broadening the applicability of orientation estimation in diverse downstream tasks.

