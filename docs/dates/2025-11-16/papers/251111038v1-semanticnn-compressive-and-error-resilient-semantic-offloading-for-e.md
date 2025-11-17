---
layout: default
title: SemanticNN: Compressive and Error-Resilient Semantic Offloading for Extremely Weak Devices
---

# SemanticNN: Compressive and Error-Resilient Semantic Offloading for Extremely Weak Devices
**arXiv**：[2511.11038v1](https://arxiv.org/abs/2511.11038) · [PDF](https://arxiv.org/pdf/2511.11038.pdf)  
**作者**：Jiaming Huang, Yi Gao, Fuchang Pan, Renjie Li, Wei Dong  

**一句话要点**：提出SemanticNN语义编解码器以解决极弱设备在动态信道下的高效协作推理卸载问题

**关键词**：语义通信, 设备边缘协作, 容错推理, 特征压缩, 嵌入式AI, 动态信道适应

## 3 点简述
- 核心问题：极弱嵌入式设备资源受限且网络不可靠，传统比特级传输方法效率低下
- 方法要点：采用BER感知解码器和软量化编码器，实现语义级容错与压缩表示
- 实验效果：在STM32上测试，特征传输量减少56.82-344.83倍，同时保持高推理精度

## 摘要（原文）

> With the rapid growth of the Internet of Things (IoT), integrating artificial intelligence (AI) on extremely weak embedded devices has garnered significant attention, enabling improved real-time performance and enhanced data privacy. However, the resource limitations of such devices and unreliable network conditions necessitate error-resilient device-edge collaboration systems. Traditional approaches focus on bit-level transmission correctness, which can be inefficient under dynamic channel conditions. In contrast, we propose SemanticNN, a semantic codec that tolerates bit-level errors in pursuit of semantic-level correctness, enabling compressive and resilient collaborative inference offloading under strict computational and communication constraints. It incorporates a Bit Error Rate (BER)-aware decoder that adapts to dynamic channel conditions and a Soft Quantization (SQ)-based encoder to learn compact representations. Building on this architecture, we introduce Feature-augmentation Learning, a novel training strategy that enhances offloading efficiency. To address encoder-decoder capability mismatches from asymmetric resources, we propose XAI-based Asymmetry Compensation to enhance decoding semantic fidelity. We conduct extensive experiments on STM32 using three models and six datasets across image classification and object detection tasks. Experimental results demonstrate that, under varying transmission error rates, SemanticNN significantly reduces feature transmission volume by 56.82-344.83x while maintaining superior inference accuracy.

