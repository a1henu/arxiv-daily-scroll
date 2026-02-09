---
layout: default
title: Don't Break the Boundary: Continual Unlearning for OOD Detection Based on Free Energy Repulsion
---

# Don't Break the Boundary: Continual Unlearning for OOD Detection Based on Free Energy Repulsion
**arXiv**：[2602.06331v1](https://arxiv.org/abs/2602.06331) · [PDF](https://arxiv.org/pdf/2602.06331.pdf)  
**作者**：Ningkang Peng, Kun Shao, Jingyang Mao, Linjing Qian, Xiaoqian Peng, Xichen Yang, Yanhui Gu  

**一句话要点**：提出TFER框架以解决OOD检测中类别遗忘与边界保持的几何矛盾

**关键词**：分布外检测, 机器遗忘, 自由能原理, 持续学习, 参数微调

## 3 点简述
- 核心问题：OOD检测依赖静态紧凑数据流形，传统遗忘方法会破坏该结构导致性能崩溃
- 方法要点：将目标类转化为OOD样本，通过自由能推拉机制实现参数高效微调
- 实验效果：在持续遗忘任务中保持剩余类判别性能，展现结构稳定性

## 摘要（原文）

> Deploying trustworthy AI in open-world environments faces a dual challenge: the necessity for robust Out-of-Distribution (OOD) detection to ensure system safety, and the demand for flexible machine unlearning to satisfy privacy compliance and model rectification. However, this objective encounters a fundamental geometric contradiction: current OOD detectors rely on a static and compact data manifold, whereas traditional classification-oriented unlearning methods disrupt this delicate structure, leading to a catastrophic loss of the model's capability to discriminate anomalies while erasing target classes. To resolve this dilemma, we first define the problem of boundary-preserving class unlearning and propose a pivotal conceptual shift: in the context of OOD detection, effective unlearning is mathematically equivalent to transforming the target class into OOD samples. Based on this, we propose the TFER (Total Free Energy Repulsion) framework. Inspired by the free energy principle, TFER constructs a novel Push-Pull game mechanism: it anchors retained classes within a low-energy ID manifold through a pull mechanism, while actively expelling forgotten classes to high-energy OOD regions using a free energy repulsion force. This approach is implemented via parameter-efficient fine-tuning, circumventing the prohibitive cost of full retraining. Extensive experiments demonstrate that TFER achieves precise unlearning while maximally preserving the model's discriminative performance on remaining classes and external OOD data. More importantly, our study reveals that the unique Push-Pull equilibrium of TFER endows the model with inherent structural stability, allowing it to effectively resist catastrophic forgetting without complex additional constraints, thereby demonstrating exceptional potential in continual unlearning tasks.

