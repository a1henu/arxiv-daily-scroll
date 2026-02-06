---
layout: default
title: Reduced-Order Surrogates for Forced Flexible Mesh Coastal-Ocean Models
---

# Reduced-Order Surrogates for Forced Flexible Mesh Coastal-Ocean Models
**arXiv**：[2602.05416v1](https://arxiv.org/abs/2602.05416) · [PDF](https://arxiv.org/pdf/2602.05416.pdf)  
**作者**：Freja Høgholm Petersen, Jesper Sandvig Mariegaard, Rocco Palmitessa, Allan P. Engsig-Karup  

**一句话要点**：提出灵活Koopman自编码器，结合气象强迫和边界条件，用于海岸-海洋模型降阶代理，提升长期预测精度。

**关键词**：降阶模型, Koopman自编码器, 海岸-海洋建模, 长期预测, 时间稳定性, 代理模型

## 3 点简述
- 核心问题：Koopman自编码器在真实海岸-海洋建模中应用有限，需评估其性能。
- 方法要点：引入灵活Koopman自编码器，结合学习线性时间算子和特征值正则化，促进时间稳定性。
- 实验或效果：在三个测试案例中，Koopman自编码器优于POD代理，相对均方根误差0.01-0.13，推理加速300-1400倍。

## 摘要（原文）

> While POD-based surrogates are widely explored for hydrodynamic applications, the use of Koopman Autoencoders for real-world coastal-ocean modelling remains relatively limited. This paper introduces a flexible Koopman autoencoder formulation that incorporates meteorological forcings and boundary conditions, and systematically compares its performance against POD-based surrogates. The Koopman autoencoder employs a learned linear temporal operator in latent space, enabling eigenvalue regularization to promote temporal stability. This strategy is evaluated alongside temporal unrolling techniques for achieving stable and accurate long-term predictions. The models are assessed on three test cases spanning distinct dynamical regimes, with prediction horizons up to one year at 30-minute temporal resolution. Across all cases, the Koopman autoencoder with temporal unrolling yields the best overall accuracy compared to the POD-based surrogates, achieving relative root-mean-squared-errors of 0.01-0.13 and $R^2$-values of 0.65-0.996. Prediction errors are largest for current velocities, and smallest for water surface elevations. Comparing to in-situ observations, the surrogate yields -0.65% to 12% change in water surface elevation prediction error when compared to prediction errors of the physics-based model. These error levels, corresponding to a few centimeters, are acceptable for many practical applications, while inference speed-ups of 300-1400x enables workflows such as ensemble forecasting and long climate simulations for coastal-ocean modelling.

