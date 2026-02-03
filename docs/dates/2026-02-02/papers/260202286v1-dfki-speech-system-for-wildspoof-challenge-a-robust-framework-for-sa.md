---
layout: default
title: DFKI-Speech System for WildSpoof Challenge: A robust framework for SASV In-the-Wild
---

# DFKI-Speech System for WildSpoof Challenge: A robust framework for SASV In-the-Wild
**arXiv**：[2602.02286v1](https://arxiv.org/abs/2602.02286) · [PDF](https://arxiv.org/pdf/2602.02286.pdf)  
**作者**：Arnab Das, Yassine El Kheir, Enes Erdem Erdogan, Feidi Kallel, Tim Polzehl, Sebastian Moeller  

**一句话要点**：提出鲁棒SASV框架，结合欺骗检测与说话人验证，用于WildSpoof挑战赛。

**关键词**：欺骗检测, 说话人验证, 图神经网络, 对比学习, 模型集成, 自监督学习

## 3 点简述
- 核心问题：在SASV任务中，需同时检测欺骗攻击并验证说话人身份，以应对野外环境挑战。
- 方法要点：欺骗检测采用自监督语音嵌入提取器与图神经网络后端，结合MoE融合高低级特征；说话人验证使用低复杂度CNN融合多尺度特征，并应用对比圆损失优化训练。
- 实验或效果：通过AS Norm分数归一化和模型集成，增强系统判别能力，提升在WildSpoof挑战赛中的性能。

## 摘要（原文）

> This paper presents the DFKI-Speech system developed for the WildSpoof Challenge under the Spoofing aware Automatic Speaker Verification (SASV) track. We propose a robust SASV framework in which a spoofing detector and a speaker verification (SV) network operate in tandem. The spoofing detector employs a self-supervised speech embedding extractor as the frontend, combined with a state-of-the-art graph neural network backend. In addition, a top-3 layer based mixture-of-experts (MoE) is used to fuse high-level and low-level features for effective spoofed utterance detection. For speaker verification, we adapt a low-complexity convolutional neural network that fuses 2D and 1D features at multiple scales, trained with the SphereFace loss. Additionally, contrastive circle loss is applied to adaptively weight positive and negative pairs within each training batch, enabling the network to better distinguish between hard and easy sample pairs. Finally, fixed imposter cohort based AS Norm score normalization and model ensembling are used to further enhance the discriminative capability of the speaker verification system.

