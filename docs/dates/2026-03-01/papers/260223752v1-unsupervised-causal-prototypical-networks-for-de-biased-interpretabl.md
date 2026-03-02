---
layout: default
title: Unsupervised Causal Prototypical Networks for De-biased Interpretable Dermoscopy Diagnosis
---

# Unsupervised Causal Prototypical Networks for De-biased Interpretable Dermoscopy Diagnosis
**arXiv**：[2602.23752v1](https://arxiv.org/abs/2602.23752) · [PDF](https://arxiv.org/pdf/2602.23752.pdf)  
**作者**：Junhao Jia, Yueyi Wu, Huangwei Chen, Haodong Jing, Haishuai Wang, Jiajun Bu, Lei Wu  

**一句话要点**：提出无监督因果原型网络CausalProto，以解决皮肤镜诊断中因数据选择偏差导致的视觉证据误导问题。

**关键词**：皮肤镜诊断, 原型网络, 因果推断, 无监督学习, 视觉可解释性, 信息瓶颈

## 3 点简述
- 核心问题：临床数据选择偏差导致原型网络学习环境混杂因素，生成虚假视觉证据，影响诊断可信度。
- 方法要点：基于结构因果模型，通过信息瓶颈约束编码器实现病理特征与环境混杂因素的无监督正交解耦，并利用后门调整进行因果干预。
- 实验或效果：在多个皮肤镜数据集上验证，CausalProto在诊断性能和视觉可解释性方面优于标准黑盒模型，未牺牲准确性。

## 摘要（原文）

> Despite the success of deep learning in dermoscopy image analysis, its inherent black-box nature hinders clinical trust, motivating the use of prototypical networks for case-based visual transparency. However, inevitable selection bias in clinical data often drives these models toward shortcut learning, where environmental confounders are erroneously encoded as predictive prototypes, generating spurious visual evidence that misleads medical decision-making. To mitigate these confounding effects, we propose CausalProto, an Unsupervised Causal Prototypical Network that fundamentally purifies the visual evidence chain. Framed within a Structural Causal Model, we employ an Information Bottleneck-constrained encoder to enforce strict unsupervised orthogonal disentanglement between pathological features and environmental confounders. By mapping these decoupled representations into independent prototypical spaces, we leverage the learned spurious dictionary to perform backdoor adjustment via do-calculus, transforming complex causal interventions into efficient expectation pooling to marginalize environmental noise. Extensive experiments on multiple dermoscopy datasets demonstrate that CausalProto achieves superior diagnostic performance and consistently outperforms standard black box models, while simultaneously providing transparent and high purity visual interpretability without suffering from the traditional accuracy compromise.

