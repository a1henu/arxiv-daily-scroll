---
layout: default
title: Empirical Analysis of Adversarial Robustness and Explainability Drift in Cybersecurity Classifiers
---

# Empirical Analysis of Adversarial Robustness and Explainability Drift in Cybersecurity Classifiers
**arXiv**：[2602.06395v1](https://arxiv.org/abs/2602.06395) · [PDF](https://arxiv.org/pdf/2602.06395.pdf)  
**作者**：Mona Rajhans, Vishal Khawarey  

**一句话要点**：提出鲁棒性指数以评估网络安全分类器在对抗攻击下的鲁棒性与可解释性漂移

**关键词**：对抗鲁棒性, 可解释性漂移, 网络安全分类器, 鲁棒性指数, 对抗训练

## 3 点简述
- 核心问题：对抗扰动导致网络安全分类器检测精度下降和可解释性漂移
- 方法要点：使用FGSM和PGD攻击评估鲁棒性，引入鲁棒性指数量化模型抗扰能力
- 实验或效果：在钓鱼网站和网络入侵数据集上验证，对抗训练提升鲁棒性指数达9%

## 摘要（原文）

> Machine learning (ML) models are increasingly deployed in cybersecurity applications such as phishing detection and network intrusion prevention. However, these models remain vulnerable to adversarial perturbations small, deliberate input modifications that can degrade detection accuracy and compromise interpretability. This paper presents an empirical study of adversarial robustness and explainability drift across two cybersecurity domains phishing URL classification and network intrusion detection. We evaluate the impact of L (infinity) bounded Fast Gradient Sign Method (FGSM) and Projected Gradient Descent (PGD) perturbations on model accuracy and introduce a quantitative metric, the Robustness Index (RI), defined as the area under the accuracy perturbation curve. Gradient based feature sensitivity and SHAP based attribution drift analyses reveal which input features are most susceptible to adversarial manipulation. Experiments on the Phishing Websites and UNSW NB15 datasets show consistent robustness trends, with adversarial training improving RI by up to 9 percent while maintaining clean-data accuracy. These findings highlight the coupling between robustness and interpretability degradation and underscore the importance of quantitative evaluation in the design of trustworthy, AI-driven cybersecurity systems.

