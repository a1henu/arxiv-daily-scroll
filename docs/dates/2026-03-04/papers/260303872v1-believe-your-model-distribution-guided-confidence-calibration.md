---
layout: default
title: Believe Your Model: Distribution-Guided Confidence Calibration
---

# Believe Your Model: Distribution-Guided Confidence Calibration
**arXiv**：[2603.03872v1](https://arxiv.org/abs/2603.03872) · [PDF](https://arxiv.org/pdf/2603.03872.pdf)  
**作者**：Xizhong Yang, Haotian Zhang, Huiming Wang, Mofei Song  

**一句话要点**：提出DistriVoting和SelfStepConf方法，利用分布先验和动态调整提升大推理模型的置信度校准与答案选择性能。

**关键词**：置信度校准, 分布先验, 高斯混合模型, 答案选择, 大推理模型, 测试时扩展

## 3 点简述
- 核心问题：现有大推理模型在测试时扩展中，置信度分布信息未充分利用于答案选择，导致置信度与准确性关联不充分。
- 方法要点：DistriVoting通过高斯混合模型分解置信度分布并应用拒绝过滤器，SelfStepConf利用步骤级置信度动态调整推理以增强分布分离。
- 实验或效果：在16个模型和5个基准测试中，方法显著优于现有先进方法，提升了置信度可靠性和预测准确性。

## 摘要（原文）

> Large Reasoning Models have demonstrated remarkable performance with the advancement of test-time scaling techniques, which enhances prediction accuracy by generating multiple candidate responses and selecting the most reliable answer. While prior work has analyzed that internal model signals like confidence scores can partly indicate response correctness and exhibit a distributional correlation with accuracy, such distributional information has not been fully utilized to guide answer selection. Motivated by this, we propose DistriVoting, which incorporates distributional priors as another signal alongside confidence during voting. Specifically, our method (1) first decomposes the mixed confidence distribution into positive and negative components using Gaussian Mixture Models, (2) then applies a reject filter based on positive/negative samples from them to mitigate overlap between the two distributions. Besides, to further alleviate the overlap from the perspective of distribution itself, we propose SelfStepConf, which uses step-level confidence to dynamically adjust inference process, increasing the separation between the two distributions to improve the reliability of confidences in voting. Experiments across 16 models and 5 benchmarks demonstrate that our method significantly outperforms state-of-the-art approaches.

