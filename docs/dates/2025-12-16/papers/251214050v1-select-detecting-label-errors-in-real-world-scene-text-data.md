---
layout: default
title: SELECT: Detecting Label Errors in Real-world Scene Text Data
---

# SELECT: Detecting Label Errors in Real-world Scene Text Data
**arXiv**：[2512.14050v1](https://arxiv.org/abs/2512.14050) · [PDF](https://arxiv.org/pdf/2512.14050.pdf)  
**作者**：Wenjun Liu, Qian Wu, Yifeng Hu, Yuke Li  

**一句话要点**：提出SELECT方法，利用多模态训练检测真实场景文本数据集中的标签错误。

**关键词**：场景文本识别, 标签错误检测, 多模态学习, 字符级处理, 序列标签对齐

## 3 点简述
- 核心问题：真实场景文本数据集中存在可变长度标签、标签序列错位和字符级错误。
- 方法要点：结合图像-文本编码器和字符级分词器，并引入SSLC过程模拟训练中的错误场景。
- 实验或效果：在检测标签错误和提高STR准确性方面优于现有方法，展示实际效用。

## 摘要（原文）

> We introduce SELECT (Scene tExt Label Errors deteCTion), a novel approach that leverages multi-modal training to detect label errors in real-world scene text datasets. Utilizing an image-text encoder and a character-level tokenizer, SELECT addresses the issues of variable-length sequence labels, label sequence misalignment, and character-level errors, outperforming existing methods in accuracy and practical utility. In addition, we introduce Similarity-based Sequence Label Corruption (SSLC), a process that intentionally introduces errors into the training labels to mimic real-world error scenarios during training. SSLC not only can cause a change in the sequence length but also takes into account the visual similarity between characters during corruption. Our method is the first to detect label errors in real-world scene text datasets successfully accounting for variable-length labels. Experimental results demonstrate the effectiveness of SELECT in detecting label errors and improving STR accuracy on real-world text datasets, showcasing its practical utility.

