---
layout: default
title: Generative Multi-modal Feedback for Singing Voice Synthesis Evaluation
---

# Generative Multi-modal Feedback for Singing Voice Synthesis Evaluation
**arXiv**：[2512.02523v1](https://arxiv.org/abs/2512.02523) · [PDF](https://arxiv.org/pdf/2512.02523.pdf)  
**作者**：Xueyan Li, Yuxin Wang, Mengjie Jiang, Qingzi Zhu, Jiang Zhang, Zoey Kim, Yazhe Niu  

**一句话要点**：提出生成式多模态反馈框架以解决歌唱语音合成评估中单维评分和标注成本高的问题。

**关键词**：歌唱语音合成评估, 多模态反馈, 音频-语言模型, 生成式奖励模型, 混合数据集微调

## 3 点简述
- 核心问题：现有歌唱语音合成评估方法依赖单维数值评分，难以捕捉表达力等多维度，且标注成本高、可解释性差。
- 方法要点：利用音频-语言模型生成涵盖旋律、内容和听觉质量的多维语言和音频反馈，通过混合数据集微调增强多样性和语言丰富性。
- 实验或效果：定量实验验证了数据集和训练策略的有效性，框架能产生音乐准确且可解释的评估，适用于指导生成模型优化。

## 摘要（原文）

> Singing voice synthesis (SVS) has advanced significantly, enabling models to generate vocals with accurate pitch and consistent style. As these capabilities improve, the need for reliable evaluation and optimization becomes increasingly critical. However, current methods like reward systems often rely on single numerical scores, struggle to capture various dimensions such as phrasing or expressiveness, and require costly annotations, limiting interpretability and generalization. To address these issues, we propose a generative feedback (i.e., reward model) framework that provides multi-dimensional language and audio feedback for SVS assessment. Our approach leverages an audio-language model to generate text and audio critiques-covering aspects such as melody, content, and auditory quality. The model is fine-tuned on a hybrid dataset combining human music reactions and synthetic critiques from a MLLMs, enhancing diversity and linguistic richness. Quantitative experiments validate the effectiveness of the proposed dataset and training strategy, demonstrating that the framework produces musically accurate and interpretable evaluations suitable for guiding generative model improvement. The code is at [https://github.com/opendilab/VocalCritic](https://github.com/opendilab/VocalCritic)

