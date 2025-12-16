---
layout: default
title: Calibrating Uncertainty for Zero-Shot Adversarial CLIP
---

# Calibrating Uncertainty for Zero-Shot Adversarial CLIP
**arXiv**：[2512.12997v1](https://arxiv.org/abs/2512.12997) · [PDF](https://arxiv.org/pdf/2512.12997.pdf)  
**作者**：Wenjing lu, Zerui Tao, Dongping Zhang, Yuning Qiu, Yang Yang, Qibin Zhao  

**一句话要点**：提出基于狄利克雷分布重参数化的对抗微调目标，以校准零样本对抗CLIP的不确定性。

**关键词**：零样本学习, 对抗鲁棒性, 不确定性校准, CLIP模型, 狄利克雷分布

## 3 点简述
- 核心问题：对抗扰动导致CLIP不确定性被抑制，产生错误校准和过度自信。
- 方法要点：通过狄利克雷分布重参数化CLIP输出，统一表示语义结构和预测置信度。
- 实验或效果：在多个零样本分类基准上恢复校准不确定性，保持清洁精度和对抗鲁棒性。

## 摘要（原文）

> CLIP delivers strong zero-shot classification but remains highly vulnerable to adversarial attacks. Previous work of adversarial fine-tuning largely focuses on matching the predicted logits between clean and adversarial examples, which overlooks uncertainty calibration and may degrade the zero-shot generalization. A common expectation in reliable uncertainty estimation is that predictive uncertainty should increase as inputs become more difficult or shift away from the training distribution. However, we frequently observe the opposite in the adversarial setting: perturbations not only degrade accuracy but also suppress uncertainty, leading to severe miscalibration and unreliable over-confidence. This overlooked phenomenon highlights a critical reliability gap beyond robustness. To bridge this gap, we propose a novel adversarial fine-tuning objective for CLIP considering both prediction accuracy and uncertainty alignments. By reparameterizing the output of CLIP as the concentration parameter of a Dirichlet distribution, we propose a unified representation that captures relative semantic structure and the magnitude of predictive confidence. Our objective aligns these distributions holistically under perturbations, moving beyond single-logit anchoring and restoring calibrated uncertainty. Experiments on multiple zero-shot classification benchmarks demonstrate that our approach effectively restores calibrated uncertainty and achieves competitive adversarial robustness while maintaining clean accuracy.

