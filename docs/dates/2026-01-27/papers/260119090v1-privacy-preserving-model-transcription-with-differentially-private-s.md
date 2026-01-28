---
layout: default
title: Privacy-Preserving Model Transcription with Differentially Private Synthetic Distillation
---

# Privacy-Preserving Model Transcription with Differentially Private Synthetic Distillation
**arXiv**：[2601.19090v1](https://arxiv.org/abs/2601.19090) · [PDF](https://arxiv.org/pdf/2601.19090.pdf)  
**作者**：Bochao Liu, Shiming Ge, Pengju Wang, Shikun Li, Tongliang Liu  

**一句话要点**：提出差分隐私合成蒸馏方法，实现无数据模型转录以保护隐私

**关键词**：差分隐私, 模型蒸馏, 合成数据生成, 隐私保护, 对抗训练, 模型转录

## 3 点简述
- 核心问题：预训练模型可能泄露私有数据或标签信息，需隐私保护部署
- 方法要点：通过生成器生成合成数据，结合差分隐私扰动标签，交替优化教师、学生和生成器
- 实验或效果：理论证明差分隐私和收敛性，实验优于26个先进方法，学生模型性能好且隐私保护

## 摘要（原文）

> While many deep learning models trained on private datasets have been deployed in various practical tasks, they may pose a privacy leakage risk as attackers could recover informative data or label knowledge from models. In this work, we present \emph{privacy-preserving model transcription}, a data-free model-to-model conversion solution to facilitate model deployment with a privacy guarantee. To this end, we propose a cooperative-competitive learning approach termed \emph{differentially private synthetic distillation} that learns to convert a pretrained model (teacher) into its privacy-preserving counterpart (student) via a trainable generator without access to private data. The learning collaborates with three players in a unified framework and performs alternate optimization: i)~the generator is learned to generate synthetic data, ii)~the teacher and student accept the synthetic data and compute differential private labels by flexible data or label noisy perturbation, and iii)~the student is updated with noisy labels and the generator is updated by taking the student as a discriminator for adversarial training. We theoretically prove that our approach can guarantee differential privacy and convergence. The transcribed student has good performance and privacy protection, while the resulting generator can generate private synthetic data for downstream tasks. Extensive experiments clearly demonstrate that our approach outperforms 26 state-of-the-arts.

