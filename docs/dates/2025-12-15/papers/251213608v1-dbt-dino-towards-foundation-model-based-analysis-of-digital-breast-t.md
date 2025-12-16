---
layout: default
title: DBT-DINO: Towards Foundation model based analysis of Digital Breast Tomosynthesis
---

# DBT-DINO: Towards Foundation model based analysis of Digital Breast Tomosynthesis
**arXiv**：[2512.13608v1](https://arxiv.org/abs/2512.13608) · [PDF](https://arxiv.org/pdf/2512.13608.pdf)  
**作者**：Felix J. Dorfner, Manon A. Dorster, Ryan Connolly, Oscar Gentilhomme, Edward Gibbs, Steven Graham, Seth Wander, Thomas Schultz, Manisha Bahl, Dania Daye, Albert E. Kim, Christopher P. Bridge  

**一句话要点**：提出DBT-DINO基础模型，用于数字乳腺断层合成影像分析，提升临床任务性能。

**关键词**：数字乳腺断层合成, 基础模型, 自监督学习, 医学影像分析, 乳腺癌筛查

## 3 点简述
- 核心问题：数字乳腺断层合成缺乏基础模型，影响三维医学影像分析。
- 方法要点：基于DINOv2自监督预训练，使用超过2500万张二维切片构建模型。
- 实验效果：在乳腺密度分类和癌症风险预测任务中表现优于基线，但病灶检测任务效果有限。

## 摘要（原文）

> Foundation models have shown promise in medical imaging but remain underexplored for three-dimensional imaging modalities. No foundation model currently exists for Digital Breast Tomosynthesis (DBT), despite its use for breast cancer screening.
>   To develop and evaluate a foundation model for DBT (DBT-DINO) across multiple clinical tasks and assess the impact of domain-specific pre-training.
>   Self-supervised pre-training was performed using the DINOv2 methodology on over 25 million 2D slices from 487,975 DBT volumes from 27,990 patients. Three downstream tasks were evaluated: (1) breast density classification using 5,000 screening exams; (2) 5-year risk of developing breast cancer using 106,417 screening exams; and (3) lesion detection using 393 annotated volumes.
>   For breast density classification, DBT-DINO achieved an accuracy of 0.79 (95\% CI: 0.76--0.81), outperforming both the MetaAI DINOv2 baseline (0.73, 95\% CI: 0.70--0.76, p<.001) and DenseNet-121 (0.74, 95\% CI: 0.71--0.76, p<.001). For 5-year breast cancer risk prediction, DBT-DINO achieved an AUROC of 0.78 (95\% CI: 0.76--0.80) compared to DINOv2's 0.76 (95\% CI: 0.74--0.78, p=.57). For lesion detection, DINOv2 achieved a higher average sensitivity of 0.67 (95\% CI: 0.60--0.74) compared to DBT-DINO with 0.62 (95\% CI: 0.53--0.71, p=.60). DBT-DINO demonstrated better performance on cancerous lesions specifically with a detection rate of 78.8\% compared to Dinov2's 77.3\%.
>   Using a dataset of unprecedented size, we developed DBT-DINO, the first foundation model for DBT. DBT-DINO demonstrated strong performance on breast density classification and cancer risk prediction. However, domain-specific pre-training showed variable benefits on the detection task, with ImageNet baseline outperforming DBT-DINO on general lesion detection, indicating that localized detection tasks require further methodological development.

