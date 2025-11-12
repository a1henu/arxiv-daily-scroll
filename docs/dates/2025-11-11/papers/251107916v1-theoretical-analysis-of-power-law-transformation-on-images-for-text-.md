---
layout: default
title: Theoretical Analysis of Power-law Transformation on Images for Text Polarity Detection
---

# Theoretical Analysis of Power-law Transformation on Images for Text Polarity Detection
**arXiv**：[2511.07916v1](https://arxiv.org/abs/2511.07916) · [PDF](https://arxiv.org/pdf/2511.07916.pdf)  
**作者**：Narendra Singh Yadav, Pavan Kumar Perepu  

**一句话要点**：理论分析幂律变换在图像文本极性检测中的现象，以改进二值化预处理。

**关键词**：文本极性检测, 图像二值化, 幂律变换, 类间方差, 计算机视觉预处理

## 3 点简述
- 核心问题：图像文本极性检测是二值化预处理的关键，影响字符识别等应用。
- 方法要点：基于幂律变换分析直方图统计，理论解释类间方差随文本极性变化的现象。
- 实验或效果：通过实证结果验证理论，但具体性能指标未知。

## 摘要（原文）

> Several computer vision applications like vehicle license plate recognition, captcha recognition, printed or handwriting character recognition from images etc., text polarity detection and binarization are the important preprocessing tasks. To analyze any image, it has to be converted to a simple binary image. This binarization process requires the knowledge of polarity of text in the images. Text polarity is defined as the contrast of text with respect to background. That means, text is darker than the background (dark text on bright background) or vice-versa. The binarization process uses this polarity information to convert the original colour or gray scale image into a binary image. In the literature, there is an intuitive approach based on power-law transformation on the original images. In this approach, the authors have illustrated an interesting phenomenon from the histogram statistics of the transformed images. Considering text and background as two classes, they have observed that maximum between-class variance between two classes is increasing (decreasing) for dark (bright) text on bright (dark) background. The corresponding empirical results have been presented. In this paper, we present a theoretical analysis of the above phenomenon.

