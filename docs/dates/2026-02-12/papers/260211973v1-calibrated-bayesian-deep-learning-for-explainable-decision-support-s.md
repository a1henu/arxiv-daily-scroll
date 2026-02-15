---
layout: default
title: Calibrated Bayesian Deep Learning for Explainable Decision Support Systems Based on Medical Imaging
---

# Calibrated Bayesian Deep Learning for Explainable Decision Support Systems Based on Medical Imaging
**arXiv**：[2602.11973v1](https://arxiv.org/abs/2602.11973) · [PDF](https://arxiv.org/pdf/2602.11973.pdf)  
**作者**：Hua Xu, Julián D. Arias-Londoño, Juan I. Godino-Llorente  

**一句话要点**：提出基于贝叶斯深度学习的校准框架，以提升医疗影像决策支持系统的可靠性与可解释性。

**关键词**：贝叶斯深度学习, 模型校准, 医疗影像分析, 不确定性量化, 决策支持系统, 可解释人工智能

## 3 点简述
- 核心问题：深度学习模型在医疗影像决策中常存在校准不足，表现为错误预测过度自信，影响临床可靠性。
- 方法要点：引入置信度-不确定性边界损失优化训练，结合双温度缩放进行后处理校准，强化预测正确性与不确定性估计的对齐。
- 实验或效果：在肺炎筛查、糖尿病视网膜病变检测和皮肤病变识别等任务上验证，实现跨模态校准改进，并在数据稀缺和不平衡场景中保持稳健性能。

## 摘要（原文）

> In critical decision support systems based on medical imaging, the reliability of AI-assisted decision-making is as relevant as predictive accuracy. Although deep learning models have demonstrated significant accuracy, they frequently suffer from miscalibration, manifested as overconfidence in erroneous predictions. To facilitate clinical acceptance, it is imperative that models quantify uncertainty in a manner that correlates with prediction correctness, allowing clinicians to identify unreliable outputs for further review. In order to address this necessity, the present paper proposes a generalizable probabilistic optimization framework grounded in Bayesian deep learning. Specifically, a novel Confidence-Uncertainty Boundary Loss (CUB-Loss) is introduced that imposes penalties on high-certainty errors and low-certainty correct predictions, explicitly enforcing alignment between prediction correctness and uncertainty estimates. Complementing this training-time optimization, a Dual Temperature Scaling (DTS) strategy is devised for post-hoc calibration, further refining the posterior distribution to improve intuitive explainability. The proposed framework is validated on three distinct medical imaging tasks: automatic screening of pneumonia, diabetic retinopathy detection, and identification of skin lesions. Empirical results demonstrate that the proposed approach achieves consistent calibration improvements across diverse modalities, maintains robust performance in data-scarce scenarios, and remains effective on severely imbalanced datasets, underscoring its potential for real clinical deployment.

