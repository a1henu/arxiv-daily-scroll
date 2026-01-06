---
layout: default
title: Multi-granularity Interactive Attention Framework for Residual Hierarchical Pronunciation Assessment
---

# Multi-granularity Interactive Attention Framework for Residual Hierarchical Pronunciation Assessment
**arXiv**：[2601.01745v1](https://arxiv.org/abs/2601.01745) · [PDF](https://arxiv.org/pdf/2601.01745.pdf)  
**作者**：Hong Han, Hao-Chen Pei, Zhao-Zheng Nie, Xin Luo, Xin-Shun Xu  

**一句话要点**：提出残差层次交互注意力框架以解决发音评估中多粒度间双向交互不足的问题

**关键词**：发音评估, 多粒度建模, 交互注意力, 残差层次结构, 语音处理

## 3 点简述
- 现有方法仅考虑相邻粒度间的单向依赖，缺乏音素、词和话语级别的双向交互
- 核心为交互注意力模块，通过注意力机制实现动态双向交互，捕捉不同粒度间的相关性
- 在speechocean762数据集上实验，模型全面领先现有最优方法

## 摘要（原文）

> Automatic pronunciation assessment plays a crucial role in computer-assisted pronunciation training systems. Due to the ability to perform multiple pronunciation tasks simultaneously, multi-aspect multi-granularity pronunciation assessment methods are gradually receiving more attention and achieving better performance than single-level modeling tasks. However, existing methods only consider unidirectional dependencies between adjacent granularity levels, lacking bidirectional interaction among phoneme, word, and utterance levels and thus insufficiently capturing the acoustic structural correlations. To address this issue, we propose a novel residual hierarchical interactive method, HIA for short, that enables bidirectional modeling across granularities. As the core of HIA, the Interactive Attention Module leverages an attention mechanism to achieve dynamic bidirectional interaction, effectively capturing linguistic features at each granularity while integrating correlations between different granularity levels. We also propose a residual hierarchical structure to alleviate the feature forgetting problem when modeling acoustic hierarchies. In addition, we use 1-D convolutional layers to enhance the extraction of local contextual cues at each granularity. Extensive experiments on the speechocean762 dataset show that our model is comprehensively ahead of the existing state-of-the-art methods.

