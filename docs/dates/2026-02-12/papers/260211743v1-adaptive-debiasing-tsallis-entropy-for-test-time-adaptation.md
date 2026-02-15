---
layout: default
title: Adaptive Debiasing Tsallis Entropy for Test-Time Adaptation
---

# Adaptive Debiasing Tsallis Entropy for Test-Time Adaptation
**arXiv**：[2602.11743v1](https://arxiv.org/abs/2602.11743) · [PDF](https://arxiv.org/pdf/2602.11743.pdf)  
**作者**：Xiangyu Wu, Dongming Jiang, Feng Yu, Yueying Tian, Jiaqi Tang, Qing-Guo Chen, Yang Yang, Jianfeng Lu  

**一句话要点**：提出自适应去偏Tsallis熵以解决测试时适应中Shannon熵的偏差问题

**关键词**：测试时适应, Tsallis熵, 自适应去偏, 视觉语言模型, 不确定性估计

## 3 点简述
- 核心问题：CLIP预训练数据不平衡导致Shannon熵在测试时产生偏差估计
- 方法要点：引入Tsallis熵并自适应调整参数q^l，结合标签调整策略提升适应效果
- 实验或效果：在ImageNet及其变体和10个跨域基准上优于现有方法

## 摘要（原文）

> Mainstream Test-Time Adaptation (TTA) methods for adapting vision-language models, e.g., CLIP, typically rely on Shannon Entropy (SE) at test time to measure prediction uncertainty and inconsistency. However, since CLIP has a built-in bias from pretraining on highly imbalanced web-crawled data, SE inevitably results in producing biased estimates of uncertainty entropy. To address this issue, we notably find and demonstrate that Tsallis Entropy (TE), a generalized form of SE, is naturally suited for characterizing biased distributions by introducing a non-extensive parameter q, with the performance of SE serving as a lower bound for TE. Building upon this, we generalize TE into Adaptive Debiasing Tsallis Entropy (ADTE) for TTA, customizing a class-specific parameter q^l derived by normalizing the estimated label bias from continuously incoming test instances, for each category. This adaptive approach allows ADTE to accurately select high-confidence views and seamlessly integrate with a label adjustment strategy to enhance adaptation, without introducing distribution-specific hyperparameter tuning. Besides, our investigation reveals that both TE and ADTE can serve as direct, advanced alternatives to SE in TTA, without any other modifications. Experimental results show that ADTE outperforms state-of-the-art methods on ImageNet and its five variants, and achieves the highest average performance on 10 cross-domain benchmarks, regardless of the model architecture or text prompts used. Our code is available at https://github.com/Jinx630/ADTE.

