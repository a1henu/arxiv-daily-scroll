---
layout: default
title: Automated Machine Learning in Radiomics: A Comparative Evaluation of Performance, Efficiency and Accessibility
---

# Automated Machine Learning in Radiomics: A Comparative Evaluation of Performance, Efficiency and Accessibility
**arXiv**：[2601.08334v1](https://arxiv.org/abs/2601.08334) · [PDF](https://arxiv.org/pdf/2601.08334.pdf)  
**作者**：Jose Lozano-Montoya, Emilio Soria-Olivas, Almudena Fuster-Matanzo, Angel Alberich-Bayarri, Ana Jimenez-Pastor  

**一句话要点**：评估AutoML在影像组学中的性能、效率与可访问性，揭示发展需求

**关键词**：影像组学, 自动化机器学习, 分类任务, 性能评估, 可访问性

## 3 点简述
- 核心问题：AutoML在影像组学中的有效性及应对特定挑战的能力尚不明确
- 方法要点：比较通用与影像组学专用AutoML框架在多样化分类任务上的表现
- 实验或效果：Simplatab在测试AUC最高，LightAutoML执行最快，多数专用框架因过时或低效被排除

## 摘要（原文）

> Automated machine learning (AutoML) frameworks can lower technical barriers for predictive and prognostic model development in radiomics by enabling researchers without programming expertise to build models. However, their effectiveness in addressing radiomics-specific challenges remains unclear. This study evaluates the performance, efficiency, and accessibility of general-purpose and radiomics-specific AutoML frameworks on diverse radiomics classification tasks, thereby highlighting development needs for radiomics. Ten public/private radiomics datasets with varied imaging modalities (CT/MRI), sizes, anatomies and endpoints were used. Six general-purpose and five radiomics-specific frameworks were tested with predefined parameters using standardized cross-validation. Evaluation metrics included AUC, runtime, together with qualitative aspects related to software status, accessibility, and interpretability. Simplatab, a radiomics-specific tool with a no-code interface, achieved the highest average test AUC (81.81%) with a moderate runtime (~1 hour). LightAutoML, a general-purpose framework, showed the fastest execution with competitive performance (78.74% mean AUC in six minutes). Most radiomics-specific frameworks were excluded from the performance analysis due to obsolescence, extensive programming requirements, or computational inefficiency. Conversely, general-purpose frameworks demonstrated higher accessibility and ease of implementation. Simplatab provides an effective balance of performance, efficiency, and accessibility for radiomics classification problems. However, significant gaps remain, including the lack of accessible survival analysis support and the limited integration of feature reproducibility and harmonization within current AutoML frameworks. Future research should focus on adapting AutoML solutions to better address these radiomics-specific challenges.

