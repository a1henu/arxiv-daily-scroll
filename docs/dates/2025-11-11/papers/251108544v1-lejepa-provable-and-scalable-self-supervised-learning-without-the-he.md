---
layout: default
title: LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics
---

# LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics
**arXiv**：[2511.08544v1](https://arxiv.org/abs/2511.08544) · [PDF](https://arxiv.org/pdf/2511.08544.pdf)  
**作者**：Randall Balestriero, Yann LeCun  

**一句话要点**：提出LeJEPA以提供可证明且可扩展的自监督学习，无需启发式方法。

**关键词**：自监督学习, 联合嵌入预测架构, 各向同性高斯分布, 可扩展训练, 理论指导, 图像识别

## 3 点简述
- 核心问题：JEPA缺乏理论指导，导致研发依赖启发式方法。
- 方法要点：结合预测损失与SIGReg，约束嵌入分布为各向同性高斯。
- 实验或效果：在ImageNet-1k上，ViT-H/14线性评估准确率达79%。

## 摘要（原文）

> Learning manipulable representations of the world and its dynamics is central to AI. Joint-Embedding Predictive Architectures (JEPAs) offer a promising blueprint, but lack of practical guidance and theory has led to ad-hoc R&D. We present a comprehensive theory of JEPAs and instantiate it in {\bf LeJEPA}, a lean, scalable, and theoretically grounded training objective. First, we identify the isotropic Gaussian as the optimal distribution that JEPAs' embeddings should follow to minimize downstream prediction risk. Second, we introduce a novel objective--{\bf Sketched Isotropic Gaussian Regularization} (SIGReg)--to constrain embeddings to reach that ideal distribution. Combining the JEPA predictive loss with SIGReg yields LeJEPA with numerous theoretical and practical benefits: (i) single trade-off hyperparameter, (ii) linear time and memory complexity, (iii) stability across hyper-parameters, architectures (ResNets, ViTs, ConvNets) and domains, (iv) heuristics-free, e.g., no stop-gradient, no teacher-student, no hyper-parameter schedulers, and (v) distributed training-friendly implementation requiring only $\approx$50 lines of code. Our empirical validation covers 10+ datasets, 60+ architectures, all with varying scales and domains. As an example, using imagenet-1k for pretraining and linear evaluation with frozen backbone, LeJEPA reaches 79\% with a ViT-H/14. We hope that the simplicity and theory-friendly ecosystem offered by LeJEPA will reestablish self-supervised pre-training as a core pillar of AI research (\href{git@github.com:rbalestr-lab/lejepa.git}{GitHub repo}).

