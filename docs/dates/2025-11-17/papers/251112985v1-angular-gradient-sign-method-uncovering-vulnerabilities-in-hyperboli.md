---
layout: default
title: Angular Gradient Sign Method: Uncovering Vulnerabilities in Hyperbolic Networks
---

# Angular Gradient Sign Method: Uncovering Vulnerabilities in Hyperbolic Networks
**arXiv**：[2511.12985v1](https://arxiv.org/abs/2511.12985) · [PDF](https://arxiv.org/pdf/2511.12985.pdf)  
**作者**：Minsoo Jo, Dongyoon Yang, Taesup Kim  

**一句话要点**：提出角梯度符号方法以攻击双曲网络中的漏洞

**关键词**：对抗攻击, 双曲网络, 几何感知, 梯度分解, 图像分类, 跨模态检索

## 3 点简述
- 现有对抗攻击方法未考虑双曲几何结构，导致攻击效率低或不一致
- 在双曲空间切空间中分解梯度，仅沿角方向施加扰动以生成对抗样本
- 实验显示在图像分类和跨模态检索任务中，攻击成功率高于传统方法

## 摘要（原文）

> Adversarial examples in neural networks have been extensively studied in Euclidean geometry, but recent advances in \textit{hyperbolic networks} call for a reevaluation of attack strategies in non-Euclidean geometries. Existing methods such as FGSM and PGD apply perturbations without regard to the underlying hyperbolic structure, potentially leading to inefficient or geometrically inconsistent attacks. In this work, we propose a novel adversarial attack that explicitly leverages the geometric properties of hyperbolic space. Specifically, we compute the gradient of the loss function in the tangent space of hyperbolic space, decompose it into a radial (depth) component and an angular (semantic) component, and apply perturbation derived solely from the angular direction. Our method generates adversarial examples by focusing perturbations in semantically sensitive directions encoded in angular movement within the hyperbolic geometry. Empirical results on image classification, cross-modal retrieval tasks and network architectures demonstrate that our attack achieves higher fooling rates than conventional adversarial attacks, while producing high-impact perturbations with deeper insights into vulnerabilities of hyperbolic embeddings. This work highlights the importance of geometry-aware adversarial strategies in curved representation spaces and provides a principled framework for attacking hierarchical embeddings.

