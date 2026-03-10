---
layout: default
title: A Hybrid Vision Transformer Approach for Mathematical Expression Recognition
---

# A Hybrid Vision Transformer Approach for Mathematical Expression Recognition
**arXiv**：[2603.07929v1](https://arxiv.org/abs/2603.07929) · [PDF](https://arxiv.org/pdf/2603.07929.pdf)  
**作者**：Anh Duy Le, Van Linh Pham, Vinh Loi Ly, Nam Quan Nguyen, Huu Thang Nguyen, Tuan Anh Tran  

**一句话要点**：提出混合视觉变换器方法以解决数学表达式识别中的二维结构复杂性问题

**关键词**：数学表达式识别, 视觉变换器, 2D位置编码, 覆盖注意力解码器, 文档分析

## 3 点简述
- 核心问题：数学表达式识别因二维结构和符号尺寸差异而比文本识别更复杂
- 方法要点：使用带2D位置编码的混合视觉变换器编码器提取符号间复杂关系，结合覆盖注意力解码器处理解析问题
- 实验或效果：在IM2LATEX-100K数据集上BLEU得分89.94，优于当前先进方法

## 摘要（原文）

> One of the crucial challenges taken in document analysis is mathematical expression recognition. Unlike text recognition which only focuses on one-dimensional structure images, mathematical expression recognition is a much more complicated problem because of its two-dimensional structure and different symbol size. In this paper, we propose using a Hybrid Vision Transformer (HVT) with 2D positional encoding as the encoder to extract the complex relationship between symbols from the image. A coverage attention decoder is used to better track attention's history to handle the under-parsing and over-parsing problems. We also showed the benefit of using the [CLS] token of ViT as the initial embedding of the decoder. Experiments performed on the IM2LATEX-100K dataset have shown the effectiveness of our method by achieving a BLEU score of 89.94 and outperforming current state-of-the-art methods.

