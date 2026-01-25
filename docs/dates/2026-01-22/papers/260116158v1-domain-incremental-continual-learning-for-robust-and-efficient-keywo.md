---
layout: default
title: Domain-Incremental Continual Learning for Robust and Efficient Keyword Spotting in Resource Constrained Systems
---

# Domain-Incremental Continual Learning for Robust and Efficient Keyword Spotting in Resource Constrained Systems
**arXiv**：[2601.16158v1](https://arxiv.org/abs/2601.16158) · [PDF](https://arxiv.org/pdf/2601.16158.pdf)  
**作者**：Prakash Dhungana, Sayed Ahmad Salehi  

**一句话要点**：提出基于原型更新的领域增量持续学习框架，以提升资源受限系统中关键词检测的鲁棒性与效率。

**关键词**：关键词检测, 持续学习, 领域增量学习, 去噪技术, 资源受限系统, 原型更新

## 3 点简述
- 核心问题：边缘设备上关键词检测模型因噪声和录制条件变化导致领域偏移，影响准确性和鲁棒性。
- 方法要点：集成双输入CNN、多阶段去噪和原型更新机制，支持完整量化模型更新，结合伪标签和重放缓冲进行增量训练。
- 实验或效果：在嘈杂测试集上验证，清洁数据准确率达99.63%，-10 dB信噪比下仍保持超过94%的鲁棒性能。

## 摘要（原文）

> Keyword Spotting (KWS) systems with small footprint models deployed on edge devices face significant accuracy and robustness challenges due to domain shifts caused by varying noise and recording conditions. To address this, we propose a comprehensive framework for continual learning designed to adapt to new domains while maintaining computational efficiency. The proposed pipeline integrates a dual-input Convolutional Neural Network, utilizing both Mel Frequency Cepstral Coefficients (MFCC) and Mel-spectrogram features, supported by a multi-stage denoising process, involving discrete wavelet transform and spectral subtraction techniques, plus model and prototype update blocks. Unlike prior methods that restrict updates to specific layers, our approach updates the complete quantized model, made possible due to compact model architecture. A subset of input samples are selected during runtime using class prototypes and confidence-driven filtering, which are then pseudo-labeled and combined with rehearsal buffer for incremental model retraining. Experimental results on noisy test dataset demonstrate the framework's effectiveness, achieving 99.63\% accuracy on clean data and maintaining robust performance (exceeding 94\% accuracy) across diverse noisy environments, even at -10 dB Signal-to-Noise Ratio. The proposed framework work confirms that integrating efficient denoising with prototype-based continual learning enables KWS models to operate autonomously and robustly in resource-constrained, dynamic environments.

