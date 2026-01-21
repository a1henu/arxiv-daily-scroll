---
layout: default
title: Face-Voice Association with Inductive Bias for Maximum Class Separation
---

# Face-Voice Association with Inductive Bias for Maximum Class Separation
**arXiv**：[2601.13651v1](https://arxiv.org/abs/2601.13651) · [PDF](https://arxiv.org/pdf/2601.13651.pdf)  
**作者**：Marta Moscati, Oleksandr Kats, Mubashir Noman, Muhammad Zaigham Zaheer, Yufang Hou, Markus Schedl, Shah Nawaz  

**一句话要点**：提出基于最大类分离归纳偏置的面部-语音关联方法，以增强多模态表示区分能力。

**关键词**：面部-语音关联, 多模态学习, 归纳偏置, 最大类分离, 类间正交性

## 3 点简述
- 核心问题：面部-语音关联中，现有方法依赖损失函数，未利用最大类分离作为归纳偏置来强化嵌入区分性。
- 方法要点：开发新方法，将不同说话者的多模态表示强制最大类分离作为归纳偏置，结合类间正交性损失。
- 实验或效果：在两种任务上实现SOTA性能，消融研究显示归纳偏置与类间正交性损失结合最有效。

## 摘要（原文）

> Face-voice association is widely studied in multimodal learning and is approached representing faces and voices with embeddings that are close for a same person and well separated from those of others. Previous work achieved this with loss functions. Recent advancements in classification have shown that the discriminative ability of embeddings can be strengthened by imposing maximum class separation as inductive bias. This technique has never been used in the domain of face-voice association, and this work aims at filling this gap. More specifically, we develop a method for face-voice association that imposes maximum class separation among multimodal representations of different speakers as an inductive bias. Through quantitative experiments we demonstrate the effectiveness of our approach, showing that it achieves SOTA performance on two task formulation of face-voice association. Furthermore, we carry out an ablation study to show that imposing inductive bias is most effective when combined with losses for inter-class orthogonality. To the best of our knowledge, this work is the first that applies and demonstrates the effectiveness of maximum class separation as an inductive bias in multimodal learning; it hence paves the way to establish a new paradigm.

