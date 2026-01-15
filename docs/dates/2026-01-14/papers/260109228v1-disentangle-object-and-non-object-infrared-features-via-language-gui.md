---
layout: default
title: Disentangle Object and Non-object Infrared Features via Language Guidance
---

# Disentangle Object and Non-object Infrared Features via Language Guidance
**arXiv**：[2601.09228v1](https://arxiv.org/abs/2601.09228) · [PDF](https://arxiv.org/pdf/2601.09228.pdf)  
**作者**：Fan Liu, Ting Wu, Chuanyi Zhang, Liang Yao, Xing Ma, Yuhui Zheng  

**一句话要点**：提出基于语言引导的视觉-语言表示学习范式，以解决红外图像中物体特征提取困难的问题。

**关键词**：红外物体检测, 视觉-语言表示学习, 特征解耦, 语义特征对齐, 物体特征提取

## 3 点简述
- 核心问题：红外图像因低对比度和弱边缘信息，难以提取区分性物体特征，影响复杂环境下的检测鲁棒性。
- 方法要点：通过语义特征对齐模块对齐物体与文本特征，并利用物体特征解耦模块最小化物体与非物体特征相关性，实现特征解耦。
- 实验或效果：在M³FD和FLIR基准上分别达到83.7%和86.1% mAP，验证了方法在提升检测性能方面的有效性。

## 摘要（原文）

> Infrared object detection focuses on identifying and locating objects in complex environments (\eg, dark, snow, and rain) where visible imaging cameras are disabled by poor illumination. However, due to low contrast and weak edge information in infrared images, it is challenging to extract discriminative object features for robust detection. To deal with this issue, we propose a novel vision-language representation learning paradigm for infrared object detection. An additional textual supervision with rich semantic information is explored to guide the disentanglement of object and non-object features. Specifically, we propose a Semantic Feature Alignment (SFA) module to align the object features with the corresponding text features. Furthermore, we develop an Object Feature Disentanglement (OFD) module that disentangles text-aligned object features and non-object features by minimizing their correlation. Finally, the disentangled object features are entered into the detection head. In this manner, the detection performance can be remarkably enhanced via more discriminative and less noisy features. Extensive experimental results demonstrate that our approach achieves superior performance on two benchmarks: M\textsuperscript{3}FD (83.7\% mAP), FLIR (86.1\% mAP). Our code will be publicly available once the paper is accepted.

