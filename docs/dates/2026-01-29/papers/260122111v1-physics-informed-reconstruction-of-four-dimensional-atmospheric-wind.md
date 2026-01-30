---
layout: default
title: Physics Informed Reconstruction of Four-Dimensional Atmospheric Wind Fields Using Multi-UAS Swarm Observations in a Synthetic Turbulent Environment
---

# Physics Informed Reconstruction of Four-Dimensional Atmospheric Wind Fields Using Multi-UAS Swarm Observations in a Synthetic Turbulent Environment
**arXiv**：[2601.22111v1](https://arxiv.org/abs/2601.22111) · [PDF](https://arxiv.org/pdf/2601.22111.pdf)  
**作者**：Abdullah Tasim, Wei Sun  

**一句话要点**：提出基于无人机群观测的物理信息神经网络框架，以重建四维大气风场

**关键词**：大气风场重建, 无人机群观测, 物理信息神经网络, 双向长短期记忆网络, 合成湍流环境

## 3 点简述
- 核心问题：传统仪器在大气边界层存在时空间隙，单无人机采样有限，难以全面恢复风场。
- 方法要点：使用双向LSTM从无人机动态估计局部风分量，并融入物理信息神经网络进行时空连续重建。
- 实验或效果：在合成湍流环境中，五无人机群配置下重建风场整体RMSE为0.118-0.154 m/s，验证了方法的准确性和可扩展性。

## 摘要（原文）

> Accurate reconstruction of atmospheric wind fields is essential for applications such as weather forecasting, hazard prediction, and wind energy assessment, yet conventional instruments leave spatio-temporal gaps within the lower atmospheric boundary layer. Unmanned aircraft systems (UAS) provide flexible in situ measurements, but individual platforms sample wind only along their flight trajectories, limiting full wind-field recovery. This study presents a framework for reconstructing four-dimensional atmospheric wind fields using measurements obtained from a coordinated UAS swarm. A synthetic turbulence environment and high-fidelity multirotor simulation are used to generate training and evaluation data. Local wind components are estimated from UAS dynamics using a bidirectional long short-term memory network (Bi-LSTM) and assimilated into a physics-informed neural network (PINN) to reconstruct a continuous wind field in space and time. For local wind estimation, the bidirectional LSTM achieves root-mean-square errors (RMSE) of 0.064 and 0.062 m/s for the north and east components in low-wind conditions, increasing to 0.122 to 0.129 m/s under moderate winds and 0.271 to 0.273 m/s in high-wind conditions, while the vertical component exhibits higher error, with RMSE values of 0.029 to 0.091 m/s. The physics-informed reconstruction recovers the dominant spatial and temporal structure of the wind field up to 1000 m altitude while preserving mean flow direction and vertical shear. Under moderate wind conditions, the reconstructed mean wind field achieves an overall RMSE between 0.118 and 0.154 m/s across evaluated UAS configurations, with the lowest error obtained using a five-UAS swarm. These results demonstrate that coordinated UAS measurements enable accurate and scalable four-dimensional wind-field reconstruction without dedicated wind sensors or fixed infrastructure.

