---
layout: default
title: Federated Modality-specific Encoders and Partially Personalized Fusion Decoder for Multimodal Brain Tumor Segmentation
---

# Federated Modality-specific Encoders and Partially Personalized Fusion Decoder for Multimodal Brain Tumor Segmentation
**arXiv**：[2603.04887v1](https://arxiv.org/abs/2603.04887) · [PDF](https://arxiv.org/pdf/2603.04887.pdf)  
**作者**：Hong Liu, Dong Wei, Qian Dai, Xian Wu, Yefeng Zheng, Liansheng Wang  

**一句话要点**：提出FedMEPD框架，通过联邦模态特定编码器和部分个性化融合解码器解决多模态脑肿瘤分割中的模态间异质性和个性化需求。

**关键词**：联邦学习, 多模态分割, 脑肿瘤分割, 个性化模型, 模态间异质性, 融合解码器

## 3 点简述
- 核心问题：联邦学习中模态间异质性和参与者个性化需求并存，限制多模态医学图像分析应用。
- 方法要点：使用联邦模态特定编码器处理模态间异质性，部分个性化解码器动态调整参数以满足个体需求。
- 实验或效果：在BraTS 2018和2020基准测试中优于现有方法，验证了设计的有效性。

## 摘要（原文）

> Most existing federated learning (FL) methods for medical image analysis only considered intramodal heterogeneity, limiting their applicability to multimodal imaging applications. In practice, some FL participants may possess only a subset of the complete imaging modalities, posing intermodal heterogeneity as a challenge to effectively training a global model on all participants' data. Meanwhile, each participant expects a personalized model tailored to its local data characteristics in FL. This work proposes a new FL framework with federated modality-specific encoders and partially personalized multimodal fusion decoders (FedMEPD) to address the two concurrent issues. Specifically, FedMEPD employs an exclusive encoder for each modality to account for the intermodal heterogeneity. While these encoders are fully federated, the decoders are partially personalized to meet individual needs -- using the discrepancy between global and local parameter updates to dynamically determine which decoder filters are personalized. Implementation-wise, a server with full-modal data employs a fusion decoder to fuse representations from all modality-specific encoders, thus bridging the modalities to optimize the encoders via backpropagation. Moreover, multiple anchors are extracted from the fused multimodal representations and distributed to the clients in addition to the model parameters. Conversely, the clients with incomplete modalities calibrate their missing-modal representations toward the global full-modal anchors via scaled dot-product cross-attention, making up for the information loss due to absent modalities. FedMEPD is validated on the BraTS 2018 and 2020 multimodal brain tumor segmentation benchmarks. Results show that it outperforms various up-to-date methods for multimodal and personalized FL, and its novel designs are effective.

