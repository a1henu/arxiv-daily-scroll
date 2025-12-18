---
layout: default
title: Intersectional Fairness in Vision-Language Models for Medical Image Disease Classification
---

# Intersectional Fairness in Vision-Language Models for Medical Image Disease Classification
**arXiv**：[2512.15249v1](https://arxiv.org/abs/2512.15249) · [PDF](https://arxiv.org/pdf/2512.15249.pdf)  
**作者**：Yupeng Zhang, Adam G. Dunn, Usman Naseem, Jinman Kim  

**一句话要点**：提出Cross-Modal Alignment Consistency框架以解决医学视觉语言模型在交叉患者亚组中的诊断公平性问题

**关键词**：医学视觉语言模型, 交叉公平性, 诊断信心标准化, 皮肤病变分类, 青光眼筛查, 隐私保护

## 3 点简述
- 医学AI系统存在交叉偏见，导致边缘化患者亚组诊断信心不足和误诊率更高
- 方法通过标准化诊断信心，无需临床推理时敏感数据，平衡模型决策置信度
- 在皮肤病变和青光眼检测中，减少误诊差距并提升AUC，验证了准确性和公平性

## 摘要（原文）

> Medical artificial intelligence (AI) systems, particularly multimodal vision-language models (VLM), often exhibit intersectional biases where models are systematically less confident in diagnosing marginalised patient subgroups. Such bias can lead to higher rates of inaccurate and missed diagnoses due to demographically skewed data and divergent distributions of diagnostic certainty. Current fairness interventions frequently fail to address these gaps or compromise overall diagnostic performance to achieve statistical parity among the subgroups. In this study, we developed Cross-Modal Alignment Consistency (CMAC-MMD), a training framework that standardises diagnostic certainty across intersectional patient subgroups. Unlike traditional debiasing methods, this approach equalises the model's decision confidence without requiring sensitive demographic data during clinical inference. We evaluated this approach using 10,015 skin lesion images (HAM10000) with external validation on 12,000 images (BCN20000), and 10,000 fundus images for glaucoma detection (Harvard-FairVLMed), stratifying performance by intersectional age, gender, and race attributes. In the dermatology cohort, the proposed method reduced the overall intersectional missed diagnosis gap (difference in True Positive Rate, $Δ$TPR) from 0.50 to 0.26 while improving the overall Area Under the Curve (AUC) from 0.94 to 0.97 compared to standard training. Similarly, for glaucoma screening, the method reduced $Δ$TPR from 0.41 to 0.31, achieving a better AUC of 0.72 (vs. 0.71 baseline). This establishes a scalable framework for developing high-stakes clinical decision support systems that are both accurate and can perform equitably across diverse patient subgroups, ensuring reliable performance without increasing privacy risks.

