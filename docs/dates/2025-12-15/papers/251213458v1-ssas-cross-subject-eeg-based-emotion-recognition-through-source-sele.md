---
layout: default
title: SSAS: Cross-subject EEG-based Emotion Recognition through Source Selection with Adversarial Strategy
---

# SSAS: Cross-subject EEG-based Emotion Recognition through Source Selection with Adversarial Strategy
**arXiv**：[2512.13458v1](https://arxiv.org/abs/2512.13458) · [PDF](https://arxiv.org/pdf/2512.13458.pdf)  
**作者**：Yici Liu, Qi Wei Oung, Hoi Leong Lee  

**一句话要点**：提出SSAS方法，通过源选择与对抗策略解决跨被试EEG情绪识别中的个体差异与负迁移问题。

**关键词**：跨被试情绪识别, 脑电信号处理, 源选择网络, 对抗训练, 域适应

## 3 点简述
- 核心问题：跨被试EEG情绪识别存在个体差异与负迁移，影响模型泛化能力。
- 方法要点：结合源选择网络与对抗策略网络，学习域不变且情绪相关的表示。
- 实验或效果：在SEED和SEED-IV数据集上表现优异，代码已开源。

## 摘要（原文）

> Electroencephalographic (EEG) signals have long been applied in the field of affective brain-computer interfaces (aBCIs). Cross-subject EEG-based emotion recognition has demonstrated significant potential in practical applications due to its suitability across diverse people. However, most studies on cross-subject EEG-based emotion recognition neglect the presence of inter-individual variability and negative transfer phenomena during model training. To address this issue, a cross-subject EEG-based emotion recognition through source selection with adversarial strategy is introduced in this paper. The proposed method comprises two modules: the source selection network (SS) and the adversarial strategies network (AS). The SS uses domain labels to reverse-engineer the training process of domain adaptation. Its key idea is to disrupt class separability and magnify inter-domain differences, thereby raising the classification difficulty and forcing the model to learn domain-invariant yet emotion-relevant representations. The AS gets the source domain selection results and the pretrained domain discriminators from SS. The pretrained domain discriminators compute a novel loss aimed at enhancing the performance of domain classification during adversarial training, ensuring the balance of adversarial strategies. This paper provides theoretical insights into the proposed method and achieves outstanding performance on two EEG-based emotion datasets, SEED and SEED-IV. The code can be found at https://github.com/liuyici/SSAS.

