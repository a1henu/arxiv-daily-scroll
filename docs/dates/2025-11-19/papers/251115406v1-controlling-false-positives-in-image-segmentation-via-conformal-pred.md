---
layout: default
title: Controlling False Positives in Image Segmentation via Conformal Prediction
---

# Controlling False Positives in Image Segmentation via Conformal Prediction
**arXiv**：[2511.15406v1](https://arxiv.org/abs/2511.15406) · [PDF](https://arxiv.org/pdf/2511.15406.pdf)  
**作者**：Luca Mossina, Corentin Friedrich  

**一句话要点**：提出基于共形预测的后处理框架，控制图像分割假阳性以支持临床决策

**关键词**：图像分割, 共形预测, 假阳性控制, 临床决策, 后处理框架, 统计保证

## 3 点简述
- 核心问题：深度分割模型缺乏对假阳性错误的统计保证，可能导致临床风险
- 方法要点：使用校准集通过共形预测选择收缩参数，构建置信掩码控制假阳性比例
- 实验或效果：在息肉分割基准上验证了目标级经验有效性，无需模型重训练

## 摘要（原文）

> Reliable semantic segmentation is essential for clinical decision making, yet deep models rarely provide explicit statistical guarantees on their errors. We introduce a simple post-hoc framework that constructs confidence masks with distribution-free, image-level control of false-positive predictions. Given any pretrained segmentation model, we define a nested family of shrunken masks obtained either by increasing the score threshold or by applying morphological erosion. A labeled calibration set is used to select a single shrink parameter via conformal prediction, ensuring that, for new images that are exchangeable with the calibration data, the proportion of false positives retained in the confidence mask stays below a user-specified tolerance with high probability. The method is model-agnostic, requires no retraining, and provides finite-sample guarantees regardless of the underlying predictor. Experiments on a polyp-segmentation benchmark demonstrate target-level empirical validity. Our framework enables practical, risk-aware segmentation in settings where over-segmentation can have clinical consequences. Code at https://github.com/deel-ai-papers/conseco.

