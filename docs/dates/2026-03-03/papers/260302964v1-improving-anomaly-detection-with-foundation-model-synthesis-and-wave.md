---
layout: default
title: Improving Anomaly Detection with Foundation-Model Synthesis and Wavelet-Domain Attention
---

# Improving Anomaly Detection with Foundation-Model Synthesis and Wavelet-Domain Attention
**arXiv**：[2603.02964v1](https://arxiv.org/abs/2603.02964) · [PDF](https://arxiv.org/pdf/2603.02964.pdf)  
**作者**：Wensheng Wu, Zheming Lu, Ziqian Lu, Zewei He, Xuecheng Sun, Zhao Wang, Jungong Han, Yunlong Yu  

**一句话要点**：提出基于基础模型的异常合成与频域注意力模块，以提升工业异常检测性能。

**关键词**：工业异常检测, 基础模型合成, 频域注意力, 小波变换, 即插即用模块, 性能提升

## 3 点简述
- 工业异常检测面临异常样本稀缺和真实异常复杂性的挑战。
- 方法包括无需微调的异常合成管道和自适应子带处理的频域注意力模块。
- 在MVTec AD和VisA数据集上验证了作为即插即用模块的显著性能提升。

## 摘要（原文）

> Industrial anomaly detection faces significant challenges due to the scarcity of anomalous samples and the complexity of real-world anomalies. In this paper, we propose a foundation model-based anomaly synthesis pipeline (FMAS) that generates highly realistic anomalous samples without fine-tuning or class-specific training. Motivated by the distinct frequency-domain characteristics of anomalies, we introduce aWavelet Domain Attention Module (WDAM), which exploits adaptive sub-band processing to enhance anomaly feature extraction. The combination of FMAS and WDAM significantly improves anomaly detection sensitivity while maintaining computational efficiency. Comprehensive experiments on MVTec AD and VisA datasets demonstrate that WDAM, as a plug-and-play module, achieves substantial performance gains against existing baselines.

