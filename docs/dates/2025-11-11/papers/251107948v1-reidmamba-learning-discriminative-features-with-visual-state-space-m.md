---
layout: default
title: ReIDMamba: Learning Discriminative Features with Visual State Space Model for Person Re-Identification
---

# ReIDMamba: Learning Discriminative Features with Visual State Space Model for Person Re-Identification
**arXiv**：[2511.07948v1](https://arxiv.org/abs/2511.07948) · [PDF](https://arxiv.org/pdf/2511.07948.pdf)  
**作者**：Hongyang Gu, Qisong Yang, Lei Pu, Siming Han, Yao Ding  

**一句话要点**：提出ReIDMamba框架，利用Mamba模型解决行人重识别中特征提取的扩展性问题

**关键词**：行人重识别, Mamba模型, 多粒度特征, 特征提取, 状态空间模型

## 3 点简述
- 核心问题：Transformer在行人重识别中面临内存和计算复杂度随序列长度二次增长的问题
- 方法要点：设计Mamba基线，引入多类令牌和多粒度特征提取器，增强特征判别性和鲁棒性
- 实验或效果：在五个基准测试中达到SOTA，参数减少三分之二，推理速度更快

## 摘要（原文）

> Extracting robust discriminative features is a critical challenge in person re-identification (ReID). While Transformer-based methods have successfully addressed some limitations of convolutional neural networks (CNNs), such as their local processing nature and information loss resulting from convolution and downsampling operations, they still face the scalability issue due to the quadratic increase in memory and computational requirements with the length of the input sequence. To overcome this, we propose a pure Mamba-based person ReID framework named ReIDMamba. Specifically, we have designed a Mamba-based strong baseline that effectively leverages fine-grained, discriminative global features by introducing multiple class tokens. To further enhance robust features learning within Mamba, we have carefully designed two novel techniques. First, the multi-granularity feature extractor (MGFE) module, designed with a multi-branch architecture and class token fusion, effectively forms multi-granularity features, enhancing both discrimination ability and fine-grained coverage. Second, the ranking-aware triplet regularization (RATR) is introduced to reduce redundancy in features from multiple branches, enhancing the diversity of multi-granularity features by incorporating both intra-class and inter-class diversity constraints, thus ensuring the robustness of person features. To our knowledge, this is the pioneering work that integrates a purely Mamba-driven approach into ReID research. Our proposed ReIDMamba model boasts only one-third the parameters of TransReID, along with lower GPU memory usage and faster inference throughput. Experimental results demonstrate ReIDMamba's superior and promising performance, achieving state-of-the-art performance on five person ReID benchmarks. Code is available at https://github.com/GuHY777/ReIDMamba.

