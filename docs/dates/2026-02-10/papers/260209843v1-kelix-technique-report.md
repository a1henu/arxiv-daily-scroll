---
layout: default
title: Kelix Technique Report
---

# Kelix Technique Report
**arXiv**：[2602.09843v1](https://arxiv.org/abs/2602.09843) · [PDF](https://arxiv.org/pdf/2602.09843.pdf)  
**作者**：Boyang Ding, Chenglong Chu, Dunju Zang, Han Li, Jiangxia Cao, Kun Gai, Muhao Wei, Ruiming Tang, Shiyao Wang, Siyang Mao, Xinchen Luo, Yahui Liu, Zhixin Ling, Zhuoran Yang, Ziming Li, Chengru Song, Guorui Zhou, Guowang Zhang, Hao Peng, Hao Wang, Jiaxin Deng, Jin Ouyang, Jinghao Zhang, Lejian Ren, Qianqian Wang, Qigen Hu, Tao Wang, Xingmei Wang, Yiping Yang, Zixing Zhang, Ziqi Wang  

**一句话要点**：提出Kelix模型以解决离散视觉表示在理解能力上弱于连续特征的问题

**关键词**：离散视觉表示, 自回归模型, 视觉语言模型, 统一理解生成, 视觉标记化

## 3 点简述
- 核心问题：现有离散视觉表示因编码容量有限导致信息丢失，理解能力弱于连续特征视觉语言模型
- 方法要点：开发完全离散的自回归统一模型，通过改进视觉标记化技术提升理解能力
- 实验或效果：Kelix模型缩小了离散与连续视觉表示之间的理解差距，实现统一理解与生成

## 摘要（原文）

> Autoregressive large language models (LLMs) scale well by expressing diverse tasks as sequences of discrete natural-language tokens and training with next-token prediction, which unifies comprehension and generation under self-supervision. Extending this paradigm to multimodal data requires a shared, discrete representation across modalities. However, most vision-language models (VLMs) still rely on a hybrid interface: discrete text tokens paired with continuous Vision Transformer (ViT) features. Because supervision is largely text-driven, these models are often biased toward understanding and cannot fully leverage large-scale self-supervised learning on non-text data. Recent work has explored discrete visual tokenization to enable fully autoregressive multimodal modeling, showing promising progress toward unified understanding and generation. Yet existing discrete vision tokens frequently lose information due to limited code capacity, resulting in noticeably weaker understanding than continuous-feature VLMs. We present Kelix, a fully discrete autoregressive unified model that closes the understanding gap between discrete and continuous visual representations.

