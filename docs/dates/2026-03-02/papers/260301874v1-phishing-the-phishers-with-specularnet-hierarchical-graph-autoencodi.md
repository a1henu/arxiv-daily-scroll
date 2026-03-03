---
layout: default
title: Phishing the Phishers with SpecularNet: Hierarchical Graph Autoencoding for Reference-Free Web Phishing Detection
---

# Phishing the Phishers with SpecularNet: Hierarchical Graph Autoencoding for Reference-Free Web Phishing Detection
**arXiv**：[2603.01874v1](https://arxiv.org/abs/2603.01874) · [PDF](https://arxiv.org/pdf/2603.01874.pdf)  
**作者**：Tailai Song, Pedro Casas, Michela Meo  

**一句话要点**：提出SpecularNet，一种基于层次图自编码的轻量级无参考网络钓鱼检测框架。

**关键词**：网络钓鱼检测, 层次图自编码, 轻量级框架, 无参考检测, DOM建模, 计算效率

## 3 点简述
- 核心问题：现有钓鱼检测方法依赖外部知识库或复杂多模态管道，限制实用性、可扩展性和可复现性。
- 方法要点：仅使用域名和HTML结构，将DOM建模为树，采用层次图自编码架构进行方向性层级消息传递。
- 实验或效果：在基准数据集上F1分数达93.9%，推理时间降至约20毫秒/网页，显著降低计算成本。

## 摘要（原文）

> Phishing remains the most pervasive threat to the Web, enabling large-scale credential theft and financial fraud through deceptive webpages. While recent reference-based and generative-AI-driven phishing detectors achieve strong accuracy, their reliance on external knowledge bases, cloud services, and complex multimodal pipelines fundamentally limits practicality, scalability, and reproducibility. In contrast, conventional deep learning approaches often fail to generalize to evolving phishing campaigns. We introduce SpecularNet, a novel lightweight framework for reference-free web phishing detection that demonstrates how carefully designed compact architectures can rival heavyweight systems. SpecularNet operates solely on the domain name and HTML structure, modeling the Document Object Model (DOM) as a tree and leveraging a hierarchical graph autoencoding architecture with directional, level-wise message passing. This design captures higher-order structural invariants of phishing webpages while enabling fast, end-to-end inference on standard CPUs. Extensive evaluation against 13 state of the art phishing detectors, including leading reference-based systems, shows that SpecularNet achieves competitive detection performance with dramatically lower computational cost. On benchmark datasets, it reaches an F1 score of 93.9%, trailing the best reference-based method slightly while reducing inference time from several seconds to approximately 20 milliseconds per webpage. Field and robustness evaluations further validate SpecularNet in real-world deployments, on a newly collected 2026 open-world dataset, and against adversarial attacks.

