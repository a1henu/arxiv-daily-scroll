---
layout: default
title: E-MoFlow: Learning Egomotion and Optical Flow from Event Data via Implicit Regularization
---

# E-MoFlow: Learning Egomotion and Optical Flow from Event Data via Implicit Regularization
**arXiv**：[2510.12753v1](https://arxiv.org/abs/2510.12753) · [PDF](https://arxiv.org/pdf/2510.12753.pdf)  
**作者**：Wenpu Li, Bangyan Liao, Yi Zhou, Qi Xu, Pian Wan, Peidong Liu  

**一句话要点**：提出E-MoFlow框架，通过隐式正则化从事件数据联合学习自运动和光流

**关键词**：事件相机, 自运动估计, 光流估计, 隐式正则化, 无监督学习, 神经表示

## 3 点简述
- 核心问题：事件相机中自运动和光流独立估计因缺乏数据关联而病态，现有方法有偏差或易陷局部最优
- 方法要点：建模自运动为连续样条、光流为隐式神经表示，嵌入时空一致性和微分几何约束
- 实验或效果：在无监督方法中达到SOTA，对一般6-DoF运动场景有效，与有监督方法竞争

## 摘要（原文）

> The estimation of optical flow and 6-DoF ego-motion, two fundamental tasks in
> 3D vision, has typically been addressed independently. For neuromorphic vision
> (e.g., event cameras), however, the lack of robust data association makes
> solving the two problems separately an ill-posed challenge, especially in the
> absence of supervision via ground truth. Existing works mitigate this
> ill-posedness by either enforcing the smoothness of the flow field via an
> explicit variational regularizer or leveraging explicit structure-and-motion
> priors in the parametrization to improve event alignment. The former notably
> introduces bias in results and computational overhead, while the latter, which
> parametrizes the optical flow in terms of the scene depth and the camera
> motion, often converges to suboptimal local minima. To address these issues, we
> propose an unsupervised framework that jointly optimizes egomotion and optical
> flow via implicit spatial-temporal and geometric regularization. First, by
> modeling camera's egomotion as a continuous spline and optical flow as an
> implicit neural representation, our method inherently embeds spatial-temporal
> coherence through inductive biases. Second, we incorporate structure-and-motion
> priors through differential geometric constraints, bypassing explicit depth
> estimation while maintaining rigorous geometric consistency. As a result, our
> framework (called E-MoFlow) unifies egomotion and optical flow estimation via
> implicit regularization under a fully unsupervised paradigm. Experiments
> demonstrate its versatility to general 6-DoF motion scenarios, achieving
> state-of-the-art performance among unsupervised methods and competitive even
> with supervised approaches.

