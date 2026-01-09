---
layout: default
title: GEnSHIN: Graphical Enhanced Spatio-temporal Hierarchical Inference Network for Traffic Flow Prediction
---

# GEnSHIN: Graphical Enhanced Spatio-temporal Hierarchical Inference Network for Traffic Flow Prediction
**arXiv**：[2601.04550v1](https://arxiv.org/abs/2601.04550) · [PDF](https://arxiv.org/pdf/2601.04550.pdf)  
**作者**：Zhiyan Zhou, Junjie Liao, Manho Zhang, Yingyi Liao, Ziai Wang  

**一句话要点**：提出GEnSHIN模型以解决交通流预测中的复杂时空依赖问题

**关键词**：交通流预测, 图神经网络, 时空依赖建模, 注意力机制, 动态图更新

## 3 点简述
- 核心问题：交通流预测需处理复杂时空依赖，现有方法可能不足。
- 方法要点：集成注意力增强GCRU、非对称双嵌入图生成和动态记忆库模块。
- 实验或效果：在METR-LA数据集上性能优越，尤其在早晚高峰表现稳定。

## 摘要（原文）

> With the acceleration of urbanization, intelligent transportation systems have an increasing demand for accurate traffic flow prediction. This paper proposes a novel Graph Enhanced Spatio-temporal Hierarchical Inference Network (GEnSHIN) to handle the complex spatio-temporal dependencies in traffic flow prediction. The model integrates three innovative designs: 1) An attention-enhanced Graph Convolutional Recurrent Unit (GCRU), which strengthens the modeling capability for long-term temporal dependencies by introducing Transformer modules; 2) An asymmetric dual-embedding graph generation mechanism, which leverages the real road network and data-driven latent asymmetric topology to generate graph structures that better fit the characteristics of actual traffic flow; 3) A dynamic memory bank module, which utilizes learnable traffic pattern prototypes to provide personalized traffic pattern representations for each sensor node, and introduces a lightweight graph updater during the decoding phase to adapt to dynamic changes in road network states. Extensive experiments on the public dataset METR-LA show that GEnSHIN achieves or surpasses the performance of comparative models across multiple metrics such as Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and Mean Absolute Percentage Error (MAPE). Notably, the model demonstrates excellent prediction stability during peak morning and evening traffic hours. Ablation experiments further validate the effectiveness of each core module and its contribution to the final performance.

