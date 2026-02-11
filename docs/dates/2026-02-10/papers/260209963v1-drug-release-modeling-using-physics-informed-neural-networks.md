---
layout: default
title: Drug Release Modeling using Physics-Informed Neural Networks
---

# Drug Release Modeling using Physics-Informed Neural Networks
**arXiv**：[2602.09963v1](https://arxiv.org/abs/2602.09963) · [PDF](https://arxiv.org/pdf/2602.09963.pdf)  
**作者**：Daanish Aleem Qureshi, Khemraj Shukla, Vikas Srivastava  

**一句话要点**：提出基于物理信息神经网络和贝叶斯物理信息神经网络的药物释放建模方法，以提升复杂几何和释放机制下的预测精度。

**关键词**：药物释放建模, 物理信息神经网络, 贝叶斯物理信息神经网络, 菲克扩散定律, 不确定性量化, 加速表征

## 3 点简述
- 核心问题：传统药物释放模型在复杂几何和释放机制中因简化假设而精度受限。
- 方法要点：将菲克扩散定律嵌入神经网络损失函数，结合有限实验数据进行长期预测。
- 实验或效果：相比基线模型平均误差降低达40%，在平面薄膜中仅需6%释放时间数据即可实现RMSE<0.05。

## 摘要（原文）

> Accurate modeling of drug release is essential for designing and developing controlled-release systems. Classical models (Fick, Higuchi, Peppas) rely on simplifying assumptions that limit their accuracy in complex geometries and release mechanisms. Here, we propose a novel approach using Physics-Informed Neural Networks (PINNs) and Bayesian PINNs (BPINNs) for predicting release from planar, 1D-wrinkled, and 2D-crumpled films. This approach uniquely integrates Fick's diffusion law with limited experimental data to enable accurate long-term predictions from short-term measurements, and is systematically benchmarked against classical drug release models. We embedded Fick's second law into PINN as loss with 10,000 Latin-hypercube collocation points and utilized previously published experimental datasets to assess drug release performance through mean absolute error (MAE) and root mean square error (RMSE), considering noisy conditions and limited-data scenarios. Our approach reduced mean error by up to 40% relative to classical baselines across all film types. The PINN formulation achieved RMSE <0.05 utilizing only the first 6% of the release time data (reducing 94% of release time required for the experiments) for the planar film. For wrinkled and crumpled films, the PINN reached RMSE <0.05 in 33% of the release time data. BPINNs provide tighter and more reliable uncertainty quantification under noise. By combining physical laws with experimental data, the proposed framework yields highly accurate long-term release predictions from short-term measurements, offering a practical route for accelerated characterization and more efficient early-stage drug release system formulation.

