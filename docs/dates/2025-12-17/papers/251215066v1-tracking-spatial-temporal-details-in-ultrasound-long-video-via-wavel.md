---
layout: default
title: Tracking spatial temporal details in ultrasound long video via wavelet analysis and memory bank
---

# Tracking spatial temporal details in ultrasound long video via wavelet analysis and memory bank
**arXiv**：[2512.15066v1](https://arxiv.org/abs/2512.15066) · [PDF](https://arxiv.org/pdf/2512.15066.pdf)  
**作者**：Chenxiao Zhang, Runshi Zhang, Junchen Wang  

**一句话要点**：提出基于记忆库的小波滤波融合网络，以解决超声长视频中低对比度和小目标分割与跟踪问题。

**关键词**：超声视频分割, 小波分析, 记忆库, 长视频跟踪, 高频特征融合

## 3 点简述
- 核心问题：超声视频低对比度和噪声背景导致器官边界误分割和小目标丢失，长视频目标跟踪困难。
- 方法要点：采用编码器-解码器结构，结合记忆库小波卷积、级联小波压缩和长短期记忆库，提取高频细节特征。
- 实验或效果：在四个超声视频数据集上测试，分割指标显著提升，尤其在小甲状腺结节分割中表现优异。

## 摘要（原文）

> Medical ultrasound videos are widely used for medical inspections, disease diagnosis and surgical planning. High-fidelity lesion area and target organ segmentation constitutes a key component of the computer-assisted surgery workflow. The low contrast levels and noisy backgrounds of ultrasound videos cause missegmentation of organ boundary, which may lead to small object losses and increase boundary segmentation errors. Object tracking in long videos also remains a significant research challenge. To overcome these challenges, we propose a memory bank-based wavelet filtering and fusion network, which adopts an encoder-decoder structure to effectively extract fine-grained detailed spatial features and integrate high-frequency (HF) information. Specifically, memory-based wavelet convolution is presented to simultaneously capture category, detailed information and utilize adjacent information in the encoder. Cascaded wavelet compression is used to fuse multiscale frequency-domain features and expand the receptive field within each convolutional layer. A long short-term memory bank using cross-attention and memory compression mechanisms is designed to track objects in long video. To fully utilize the boundary-sensitive HF details of feature maps, an HF-aware feature fusion module is designed via adaptive wavelet filters in the decoder. In extensive benchmark tests conducted on four ultrasound video datasets (two thyroid nodule, the thyroid gland, the heart datasets) compared with the state-of-the-art methods, our method demonstrates marked improvements in segmentation metrics. In particular, our method can more accurately segment small thyroid nodules, demonstrating its effectiveness for cases involving small ultrasound objects in long video. The code is available at https://github.com/XiAooZ/MWNet.

