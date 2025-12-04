---
layout: default
title: HieroGlyphTranslator: Automatic Recognition and Translation of Egyptian Hieroglyphs to English
---

# HieroGlyphTranslator: Automatic Recognition and Translation of Egyptian Hieroglyphs to English
**arXiv**：[2512.03817v1](https://arxiv.org/abs/2512.03817) · [PDF](https://arxiv.org/pdf/2512.03817.pdf)  
**作者**：Ahmed Nasser, Marwan Mohamed, Alaa Sherif, Basmala Mahmoud, Shereen Yehia, Asmaa Saad, Mariam S. El-Rahmany, Ensaf H. Mohamed  

**一句话要点**：提出基于深度学习的埃及象形文字自动识别与翻译方法，从图像到英文。

**关键词**：埃及象形文字识别, 图像翻译, 深度学习, CNN模型, BLEU评分

## 3 点简述
- 核心问题：埃及象形文字图像翻译为英文，面临单字符多义等挑战。
- 方法要点：采用三阶段流程，包括分割、符号映射至Gardiner码和CNN翻译。
- 实验或效果：使用两个数据集，模型BLEU得分42.2，优于先前研究。

## 摘要（原文）

> Egyptian hieroglyphs, the ancient Egyptian writing system, are composed entirely of drawings. Translating these glyphs into English poses various challenges, including the fact that a single glyph can have multiple meanings. Deep learning translation applications are evolving rapidly, producing remarkable results that significantly impact our lives. In this research, we propose a method for the automatic recognition and translation of ancient Egyptian hieroglyphs from images to English. This study utilized two datasets for classification and translation: the Morris Franken dataset and the EgyptianTranslation dataset. Our approach is divided into three stages: segmentation (using Contour and Detectron2), mapping symbols to Gardiner codes, and translation (using the CNN model). The model achieved a BLEU score of 42.2, a significant result compared to previous research.

