---
layout: default
title: Towards Spatio-Temporal Extrapolation of Phase-Field Simulations with Convolution-Only Neural Networks
---

# Towards Spatio-Temporal Extrapolation of Phase-Field Simulations with Convolution-Only Neural Networks
**arXiv**：[2601.04510v1](https://arxiv.org/abs/2601.04510) · [PDF](https://arxiv.org/pdf/2601.04510.pdf)  
**作者**：Christophe Bonneville, Nathan Bieberdorf, Pieterjan Robbe, Mark Asta, Habib Najm, Laurent Capolungo, Cosmin Safta  

**一句话要点**：提出全卷积条件参数化U-Net代理模型，用于液态金属脱合金相场模拟的时空外推。

**关键词**：相场模拟, 时空外推, 卷积神经网络, 条件扩散模型, 液态金属脱合金

## 3 点简述
- 液态金属脱合金相场模拟计算成本高，难以处理大域长时问题。
- 采用卷积自注意力、物理引导填充和洪水填充校正器，结合条件扩散模型生成初始条件。
- 在训练域内误差低于5%，外推时低于15%，加速比高达36,000倍。

## 摘要（原文）

> Phase-field simulations of liquid metal dealloying (LMD) can capture complex microstructural evolutions but can be prohibitively expensive for large domains and long time horizons. In this paper, we introduce a fully convolutional, conditionally parameterized U-Net surrogate designed to extrapolate far beyond its training data in both space and time. The architecture integrates convolutional self-attention, physically informed padding, and a flood-fill corrector method to maintain accuracy under extreme extrapolation, while conditioning on simulation parameters allows for flexible time-step skipping and adaptation to varying alloy compositions. To remove the need for costly solver-based initialization, we couple the surrogate with a conditional diffusion model that generates synthetic, physically consistent initial conditions. We train our surrogate on simulations generated over small domain sizes and short time spans, but, by taking advantage of the convolutional nature of U-Nets, we are able to run and extrapolate surrogate simulations for longer time horizons than what would be achievable with classic numerical solvers. Across multiple alloy compositions, the framework is able to reproduce the LMD physics accurately. It predicts key quantities of interest and spatial statistics with relative errors typically below 5% in the training regime and under 15% during large-scale, long time-horizon extrapolations. Our framework can also deliver speed-ups of up to 36,000 times, bringing the time to run weeks-long simulations down to a few seconds. This work is a first stepping stone towards high-fidelity extrapolation in both space and time of phase-field simulation for LMD.

