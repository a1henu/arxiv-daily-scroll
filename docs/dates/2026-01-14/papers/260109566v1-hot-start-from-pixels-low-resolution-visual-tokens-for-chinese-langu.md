---
layout: default
title: Hot-Start from Pixels: Low-Resolution Visual Tokens for Chinese Language Modeling
---

# Hot-Start from Pixels: Low-Resolution Visual Tokens for Chinese Language Modeling
**arXiv**：[2601.09566v1](https://arxiv.org/abs/2601.09566) · [PDF](https://arxiv.org/pdf/2601.09566.pdf)  
**作者**：Shuyang Xiang, Hao Guan  

**一句话要点**：提出基于低分辨率视觉输入的字符表示方法，用于中文语言建模，以补充传统索引方式。

**关键词**：中文语言建模, 视觉字符表示, 低分辨率输入, 热启动效应, 字符级建模

## 3 点简述
- 核心问题：传统中文语言模型忽略字符视觉形式，可能丢失语义和语音信息。
- 方法要点：使用灰度图像作为输入，分辨率低至8×8像素，替代字符索引进行解码。
- 实验或效果：视觉输入准确率达39.2%，与索引基线相当，并展示热启动效应，训练早期性能更优。

## 摘要（原文）

> Large language models typically represent Chinese characters as discrete index-based tokens, largely ignoring their visual form. For logographic scripts, visual structure carries semantic and phonetic information, which may aid prediction. We investigate whether low-resolution visual inputs can serve as an alternative for character-level modeling. Instead of token IDs, our decoder receives grayscale images of individual characters, with resolutions as low as $8 \times 8$ pixels. Remarkably, these inputs achieve 39.2\% accuracy, comparable to the index-based baseline of 39.1\%. Such low-resource settings also exhibit a pronounced \emph{hot-start} effect: by 0.4\% of total training, accuracy reaches above 12\%, while index-based models lag at below 6\%. Overall, our results demonstrate that minimal visual structure can provide a robust and efficient signal for Chinese language modeling, offering an alternative perspective on character representation that complements traditional index-based approaches.

