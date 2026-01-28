---
layout: default
title: A new Image Similarity Metric for a Perceptual and Transparent Geometric and Chromatic Assessment
---

# A new Image Similarity Metric for a Perceptual and Transparent Geometric and Chromatic Assessment
**arXiv**：[2601.19680v1](https://arxiv.org/abs/2601.19680) · [PDF](https://arxiv.org/pdf/2601.19680.pdf)  
**作者**：Antonio Di Marino, Vincenzo Bevilacqua, Emanuel Di Nardo, Angelo Ciaramella, Ivanoe De Falco, Giovanna Sannino  

**一句话要点**：提出基于纹理和色度评估的感知图像相似度度量，以提升形状和颜色失真下的性能与透明度。

**关键词**：图像相似度度量, 感知评估, 纹理失真, Oklab色彩空间, Earth Mover's Distance, 视觉解释

## 3 点简述
- 现有图像相似度度量非感知性，难以评估纹理失真。
- 新度量结合纹理差异（Earth Mover's Distance）和色度差异（Oklab色彩空间）。
- 在Berkeley-Adobe数据集上优于现有方法，并提供视觉解释增强透明度。

## 摘要（原文）

> In the literature, several studies have shown that state-of-the-art image similarity metrics are not perceptual metrics; moreover, they have difficulty evaluating images, especially when texture distortion is also present. In this work, we propose a new perceptual metric composed of two terms. The first term evaluates the dissimilarity between the textures of two images using Earth Mover's Distance. The second term evaluates the chromatic dissimilarity between two images in the Oklab perceptual color space. We evaluated the performance of our metric on a non-traditional dataset, called Berkeley-Adobe Perceptual Patch Similarity, which contains a wide range of complex distortions in shapes and colors. We have shown that our metric outperforms the state of the art, especially when images contain shape distortions, confirming also its greater perceptiveness. Furthermore, although deep black-box metrics could be very accurate, they only provide similarity scores between two images, without explaining their main differences and similarities. Our metric, on the other hand, provides visual explanations to support the calculated score, making the similarity assessment transparent and justified.

