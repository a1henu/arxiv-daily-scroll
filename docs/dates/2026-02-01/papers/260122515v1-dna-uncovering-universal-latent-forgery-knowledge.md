---
layout: default
title: DNA: Uncovering Universal Latent Forgery Knowledge
---

# DNA: Uncovering Universal Latent Forgery Knowledge
**arXiv**：[2601.22515v1](https://arxiv.org/abs/2601.22515) · [PDF](https://arxiv.org/pdf/2601.22515.pdf)  
**作者**：Jingtong Dou, Chuancheng Shi, Yemin Wang, Shiming Guo, Anqi Yi, Wenhua Wu, Li Zhang, Fei Shen, Tat-Seng Chua  

**一句话要点**：提出DNA框架以唤醒预训练模型中的伪造检测能力，避免端到端微调。

**关键词**：伪造检测, 预训练模型, 特征挖掘, 少样本学习, 鲁棒性评估

## 3 点简述
- 核心问题：生成AI超逼真化使表面伪影检测失效，现有方法依赖资源密集型微调。
- 方法要点：通过粗到细挖掘机制，定位关键层并隔离伪造判别单元，利用三元融合评分和曲率截断策略。
- 实验或效果：在少样本条件下实现优越检测性能，跨架构和未见生成模型展现强鲁棒性。

## 摘要（原文）

> As generative AI achieves hyper-realism, superficial artifact detection has become obsolete. While prevailing methods rely on resource-intensive fine-tuning of black-box backbones, we propose that forgery detection capability is already encoded within pre-trained models rather than requiring end-to-end retraining. To elicit this intrinsic capability, we propose the discriminative neural anchors (DNA) framework, which employs a coarse-to-fine excavation mechanism. First, by analyzing feature decoupling and attention distribution shifts, we pinpoint critical intermediate layers where the focus of the model logically transitions from global semantics to local anomalies. Subsequently, we introduce a triadic fusion scoring metric paired with a curvature-truncation strategy to strip away semantic redundancy, precisely isolating the forgery-discriminative units (FDUs) inherently imprinted with sensitivity to forgery traces. Moreover, we introduce HIFI-Gen, a high-fidelity synthetic benchmark built upon the very latest models, to address the lag in existing datasets. Experiments demonstrate that by solely relying on these anchors, DNA achieves superior detection performance even under few-shot conditions. Furthermore, it exhibits remarkable robustness across diverse architectures and against unseen generative models, validating that waking up latent neurons is more effective than extensive fine-tuning.

