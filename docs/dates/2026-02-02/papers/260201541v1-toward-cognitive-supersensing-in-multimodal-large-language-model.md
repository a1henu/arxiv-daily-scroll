---
layout: default
title: Toward Cognitive Supersensing in Multimodal Large Language Model
---

# Toward Cognitive Supersensing in Multimodal Large Language Model
**arXiv**：[2602.01541v1](https://arxiv.org/abs/2602.01541) · [PDF](https://arxiv.org/pdf/2602.01541.pdf)  
**作者**：Boyi Li, Yifan Shen, Yuanzhe Liu, Yifan Xu, Jiateng Liu, Xinzhuo Li, Zhengyuan Li, Jingyuan Zhu, Yunhan Zhong, Fangzhou Lan, Jianguo Cao, James M. Rehg, Heng Ji, Ismini Lourentzou, Xu Cao  

**一句话要点**：提出Cognitive Supersensing训练范式，通过视觉潜在嵌入增强多模态大语言模型的认知推理能力。

**关键词**：多模态大语言模型, 视觉推理, 认知超感知, 潜在视觉意象预测, 视觉问答基准

## 3 点简述
- 核心问题：多模态大语言模型在复杂认知任务中视觉推理能力不足，缺乏类似人类视觉空间草稿和视觉意象的机制。
- 方法要点：引入Latent Visual Imagery Prediction头，联合学习视觉认知潜在嵌入序列并与答案对齐，形成基于视觉的内部推理链。
- 实验或效果：在CogSense-Bench上显著超越基线，并在数学和科学VQA基准上表现出优越泛化能力。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable success in open-vocabulary perceptual tasks, yet their ability to solve complex cognitive problems remains limited, especially when visual details are abstract and require visual memory. Current approaches primarily scale Chain-of-Thought (CoT) reasoning in the text space, even when language alone is insufficient for clear and structured reasoning, and largely neglect visual reasoning mechanisms analogous to the human visuospatial sketchpad and visual imagery. To mitigate this deficiency, we introduce Cognitive Supersensing, a novel training paradigm that endows MLLMs with human-like visual imagery capabilities by integrating a Latent Visual Imagery Prediction (LVIP) head that jointly learns sequences of visual cognitive latent embeddings and aligns them with the answer, thereby forming vision-based internal reasoning chains. We further introduce a reinforcement learning stage that optimizes text reasoning paths based on this grounded visual latent. To evaluate the cognitive capabilities of MLLMs, we present CogSense-Bench, a comprehensive visual question answering (VQA) benchmark assessing five cognitive dimensions. Extensive experiments demonstrate that MLLMs trained with Cognitive Supersensing significantly outperform state-of-the-art baselines on CogSense-Bench and exhibit superior generalization on out-of-domain mathematics and science VQA benchmarks, suggesting that internal visual imagery is potentially key to bridging the gap between perceptual recognition and cognitive understanding. We will open-source the CogSense-Bench and our model weights.

