---
layout: default
title: Mimir: Hierarchical Goal-Driven Diffusion with Uncertainty Propagation for End-to-End Autonomous Driving
---

# Mimir: Hierarchical Goal-Driven Diffusion with Uncertainty Propagation for End-to-End Autonomous Driving
**arXiv**：[2512.07130v1](https://arxiv.org/abs/2512.07130) · [PDF](https://arxiv.org/pdf/2512.07130.pdf)  
**作者**：Zebin Xing, Yupeng Zheng, Qichao Zhang, Zhixing Ding, Pengxuan Yang, Songen Gu, Zhongpu Xia, Dongbin Zhao  

**一句话要点**：提出Mimir框架，通过不确定性估计和多速率引导解决端到端自动驾驶中高层引导不准确和计算开销大的问题。

**关键词**：端到端自动驾驶, 不确定性估计, 多速率引导, 轨迹生成, 拉普拉斯分布, 推理加速

## 3 点简述
- 核心问题：端到端自动驾驶中高层引导信号不准确和复杂引导模块计算开销大，限制性能提升。
- 方法要点：采用拉普拉斯分布估计目标点不确定性以增强鲁棒性，并引入多速率引导机制提前预测扩展目标点以加速推理。
- 实验或效果：在Navhard和Navtest基准测试中，驾驶分数EPDMS提升20%，高层模块推理速度提高1.6倍，且不损失准确性。

## 摘要（原文）

> End-to-end autonomous driving has emerged as a pivotal direction in the field of autonomous systems. Recent works have demonstrated impressive performance by incorporating high-level guidance signals to steer low-level trajectory planners. However, their potential is often constrained by inaccurate high-level guidance and the computational overhead of complex guidance modules. To address these limitations, we propose Mimir, a novel hierarchical dual-system framework capable of generating robust trajectories relying on goal points with uncertainty estimation: (1) Unlike previous approaches that deterministically model, we estimate goal point uncertainty with a Laplace distribution to enhance robustness; (2) To overcome the slow inference speed of the guidance system, we introduce a multi-rate guidance mechanism that predicts extended goal points in advance. Validated on challenging Navhard and Navtest benchmarks, Mimir surpasses previous state-of-the-art methods with a 20% improvement in the driving score EPDMS, while achieving 1.6 times improvement in high-level module inference speed without compromising accuracy. The code and models will be released soon to promote reproducibility and further development. The code is available at https://github.com/ZebinX/Mimir-Uncertainty-Driving

