---
layout: default
title: UbiQVision: Quantifying Uncertainty in XAI for Image Recognition
---

# UbiQVision: Quantifying Uncertainty in XAI for Image Recognition
**arXiv**：[2512.20288v1](https://arxiv.org/abs/2512.20288) · [PDF](https://arxiv.org/pdf/2512.20288.pdf)  
**作者**：Akshat Dubey, Aleksandar Anžel, Bahar İlgen, Georges Hattab  

**一句话要点**：提出UbiQVision框架，量化医学图像识别中SHAP解释的不确定性。

**关键词**：不确定性量化, 可解释人工智能, 医学图像识别, SHAP解释, Dempster-Shafer理论, Dirichlet采样

## 3 点简述
- 核心问题：SHAP解释在认知和随机不确定性下不稳定，影响医学图像模型可解释性。
- 方法要点：使用Dirichlet后验采样和Dempster-Shafer理论，结合信念、可信和融合映射量化不确定性。
- 实验或效果：在三个医学影像数据集上评估，涵盖病理学、眼科学和放射学，处理不同类别分布和图像质量。

## 摘要（原文）

> Recent advances in deep learning have led to its widespread adoption across diverse domains, including medical imaging. This progress is driven by increasingly sophisticated model architectures, such as ResNets, Vision Transformers, and Hybrid Convolutional Neural Networks, that offer enhanced performance at the cost of greater complexity. This complexity often compromises model explainability and interpretability. SHAP has emerged as a prominent method for providing interpretable visualizations that aid domain experts in understanding model predictions. However, SHAP explanations can be unstable and unreliable in the presence of epistemic and aleatoric uncertainty. In this study, we address this challenge by using Dirichlet posterior sampling and Dempster-Shafer theory to quantify the uncertainty that arises from these unstable explanations in medical imaging applications. The framework uses a belief, plausible, and fusion map approach alongside statistical quantitative analysis to produce quantification of uncertainty in SHAP. Furthermore, we evaluated our framework on three medical imaging datasets with varying class distributions, image qualities, and modality types which introduces noise due to varying image resolutions and modality-specific aspect covering the examples from pathology, ophthalmology, and radiology, introducing significant epistemic uncertainty.

