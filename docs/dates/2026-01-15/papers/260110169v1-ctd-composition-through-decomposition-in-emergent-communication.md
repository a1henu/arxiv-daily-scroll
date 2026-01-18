---
layout: default
title: CtD: Composition through Decomposition in Emergent Communication
---

# CtD: Composition through Decomposition in Emergent Communication
**arXiv**：[2601.10169v1](https://arxiv.org/abs/2601.10169) · [PDF](https://arxiv.org/pdf/2601.10169.pdf)  
**作者**：Boaz Carmeli, Ron Meir, Yonatan Belinkov  

**一句话要点**：提出'分解组合'方法，使人工神经代理在涌现通信中实现零样本组合泛化描述新图像。

**关键词**：涌现通信, 组合泛化, 神经代理, 图像描述, 零样本学习, 多目标协调

## 3 点简述
- 核心问题：人工代理如何像人类一样通过组合已知概念描述未见图像，实现组合泛化。
- 方法要点：采用两阶段训练，先分解图像学习基础概念代码本，再组合代码本描述新图像。
- 实验或效果：在协调游戏中，代理能零样本泛化，无需额外训练即可描述新图像。

## 摘要（原文）

> Compositionality is a cognitive mechanism that allows humans to systematically combine known concepts in novel ways. This study demonstrates how artificial neural agents acquire and utilize compositional generalization to describe previously unseen images. Our method, termed "Composition through Decomposition", involves two sequential training steps. In the 'Decompose' step, the agents learn to decompose an image into basic concepts using a codebook acquired during interaction in a multi-target coordination game. Subsequently, in the 'Compose' step, the agents employ this codebook to describe novel images by composing basic concepts into complex phrases. Remarkably, we observe cases where generalization in the `Compose' step is achieved zero-shot, without the need for additional training.

