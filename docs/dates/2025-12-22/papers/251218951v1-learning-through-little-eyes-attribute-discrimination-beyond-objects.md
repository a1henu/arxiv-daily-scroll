---
layout: default
title: Learning Through Little Eyes: Attribute Discrimination Beyond Objects
---

# Learning Through Little Eyes: Attribute Discrimination Beyond Objects
**arXiv**：[2512.18951v1](https://arxiv.org/abs/2512.18951) · [PDF](https://arxiv.org/pdf/2512.18951.pdf)  
**作者**：Patrick Batsell, Tsutsui Satoshi, Bihan Wen  

**一句话要点**：提出基于婴儿视角视频的属性识别基准，以评估CVCL模型在颜色、大小和纹理上的判别能力。

**关键词**：婴儿视角学习, 属性识别, 对比学习, 视觉语言模型, 细粒度分类

## 3 点简述
- 核心问题：婴儿尺度学习是否支持细粒度属性识别，如颜色、大小和纹理。
- 方法要点：引入系统变化颜色、大小和纹理的基准，对比CVCL与CLIP模型。
- 实验或效果：CVCL在大小识别上更优，CLIP在颜色识别上更准，两者均未能语言化纹理。

## 摘要（原文）

> Infants learn to recognize not only object categories but also fine grained attributes such as color, size, and texture within their first two years of life. Prior work explores Childs View for Contrastive Learning (CVCL), a CLIP style model trained on infant egocentric video as a computational model of early infant learning, but it focuses only on class level recognition. This leaves it unclear whether infant scale learning also supports attribute discrimination. To address this, we introduce a benchmark that systematically varies color, size, and texture, allowing controlled tests of within class attribute recognition. Comparing CVCL with CLIP shows clear differences. CVCL is better at size discrimination, while CLIP achieves higher accuracy on color discrimination. Both models represent texture in image embeddings but fail to ground texture linguistically, suggesting a gap between visual and language spaces.

