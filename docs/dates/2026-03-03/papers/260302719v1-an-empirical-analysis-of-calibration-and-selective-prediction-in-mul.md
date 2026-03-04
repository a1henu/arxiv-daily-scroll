---
layout: default
title: An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification
---

# An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification
**arXiv**：[2603.02719v1](https://arxiv.org/abs/2603.02719) · [PDF](https://arxiv.org/pdf/2603.02719.pdf)  
**作者**：L. Julián Lechuga López, Farah E. Shamout, Tim G. J. Rudner  

**一句话要点**：实证分析多模态临床条件分类中的校准与选择性预测，揭示性能下降与类别依赖校准偏差

**关键词**：多模态临床分类, 选择性预测, 校准偏差, ICU数据分析, 不确定性评估

## 3 点简述
- 核心问题：选择性预测在临床AI中可能因校准偏差导致性能下降，尤其在少数类别上
- 方法要点：使用多模态ICU数据评估多种先进模型，分析不确定性预测的可靠性
- 实验或效果：发现模型常对正确预测分配高不确定性，错误预测分配低不确定性，聚合指标可能掩盖问题

## 摘要（原文）

> As artificial intelligence systems move toward clinical deployment, ensuring reliable prediction behavior is fundamental for safety-critical decision-making tasks. One proposed safeguard is selective prediction, where models can defer uncertain predictions to human experts for review. In this work, we empirically evaluate the reliability of uncertainty-based selective prediction in multilabel clinical condition classification using multimodal ICU data. Across a range of state-of-the-art unimodal and multimodal models, we find that selective prediction can substantially degrade performance despite strong standard evaluation metrics. This failure is driven by severe class-dependent miscalibration, whereby models assign high uncertainty to correct predictions and low uncertainty to incorrect ones, particularly for underrepresented clinical conditions. Our results show that commonly used aggregate metrics can obscure these effects, limiting their ability to assess selective prediction behavior in this setting. Taken together, our findings characterize a task-specific failure mode of selective prediction in multimodal clinical condition classification and highlight the need for calibration-aware evaluation to provide strong guarantees of safety and robustness in clinical AI.

