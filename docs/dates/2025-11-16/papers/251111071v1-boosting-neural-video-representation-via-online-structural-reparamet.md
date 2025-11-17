---
layout: default
title: Boosting Neural Video Representation via Online Structural Reparameterization
---

# Boosting Neural Video Representation via Online Structural Reparameterization
**arXiv**：[2511.11071v1](https://arxiv.org/abs/2511.11071) · [PDF](https://arxiv.org/pdf/2511.11071.pdf)  
**作者**：Ziyi Li, Qingyu Mao, Shuai Liu, Qilei Li, Fanyang Meng, Yongsheng Liang  

**一句话要点**：提出在线结构重参数化框架以增强神经视频表示能力

**关键词**：神经视频表示, 在线重参数化, 视频压缩, 模型容量增强, 计算效率优化

## 3 点简述
- 神经视频表示模型容量有限，导致性能瓶颈和计算开销大
- 引入多分支卷积块和在线重参数化，动态融合参数提升模型能力
- 实验显示PSNR平均提升0.37-2.7 dB，保持训练和推理效率

## 摘要（原文）

> Neural Video Representation~(NVR) is a promising paradigm for video compression, showing great potential in improving video storage and transmission efficiency. While recent advances have made efforts in architectural refinements to improve representational capability, these methods typically involve complex designs, which may incur increased computational overhead and lack the flexibility to integrate into other frameworks. Moreover, the inherent limitation in model capacity restricts the expressiveness of NVR networks, resulting in a performance bottleneck. To overcome these limitations, we propose Online-RepNeRV, a NVR framework based on online structural reparameterization. Specifically, we propose a universal reparameterization block named ERB, which incorporates multiple parallel convolutional paths to enhance the model capacity. To mitigate the overhead, an online reparameterization strategy is adopted to dynamically fuse the parameters during training, and the multi-branch structure is equivalently converted into a single-branch structure after training. As a result, the additional computational and parameter complexity is confined to the encoding stage, without affecting the decoding efficiency. Extensive experiments on mainstream video datasets demonstrate that our method achieves an average PSNR gain of 0.37-2.7 dB over baseline methods, while maintaining comparable training time and decoding speed.

