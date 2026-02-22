---
layout: default
title: DRetHTR: Linear-Time Decoder-Only Retentive Network for Handwritten Text Recognition
---

# DRetHTR: Linear-Time Decoder-Only Retentive Network for Handwritten Text Recognition
**arXiv**：[2602.17387v1](https://arxiv.org/abs/2602.17387) · [PDF](https://arxiv.org/pdf/2602.17387.pdf)  
**作者**：Changhun Kim, Martin Mayr, Thomas Gorges, Fei Wu, Mathias Seuret, Andreas Maier, Vincent Christlein  

**一句话要点**：提出DRetHTR以解决手写文本识别中Transformer解码慢和内存占用高的问题

**关键词**：手写文本识别, Retentive Networks, 解码器模型, 线性时间解码, 内存效率, 软注意力替代

## 3 点简述
- 核心问题：Transformer在手写文本识别中因KV缓存增长导致解码慢和内存密集
- 方法要点：基于Retentive Networks构建解码器，用软注意力替代软注意力并注入多尺度序列先验
- 实验或效果：在IAM-A、RIMES和Bentham数据集上实现最佳字符错误率，解码速度提升1.6-1.9倍，内存使用减少38-42%

## 摘要（原文）

> State-of-the-art handwritten text recognition (HTR) systems commonly use Transformers, whose growing key-value (KV) cache makes decoding slow and memory-intensive. We introduce DRetHTR, a decoder-only model built on Retentive Networks (RetNet). Compared to an equally sized decoder-only Transformer baseline, DRetHTR delivers 1.6-1.9x faster inference with 38-42% less memory usage, without loss of accuracy. By replacing softmax attention with softmax-free retention and injecting multi-scale sequential priors, DRetHTR avoids a growing KV cache: decoding is linear in output length in both time and memory. To recover the local-to-global inductive bias of attention, we propose layer-wise gamma scaling, which progressively enlarges the effective retention horizon in deeper layers. This encourages early layers to model short-range dependencies and later layers to capture broader context, mitigating the flexibility gap introduced by removing softmax. Consequently, DRetHTR achieves best reported test character error rates of 2.26% (IAM-A, en), 1.81% (RIMES, fr), and 3.46% (Bentham, en), and is competitive on READ-2016 (de) with 4.21%. This demonstrates that decoder-only RetNet enables Transformer-level HTR accuracy with substantially improved decoding speed and memory efficiency.

