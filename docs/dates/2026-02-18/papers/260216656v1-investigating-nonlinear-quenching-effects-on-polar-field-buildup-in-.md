---
layout: default
title: Investigating Nonlinear Quenching Effects on Polar Field Buildup in the Sun Using Physics-Informed Neural Networks
---

# Investigating Nonlinear Quenching Effects on Polar Field Buildup in the Sun Using Physics-Informed Neural Networks
**arXiv**：[2602.16656v1](https://arxiv.org/abs/2602.16656) · [PDF](https://arxiv.org/pdf/2602.16656.pdf)  
**作者**：Jithu J. Athalathil, Mohammed H. Talafha, Bhargav Vaidya  

**一句话要点**：利用物理信息神经网络研究太阳极区磁场非线性淬灭效应

**关键词**：物理信息神经网络, 太阳发电机, 表面通量输运, 非线性淬灭, 太阳周期预测, 极区磁场

## 3 点简述
- 核心问题：非线性淬灭机制（倾斜淬灭和纬度淬灭）如何调控太阳极区磁场积累和太阳周期振幅。
- 方法要点：采用物理信息神经网络求解表面通量输运方程，直接嵌入物理约束以隔离淬灭机制贡献。
- 实验或效果：结果显示倾斜淬灭随扩散性增强而强化，纬度淬灭主导平流主导区域，非线性交互可解释强弱周期交替。

## 摘要（原文）

> The solar dynamo relies on the regeneration of the poloidal magnetic field through processes strongly modulated by nonlinear feedbacks such as tilt quenching (TQ) and latitude quenching (LQ). These mechanisms play a decisive role in regulating the buildup of the Sun's polar field and, in turn, the amplitude of future solar cycles. In this work, we employ Physics-Informed Neural Networks (PINN) to solve the surface flux transport (SFT) equation, embedding physical constraints directly into the neural network framework. By systematically varying transport parameters, we isolate the relative contributions of TQ and LQ to polar dipole buildup. We use the residual dipole moment as a diagnostic for cycle-to-cycle amplification and show that TQ suppression strengthens with increasing diffusivity, while LQ dominates in advection-dominated regimes. The ratio $ΔD_{\mathrm{LQ}}/ΔD_{\mathrm{TQ}}$ exhibits a smooth inverse-square dependence on the dynamo effectivity range, refining previous empirical fits with improved accuracy and reduced scatter. The results further reveal that the need for a decay term is not essential for PINN set-up due to the training process. Compared with the traditional 1D SFT model, the PINN framework achieves significantly lower error metrics and more robust recovery of nonlinear trends. Our results suggest that the nonlinear interplay between LQ and TQ can naturally produce alternations between weak and strong cycles, providing a physical explanation for the observed even-odd cycle modulation. These findings demonstrate the potential of PINN as an accurate, efficient, and physically consistent tool for solar cycle prediction.

