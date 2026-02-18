---
layout: default
title: X-MAP: eXplainable Misclassification Analysis and Profiling for Spam and Phishing Detection
---

# X-MAP: eXplainable Misclassification Analysis and Profiling for Spam and Phishing Detection
**arXiv**：[2602.15298v1](https://arxiv.org/abs/2602.15298) · [PDF](https://arxiv.org/pdf/2602.15298.pdf)  
**作者**：Qi Zhang, Dian Chen, Lance M. Kaplan, Audun Jøsang, Dong Hyun Jeong, Feng Chen, Jin-Hee Cho  

**一句话要点**：提出X-MAP框架以解释垃圾邮件和钓鱼检测中的误分类模式

**关键词**：误分类分析, 可解释人工智能, 垃圾邮件检测, 钓鱼检测, 主题建模, SHAP

## 3 点简述
- 核心问题：误分类在垃圾邮件和钓鱼检测中危害大，现有方法可标记潜在错误但解释性有限。
- 方法要点：结合SHAP特征归因与非负矩阵分解，构建可解释主题轮廓，用Jensen-Shannon散度测量偏差。
- 实验效果：在SMS和钓鱼数据集上，误分类消息偏差至少大两倍，作为检测器AUROC达0.98，修复层可恢复97%误拒预测。

## 摘要（原文）

> Misclassifications in spam and phishing detection are very harmful, as false negatives expose users to attacks while false positives degrade trust. Existing uncertainty-based detectors can flag potential errors, but possibly be deceived and offer limited interpretability. This paper presents X-MAP, an eXplainable Misclassification Analysis and Profilling framework that reveals topic-level semantic patterns behind model failures. X-MAP combines SHAP-based feature attributions with non-negative matrix factorization to build interpretable topic profiles for reliably classified spam/phishing and legitimate messages, and measures each message's deviation from these profiles using Jensen-Shannon divergence. Experiments on SMS and phishing datasets show that misclassified messages exhibit at least two times larger divergence than correctly classified ones. As a detector, X-MAP achieves up to 0.98 AUROC and lowers the false-rejection rate at 95% TRR to 0.089 on positive predictions. When used as a repair layer on base detectors, it recovers up to 97% of falsely rejected correct predictions with moderate leakage. These results demonstrate X-MAP's effectiveness and interpretability for improving spam and phishing detection.

