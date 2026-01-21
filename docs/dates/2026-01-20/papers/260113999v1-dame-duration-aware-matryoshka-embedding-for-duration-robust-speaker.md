---
layout: default
title: DAME: Duration-Aware Matryoshka Embedding for Duration-Robust Speaker Verification
---

# DAME: Duration-Aware Matryoshka Embedding for Duration-Robust Speaker Verification
**arXiv**：[2601.13999v1](https://arxiv.org/abs/2601.13999) · [PDF](https://arxiv.org/pdf/2601.13999.pdf)  
**作者**：Youngmoon Jung, Joon-Young Yang, Ju-ho Kim, Jaeyoung Roh, Chang Woo Han, Hoon-Young Cho  

**一句话要点**：提出DAME框架以解决短语音说话人验证中嵌入维度与时长不匹配的问题

**关键词**：说话人验证, 短语音处理, 嵌入学习, 时长感知, 模型无关框架, 性能优化

## 3 点简述
- 核心问题：短语音说话人验证因信息有限而困难，现有方法使用固定维度嵌入，导致容量与时长信息不匹配
- 方法要点：DAME构建嵌套子嵌入层次，低维捕获短语音特征，高维编码长语音细节，支持从头训练和微调
- 实验或效果：在VoxCeleb和VOiCES数据集上，DAME降低短时长试验错误率，保持全长性能，无额外推理成本

## 摘要（原文）

> Short-utterance speaker verification remains challenging due to limited speaker-discriminative cues in short speech segments. While existing methods focus on enhancing speaker encoders, the embedding learning strategy still forces a single fixed-dimensional representation reused for utterances of any length, leaving capacity misaligned with the information available at different durations. We propose Duration-Aware Matryoshka Embedding (DAME), a model-agnostic framework that builds a nested hierarchy of sub-embeddings aligned to utterance durations: lower-dimensional representations capture compact speaker traits from short utterances, while higher dimensions encode richer details from longer speech. DAME supports both training from scratch and fine-tuning, and serves as a direct alternative to conventional large-margin fine-tuning, consistently improving performance across durations. On the VoxCeleb1-O/E/H and VOiCES evaluation sets, DAME consistently reduces the equal error rate on 1-s and other short-duration trials, while maintaining full-length performance with no additional inference cost. These gains generalize across various speaker encoder architectures under both general training and fine-tuning setups.

