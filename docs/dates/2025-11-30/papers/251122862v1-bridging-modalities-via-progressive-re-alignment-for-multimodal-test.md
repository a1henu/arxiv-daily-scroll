---
layout: default
title: Bridging Modalities via Progressive Re-alignment for Multimodal Test-Time Adaptation
---

# Bridging Modalities via Progressive Re-alignment for Multimodal Test-Time Adaptation
**arXiv**：[2511.22862v1](https://arxiv.org/abs/2511.22862) · [PDF](https://arxiv.org/pdf/2511.22862.pdf)  
**作者**：Jiacheng Li, Songhe Feng  

**一句话要点**：提出BriMPR框架以解决多模态测试时适应中的模态耦合效应问题

**关键词**：多模态学习, 测试时适应, 特征对齐, 提示调谐, 对比学习, 域偏移

## 3 点简述
- 核心问题：多模态场景中，单模态浅层特征偏移与跨模态高层语义错位的耦合效应阻碍测试时适应扩展。
- 方法要点：采用分治策略，先通过提示调谐校准单模态全局特征分布，再引入跨模态实例对比学习增强信息交互。
- 实验或效果：在基于损坏和真实域偏移基准的MMTTA任务上，实验证明了方法的优越性。

## 摘要（原文）

> Test-time adaptation (TTA) enables online model adaptation using only unlabeled test data, aiming to bridge the gap between source and target distributions. However, in multimodal scenarios, varying degrees of distribution shift across different modalities give rise to a complex coupling effect of unimodal shallow feature shift and cross-modal high-level semantic misalignment, posing a major obstacle to extending existing TTA methods to the multimodal field. To address this challenge, we propose a novel multimodal test-time adaptation (MMTTA) framework, termed as Bridging Modalities via Progressive Re-alignment (BriMPR). BriMPR, consisting of two progressively enhanced modules, tackles the coupling effect with a divide-and-conquer strategy. Specifically, we first decompose MMTTA into multiple unimodal feature alignment sub-problems. By leveraging the strong function approximation ability of prompt tuning, we calibrate the unimodal global feature distributions to their respective source distributions, so as to achieve the initial semantic re-alignment across modalities. Subsequently, we assign the credible pseudo-labels to combinations of masked and complete modalities, and introduce inter-modal instance-wise contrastive learning to further enhance the information interaction among modalities and refine the alignment. Extensive experiments on MMTTA tasks, including both corruption-based and real-world domain shift benchmarks, demonstrate the superiority of our method. Our source code is available at [this URL](https://github.com/Luchicken/BriMPR).

