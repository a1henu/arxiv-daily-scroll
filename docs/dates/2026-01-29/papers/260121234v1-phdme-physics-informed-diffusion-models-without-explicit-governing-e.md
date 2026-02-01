---
layout: default
title: PHDME: Physics-Informed Diffusion Models without Explicit Governing Equations
---

# PHDME: Physics-Informed Diffusion Models without Explicit Governing Equations
**arXiv**：[2601.21234v1](https://arxiv.org/abs/2601.21234) · [PDF](https://arxiv.org/pdf/2601.21234.pdf)  
**作者**：Kaiyuan Tan, Kendra Givens, Peilun Li, Thomas Beckers  

**一句话要点**：提出PHDME框架，利用端口哈密顿结构先验解决稀疏观测和不完整物理下的轨迹预测问题。

**关键词**：扩散模型, 端口哈密顿系统, 物理信息机器学习, 稀疏观测, 轨迹预测, 不确定性校准

## 3 点简述
- 核心问题：扩散模型在稀疏数据下不可靠，且物理信息机器学习通常需要显式控制方程，而实际中方程可能不完整。
- 方法要点：结合高斯过程端口哈密顿系统和扩散模型，通过物理一致数据集和残差损失训练，无需完整方程。
- 实验或效果：在PDE基准和真实弹簧系统上验证，提高了数据稀缺下的准确性和物理一致性。

## 摘要（原文）

> Diffusion models provide expressive priors for forecasting trajectories of dynamical systems, but are typically unreliable in the sparse data regime. Physics-informed machine learning (PIML) improves reliability in such settings; however, most methods require \emph{explicit governing equations} during training, which are often only partially known due to complex and nonlinear dynamics. We introduce \textbf{PHDME}, a port-Hamiltonian diffusion framework designed for \emph{sparse observations} and \emph{incomplete physics}. PHDME leverages port-Hamiltonian structural prior but does not require full knowledge of the closed-form governing equations. Our approach first trains a Gaussian process distributed Port-Hamiltonian system (GP-dPHS) on limited observations to capture an energy-based representation of the dynamics. The GP-dPHS is then used to generate a physically consistent artificial dataset for diffusion training, and to inform the diffusion model with a structured physics residual loss. After training, the diffusion model acts as an amortized sampler and forecaster for fast trajectory generation. Finally, we apply split conformal calibration to provide uncertainty statements for the generated predictions. Experiments on PDE benchmarks and a real-world spring system show improved accuracy and physical consistency under data scarcity.

