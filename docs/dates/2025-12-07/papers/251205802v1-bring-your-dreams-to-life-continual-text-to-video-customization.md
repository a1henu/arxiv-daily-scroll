---
layout: default
title: Bring Your Dreams to Life: Continual Text-to-Video Customization
---

# Bring Your Dreams to Life: Continual Text-to-Video Customization
**arXiv**：[2512.05802v1](https://arxiv.org/abs/2512.05802) · [PDF](https://arxiv.org/pdf/2512.05802.pdf)  
**作者**：Jiahua Dong, Xudong Wang, Wenqi Liang, Zongyan Han, Meng Cao, Duzhen Zhang, Hanbin Zhao, Zhi Han, Salman Khan, Fahad Shahbaz Khan  

**一句话要点**：提出CCVD模型以解决持续文本到视频定制中的遗忘和概念忽视问题

**关键词**：持续学习, 文本到视频生成, 概念定制, 扩散模型, 遗忘缓解

## 3 点简述
- 核心问题：现有方法在持续学习新概念时易遗忘旧概念并忽视用户条件
- 方法要点：引入概念特定属性保留模块和可控条件合成以增强特征对齐
- 实验或效果：CCVD在多项任务中优于现有模型，代码已开源

## 摘要（原文）

> Customized text-to-video generation (CTVG) has recently witnessed great progress in generating tailored videos from user-specific text. However, most CTVG methods assume that personalized concepts remain static and do not expand incrementally over time. Additionally, they struggle with forgetting and concept neglect when continuously learning new concepts, including subjects and motions. To resolve the above challenges, we develop a novel Continual Customized Video Diffusion (CCVD) model, which can continuously learn new concepts to generate videos across various text-to-video generation tasks by tackling forgetting and concept neglect. To address catastrophic forgetting, we introduce a concept-specific attribute retention module and a task-aware concept aggregation strategy. They can capture the unique characteristics and identities of old concepts during training, while combining all subject and motion adapters of old concepts based on their relevance during testing. Besides, to tackle concept neglect, we develop a controllable conditional synthesis to enhance regional features and align video contexts with user conditions, by incorporating layer-specific region attention-guided noise estimation. Extensive experimental comparisons demonstrate that our CCVD outperforms existing CTVG models. The code is available at https://github.com/JiahuaDong/CCVD.

