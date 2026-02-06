---
layout: default
title: EoCD: Encoder only Remote Sensing Change Detection
---

# EoCD: Encoder only Remote Sensing Change Detection
**arXiv**：[2602.05882v1](https://arxiv.org/abs/2602.05882) · [PDF](https://arxiv.org/pdf/2602.05882.pdf)  
**作者**：Mubashir Noman, Mustansar Fiaz, Hiyam Debary, Abdul Hannan, Shah Nawaz, Fahad Shahbaz Khan, Salman Khan  

**一句话要点**：提出EoCD方法，通过早期融合与无参数多尺度特征融合模块简化遥感变化检测模型。

**关键词**：遥感变化检测, 早期融合, 无参数特征融合, 编码器简化, 模型复杂度降低

## 3 点简述
- 现有方法依赖孪生编码器或复杂解码器，导致计算成本高且模型复杂。
- EoCD采用早期融合时间数据，并用无参数多尺度特征融合模块替代解码器，显著降低模型复杂度。
- 在四个挑战性数据集上实验显示，EoCD在性能与预测速度间取得平衡，且性能主要依赖编码器。

## 摘要（原文）

> Being a cornerstone of temporal analysis, change detection has been playing a pivotal role in modern earth observation. Existing change detection methods rely on the Siamese encoder to individually extract temporal features followed by temporal fusion. Subsequently, these methods design sophisticated decoders to improve the change detection performance without taking into consideration the complexity of the model. These aforementioned issues intensify the overall computational cost as well as the network's complexity which is undesirable. Alternatively, few methods utilize the early fusion scheme to combine the temporal images. These methods prevent the extra overhead of Siamese encoder, however, they also rely on sophisticated decoders for better performance. In addition, these methods demonstrate inferior performance as compared to late fusion based methods. To bridge these gaps, we introduce encoder only change detection (EoCD) that is a simple and effective method for the change detection task. The proposed method performs the early fusion of the temporal data and replaces the decoder with a parameter-free multiscale feature fusion module thereby significantly reducing the overall complexity of the model. EoCD demonstrate the optimal balance between the change detection performance and the prediction speed across a variety of encoder architectures. Additionally, EoCD demonstrate that the performance of the model is predominantly dependent on the encoder network, making the decoder an additional component. Extensive experimentation on four challenging change detection datasets reveals the effectiveness of the proposed method.

