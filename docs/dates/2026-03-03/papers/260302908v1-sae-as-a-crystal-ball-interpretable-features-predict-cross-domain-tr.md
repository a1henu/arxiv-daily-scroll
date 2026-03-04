---
layout: default
title: SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training
---

# SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training
**arXiv**：[2603.02908v1](https://arxiv.org/abs/2603.02908) · [PDF](https://arxiv.org/pdf/2603.02908.pdf)  
**作者**：Qi Zhang, Yifei Wang, Xiaohan Wang, Jiajun Chai, Guojun Yin, Wei Lin, Yisen Wang  

**一句话要点**：提出SAE-based Transferability Score以预测大语言模型微调前的跨域迁移性

**关键词**：大语言模型, 迁移学习, 稀疏自编码器, 微调预测, 跨域性能, 可解释性

## 3 点简述
- 核心问题：大语言模型微调后性能变化难以预测，影响跨域应用。
- 方法要点：利用稀疏自编码器提取特征，计算特征维度偏移与下游域相关性。
- 实验或效果：在多个模型和域上验证，Pearson相关系数超过0.7，准确预测迁移性。

## 摘要（原文）

> In recent years, pre-trained large language models have achieved remarkable success across diverse tasks. Besides the pivotal role of self-supervised pre-training, their effectiveness in downstream applications also depends critically on the post-training process, which adapts models to task-specific data and objectives. However, this process inevitably introduces model shifts that can influence performance in different domains, and how such shifts transfer remains poorly understood. To open up the black box, we propose the SAE-based Transferability Score (STS), a new metric that leverages sparse autoencoders (SAEs) to forecast post-training transferability. Taking supervised fine-tuning as an example, STS identifies shifted dimensions in SAE representations and calculates their correlations with downstream domains, enabling reliable estimation of transferability \textit{before} fine-tuning. Extensive experiments across multiple models and domains show that STS accurately predicts the transferability of supervised fine-tuning, achieving Pearson correlation coefficients above 0.7 with actual performance changes. Beyond this, we take an initial step toward extending STS to reinforcement learning. We believe that STS can serve as an {\color{black} interpretable} tool for guiding post-training strategies in LLMs. Code is available at https://github.com/PKU-ML/STS.

