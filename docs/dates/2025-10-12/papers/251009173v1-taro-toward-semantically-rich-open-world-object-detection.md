---
layout: default
title: TARO: Toward Semantically Rich Open-World Object Detection
---

# TARO: Toward Semantically Rich Open-World Object Detection
**arXiv**：[2510.09173v1](https://arxiv.org/abs/2510.09173) · [PDF](https://arxiv.org/pdf/2510.09173.pdf)  
**作者**：Yuchen Zhang, Yao Lu, Johannes Betz  

**一句话要点**：提出TARO框架以解决开放世界物体检测中未知对象语义分类不足的问题

**关键词**：开放世界物体检测, 语义层次分类, 稀疏最大头, 未知对象识别, 自动驾驶安全

## 3 点简述
- 核心问题：现有检测器在封闭世界假设下，无法对未知对象进行语义丰富的分类
- 方法要点：采用稀疏最大头建模物体性，结合层次引导重标签和分类模块学习语义层次
- 实验或效果：TARO可将29.9%未知对象分类为粗类别，减少未知与已知类混淆

## 摘要（原文）

> Modern object detectors are largely confined to a "closed-world" assumption,
> limiting them to a predefined set of classes and posing risks when encountering
> novel objects in real-world scenarios. While open-set detection methods aim to
> address this by identifying such instances as 'Unknown', this is often
> insufficient. Rather than treating all unknowns as a single class, assigning
> them more descriptive subcategories can enhance decision-making in
> safety-critical contexts. For example, identifying an object as an 'Unknown
> Animal' (requiring an urgent stop) versus 'Unknown Debris' (requiring a safe
> lane change) is far more useful than just 'Unknown' in autonomous driving. To
> bridge this gap, we introduce TARO, a novel detection framework that not only
> identifies unknown objects but also classifies them into coarse parent
> categories within a semantic hierarchy. TARO employs a unique architecture with
> a sparsemax-based head for modeling objectness, a hierarchy-guided relabeling
> component that provides auxiliary supervision, and a classification module that
> learns hierarchical relationships. Experiments show TARO can categorize up to
> 29.9% of unknowns into meaningful coarse classes, significantly reduce
> confusion between unknown and known classes, and achieve competitive
> performance in both unknown recall and known mAP. Code will be made available.

