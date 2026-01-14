---
layout: default
title: Decodable but not structured: linear probing enables Underwater Acoustic Target Recognition with pretrained audio embeddings
---

# Decodable but not structured: linear probing enables Underwater Acoustic Target Recognition with pretrained audio embeddings
**arXiv**：[2601.08358v1](https://arxiv.org/abs/2601.08358) · [PDF](https://arxiv.org/pdf/2601.08358.pdf)  
**作者**：Hilde I. Hummel, Sandjai Bhulai, Rob D. van der Mei, Burooj Ghani  

**一句话要点**：提出线性探测方法，利用预训练音频嵌入实现水下声学目标识别，降低标注数据需求。

**关键词**：水下声学目标识别, 迁移学习, 线性探测, 预训练音频嵌入, 被动声学监测

## 3 点简述
- 核心问题：水下声学目标识别因标注数据稀缺而受限，需自动化方法监测船舶噪声影响。
- 方法要点：冻结预训练音频模型权重，通过线性探测抑制录音特异性，提取船舶类型特征。
- 实验或效果：线性探测在低计算成本下实现有效识别，显著减少高质量标注数据需求。

## 摘要（原文）

> Increasing levels of anthropogenic noise from ships contribute significantly to underwater sound pollution, posing risks to marine ecosystems. This makes monitoring crucial to understand and quantify the impact of the ship radiated noise. Passive Acoustic Monitoring (PAM) systems are widely deployed for this purpose, generating years of underwater recordings across diverse soundscapes. Manual analysis of such large-scale data is impractical, motivating the need for automated approaches based on machine learning. Recent advances in automatic Underwater Acoustic Target Recognition (UATR) have largely relied on supervised learning, which is constrained by the scarcity of labeled data. Transfer Learning (TL) offers a promising alternative to mitigate this limitation. In this work, we conduct the first empirical comparative study of transfer learning for UATR, evaluating multiple pretrained audio models originating from diverse audio domains. The pretrained model weights are frozen, and the resulting embeddings are analyzed through classification, clustering, and similarity-based evaluations. The analysis shows that the geometrical structure of the embedding space is largely dominated by recording-specific characteristics. However, a simple linear probe can effectively suppress this recording-specific information and isolate ship-type features from these embeddings. As a result, linear probing enables effective automatic UATR using pretrained audio models at low computational cost, significantly reducing the need for a large amounts of high-quality labeled ship recordings.

