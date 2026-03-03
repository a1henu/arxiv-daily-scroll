---
layout: default
title: Explanation-Guided Adversarial Training for Robust and Interpretable Models
---

# Explanation-Guided Adversarial Training for Robust and Interpretable Models
**arXiv**：[2603.01938v1](https://arxiv.org/abs/2603.01938) · [PDF](https://arxiv.org/pdf/2603.01938.pdf)  
**作者**：Chao Chen, Yanhui Chen, Shanshan Lin, Dongsheng Hong, Shu Wu, Xiangwen Liao, Chuanyi Liu  

**一句话要点**：提出解释引导对抗训练框架，以同时提升模型鲁棒性与可解释性。

**关键词**：对抗训练, 可解释性学习, 鲁棒性提升, 解释引导, 分布外泛化, 归因稳定性

## 3 点简述
- 核心问题：深度神经网络在对抗攻击和分布外场景下预测和解释不稳定，且现有方法难以兼顾鲁棒性与可解释性。
- 方法要点：结合对抗训练与解释引导学习，通过动态生成对抗样本并施加解释约束，联合优化分类性能、鲁棒性和归因稳定性。
- 实验或效果：在分布外基准数据集上，EGAT在干净和对抗准确率上显著优于基线，训练时间仅增加16%，并产生更语义有意义的解释。

## 摘要（原文）

> Deep neural networks (DNNs) have achieved remarkable performance in many tasks, yet they often behave as opaque black boxes. Explanation-guided learning (EGL) methods steer DNNs using human-provided explanations or supervision on model attributions. These approaches improve interpretability but typically assume benign inputs and incur heavy annotation costs. In contrast, both predictions and saliency maps of DNNs could dramatically alter facing imperceptible perturbations or unseen patterns. Adversarial training (AT) can substantially improve robustness, but it does not guarantee that model decisions rely on semantically meaningful features. In response, we propose Explanation-Guided Adversarial Training (EGAT), a unified framework that integrates the strength of AT and EGL to simultaneously improve prediction performance, robustness, and explanation quality. EGAT generates adversarial examples on the fly while imposing explanation-based constraints on the model. By jointly optimizing classification performance, adversarial robustness, and attributional stability, EGAT is not only more resistant to unexpected cases, including adversarial attacks and out-of-distribution (OOD) scenarios, but also offer human-interpretable justifications for the decisions. We further formalize EGAT within the Probably Approximately Correct learning framework, demonstrating theoretically that it yields more stable predictions under unexpected situations compared to standard AT. Empirical evaluations on OOD benchmark datasets show that EGAT consistently outperforms competitive baselines in both clean accuracy and adversarial accuracy +37% while producing more semantically meaningful explanations, and requiring only a limited increase +16% in training time.

