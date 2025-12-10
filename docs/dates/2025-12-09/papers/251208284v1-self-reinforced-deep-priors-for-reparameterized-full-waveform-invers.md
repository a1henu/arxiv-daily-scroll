---
layout: default
title: Self-Reinforced Deep Priors for Reparameterized Full Waveform Inversion
---

# Self-Reinforced Deep Priors for Reparameterized Full Waveform Inversion
**arXiv**：[2512.08284v1](https://arxiv.org/abs/2512.08284) · [PDF](https://arxiv.org/pdf/2512.08284.pdf)  
**作者**：Guangyuan Zou, Junlun Li, Feng Liu, Xuejing Zheng, Jianjian Xie, Guoyi Chen  

**一句话要点**：提出自增强深度先验重参数化全波形反演框架，以解决复杂地质条件下反演不稳定和伪影问题。

**关键词**：全波形反演, 深度先验, 重参数化, 自增强学习, 速度模型重建, 不适定问题

## 3 点简述
- 核心问题：传统深度先验全波形反演使用固定随机输入，无法利用网络输入输出映射，加剧反演不适定性。
- 方法要点：通过转向算法交替更新网络参数和输入，实现自适应结构增强和正则化改进。
- 实验或效果：合成和实地数据测试显示，该方法提升分辨率、精度和深度穿透，无需手动频带选择和时间窗选取。

## 摘要（原文）

> Full waveform inversion (FWI) has become a widely adopted technique for high-resolution subsurface imaging. However, its inherent strong nonlinearity often results in convergence toward local minima. Recently, deep image prior-based reparameterized FWI (DIP-FWI) has been proposed to alleviate the dependence on massive training data. By exploiting the spectral bias and implicit regularization in the neural network architecture, DIP-FWI can effectively avoid local minima and reconstruct more geologically plausible velocity models. Nevertheless, existing DIP-FWI typically use a fixed random input throughout the inversion process, which fails to utilize the mapping and correlation between the input and output of the network. Moreover, under complex geological conditions, the lack of informative prior in the input can exacerbate the ill-posedness of the inverse problem, leading to artifacts and unstable reconstructions. To address these limitations, we propose a self-reinforced DIP-FWI (SRDIP-FWI) framework, in which a steering algorithm alternately updates both the network parameters and the input at each iteration using feedback from the current network output. This design allows adaptive structural enhancement and improved regularization, thereby effectively mitigating the ill-posedness in FWI. Additionally, we analyze the spectral bias of the network in SRDIP-FWI and quantify its role in multiscale velocity model building. Synthetic tests and field land data application demonstrate that SRDIP-FWI achieves superior resolution, improved accuracy and greater depth penetration compared to multiscale FWI. More importantly, SRDIP-FWI eliminates the need for manual frequency-band selection and time-window picking, substantially simplifying the inversion workflow. Overall, the proposed method provides a novel, adaptive and robust framework for accurate subsurface velocity model reconstruction.

