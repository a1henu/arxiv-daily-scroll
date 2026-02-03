---
layout: default
title: Your AI-Generated Image Detector Can Secretly Achieve SOTA Accuracy, If Calibrated
---

# Your AI-Generated Image Detector Can Secretly Achieve SOTA Accuracy, If Calibrated
**arXiv**：[2602.01973v1](https://arxiv.org/abs/2602.01973) · [PDF](https://arxiv.org/pdf/2602.01973.pdf)  
**作者**：Muli Yang, Gabriel James Goenawan, Henan Wang, Huaiyuan Qin, Chenghao Xu, Yanhua Yang, Fen Fang, Ying Sun, Joo-Hwee Lim, Hongyuan Zhu  

**一句话要点**：提出基于贝叶斯决策理论的后处理校准框架，以提升AI生成图像检测器在开放世界中的鲁棒性。

**关键词**：AI生成图像检测, 后处理校准, 分布偏移, 贝叶斯决策理论, 鲁棒性提升, 轻量级框架

## 3 点简述
- 现有AI生成图像检测器在测试时存在系统偏差，常将假图像误判为真，源于分布偏移和训练中的隐式先验。
- 方法通过可学习标量校正模型logits，在目标分布的小验证集上优化，无需重新训练主干网络。
- 实验表明，该方法在挑战性基准上显著提升检测鲁棒性，提供轻量级、原则性的自适应解决方案。

## 摘要（原文）

> Despite being trained on balanced datasets, existing AI-generated image detectors often exhibit systematic bias at test time, frequently misclassifying fake images as real. We hypothesize that this behavior stems from distributional shift in fake samples and implicit priors learned during training. Specifically, models tend to overfit to superficial artifacts that do not generalize well across different generation methods, leading to a misaligned decision threshold when faced with test-time distribution shift. To address this, we propose a theoretically grounded post-hoc calibration framework based on Bayesian decision theory. In particular, we introduce a learnable scalar correction to the model's logits, optimized on a small validation set from the target distribution while keeping the backbone frozen. This parametric adjustment compensates for distributional shift in model output, realigning the decision boundary even without requiring ground-truth labels. Experiments on challenging benchmarks show that our approach significantly improves robustness without retraining, offering a lightweight and principled solution for reliable and adaptive AI-generated image detection in the open world. Code is available at https://github.com/muliyangm/AIGI-Det-Calib.

