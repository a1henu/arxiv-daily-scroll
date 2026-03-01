---
layout: default
title: From Calibration to Refinement: Seeking Certainty via Probabilistic Evidence Propagation for Noisy-Label Person Re-Identification
---

# From Calibration to Refinement: Seeking Certainty via Probabilistic Evidence Propagation for Noisy-Label Person Re-Identification
**arXiv**：[2602.23133v1](https://arxiv.org/abs/2602.23133) · [PDF](https://arxiv.org/pdf/2602.23133.pdf)  
**作者**：Xin Yuan, Zhiyong Zhang, Xin Xu, Zheng Wang, Chia-Wen Lin  

**一句话要点**：提出CARE方法，通过概率证据传播从校准到精炼，解决噪声标签行人重识别中的过自信和样本选择问题。

**关键词**：行人重识别, 噪声标签学习, 概率校准, 样本选择, 证据传播, 两阶段框架

## 3 点简述
- 核心问题：现有方法因softmax平移不变性导致过自信预测，且小损失准则丢弃重要难正样本。
- 方法要点：两阶段框架，校准阶段用概率证据校准消除平移不变性，精炼阶段用证据传播精炼准确区分干净与噪声样本。
- 实验或效果：在Market1501等数据集上，针对随机和模式噪声，CARE实现竞争性性能。

## 摘要（原文）

> With the increasing demand for robust person Re-ID in unconstrained environments, learning from datasets with noisy labels and sparse per-identity samples remains a critical challenge. Existing noise-robust person Re-ID methods primarily rely on loss-correction or sample-selection strategies using softmax outputs. However, these methods suffer from two key limitations: 1) Softmax exhibits translation invariance, leading to over-confident and unreliable predictions on corrupted labels. 2) Conventional sample selection based on small-loss criteria often discards valuable hard positives that are crucial for learning discriminative features. To overcome these issues, we propose the CAlibration-to-REfinement (CARE) method, a two-stage framework that seeks certainty through probabilistic evidence propagation from calibration to refinement. In the calibration stage, we propose the probabilistic evidence calibration (PEC) that dismantles softmax translation invariance by injecting adaptive learnable parameters into the similarity function, and employs an evidential calibration loss to mitigate overconfidence on mislabeled samples. In the refinement stage, we design the evidence propagation refinement (EPR) that can more accurately distinguish between clean and noisy samples. Specifically, the EPR contains two steps: Firstly, the composite angular margin (CAM) metric is proposed to precisely distinguish clean but hard-to-learn positive samples from mislabeled ones in a hyperspherical space; Secondly, the certainty-oriented sphere weighting (COSW) is developed to dynamically allocate the importance of samples according to CAM, ensuring clean instances drive model updates. Extensive experimental results on Market1501, DukeMTMC-ReID, and CUHK03 datasets under both random and patterned noises show that CARE achieves competitive performance.

