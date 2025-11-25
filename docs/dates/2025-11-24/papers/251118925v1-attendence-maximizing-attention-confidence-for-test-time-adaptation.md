---
layout: default
title: AttenDence: Maximizing Attention Confidence for Test Time Adaptation
---

# AttenDence: Maximizing Attention Confidence for Test Time Adaptation
**arXiv**：[2511.18925v1](https://arxiv.org/abs/2511.18925) · [PDF](https://arxiv.org/pdf/2511.18925.pdf)  
**作者**：Yash Mali  

**一句话要点**：提出最小化注意力分布熵以增强测试时适应中模型对相关图像区域的关注置信度

**关键词**：测试时适应, 注意力机制, 熵最小化, 分布偏移, Transformer模型

## 3 点简述
- 核心问题：测试时分布偏移下模型适应能力不足，传统方法依赖输出分布熵最小化
- 方法要点：利用Transformer注意力机制，最小化CLS令牌到图像补丁的注意力分布熵
- 实验或效果：在多种损坏类型下提升鲁棒性，单测试样本有效，不影响干净数据性能

## 摘要（原文）

> Test-time adaptation (TTA) enables models to adapt to distribution shifts at inference time. While entropy minimization over the output distribution has proven effective for TTA, transformers offer an additional unsupervised learning signal through their attention mechanisms. We propose minimizing the entropy of attention distributions from the CLS token to image patches as a novel TTA objective.This approach encourages the model to attend more confidently to relevant image regions under distribution shift and is effective even when only a single test image is available. We demonstrate that attention entropy minimization improves robustness across diverse corruption types while not hurting performance on clean data on a single sample stream of images at test time.

