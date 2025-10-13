---
layout: default
title: D-TPT: Dimensional Entropy Maximization for Calibrating Test-Time Prompt Tuning in Vision-Language Models
---

# D-TPT: Dimensional Entropy Maximization for Calibrating Test-Time Prompt Tuning in Vision-Language Models
**arXiv**：[2510.09473v1](https://arxiv.org/abs/2510.09473) · [PDF](https://arxiv.org/pdf/2510.09473.pdf)  
**作者**：Jisu Han, Wonjun Hwang  

**一句话要点**：提出维度熵最大化方法以解决测试时提示调优中的校准性能下降问题

**关键词**：测试时适应, 视觉语言模型, 提示调优, 校准误差, 维度熵最大化

## 3 点简述
- 核心问题：模态间隙由单一主导特征维度引起，导致预测敏感性和校准误差增加
- 方法要点：通过正则化文本特征分布向均匀性，减少主导维度依赖，提升校准
- 实验或效果：缓解校准性能退化，增强视觉语言模型在真实部署中的可靠性

## 摘要（原文）

> Test-time adaptation paradigm provides flexibility towards domain shifts by
> performing immediate adaptation on unlabeled target data from the source model.
> Vision-Language Models (VLMs) leverage their generalization capabilities for
> diverse downstream tasks, and test-time prompt tuning has emerged as a
> prominent solution for adapting VLMs. In this work, we explore contrastive VLMs
> and identify the modality gap caused by a single dominant feature dimension
> across modalities. We observe that the dominant dimensions in both text and
> image modalities exhibit high predictive sensitivity, and that constraining
> their influence can improve calibration error. Building on this insight, we
> propose dimensional entropy maximization that regularizes the distribution of
> textual features toward uniformity to mitigate the dependency of dominant
> dimensions. Our method alleviates the degradation of calibration performance in
> test-time prompt tuning, offering a simple yet effective solution to enhance
> the reliability of VLMs in real-world deployment scenarios.

