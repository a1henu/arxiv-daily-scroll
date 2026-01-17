---
layout: default
title: We Need a More Robust Classifier: Dual Causal Learning Empowers Domain-Incremental Time Series Classification
---

# We Need a More Robust Classifier: Dual Causal Learning Empowers Domain-Incremental Time Series Classification
**arXiv**：[2601.10312v1](https://arxiv.org/abs/2601.10312) · [PDF](https://arxiv.org/pdf/2601.10312.pdf)  
**作者**：Zhipeng Liu, Peibo Duan, Xuan Tang, Haodong Jing, Mingyang Geng, Yongsheng Huang, Jialu Xu, Bin Zhang, Binwu Wang  

**一句话要点**：提出双因果解耦框架以增强时间序列分类在域增量学习中的鲁棒性

**关键词**：时间序列分类, 域增量学习, 因果解耦, 鲁棒性增强, 双因果干预

## 3 点简述
- 核心问题：现有时间序列分类方法在域增量学习中面临鲁棒性不足的挑战
- 方法要点：通过时间特征解耦模块和双因果干预机制捕获类因果特征并消除混淆影响
- 实验或效果：在多个数据集和模型上验证了性能提升，并建立了综合基准

## 摘要（原文）

> The World Wide Web thrives on intelligent services that rely on accurate time series classification, which has recently witnessed significant progress driven by advances in deep learning. However, existing studies face challenges in domain incremental learning. In this paper, we propose a lightweight and robust dual-causal disentanglement framework (DualCD) to enhance the robustness of models under domain incremental scenarios, which can be seamlessly integrated into time series classification models. Specifically, DualCD first introduces a temporal feature disentanglement module to capture class-causal features and spurious features. The causal features can offer sufficient predictive power to support the classifier in domain incremental learning settings. To accurately capture these causal features, we further design a dual-causal intervention mechanism to eliminate the influence of both intra-class and inter-class confounding features. This mechanism constructs variant samples by combining the current class's causal features with intra-class spurious features and with causal features from other classes. The causal intervention loss encourages the model to accurately predict the labels of these variant samples based solely on the causal features. Extensive experiments on multiple datasets and models demonstrate that DualCD effectively improves performance in domain incremental scenarios. We summarize our rich experiments into a comprehensive benchmark to facilitate research in domain incremental time series classification.

