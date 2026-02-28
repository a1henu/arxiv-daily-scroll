---
layout: default
title: Takeuchi's Information Criteria as Generalization Measures for DNNs Close to NTK Regime
---

# Takeuchi's Information Criteria as Generalization Measures for DNNs Close to NTK Regime
**arXiv**：[2602.23219v1](https://arxiv.org/abs/2602.23219) · [PDF](https://arxiv.org/pdf/2602.23219.pdf)  
**作者**：Hiroki Naganuma, Taiji Suzuki, Rio Yokota, Masahiro Nomura, Kohta Ishikawa, Ikuro Sato  

**一句话要点**：探究Takeuchi信息准则在接近NTK机制下作为深度神经网络泛化度量的有效性

**关键词**：泛化度量, Takeuchi信息准则, 神经切线机制, 深度神经网络, 超参数优化, 统计奇异模型

## 3 点简述
- 研究深度神经网络泛化度量难题，聚焦Takeuchi信息准则在统计奇异模型中的应用条件
- 理论分析表明TIC在接近神经切线机制时有效，实验训练超5000个模型验证相关性
- TIC在NTK机制外相关性消失，但优于现有方法用于超参数优化的试验剪枝

## 摘要（原文）

> Generalization measures have been studied extensively in the machine learning community to better characterize generalization gaps. However, establishing a reliable generalization measure for statistically singular models such as deep neural networks (DNNs) is difficult due to their complex nature. This study focuses on Takeuchi's information criterion (TIC) to investigate the conditions under which this classical measure can effectively explain the generalization gaps of DNNs. Importantly, the developed theory indicates the applicability of TIC near the neural tangent kernel (NTK) regime. In a series of experiments, we trained more than 5,000 DNN models with 12 architectures, including large models (e.g., VGG-16), on four datasets, and estimated the corresponding TIC values to examine the relationship between the generalization gap and the TIC estimates. We applied several TIC approximation methods with feasible computational costs and assessed the accuracy trade-off. Our experimental results indicate that the estimated TIC values correlate well with the generalization gap under conditions close to the NTK regime. However, we show both theoretically and empirically that outside the NTK regime such correlation disappears. Finally, we demonstrate that TIC provides better trial pruning ability than existing methods for hyperparameter optimization.

