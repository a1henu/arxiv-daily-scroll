---
layout: default
title: Watch Closely: Mitigating Object Hallucinations in Large Vision-Language Models with Disentangled Decoding
---

# Watch Closely: Mitigating Object Hallucinations in Large Vision-Language Models with Disentangled Decoding
**arXiv**：[2512.19070v1](https://arxiv.org/abs/2512.19070) · [PDF](https://arxiv.org/pdf/2512.19070.pdf)  
**作者**：Ruiqi Ma, Yu Yan, Chunhong Zhang, Minghao Yin, XinChao Liu, Zhihong Jin, Zheng Hu  

**一句话要点**：提出无训练的解耦解码方法以缓解大视觉语言模型中的对象幻觉问题

**关键词**：对象幻觉, 视觉语言模型, 解耦解码, 图像分割, 无训练方法

## 3 点简述
- 核心问题：大视觉语言模型在对象识别任务中存在严重幻觉，生成与视觉内容不符的流畅文本
- 方法要点：通过图像分割和增强，结合空白图像消除语言先验，无需训练
- 实验或效果：减少语言和视觉模态的幻觉，增强模型视觉性能

## 摘要（原文）

> Large Vision-Language Models (LVLMs) bridge the gap between visual and linguistic modalities, demonstrating strong potential across a variety of domains. However, despite significant progress, LVLMs still suffer from severe hallucination issues in object recognition tasks. These models often fail to accurately identify certain objects, leading to text generation that appears fluent but does not correspond to the visual content, which can have serious consequences in real-world applications. Recently, several methods have been proposed to alleviate LVLM hallucinations, but most focus solely on reducing hallucinations in the language modality. To mitigate hallucinations in both the language and visual modalities, we introduce Hallucination Disentangled Decoding (HDD) method that requires no training. HDD enhances the original image by segmenting it and selecting images that augment the original, while also utilizing a blank image to eliminate language prior hallucinations in both the original and segmented images. This design not only reduces the model's dependence on language priors but also enhances its visual performance. (Code: https://github.com/rickeyhhh/Hallucination-Disentangled-Decoding)

