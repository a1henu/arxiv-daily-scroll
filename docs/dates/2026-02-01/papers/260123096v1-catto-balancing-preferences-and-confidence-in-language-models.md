---
layout: default
title: CATTO: Balancing Preferences and Confidence in Language Models
---

# CATTO: Balancing Preferences and Confidence in Language Models
**arXiv**：[2601.23096v1](https://arxiv.org/abs/2601.23096) · [PDF](https://arxiv.org/pdf/2601.23096.pdf)  
**作者**：Nisarg Parikh, Kunjal Panchal, Ananya Sai, Pannaga Shivaswamy, Andrew Lan  

**一句话要点**：提出CATTO校准目标，以解决大语言模型置信度与预测正确性不匹配的问题。

**关键词**：大语言模型, 置信度校准, 偏好优化, 令牌级训练, 校准误差, 测试时缩放

## 3 点简述
- 核心问题：大语言模型置信度校准不佳，偏好对齐方法加剧了预测概率与正确性的脱节。
- 方法要点：引入校准感知的令牌级训练目标CATTO，结合偏好优化目标，对齐置信度与经验正确性。
- 实验或效果：CATTO显著降低校准误差，保持或提升任务准确率，并引入置信度@k测试时缩放机制。

## 摘要（原文）

> Large language models (LLMs) often make accurate next token predictions but their confidence in these predictions can be poorly calibrated: high-confidence predictions are frequently wrong, and low-confidence predictions may be correct. This miscalibration is exacerbated by preference-based alignment methods breaking the link between predictive probability and correctness. We introduce a Calibration Aware Token-level Training Objective (CATTO), a calibration-aware objective that aligns predicted confidence with empirical prediction correctness, which can be combined with the original preference optimization objectives. Empirically, CATTO reduces Expected Calibration Error (ECE) by 2.22%-7.61% in-distribution and 1.46%-10.44% out-of-distribution compared to direct preference optimization (DPO), and by 0.22%-1.24% in-distribution and 1.23%-5.07% out-of-distribution compared to the strongest DPO baseline. This improvement in confidence does not come at a cost of losing task accuracy, where CATTO maintains or slightly improves multiple-choice question-answering accuracy on five datasets. We also introduce Confidence@k, a test-time scaling mechanism leveraging calibrated token probabilities for Bayes-optimal selection of output tokens.

