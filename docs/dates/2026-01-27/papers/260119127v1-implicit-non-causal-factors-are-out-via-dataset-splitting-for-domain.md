---
layout: default
title: Implicit Non-Causal Factors are Out via Dataset Splitting for Domain Generalization Object Detection
---

# Implicit Non-Causal Factors are Out via Dataset Splitting for Domain Generalization Object Detection
**arXiv**：[2601.19127v1](https://arxiv.org/abs/2601.19127) · [PDF](https://arxiv.org/pdf/2601.19127.pdf)  
**作者**：Zhilong Zhang, Lei Zhang, Qing He, Shuyin Xia, Guoyin Wang, Fuxiang Huang  

**一句话要点**：提出GB-DAL方法，通过数据集分割和模拟非因果因素增强，以解决开放世界目标检测中的隐式非因果因素问题。

**关键词**：域泛化目标检测, 隐式非因果因素, 域对抗学习, 数据集分割, 数据增强, 开放世界检测

## 3 点简述
- 核心问题：开放世界目标检测中，隐式非因果因素阻碍域不变表示学习，传统域对抗学习方法因稀疏域标签和隐式偏差而受限。
- 方法要点：引入GB-DAL，包括PGBS模块生成密集域以捕获更多非因果因素，以及SNF模块通过数据增强模拟非因果因素降低其隐式性。
- 实验或效果：在多个基准测试中，GB-DAL展现出优于现有方法的泛化性能，适应新环境的能力更强。

## 摘要（原文）

> Open world object detection faces a significant challenge in domain-invariant representation, i.e., implicit non-causal factors. Most domain generalization (DG) methods based on domain adversarial learning (DAL) pay much attention to learn domain-invariant information, but often overlook the potential non-causal factors. We unveil two critical causes: 1) The domain discriminator-based DAL method is subject to the extremely sparse domain label, i.e., assigning only one domain label to each dataset, thus can only associate explicit non-causal factor, which is incredibly limited. 2) The non-causal factors, induced by unidentified data bias, are excessively implicit and cannot be solely discerned by conventional DAL paradigm. Based on these key findings, inspired by the Granular-Ball perspective, we propose an improved DAL method, i.e., GB-DAL. The proposed GB-DAL utilizes Prototype-based Granular Ball Splitting (PGBS) module to generate more dense domains from limited datasets, akin to more fine-grained granular balls, indicating more potential non-causal factors. Inspired by adversarial perturbations akin to non-causal factors, we propose a Simulated Non-causal Factors (SNF) module as a means of data augmentation to reduce the implicitness of non-causal factors, and facilitate the training of GB-DAL. Comparative experiments on numerous benchmarks demonstrate that our method achieves better generalization performance in novel circumstances.

