---
layout: default
title: Cross-modal Prompting for Balanced Incomplete Multi-modal Emotion Recognition
---

# Cross-modal Prompting for Balanced Incomplete Multi-modal Emotion Recognition
**arXiv**：[2512.11239v1](https://arxiv.org/abs/2512.11239) · [PDF](https://arxiv.org/pdf/2512.11239.pdf)  
**作者**：Wen-Jue He, Xiaofeng Zhu, Zheng Zhang  

**一句话要点**：提出跨模态提示方法以解决不完整多模态情感识别中的性能差距和模态欠优化问题。

**关键词**：不完整多模态情感识别, 跨模态提示, 动态梯度调制, 模态特征增强, 知识传播, 平衡策略

## 3 点简述
- 核心问题：不完整多模态数据导致性能差距和模态欠优化，阻碍情感识别效果。
- 方法要点：设计跨模态提示方法，通过渐进提示生成和动态梯度调制增强模态特征一致性。
- 实验或效果：在4个数据集上验证，优于7种先进方法，提升识别准确率。

## 摘要（原文）

> Incomplete multi-modal emotion recognition (IMER) aims at understanding human intentions and sentiments by comprehensively exploring the partially observed multi-source data. Although the multi-modal data is expected to provide more abundant information, the performance gap and modality under-optimization problem hinder effective multi-modal learning in practice, and are exacerbated in the confrontation of the missing data. To address this issue, we devise a novel Cross-modal Prompting (ComP) method, which emphasizes coherent information by enhancing modality-specific features and improves the overall recognition accuracy by boosting each modality's performance. Specifically, a progressive prompt generation module with a dynamic gradient modulator is proposed to produce concise and consistent modality semantic cues. Meanwhile, cross-modal knowledge propagation selectively amplifies the consistent information in modality features with the delivered prompts to enhance the discrimination of the modality-specific output. Additionally, a coordinator is designed to dynamically re-weight the modality outputs as a complement to the balance strategy to improve the model's efficacy. Extensive experiments on 4 datasets with 7 SOTA methods under different missing rates validate the effectiveness of our proposed method.

