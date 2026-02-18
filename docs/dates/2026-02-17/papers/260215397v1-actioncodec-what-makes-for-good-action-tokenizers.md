---
layout: default
title: ActionCodec: What Makes for Good Action Tokenizers
---

# ActionCodec: What Makes for Good Action Tokenizers
**arXiv**：[2602.15397v1](https://arxiv.org/abs/2602.15397) · [PDF](https://arxiv.org/pdf/2602.15397.pdf)  
**作者**：Zibin Dong, Yicheng Liu, Shiduo Zhang, Baijun Ye, Yifu Yuan, Fei Ni, Jingjing Gong, Xipeng Qiu, Hang Zhao, Yinchuan Li, Jianye Hao  

**一句话要点**：提出ActionCodec以优化视觉-语言-动作模型的动作分词器设计原则

**关键词**：动作分词器, 视觉-语言-动作模型, 信息论设计原则, 训练效率优化, 无机器人预训练

## 3 点简述
- 核心问题：现有动作分词器设计仅关注重建保真度，未考虑其对VLA模型优化的直接影响。
- 方法要点：基于信息论原则，建立最大化时间令牌重叠、最小化词汇冗余等设计准则，开发ActionCodec。
- 实验或效果：在LIBERO等基准上，ActionCodec显著提升训练效率和模型性能，达到无机器人预训练的新SOTA。

## 摘要（原文）

> Vision-Language-Action (VLA) models leveraging the native autoregressive paradigm of Vision-Language Models (VLMs) have demonstrated superior instruction-following and training efficiency. Central to this paradigm is action tokenization, yet its design has primarily focused on reconstruction fidelity, failing to address its direct impact on VLA optimization. Consequently, the fundamental question of \textit{what makes for good action tokenizers} remains unanswered. In this paper, we bridge this gap by establishing design principles specifically from the perspective of VLA optimization. We identify a set of best practices based on information-theoretic insights, including maximized temporal token overlap, minimized vocabulary redundancy, enhanced multimodal mutual information, and token independence. Guided by these principles, we introduce \textbf{ActionCodec}, a high-performance action tokenizer that significantly enhances both training efficiency and VLA performance across diverse simulation and real-world benchmarks. Notably, on LIBERO, a SmolVLM2-2.2B fine-tuned with ActionCodec achieves a 95.5\% success rate without any robotics pre-training. With advanced architectural enhancements, this reaches 97.4\%, representing a new SOTA for VLA models without robotics pre-training. We believe our established design principles, alongside the released model, will provide a clear roadmap for the community to develop more effective action tokenizers.

