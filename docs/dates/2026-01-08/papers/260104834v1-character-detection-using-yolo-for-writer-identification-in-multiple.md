---
layout: default
title: Character Detection using YOLO for Writer Identification in multiple Medieval books
---

# Character Detection using YOLO for Writer Identification in multiple Medieval books
**arXiv**：[2601.04834v1](https://arxiv.org/abs/2601.04834) · [PDF](https://arxiv.org/pdf/2601.04834.pdf)  
**作者**：Alessandra Scotto di Freca, Tiziana D Alessandro, Francesco Fontanella, Filippo Sarria, Claudio De Stefano  

**一句话要点**：提出基于YOLO的字符检测方法，用于多本中世纪书籍的书写者识别

**关键词**：字符检测, YOLO, 书写者识别, 古文书学, 中世纪手稿, 目标检测

## 3 点简述
- 核心问题：中世纪手稿中书写者识别，以辅助古文书学中的年代确定和书写风格演变研究。
- 方法要点：使用YOLOv5替代模板匹配和CNN，自动检测字符'a'，提高检测数量和准确性。
- 实验或效果：YOLO提取更多字符，提升第二阶段分类精度，置信度分数支持拒绝阈值，增强未见手稿的识别可靠性。

## 摘要（原文）

> Paleography is the study of ancient and historical handwriting, its key objectives include the dating of manuscripts and understanding the evolution of writing. Estimating when a document was written and tracing the development of scripts and writing styles can be aided by identifying the individual scribes who contributed to a medieval manuscript. Although digital technologies have made significant progress in this field, the general problem remains unsolved and continues to pose open challenges. ... We previously proposed an approach focused on identifying specific letters or abbreviations that characterize each writer. In that study, we considered the letter "a", as it was widely present on all pages of text and highly distinctive, according to the suggestions of expert paleographers. We used template matching techniques to detect the occurrences of the character "a" on each page and the convolutional neural network (CNN) to attribute each instance to the correct scribe. Moving from the interesting results achieved from this previous system and being aware of the limitations of the template matching technique, which requires an appropriate threshold to work, we decided to experiment in the same framework with the use of the YOLO object detection model to identify the scribe who contributed to the writing of different medieval books. We considered the fifth version of YOLO to implement the YOLO object detection model, which completely substituted the template matching and CNN used in the previous work. The experimental results demonstrate that YOLO effectively extracts a greater number of letters considered, leading to a more accurate second-stage classification. Furthermore, the YOLO confidence score provides a foundation for developing a system that applies a rejection threshold, enabling reliable writer identification even in unseen manuscripts.

