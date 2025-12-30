---
layout: default
title: Holi-DETR: Holistic Fashion Item Detection Leveraging Contextual Information
---

# Holi-DETR: Holistic Fashion Item Detection Leveraging Contextual Information
**arXiv**：[2512.23221v1](https://arxiv.org/abs/2512.23221) · [PDF](https://arxiv.org/pdf/2512.23221.pdf)  
**作者**：Youngchae Kwon, Jinyoung Choi, Injung Kim  

**一句话要点**：提出Holi-DETR以解决时尚物品检测中的歧义问题，通过整合上下文信息实现整体检测。

**关键词**：时尚物品检测, 上下文信息, 检测Transformer, 整体检测, 歧义减少

## 3 点简述
- 核心问题：时尚物品外观多样且子类别相似，导致检测歧义。
- 方法要点：利用物品共现关系、空间布局和人体关键点三种上下文信息，改进DETR架构。
- 实验或效果：在平均精度上，相比原始DETR和Co-DETR分别提升3.6和1.1个百分点。

## 摘要（原文）

> Fashion item detection is challenging due to the ambiguities introduced by the highly diverse appearances of fashion items and the similarities among item subcategories. To address this challenge, we propose a novel Holistic Detection Transformer (Holi-DETR) that detects fashion items in outfit images holistically, by leveraging contextual information. Fashion items often have meaningful relationships as they are combined to create specific styles. Unlike conventional detectors that detect each item independently, Holi-DETR detects multiple items while reducing ambiguities by leveraging three distinct types of contextual information: (1) the co-occurrence relationship between fashion items, (2) the relative position and size based on inter-item spatial arrangements, and (3) the spatial relationships between items and human body key-points. %Holi-DETR explicitly incorporates three types of contextual information: (1) the co-occurrence probability between fashion items, (2) the relative position and size based on inter-item spatial arrangements, and (3) the spatial relationships between items and human body key-points. To this end, we propose a novel architecture that integrates these three types of heterogeneous contextual information into the Detection Transformer (DETR) and its subsequent models. In experiments, the proposed methods improved the performance of the vanilla DETR and the more recently developed Co-DETR by 3.6 percent points (pp) and 1.1 pp, respectively, in terms of average precision (AP).

