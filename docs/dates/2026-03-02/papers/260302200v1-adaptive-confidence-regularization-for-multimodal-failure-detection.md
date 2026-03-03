---
layout: default
title: Adaptive Confidence Regularization for Multimodal Failure Detection
---

# Adaptive Confidence Regularization for Multimodal Failure Detection
**arXiv**：[2603.02200v1](https://arxiv.org/abs/2603.02200) · [PDF](https://arxiv.org/pdf/2603.02200.pdf)  
**作者**：Moru Liu, Hao Dong, Olga Fink, Mario Trapp  

**一句话要点**：提出自适应置信度正则化框架以解决多模态失败检测问题

**关键词**：多模态失败检测, 置信度正则化, 自适应训练, 异常合成, 可靠性提升

## 3 点简述
- 核心问题：多模态模型在自动驾驶等高风险领域需可靠失败检测机制
- 方法要点：基于置信度退化现象设计自适应损失函数和特征交换合成异常
- 实验或效果：在四个数据集上验证了方法的稳健性和一致性提升

## 摘要（原文）

> The deployment of multimodal models in high-stakes domains, such as self-driving vehicles and medical diagnostics, demands not only strong predictive performance but also reliable mechanisms for detecting failures. In this work, we address the largely unexplored problem of failure detection in multimodal contexts. We propose Adaptive Confidence Regularization (ACR), a novel framework specifically designed to detect multimodal failures. Our approach is driven by a key observation: in most failure cases, the confidence of the multimodal prediction is significantly lower than that of at least one unimodal branch, a phenomenon we term confidence degradation. To mitigate this, we introduce an Adaptive Confidence Loss that penalizes such degradations during training. In addition, we propose Multimodal Feature Swapping, a novel outlier synthesis technique that generates challenging, failure-aware training examples. By training with these synthetic failures, ACR learns to more effectively recognize and reject uncertain predictions, thereby improving overall reliability. Extensive experiments across four datasets, three modalities, and multiple evaluation settings demonstrate that ACR achieves consistent and robust gains. The source code will be available at https://github.com/mona4399/ACR.

