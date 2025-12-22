---
layout: default
title: Do Foundational Audio Encoders Understand Music Structure?
---

# Do Foundational Audio Encoders Understand Music Structure?
**arXiv**：[2512.17209v1](https://arxiv.org/abs/2512.17209) · [PDF](https://arxiv.org/pdf/2512.17209.pdf)  
**作者**：Keisuke Toyama, Zhi Zhong, Akira Takahashi, Shusuke Takahashi, Yuki Mitsufuji  

**一句话要点**：评估11种基础音频编码器在音乐结构分析中的性能，揭示自监督学习与音乐数据训练的关键作用

**关键词**：音乐结构分析, 基础音频编码器, 自监督学习, 掩码语言建模, 音乐信息检索

## 3 点简述
- 核心问题：基础音频编码器在音乐结构分析中的应用效果及影响因素尚不明确
- 方法要点：系统比较11种编码器，分析学习方法、训练数据和上下文长度的影响
- 实验或效果：发现基于音乐数据的掩码语言建模自监督学习编码器表现最佳

## 摘要（原文）

> In music information retrieval (MIR) research, the use of pretrained foundational audio encoders (FAEs) has recently become a trend. FAEs pretrained on large amounts of music and audio data have been shown to improve performance on MIR tasks such as music tagging and automatic music transcription. However, their use for music structure analysis (MSA) remains underexplored. Although many open-source FAE models are available, only a small subset has been examined for MSA, and the impact of factors such as learning methods, training data, and model context length on MSA performance remains unclear. In this study, we conduct comprehensive experiments on 11 types of FAEs to investigate how these factors affect MSA performance. Our results demonstrate that FAEs using selfsupervised learning with masked language modeling on music data are particularly effective for MSA. These findings pave the way for future research in MSA.

