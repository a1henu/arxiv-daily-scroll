---
layout: default
title: Learning False Discovery Rate Control via Model-Based Neural Networks
---

# Learning False Discovery Rate Control via Model-Based Neural Networks
**arXiv**：[2602.05798v1](https://arxiv.org/abs/2602.05798) · [PDF](https://arxiv.org/pdf/2602.05798.pdf)  
**作者**：Arnau Vilella, Jasin Machkour, Michael Muma, Daniel P. Palomar  

**一句话要点**：提出基于神经网络的FDR控制方法，以增强高维变量选择的统计功效。

**关键词**：假发现率控制, 高维变量选择, 神经网络, T-Rex Selector, 合成数据训练, 统计功效

## 3 点简述
- 核心问题：现有FDR控制方法在变量选择中过于保守，导致实际FDP与目标FDR存在差距。
- 方法要点：在T-Rex Selector框架中，用神经网络替代解析FDP估计器，通过合成数据训练实现更精确的FDP近似。
- 实验或效果：模拟和合成GWAS实验显示，该方法在保持近似FDR控制的同时，提高了真实变量的检测能力。

## 摘要（原文）

> Controlling the false discovery rate (FDR) in high-dimensional variable selection requires balancing rigorous error control with statistical power. Existing methods with provable guarantees are often overly conservative, creating a persistent gap between the realized false discovery proportion (FDP) and the target FDR level. We introduce a learning-augmented enhancement of the T-Rex Selector framework that narrows this gap. Our approach replaces the analytical FDP estimator with a neural network trained solely on diverse synthetic datasets, enabling a substantially tighter and more accurate approximation of the FDP. This refinement allows the procedure to operate much closer to the desired FDR level, thereby increasing discovery power while maintaining effective approximate control. Through extensive simulations and a challenging synthetic genome-wide association study (GWAS), we demonstrate that our method achieves superior detection of true variables compared to existing approaches.

