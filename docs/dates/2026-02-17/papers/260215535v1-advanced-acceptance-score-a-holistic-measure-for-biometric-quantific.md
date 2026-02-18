---
layout: default
title: Advanced Acceptance Score: A Holistic Measure for Biometric Quantification
---

# Advanced Acceptance Score: A Holistic Measure for Biometric Quantification
**arXiv**：[2602.15535v1](https://arxiv.org/abs/2602.15535) · [PDF](https://arxiv.org/pdf/2602.15535.pdf)  
**作者**：Aman Verma, Seshan Srirangarajan, Sumantra Dutta Roy  

**一句话要点**：提出高级接受分数作为手势生物特征量化的整体评估指标，以解决现有错误率无法衡量分数质量的问题。

**关键词**：生物特征量化, 手势识别, 评估指标, 分数质量, 排名偏差, 身份特征解缠

## 3 点简述
- 核心问题：现有生物特征容量估计依赖错误率，但无法评估分数质量，导致量化不全面。
- 方法要点：基于排名顺序和相关性，结合排名偏差、趋势补偿和身份特征解缠，加权集成形成整体指标。
- 实验或效果：在三个数据集和五个SOTA模型上验证，所选最优分数更合适，且与现有指标相关，可靠性高。

## 摘要（原文）

> Quantifying biometric characteristics within hand gestures involve derivation of fitness scores from a gesture and identity aware feature space. However, evaluating the quality of these scores remains an open question. Existing biometric capacity estimation literature relies upon error rates. But these rates do not indicate goodness of scores. Thus, in this manuscript we present an exhaustive set of evaluation measures. We firstly identify ranking order and relevance of output scores as the primary basis for evaluation. In particular, we consider both rank deviation as well as rewards for: (i) higher scores of high ranked gestures and (ii) lower scores of low ranked gestures. We also compensate for correspondence between trends of output and ground truth scores. Finally, we account for disentanglement between identity features of gestures as a discounting factor. Integrating these elements with adequate weighting, we formulate advanced acceptance score as a holistic evaluation measure. To assess effectivity of the proposed we perform in-depth experimentation over three datasets with five state-of-the-art (SOTA) models. Results show that the optimal score selected with our measure is more appropriate than existing other measures. Also, our proposed measure depicts correlation with existing measures. This further validates its reliability. We have made our \href{https://github.com/AmanVerma2307/MeasureSuite}{code} public.

