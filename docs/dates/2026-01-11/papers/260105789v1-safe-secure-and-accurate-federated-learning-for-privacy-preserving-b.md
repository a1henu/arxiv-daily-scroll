---
layout: default
title: SAFE: Secure and Accurate Federated Learning for Privacy-Preserving Brain-Computer Interfaces
---

# SAFE: Secure and Accurate Federated Learning for Privacy-Preserving Brain-Computer Interfaces
**arXiv**：[2601.05789v1](https://arxiv.org/abs/2601.05789) · [PDF](https://arxiv.org/pdf/2601.05789.pdf)  
**作者**：Tianwang Jia, Xiaoqing Chen, Dongrui Wu  

**一句话要点**：提出SAFE联邦学习方法，以保护隐私并提升脑机接口的解码准确性和对抗鲁棒性。

**关键词**：联邦学习, 脑机接口, 隐私保护, 对抗鲁棒性, EEG解码

## 3 点简述
- 核心问题：脑机接口面临泛化不足、对抗攻击和隐私泄露挑战。
- 方法要点：采用本地批量特定归一化和联邦对抗训练，增强模型性能。
- 实验或效果：在五个EEG数据集上优于14种先进方法，无需目标用户校准数据。

## 摘要（原文）

> Electroencephalogram (EEG)-based brain-computer interfaces (BCIs) are widely adopted due to their efficiency and portability; however, their decoding algorithms still face multiple challenges, including inadequate generalization, adversarial vulnerability, and privacy leakage. This paper proposes Secure and Accurate FEderated learning (SAFE), a federated learning-based approach that protects user privacy by keeping data local during model training. SAFE employs local batch-specific normalization to mitigate cross-subject feature distribution shifts and hence improves model generalization. It further enhances adversarial robustness by introducing perturbations in both the input space and the parameter space through federated adversarial training and adversarial weight perturbation. Experiments on five EEG datasets from motor imagery (MI) and event-related potential (ERP) BCI paradigms demonstrated that SAFE consistently outperformed 14 state-of-the-art approaches in both decoding accuracy and adversarial robustness, while ensuring privacy protection. Notably, it even outperformed centralized training approaches that do not consider privacy protection at all. To our knowledge, SAFE is the first algorithm to simultaneously achieve high decoding accuracy, strong adversarial robustness, and reliable privacy protection without using any calibration data from the target subject, making it highly desirable for real-world BCIs.

