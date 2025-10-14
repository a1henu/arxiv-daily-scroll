---
layout: default
title: Compositional Zero-Shot Learning: A Survey
---

# Compositional Zero-Shot Learning: A Survey
**arXiv**：[2510.11106v1](https://arxiv.org/abs/2510.11106) · [PDF](https://arxiv.org/pdf/2510.11106.pdf)  
**作者**：Ans Munir, Faisal Z. Qureshi, Mohsen Ali, Muhammad Haris Khan  

**一句话要点**：综述组合零样本学习方法，解决未见属性-对象组合识别问题

**关键词**：组合零样本学习, 解缠方法, 跨模态学习, 零样本识别, 计算机视觉综述

## 3 点简述
- 核心问题：模型需识别训练中未见的属性与对象组合，视觉外观高度依赖上下文
- 方法要点：基于解缠分类法，涵盖无解缠、文本解缠、视觉解缠和跨模态解缠
- 实验或效果：比较不同方法在封闭与开放世界设置下的优势与局限

## 摘要（原文）

> Compositional Zero-Shot Learning (CZSL) is a critical task in computer vision
> that enables models to recognize unseen combinations of known attributes and
> objects during inference, addressing the combinatorial challenge of requiring
> training data for every possible composition. This is particularly challenging
> because the visual appearance of primitives is highly contextual; for example,
> ``small'' cats appear visually distinct from ``older'' ones, and ``wet'' cars
> differ significantly from ``wet'' cats. Effectively modeling this contextuality
> and the inherent compositionality is crucial for robust compositional zero-shot
> recognition. This paper presents, to our knowledge, the first comprehensive
> survey specifically focused on Compositional Zero-Shot Learning. We
> systematically review the state-of-the-art CZSL methods, introducing a taxonomy
> grounded in disentanglement, with four families of approaches: no explicit
> disentanglement, textual disentanglement, visual disentanglement, and
> cross-modal disentanglement. We provide a detailed comparative analysis of
> these methods, highlighting their core advantages and limitations in different
> problem settings, such as closed-world and open-world CZSL. Finally, we
> identify the most significant open challenges and outline promising future
> research directions. This survey aims to serve as a foundational resource to
> guide and inspire further advancements in this fascinating and important field.
> Papers studied in this survey with their official code are available on our
> github: https://github.com/ans92/Compositional-Zero-Shot-Learning

