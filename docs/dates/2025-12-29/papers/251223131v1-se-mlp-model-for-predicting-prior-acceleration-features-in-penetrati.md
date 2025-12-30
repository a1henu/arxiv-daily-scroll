---
layout: default
title: SE-MLP Model for Predicting Prior Acceleration Features in Penetration Signals
---

# SE-MLP Model for Predicting Prior Acceleration Features in Penetration Signals
**arXiv**：[2512.23131v1](https://arxiv.org/abs/2512.23131) · [PDF](https://arxiv.org/pdf/2512.23131.pdf)  
**作者**：Yankang Li, Changsheng Li  

**一句话要点**：提出SE-MLP模型以快速预测侵彻信号先验加速度特征，解决仿真计算耗时昂贵问题。

**关键词**：侵彻信号处理, 加速度特征预测, 多层感知机, 通道注意力机制, 残差连接, 工程应用验证

## 3 点简述
- 核心问题：侵彻过程识别依赖先验加速度特征，但传统方法仿真周期长、计算成本高。
- 方法要点：集成通道注意力机制与残差连接的多层感知机，建立物理参数到加速度特征的非线性映射。
- 实验或效果：相比MLP、XGBoost和Transformer，SE-MLP在预测精度、泛化性和稳定性上表现更优，工程误差可接受。

## 摘要（原文）

> Accurate identification of the penetration process relies heavily on prior feature values of penetration acceleration. However, these feature values are typically obtained through long simulation cycles and expensive computations. To overcome this limitation, this paper proposes a multi-layer Perceptron architecture, termed squeeze and excitation multi-layer perceptron (SE-MLP), which integrates a channel attention mechanism with residual connections to enable rapid prediction of acceleration feature values. Using physical parameters under different working conditions as inputs, the model outputs layer-wise acceleration features, thereby establishing a nonlinear mapping between physical parameters and penetration characteristics. Comparative experiments against conventional MLP, XGBoost, and Transformer models demonstrate that SE-MLP achieves superior prediction accuracy, generalization, and stability. Ablation studies further confirm that both the channel attention module and residual structure contribute significantly to performance gains. Numerical simulations and range recovery tests show that the discrepancies between predicted and measured acceleration peaks and pulse widths remain within acceptable engineering tolerances. These results validate the feasibility and engineering applicability of the proposed method and provide a practical basis for rapidly generating prior feature values for penetration fuzes.

