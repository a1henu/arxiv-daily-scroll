---
layout: default
title: Leveraging generative adversarial networks with spatially adaptive denormalization for multivariate stochastic seismic data inversion
---

# Leveraging generative adversarial networks with spatially adaptive denormalization for multivariate stochastic seismic data inversion
**arXiv**：[2512.02863v1](https://arxiv.org/abs/2512.02863) · [PDF](https://arxiv.org/pdf/2512.02863.pdf)  
**作者**：Roberto Miele, Leonardo Azevedo  

**一句话要点**：提出SPADE-GANInv算法，利用空间自适应去归一化GAN进行地震数据多变量随机反演

**关键词**：生成对抗网络, 地震反演, 多变量预测, 空间自适应去归一化, 地统计模拟, 概率建模

## 3 点简述
- 核心问题：传统GAN在多变量地震反演中网络大、不稳定，难以预测耦合属性。
- 方法要点：集成预训练SPADE-GAN与地统计模拟，迭代更新概率模型以预测岩相和连续属性。
- 实验或效果：在合成和现场数据中验证，能准确预测岩相、孔隙度和声阻抗，减少先验偏差影响。

## 摘要（原文）

> Probabilistic seismic inverse modeling often requires the prediction of both spatially correlated geological heterogeneities (e.g., facies) and continuous parameters (e.g., rock and elastic properties). Generative adversarial networks (GANs) provide an efficient training-image-based simulation framework capable of reproducing complex geological models with high accuracy and comparably low generative cost. However, their application in stochastic geophysical inversion for multivariate property prediction is limited, as representing multiple coupled properties requires large and unstable networks with high memory and training demands. A more recent variant of GANs with spatially adaptive denormalization (SPADE-GAN) enables the direct conditioning of facies spatial distributions on local probability maps. Leveraging on such features, an iterative geostatistical inversion algorithm is proposed, SPADE-GANInv, integrating a pre-trained SPADE-GAN with geostatistical simulation, for the prediction of facies and multiple correlated continuous properties from seismic data. The SPADE-GAN is trained to reproduce realistic facies geometries, while sequential stochastic co-simulation predicts the spatial variability of the facies-dependent continuous properties. At each iteration, a set of subsurface realizations is generated and used to compute synthetic seismic data. The realizations providing the highest similarity coefficient to the observed data are used to update the subsurface probability models in the next iteration. The method is demonstrated on both 2-D synthetic scenarios and field data, targeting the prediction of facies, porosity, and acoustic impedance from full-stack seismic data. Results show that the algorithm enables accurate multivariate prediction, mitigates the impact of biased prior data, and accommodates additional local conditioning such as well logs.

