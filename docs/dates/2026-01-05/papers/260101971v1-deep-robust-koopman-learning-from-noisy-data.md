---
layout: default
title: Deep Robust Koopman Learning from Noisy Data
---

# Deep Robust Koopman Learning from Noisy Data
**arXiv**：[2601.01971v1](https://arxiv.org/abs/2601.01971) · [PDF](https://arxiv.org/pdf/2601.01971.pdf)  
**作者**：Aditya Singh, Rajpal Singh, Jishnu Keshavan  

**一句话要点**：提出基于自编码器的深度鲁棒Koopman学习方法，从噪声数据中学习提升函数和降偏Koopman算子。

**关键词**：Koopman算子, 噪声鲁棒性, 自编码器, 非线性系统, 机械臂控制

## 3 点简述
- 核心问题：噪声数据导致Koopman算子估计偏差，影响非线性系统预测与控制性能。
- 方法要点：通过自编码器联合学习前后向动态一致的提升函数，合成降偏Koopman算子。
- 实验或效果：理论分析验证降偏效果，仿真和Franka FR3机械臂实验展示噪声鲁棒性。

## 摘要（原文）

> Koopman operator theory has emerged as a leading data-driven approach that relies on a judicious choice of observable functions to realize global linear representations of nonlinear systems in the lifted observable space. However, real-world data is often noisy, making it difficult to obtain an accurate and unbiased approximation of the Koopman operator. The Koopman operator generated from noisy datasets is typically corrupted by noise-induced bias that severely degrades prediction and downstream tracking performance. In order to address this drawback, this paper proposes a novel autoencoder-based neural architecture to jointly learn the appropriate lifting functions and the reduced-bias Koopman operator from noisy data. The architecture initially learns the Koopman basis functions that are consistent for both the forward and backward temporal dynamics of the system. Subsequently, by utilizing the learned forward and backward temporal dynamics, the Koopman operator is synthesized with a reduced bias making the method more robust to noise compared to existing techniques. Theoretical analysis is used to demonstrate significant bias reduction in the presence of training noise. Dynamics prediction and tracking control simulations are conducted for multiple serial manipulator arms, including performance comparisons with leading alternative designs, to demonstrate its robustness under various noise levels. Experimental studies with the Franka FR3 7-DoF manipulator arm are further used to demonstrate the effectiveness of the proposed approach in a practical setting.

