---
layout: default
title: SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence
---

# SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence
**arXiv**：[2601.22114v1](https://arxiv.org/abs/2601.22114) · [PDF](https://arxiv.org/pdf/2601.22114.pdf)  
**作者**：Saoud Aldowaish, Yashwanth Karumanchi, Kai-Chen Chiang, Soroosh Noorzad, Morteza Fayazi  

**一句话要点**：提出SINA以解决电路原理图图像到网表转换中组件识别和连接推断的难题

**关键词**：电路原理图图像处理, 网表生成, 深度学习, 连接组件标记, 光学字符识别, 视觉语言模型

## 3 点简述
- 当前方法在电路原理图图像转换网表时，组件识别和连接推断存在困难
- SINA集成深度学习、CCL、OCR和VLM，实现自动化组件检测、连接提取和参考标识符分配
- 实验显示SINA网表生成准确率达96.47%，比现有方法高2.72倍

## 摘要（原文）

> Current methods for converting circuit schematic images into machine-readable netlists struggle with component recognition and connectivity inference. In this paper, we present SINA, an open-source, fully automated circuit schematic image-to-netlist generator. SINA integrates deep learning for accurate component detection, Connected-Component Labeling (CCL) for precise connectivity extraction, and Optical Character Recognition (OCR) for component reference designator retrieval, while employing a Vision-Language Model (VLM) for reliable reference designator assignments. In our experiments, SINA achieves 96.47% overall netlist-generation accuracy, which is 2.72x higher than state-of-the-art approaches.

