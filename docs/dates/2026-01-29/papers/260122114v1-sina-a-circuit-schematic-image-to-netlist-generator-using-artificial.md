---
layout: default
title: SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence
---

# SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence
**arXiv**：[2601.22114v1](https://arxiv.org/abs/2601.22114) · [PDF](https://arxiv.org/pdf/2601.22114.pdf)  
**作者**：Saoud Aldowaish, Yashwanth Karumanchi, Kai-Chen Chiang, Soroosh Noorzad, Morteza Fayazi  

**一句话要点**：提出SINA以解决电路原理图图像转网表时组件识别和连接推断的难题

**关键词**：电路原理图图像转网表, 组件检测, 连接提取, 光学字符识别, 视觉语言模型, 开源工具

## 3 点简述
- 核心问题：现有方法在电路原理图图像转网表时，组件识别和连接推断准确率低
- 方法要点：集成深度学习检测组件、CCL提取连接、OCR获取参考标识符，并使用VLM分配标识符
- 实验或效果：SINA在实验中实现96.47%的网表生成准确率，比现有最佳方法高2.72倍

## 摘要（原文）

> Current methods for converting circuit schematic images into machine-readable netlists struggle with component recognition and connectivity inference. In this paper, we present SINA, an open-source, fully automated circuit schematic image-to-netlist generator. SINA integrates deep learning for accurate component detection, Connected-Component Labeling (CCL) for precise connectivity extraction, and Optical Character Recognition (OCR) for component reference designator retrieval, while employing a Vision-Language Model (VLM) for reliable reference designator assignments. In our experiments, SINA achieves 96.47% overall netlist-generation accuracy, which is 2.72x higher than state-of-the-art approaches.

