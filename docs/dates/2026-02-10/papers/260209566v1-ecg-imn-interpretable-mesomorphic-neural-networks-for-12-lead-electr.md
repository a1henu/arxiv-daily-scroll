---
layout: default
title: ECG-IMN: Interpretable Mesomorphic Neural Networks for 12-Lead Electrocardiogram Interpretation
---

# ECG-IMN: Interpretable Mesomorphic Neural Networks for 12-Lead Electrocardiogram Interpretation
**arXiv**：[2602.09566v1](https://arxiv.org/abs/2602.09566) · [PDF](https://arxiv.org/pdf/2602.09566.pdf)  
**作者**：Vajira Thambawita, Jonas L. Isaksen, Jørgen K. Kanters, Hugo L. Hammer, Pål Halvorsen  

**一句话要点**：提出ECG-IMN以解决12导联心电图分类中深度学习模型可解释性不足的问题。

**关键词**：心电图分类, 可解释人工智能, 超网络, 12导联心电图, 医学诊断

## 3 点简述
- 核心问题：深度学习模型在ECG诊断中性能高但缺乏透明度，阻碍临床部署。
- 方法要点：使用超网络架构，通过卷积骨干生成样本特定线性模型参数，实现内在可解释性。
- 实验或效果：在PTB-XL数据集上验证，性能与黑盒基线相当，并提供忠实解释。

## 摘要（原文）

> Deep learning has achieved expert-level performance in automated electrocardiogram (ECG) diagnosis, yet the "black-box" nature of these models hinders their clinical deployment. Trust in medical AI requires not just high accuracy but also transparency regarding the specific physiological features driving predictions. Existing explainability methods for ECGs typically rely on post-hoc approximations (e.g., Grad-CAM and SHAP), which can be unstable, computationally expensive, and unfaithful to the model's actual decision-making process. In this work, we propose the ECG-IMN, an Interpretable Mesomorphic Neural Network tailored for high-resolution 12-lead ECG classification. Unlike standard classifiers, the ECG-IMN functions as a hypernetwork: a deep convolutional backbone generates the parameters of a strictly linear model specific to each input sample. This architecture enforces intrinsic interpretability, as the decision logic is mathematically transparent and the generated weights (W) serve as exact, high-resolution feature attribution maps. We introduce a transition decoder that effectively maps latent features to sample-wise weights, enabling precise localization of pathological evidence (e.g., ST-elevation, T-wave inversion) in both time and lead dimensions. We evaluate our approach on the PTB-XL dataset for classification tasks, demonstrating that the ECG-IMN achieves competitive predictive performance (AUROC comparable to black-box baselines) while providing faithful, instance-specific explanations. By explicitly decoupling parameter generation from prediction execution, our framework bridges the gap between deep learning capability and clinical trustworthiness, offering a principled path toward "white-box" cardiac diagnostics.

