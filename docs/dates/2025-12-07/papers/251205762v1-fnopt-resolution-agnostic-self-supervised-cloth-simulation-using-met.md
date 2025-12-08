---
layout: default
title: FNOPT: Resolution-Agnostic, Self-Supervised Cloth Simulation using Meta-Optimization with Fourier Neural Operators
---

# FNOPT: Resolution-Agnostic, Self-Supervised Cloth Simulation using Meta-Optimization with Fourier Neural Operators
**arXiv**：[2512.05762v1](https://arxiv.org/abs/2512.05762) · [PDF](https://arxiv.org/pdf/2512.05762.pdf)  
**作者**：Ruochen Chen, Thuy Tran, Shaifali Parashar  

**一句话要点**：提出FNOpt框架，通过元优化与傅里叶神经算子实现分辨率无关的自监督布料模拟。

**关键词**：布料模拟, 自监督学习, 傅里叶神经算子, 元优化, 分辨率无关

## 3 点简述
- 核心问题：现有神经模拟器依赖大量真实数据或牺牲细节，跨分辨率和运动模式泛化差。
- 方法要点：将时间积分公式化为优化问题，用傅里叶神经算子参数化神经优化器，自监督训练。
- 实验或效果：在粗网格上训练，泛化到细分辨率，捕获皱纹并保持稳定性，在基准数据集上优于先前方法。

## 摘要（原文）

> We present FNOpt, a self-supervised cloth simulation framework that formulates time integration as an optimization problem and trains a resolution-agnostic neural optimizer parameterized by a Fourier neural operator (FNO). Prior neural simulators often rely on extensive ground truth data or sacrifice fine-scale detail, and generalize poorly across resolutions and motion patterns. In contrast, FNOpt learns to simulate physically plausible cloth dynamics and achieves stable and accurate rollouts across diverse mesh resolutions and motion patterns without retraining. Trained only on a coarse grid with physics-based losses, FNOpt generalizes to finer resolutions, capturing fine-scale wrinkles and preserving rollout stability. Extensive evaluations on a benchmark cloth simulation dataset demonstrate that FNOpt outperforms prior learning-based approaches in out-of-distribution settings in both accuracy and robustness. These results position FNO-based meta-optimization as a compelling alternative to previous neural simulators for cloth, thus reducing the need for curated data and improving cross-resolution reliability.

