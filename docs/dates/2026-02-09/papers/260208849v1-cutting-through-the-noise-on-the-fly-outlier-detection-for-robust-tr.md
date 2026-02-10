---
layout: default
title: Cutting Through the Noise: On-the-fly Outlier Detection for Robust Training of Machine Learning Interatomic Potentials
---

# Cutting Through the Noise: On-the-fly Outlier Detection for Robust Training of Machine Learning Interatomic Potentials
**arXiv**：[2602.08849v1](https://arxiv.org/abs/2602.08849) · [PDF](https://arxiv.org/pdf/2602.08849.pdf)  
**作者**：Terry C. W. Lam, Niamh O'Neill, Christoph Schran, Lars L. Schaaf  

**一句话要点**：提出在线离群点检测方案以提升机器学习原子间势在含噪数据上的训练鲁棒性

**关键词**：机器学习原子间势, 离群点检测, 鲁棒训练, 指数移动平均, SPICE数据集

## 3 点简述
- 机器学习原子间势的准确性受数值噪声影响，噪声源于未收敛或不一致的电子结构计算
- 通过指数移动平均跟踪损失分布，在单次训练中自动识别并降权离群点，无需额外参考计算
- 实验表明该方法防止过拟合，在液态水和SPICE数据集上显著提升性能，降低能量误差

## 摘要（原文）

> The accuracy of machine learning interatomic potentials suffers from reference data that contains numerical noise. Often originating from unconverged or inconsistent electronic-structure calculations, this noise is challenging to identify. Existing mitigation strategies such as manual filtering or iterative refinement of outliers, require either substantial expert effort or multiple expensive retraining cycles, making them difficult to scale to large datasets. Here, we introduce an on-the-fly outlier detection scheme that automatically down-weights noisy samples, without requiring additional reference calculations. By tracking the loss distribution via an exponential moving average, this unsupervised method identifies outliers throughout a single training run. We show that this approach prevents overfitting and matches the performance of iterative refinement baselines with significantly reduced overhead. The method's effectiveness is demonstrated by recovering accurate physical observables for liquid water from unconverged reference data, including diffusion coefficients. Furthermore, we validate its scalability by training a foundation model for organic chemistry on the SPICE dataset, where it reduces energy errors by a factor of three. This framework provides a simple, automated solution for training robust models on imperfect datasets across dataset sizes.

