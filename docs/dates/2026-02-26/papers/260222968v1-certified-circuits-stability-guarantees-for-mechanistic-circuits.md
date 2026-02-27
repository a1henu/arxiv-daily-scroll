---
layout: default
title: Certified Circuits: Stability Guarantees for Mechanistic Circuits
---

# Certified Circuits: Stability Guarantees for Mechanistic Circuits
**arXiv**：[2602.22968v1](https://arxiv.org/abs/2602.22968) · [PDF](https://arxiv.org/pdf/2602.22968.pdf)  
**作者**：Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer  

**一句话要点**：提出Certified Circuits框架，通过随机数据子采样为机制电路发现提供稳定性保证

**关键词**：机制可解释性, 电路发现, 稳定性认证, 神经网络解释, 数据扰动, 泛化能力

## 3 点简述
- 现有机制电路发现方法脆弱，依赖概念数据集且泛化差，可能捕获伪影而非概念
- 框架包装黑盒发现算法，基于编辑距离扰动认证电路组件决策稳定性，剔除不稳定神经元
- 在ImageNet和OOD数据集上，认证电路准确率提升达91%，神经元减少45%，基线失效时仍可靠

## 摘要（原文）

> Understanding how neural networks arrive at their predictions is essential for debugging, auditing, and deployment. Mechanistic interpretability pursues this goal by identifying circuits - minimal subnetworks responsible for specific behaviors. However, existing circuit discovery methods are brittle: circuits depend strongly on the chosen concept dataset and often fail to transfer out-of-distribution, raising doubts whether they capture concept or dataset-specific artifacts. We introduce Certified Circuits, which provide provable stability guarantees for circuit discovery. Our framework wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. Unstable neurons are abstained from, yielding circuits that are more compact and more accurate. On ImageNet and OOD datasets, certified circuits achieve up to 91% higher accuracy while using 45% fewer neurons, and remain reliable where baselines degrade. Certified Circuits puts circuit discovery on formal ground by producing mechanistic explanations that are provably stable and better aligned with the target concept. Code will be released soon!

