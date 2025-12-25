---
layout: default
title: MiST: Understanding the Role of Mid-Stage Scientific Training in Developing Chemical Reasoning Models
---

# MiST: Understanding the Role of Mid-Stage Scientific Training in Developing Chemical Reasoning Models
**arXiv**：[2512.21231v1](https://arxiv.org/abs/2512.21231) · [PDF](https://arxiv.org/pdf/2512.21231.pdf)  
**作者**：Andres M Bran, Tong Xie, Shai Pranesh, Jeffrey Meng, Xuan Vu Nguyen, Jeremy Goumaz, David Ming Segura, Ruizhi Xu, Dongzhan Zhou, Wenjie Zhang, Bram Hoex, Philippe Schwaller  

**一句话要点**：提出MiST方法以解决化学推理模型训练中的潜在可解性限制问题

**关键词**：化学推理模型, 潜在可解性, 中期训练, 强化学习, 符号能力, 化学知识

## 3 点简述
- 核心问题：强化学习需基础模型对正确答案有非零概率，即潜在可解性，否则训练失败。
- 方法要点：通过数据混合、继续预训练和监督微调等中期训练技术提升潜在可解性。
- 实验或效果：在有机反应命名和无机材料生成任务上，准确率分别从10.9%提升至63.9%和从40.6%提升至67.4%。

## 摘要（原文）

> Large Language Models can develop reasoning capabilities through online fine-tuning with rule-based rewards. However, recent studies reveal a critical constraint: reinforcement learning succeeds only when the base model already assigns non-negligible probability to correct answers -- a property we term 'latent solvability'. This work investigates the emergence of chemical reasoning capabilities and what these prerequisites mean for chemistry. We identify two necessary conditions for RL-based chemical reasoning: 1) Symbolic competence, and 2) Latent chemical knowledge. We propose mid-stage scientific training (MiST): a set of mid-stage training techniques to satisfy these, including data-mixing with SMILES/CIF-aware pre-processing, continued pre-training on 2.9B tokens, and supervised fine-tuning on 1B tokens. These steps raise the latent-solvability score on 3B and 7B models by up to 1.8x, and enable RL to lift top-1 accuracy from 10.9 to 63.9% on organic reaction naming, and from 40.6 to 67.4% on inorganic material generation. Similar results are observed for other challenging chemical tasks, while producing interpretable reasoning traces. Our results define clear prerequisites for chemical reasoning training and highlight the broader role of mid-stage training in unlocking reasoning capabilities.

