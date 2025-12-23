---
layout: default
title: MAGIC: Achieving Superior Model Merging via Magnitude Calibration
---

# MAGIC: Achieving Superior Model Merging via Magnitude Calibration
**arXiv**：[2512.19320v1](https://arxiv.org/abs/2512.19320) · [PDF](https://arxiv.org/pdf/2512.19320.pdf)  
**作者**：Yayuan Li, Jian Zhang, Jintao Guo, Zihan Cheng, Lei Qi, Yinghuan Shi, Yang Gao  

**一句话要点**：提出MAGIC框架通过幅度校准提升模型合并性能，无需额外训练。

**关键词**：模型合并, 幅度校准, 特征对齐, 计算机视觉, 自然语言处理, 无训练优化

## 3 点简述
- 核心问题：模型合并中特征幅度扰动导致性能下降，现有方法忽视幅度对齐。
- 方法要点：MAGIC在特征和权重空间进行幅度校准，包括FSC、WSC和DSC三种变体。
- 实验或效果：在计算机视觉和NLP任务上显著提升性能，如CV任务+4.3%，NLP任务+8.0%。

## 摘要（原文）

> The proliferation of pre-trained models has given rise to a wide array of specialised, fine-tuned models. Model merging aims to merge the distinct capabilities of these specialised models into a unified model, requiring minimal or even no additional training. A core objective of model merging is to ensure the merged model retains the behavioural characteristics of the specialised models, typically achieved through feature alignment. We identify that features consist of two critical components: direction and magnitude. Prior research has predominantly focused on directional alignment, while the influence of magnitude remains largely neglected, despite its pronounced vulnerability to perturbations introduced by common merging operations (e.g., parameter fusion and sparsification). Such perturbations to magnitude inevitably lead to feature deviations in the merged model from the specialised models, resulting in subsequent performance degradation. To address this, we propose MAGnItude Calibration (MAGIC), a plug-and-play framework that rectifies layer-wise magnitudes in feature and weight spaces, with three variants. Specifically, our Feature Space Calibration (FSC) realigns the merged model's features using a small set of unlabelled data, while Weight Space Calibration (WSC) extends this calibration to the weight space without requiring additional data. Combining these yields Dual Space Calibration (DSC). Comprehensive experiments demonstrate that MAGIC consistently boosts performance across diverse Computer Vision tasks (+4.3% on eight datasets) and NLP tasks (+8.0% on Llama) without additional training. Our code is available at: https://github.com/lyymuwu/MAGIC

