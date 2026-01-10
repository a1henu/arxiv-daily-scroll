---
layout: default
title: A Lightweight and Explainable Vision-Language Framework for Crop Disease Visual Question Answering
---

# A Lightweight and Explainable Vision-Language Framework for Crop Disease Visual Question Answering
**arXiv**：[2601.05143v1](https://arxiv.org/abs/2601.05143) · [PDF](https://arxiv.org/pdf/2601.05143.pdf)  
**作者**：Md. Zahid Hossain, Most. Sharmin Sultana Samu, Md. Rakibul Islam, Md. Siam Ansary  

**一句话要点**：提出轻量级可解释视觉语言框架，用于作物病害视觉问答，结合Swin Transformer与序列解码器。

**关键词**：作物病害识别, 视觉问答, 轻量级框架, Swin Transformer, 跨模态对齐, 可解释性分析

## 3 点简述
- 核心问题：作物病害视觉问答需准确视觉理解和可靠语言生成，以识别叶片图像中的作物和病害。
- 方法要点：采用Swin Transformer视觉编码器和序列到序列语言解码器，通过两阶段训练提升视觉表示学习和跨模态对齐。
- 实验或效果：在大规模数据集上评估，分类和自然语言生成指标表现优异，模型参数少且优于大规模基线，可解释性通过Grad-CAM和令牌级归因验证。

## 摘要（原文）

> Visual question answering for crop disease analysis requires accurate visual understanding and reliable language generation. This work presents a lightweight vision-language framework for crop and disease identification from leaf images. The proposed approach combines a Swin Transformer vision encoder with sequence-to-sequence language decoders. A two-stage training strategy is adopted to improve visual representation learning and cross-modal alignment. The model is evaluated on a large-scale crop disease dataset using classification and natural language generation metrics. Experimental results show high accuracy for both crop and disease identification. The framework also achieves strong performance on BLEU, ROUGE and BERTScore. Our proposed models outperform large-scale vision-language baselines while using significantly fewer parameters. Explainability is assessed using Grad-CAM and token-level attribution. Qualitative results demonstrate robust performance under diverse user-driven queries. These findings highlight the effectiveness of task-specific visual pretraining for crop disease visual question answering.

