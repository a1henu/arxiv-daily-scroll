---
layout: default
title: MeanFuser: Fast One-Step Multi-Modal Trajectory Generation and Adaptive Reconstruction via MeanFlow for End-to-End Autonomous Driving
---

# MeanFuser: Fast One-Step Multi-Modal Trajectory Generation and Adaptive Reconstruction via MeanFlow for End-to-End Autonomous Driving
**arXiv**：[2602.20060v1](https://arxiv.org/abs/2602.20060) · [PDF](https://arxiv.org/pdf/2602.20060.pdf)  
**作者**：Junli Wang, Xueyi Liu, Yinan Zheng, Zebing Xing, Pengfei Li, Guang Li, Kun Ma, Guang Chen, Hangjun Ye, Zhongpu Xia, Long Chen, Qichao Zhang  

**一句话要点**：提出MeanFuser，通过高斯混合噪声和平均流匹配，实现高效稳健的端到端自动驾驶轨迹生成。

**关键词**：自动驾驶, 轨迹生成, 生成模型, 流匹配, 端到端学习, 多模态规划

## 3 点简述
- 核心问题：现有基于离散锚点的生成模型在轨迹规划中面临词汇表大小与性能的权衡，影响稳健性。
- 方法要点：引入高斯混合噪声实现连续轨迹表示，采用平均流匹配加速推理，设计自适应重建模块优化轨迹选择。
- 实验或效果：在NAVSIM基准测试中表现出色，无需PDM Score监督，推理效率高，提供稳健高效解决方案。

## 摘要（原文）

> Generative models have shown great potential in trajectory planning. Recent studies demonstrate that anchor-guided generative models are effective in modeling the uncertainty of driving behaviors and improving overall performance. However, these methods rely on discrete anchor vocabularies that must sufficiently cover the trajectory distribution during testing to ensure robustness, inducing an inherent trade-off between vocabulary size and model performance. To overcome this limitation, we propose MeanFuser, an end-to-end autonomous driving method that enhances both efficiency and robustness through three key designs. (1) We introduce Gaussian Mixture Noise (GMN) to guide generative sampling, enabling a continuous representation of the trajectory space and eliminating the dependency on discrete anchor vocabularies. (2) We adapt ``MeanFlow Identity" to end-to-end planning, which models the mean velocity field between GMN and trajectory distribution instead of the instantaneous velocity field used in vanilla flow matching methods, effectively eliminating numerical errors from ODE solvers and significantly accelerating inference. (3) We design a lightweight Adaptive Reconstruction Module (ARM) that enables the model to implicitly select from all sampled proposals or reconstruct a new trajectory when none is satisfactory via attention weights. Experiments on the NAVSIM closed-loop benchmark demonstrate that MeanFuser achieves outstanding performance without the supervision of the PDM Score. and exceptional inference efficiency, offering a robust and efficient solution for end-to-end autonomous driving. Our code and model are available at https://github.com/wjl2244/MeanFuser.

