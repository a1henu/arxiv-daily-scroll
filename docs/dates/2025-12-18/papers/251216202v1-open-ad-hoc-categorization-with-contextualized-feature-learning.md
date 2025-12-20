---
layout: default
title: Open Ad-hoc Categorization with Contextualized Feature Learning
---

# Open Ad-hoc Categorization with Contextualized Feature Learning
**arXiv**：[2512.16202v1](https://arxiv.org/abs/2512.16202) · [PDF](https://arxiv.org/pdf/2512.16202.pdf)  
**作者**：Zilin Wang, Sangwoo Mo, Stella X. Yu, Sima Behpour, Liu Ren  

**一句话要点**：提出OAK模型，通过上下文特征学习解决开放临时分类问题，实现自适应视觉场景分类。

**关键词**：开放临时分类, 上下文特征学习, 视觉聚类, 图像-文本对齐, 可解释显著图

## 3 点简述
- 核心问题：研究开放临时分类，基于少量标注样本和大量未标注数据动态发现和扩展临时类别。
- 方法要点：在冻结CLIP输入端引入可学习上下文令牌，结合图像-文本对齐和视觉聚类目标优化。
- 实验或效果：在Stanford和Clevr-4数据集上达到SOTA，如Stanford Mood新颖类准确率87.4%，并生成可解释显著图。

## 摘要（原文）

> Adaptive categorization of visual scenes is essential for AI agents to handle changing tasks. Unlike fixed common categories for plants or animals, ad-hoc categories are created dynamically to serve specific goals. We study open ad-hoc categorization: Given a few labeled exemplars and abundant unlabeled data, the goal is to discover the underlying context and to expand ad-hoc categories through semantic extension and visual clustering around it.
>   Building on the insight that ad-hoc and common categories rely on similar perceptual mechanisms, we propose OAK, a simple model that introduces a small set of learnable context tokens at the input of a frozen CLIP and optimizes with both CLIP's image-text alignment objective and GCD's visual clustering objective.
>   On Stanford and Clevr-4 datasets, OAK achieves state-of-the-art in accuracy and concept discovery across multiple categorizations, including 87.4% novel accuracy on Stanford Mood, surpassing CLIP and GCD by over 50%. Moreover, OAK produces interpretable saliency maps, focusing on hands for Action, faces for Mood, and backgrounds for Location, promoting transparency and trust while enabling adaptive and generalizable categorization.

