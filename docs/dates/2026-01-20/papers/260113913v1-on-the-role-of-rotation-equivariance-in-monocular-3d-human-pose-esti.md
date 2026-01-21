---
layout: default
title: On the Role of Rotation Equivariance in Monocular 3D Human Pose Estimation
---

# On the Role of Rotation Equivariance in Monocular 3D Human Pose Estimation
**arXiv**：[2601.13913v1](https://arxiv.org/abs/2601.13913) · [PDF](https://arxiv.org/pdf/2601.13913.pdf)  
**作者**：Pavlo Melnyk, Cuong Le, Urs Waldmann, Per-Erik Forssén, Bastian Wandt  

**一句话要点**：提出利用旋转等变性提升单目3D人体姿态估计性能，通过数据增强学习优于设计等变方法。

**关键词**：单目3D人体姿态估计, 旋转等变性, 2D到3D提升, 数据增强, 计算机视觉

## 3 点简述
- 核心问题：现有2D到3D提升模型在输入旋转时性能下降，单目3D姿态估计为不适定问题。
- 方法要点：主张学习人体姿态及其平面内旋转，通过数据增强赋予模型旋转等变性，简化学习过程。
- 实验或效果：在标准基准测试中验证，旋转等变性提升模型对图像平面旋转姿态的性能，超越设计等变方法。

## 摘要（原文）

> Estimating 3D from 2D is one of the central tasks in computer vision. In this work, we consider the monocular setting, i.e. single-view input, for 3D human pose estimation (HPE). Here, the task is to predict a 3D point set of human skeletal joints from a single 2D input image. While by definition this is an ill-posed problem, recent work has presented methods that solve it with up to several-centimetre error. Typically, these methods employ a two-step approach, where the first step is to detect the 2D skeletal joints in the input image, followed by the step of 2D-to-3D lifting. We find that common lifting models fail when encountering a rotated input. We argue that learning a single human pose along with its in-plane rotations is considerably easier and more geometrically grounded than directly learning a point-to-point mapping. Furthermore, our intuition is that endowing the model with the notion of rotation equivariance without explicitly constraining its parameter space should lead to a more straightforward learning process than one with equivariance by design. Utilising the common HPE benchmarks, we confirm that the 2D rotation equivariance per se improves the model performance on human poses akin to rotations in the image plane, and can be efficiently and straightforwardly learned by augmentation, outperforming state-of-the-art equivariant-by-design methods.

