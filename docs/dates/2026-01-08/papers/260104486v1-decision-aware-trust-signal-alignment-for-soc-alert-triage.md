---
layout: default
title: Decision-Aware Trust Signal Alignment for SOC Alert Triage
---

# Decision-Aware Trust Signal Alignment for SOC Alert Triage
**arXiv**：[2601.04486v1](https://arxiv.org/abs/2601.04486) · [PDF](https://arxiv.org/pdf/2601.04486.pdf)  
**作者**：Israt Jahan Chowdhury, Md Abu Yousuf Tanvir  

**一句话要点**：提出决策感知信任信号对齐框架以解决SOC警报分类中模型置信度与决策成本不匹配问题

**关键词**：SOC警报分类, 决策感知信任信号, 成本敏感阈值, 置信度校准, 不确定性提示, 人机交互评估

## 3 点简述
- 核心问题：SOC警报分类中模型置信度未考虑决策成本不对称性，导致假阴性风险高和警报过载
- 方法要点：结合校准置信度、轻量不确定性提示和成本敏感决策阈值，构建独立于检测模型的决策支持层
- 实验或效果：在UNSW-NB15基准上，决策对齐信任信号显著降低假阴性，成本加权损失减少数个数量级

## 摘要（原文）

> Detection systems that utilize machine learning are progressively implemented at Security Operations Centers (SOCs) to help an analyst to filter through high volumes of security alerts. Practically, such systems tend to reveal probabilistic results or confidence scores which are ill-calibrated and hard to read when under pressure. Qualitative and survey based studies of SOC practice done before reveal that poor alert quality and alert overload greatly augment the burden on the analyst, especially when tool outputs are not coherent with decision requirements, or signal noise. One of the most significant limitations is that model confidence is usually shown without expressing that there are asymmetric costs in decision making where false alarms are much less harmful than missed attacks. The present paper presents a decision-sensitive trust signal correspondence scheme of SOC alert triage. The framework combines confidence that has been calibrated, lightweight uncertainty cues, and cost-sensitive decision thresholds into coherent decision-support layer, instead of making changes to detection models. To enhance probabilistic consistency, the calibration is done using the known post-hoc methods and the uncertainty cues give conservative protection in situations where model certainty is low. To measure the model-independent performance of the suggested model, we apply the Logistic Regression and the Random Forest classifiers to the UNSW-NB15 intrusion detection benchmark. According to simulation findings, false negatives are greatly amplified by the presence of misaligned displays of confidence, whereas cost weighted loss decreases by orders of magnitude between models with decision aligned trust signals. Lastly, we describe a human-in-the-loop study plan that would allow empirically assessing the decision-making of the analysts with aligned and misaligned trust interfaces.

