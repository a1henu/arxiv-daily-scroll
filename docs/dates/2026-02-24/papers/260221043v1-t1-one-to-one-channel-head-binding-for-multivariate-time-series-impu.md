---
layout: default
title: T1: One-to-One Channel-Head Binding for Multivariate Time-Series Imputation
---

# T1: One-to-One Channel-Head Binding for Multivariate Time-Series Imputation
**arXiv**：[2602.21043v1](https://arxiv.org/abs/2602.21043) · [PDF](https://arxiv.org/pdf/2602.21043.pdf)  
**作者**：Dongik Park, Hyunwoo Ryu, Suahn Bae, Keondo Park, Hyung-Sin Kim  

**一句话要点**：提出T1模型，通过通道-头绑定机制解决多元时间序列缺失值插补问题。

**关键词**：多元时间序列插补, 通道-头绑定, CNN-Transformer混合架构, 缺失值处理, 自适应注意力

## 3 点简述
- 核心问题：多元时间序列缺失值插补在多样缺失模式和重度缺失下性能不佳，现有方法难以平衡时间模式提取与跨变量信息选择性转移。
- 方法要点：采用CNN-Transformer混合架构，引入通道-头绑定机制，实现CNN通道与注意力头的一对一对应，自适应调整信息转移权重。
- 实验或效果：在11个基准数据集上实现最优性能，平均MSE降低46%，在极端稀疏（70%缺失率）下表现突出，无需重训练即可泛化到未见缺失模式。

## 摘要（原文）

> Imputing missing values in multivariate time series remains challenging, especially under diverse missing patterns and heavy missingness. Existing methods suffer from suboptimal performance as corrupted temporal features hinder effective cross-variable information transfer, amplifying reconstruction errors. Robust imputation requires both extracting temporal patterns from sparse observations within each variable and selectively transferring information across variables--yet current approaches excel at one while compromising the other. We introduce T1 (Time series imputation with 1-to-1 channel-head binding), a CNN-Transformer hybrid architecture that achieves robust imputation through Channel-Head Binding--a mechanism creating one-to-one correspondence between CNN channels and attention heads. This design enables selective information transfer: when missingness corrupts certain temporal patterns, their corresponding attention pathways adaptively down-weight based on remaining observable patterns while preserving reliable cross-variable connections through unaffected channels. Experiments on 11 benchmark datasets demonstrate that T1 achieves state-of-the-art performance, reducing MSE by 46% on average compared to the second-best baseline, with particularly strong gains under extreme sparsity (70% missing ratio). The model generalizes to unseen missing patterns without retraining and uses a consistent hyperparameter configuration across all datasets. The code is available at https://github.com/Oppenheimerdinger/T1.

