---
layout: default
title: Robot-DIFT: Distilling Diffusion Features for Geometrically Consistent Visuomotor Control
---

# Robot-DIFT: Distilling Diffusion Features for Geometrically Consistent Visuomotor Control
**arXiv**：[2602.11934v1](https://arxiv.org/abs/2602.11934) · [PDF](https://arxiv.org/pdf/2602.11934.pdf)  
**作者**：Yu Deng, Yufeng Jin, Xiaogang Jia, Jiahong Xue, Gerhard Neumann, Georgia Chalvatzaki  

**一句话要点**：提出Robot-DIFT框架，通过流形蒸馏将扩散模型几何先验蒸馏至确定性网络，以提升机器人视觉运动控制的几何一致性。

**关键词**：机器人视觉运动控制, 扩散模型, 特征蒸馏, 几何一致性, 流形学习, 实时推理

## 3 点简述
- 核心问题：当前视觉骨干网络在语义不变性优化下，对毫米级姿态变化的几何敏感性不足，阻碍通用机器人操作。
- 方法要点：利用流形蒸馏，将冻结扩散教师模型的几何依赖蒸馏到确定性空间-语义特征金字塔网络，确保稳定实时推理。
- 实验或效果：在DROID数据集预训练后，相比判别性基线，展现出更优的几何一致性和控制性能。

## 摘要（原文）

> We hypothesize that a key bottleneck in generalizable robot manipulation is not solely data scale or policy capacity, but a structural mismatch between current visual backbones and the physical requirements of closed-loop control. While state-of-the-art vision encoders (including those used in VLAs) optimize for semantic invariance to stabilize classification, manipulation typically demands geometric sensitivity the ability to map millimeter-level pose shifts to predictable feature changes. Their discriminative objective creates a "blind spot" for fine-grained control, whereas generative diffusion models inherently encode geometric dependencies within their latent manifolds, encouraging the preservation of dense multi-scale spatial structure. However, directly deploying stochastic diffusion features for control is hindered by stochastic instability, inference latency, and representation drift during fine-tuning. To bridge this gap, we propose Robot-DIFT, a framework that decouples the source of geometric information from the process of inference via Manifold Distillation. By distilling a frozen diffusion teacher into a deterministic Spatial-Semantic Feature Pyramid Network (S2-FPN), we retain the rich geometric priors of the generative model while ensuring temporal stability, real-time execution, and robustness against drift. Pretrained on the large-scale DROID dataset, Robot-DIFT demonstrates superior geometric consistency and control performance compared to leading discriminative baselines, supporting the view that how a model learns to see dictates how well it can learn to act.

