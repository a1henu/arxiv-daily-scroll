---
layout: default
title: Architecture inside the mirage: evaluating generative image models on architectural style, elements, and typologies
---

# Architecture inside the mirage: evaluating generative image models on architectural style, elements, and typologies
**arXiv**：[2601.09169v1](https://arxiv.org/abs/2601.09169) · [PDF](https://arxiv.org/pdf/2601.09169.pdf)  
**作者**：Jamie Magrill, Leah Gornstein, Sandra Seekins, Barry Magrill  

**一句话要点**：评估五种生成式AI图像平台在建筑风格、元素和类型上的准确性，揭示其局限性并提出应用建议。

**关键词**：生成式AI图像平台, 建筑风格评估, 文本到图像准确性, 历史建筑元素, 合成内容标签, 训练数据集标准

## 3 点简述
- 核心问题：生成式AI文本到图像系统在建筑领域生成准确图像的能力尚未充分评估，可能影响历史规则的应用。
- 方法要点：使用30个建筑提示评估五种平台，生成600张图像，由两位建筑史学家基于预设标准独立评分。
- 实验或效果：整体准确性有限（平均42%），常见提示比罕见提示准确2.7倍，平台间失败率差异显著。

## 摘要（原文）

> Generative artificial intelligence (GenAI) text-to-image systems are increasingly used to generate architectural imagery, yet their capacity to reproduce accurate images in a historically rule-bound field remains poorly characterized. We evaluated five widely used GenAI image platforms (Adobe Firefly, DALL-E 3, Google Imagen 3, Microsoft Image Generator, and Midjourney) using 30 architectural prompts spanning styles, typologies, and codified elements. Each prompt-generator pair produced four images (n = 600 images total). Two architectural historians independently scored each image for accuracy against predefined criteria, resolving disagreements by consensus. Set-level performance was summarized as zero to four accurate images per four-image set. Image output from Common prompts was 2.7-fold more accurate than from Rare prompts (p < 0.05). Across platforms, overall accuracy was limited (highest accuracy score 52 percent; lowest 32 percent; mean 42 percent). All-correct (4 out of 4) outcomes were similar across platforms. By contrast, all-incorrect (0 out of 4) outcomes varied substantially, with Imagen 3 exhibiting the fewest failures and Microsoft Image Generator exhibiting the highest number of failures. Qualitative review of the image dataset identified recurring patterns including over-embellishment, confusion between medieval styles and their later revivals, and misrepresentation of descriptive prompts (for example, egg-and-dart, banded column, pendentive). These findings support the need for visible labeling of GenAI synthetic content, provenance standards for future training datasets, and cautious educational use of GenAI architectural imagery.

