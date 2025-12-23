---
layout: default
title: Steering Vision-Language Pre-trained Models for Incremental Face Presentation Attack Detection
---

# Steering Vision-Language Pre-trained Models for Incremental Face Presentation Attack Detection
**arXiv**：[2512.19022v1](https://arxiv.org/abs/2512.19022) · [PDF](https://arxiv.org/pdf/2512.19022.pdf)  
**作者**：Haoze Li, Jie Zhang, Guoying Zhao, Stephen Lin, Shiguang Shan  

**一句话要点**：提出SVLP-IL框架，基于视觉语言预训练模型解决无排练增量学习中的面部呈现攻击检测问题。

**关键词**：面部呈现攻击检测, 增量学习, 视觉语言预训练模型, 无排练学习, 灾难性遗忘, 跨模态表示

## 3 点简述
- 核心问题：面部呈现攻击检测需增量学习应对新攻击，但隐私限制禁止保留旧数据，导致灾难性遗忘。
- 方法要点：通过多角度提示和选择性弹性权重巩固，平衡稳定性和可塑性，减少遗忘并适应新域。
- 实验或效果：在多个基准测试中，SVLP-IL显著降低遗忘，提升未见域性能，提供隐私合规的实用方案。

## 摘要（原文）

> Face Presentation Attack Detection (PAD) demands incremental learning (IL) to combat evolving spoofing tactics and domains. Privacy regulations, however, forbid retaining past data, necessitating rehearsal-free IL (RF-IL). Vision-Language Pre-trained (VLP) models, with their prompt-tunable cross-modal representations, enable efficient adaptation to new spoofing styles and domains. Capitalizing on this strength, we propose \textbf{SVLP-IL}, a VLP-based RF-IL framework that balances stability and plasticity via \textit{Multi-Aspect Prompting} (MAP) and \textit{Selective Elastic Weight Consolidation} (SEWC). MAP isolates domain dependencies, enhances distribution-shift sensitivity, and mitigates forgetting by jointly exploiting universal and domain-specific cues. SEWC selectively preserves critical weights from previous tasks, retaining essential knowledge while allowing flexibility for new adaptations. Comprehensive experiments across multiple PAD benchmarks show that SVLP-IL significantly reduces catastrophic forgetting and enhances performance on unseen domains. SVLP-IL offers a privacy-compliant, practical solution for robust lifelong PAD deployment in RF-IL settings.

