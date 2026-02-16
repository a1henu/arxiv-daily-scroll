---
layout: default
title: Channel-Aware Probing for Multi-Channel Imaging
---

# Channel-Aware Probing for Multi-Channel Imaging
**arXiv**：[2602.12696v1](https://arxiv.org/abs/2602.12696) · [PDF](https://arxiv.org/pdf/2602.12696.pdf)  
**作者**：Umar Marikkar, Syed Sameed Husain, Muhammad Awais, Sara Atito  

**一句话要点**：提出通道感知探测以解决多通道成像中预训练编码器重用难题

**关键词**：多通道成像, 预训练编码器, 通道感知探测, 独立特征编码, 分离池化, 视觉编码器评估

## 3 点简述
- 多通道成像数据通道配置多变，阻碍预训练编码器重用和固定通道训练
- CAP通过独立特征编码和分离池化，在编码器和探测层控制特征流以利用通道多样性
- 在三个基准测试中，CAP提升探测性能，匹配从头训练，并缩小与全微调的差距

## 摘要（原文）

> Training and evaluating vision encoders on Multi-Channel Imaging (MCI) data remains challenging as channel configurations vary across datasets, preventing fixed-channel training and limiting reuse of pre-trained encoders on new channel settings. Prior work trains MCI encoders but typically evaluates them via full fine-tuning, leaving probing with frozen pre-trained encoders comparatively underexplored. Existing studies that perform probing largely focus on improving representations, rather than how to best leverage fixed representations for downstream tasks. Although the latter problem has been studied in other domains, directly transferring those strategies to MCI yields weak results, even worse than training from scratch. We therefore propose Channel-Aware Probing (CAP), which exploits the intrinsic inter-channel diversity in MCI datasets by controlling feature flow at both the encoder and probe levels. CAP uses Independent Feature Encoding (IFE) to encode each channel separately, and Decoupled Pooling (DCP) to pool within channels before aggregating across channels. Across three MCI benchmarks, CAP consistently improves probing performance over the default probing protocol, matches fine-tuning from scratch, and largely reduces the gap to full fine-tuning from the same MCI pre-trained checkpoints. Code can be found in https://github.com/umarikkar/CAP.

