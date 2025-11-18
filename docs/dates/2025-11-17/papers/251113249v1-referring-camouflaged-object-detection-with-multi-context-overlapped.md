---
layout: default
title: Referring Camouflaged Object Detection With Multi-Context Overlapped Windows Cross-Attention
---

# Referring Camouflaged Object Detection With Multi-Context Overlapped Windows Cross-Attention
**arXiv**：[2511.13249v1](https://arxiv.org/abs/2511.13249) · [PDF](https://arxiv.org/pdf/2511.13249.pdf)  
**作者**：Yu Wen, Shuyong Gao, Shuping Zhang, Miao Huang, Lili Tao, Han Yang, Haozhe Xing, Lihe Zhang, Boxue Hou  

**一句话要点**：提出RFMNet以通过多上下文融合和重叠窗口交叉注意力提升参考伪装物体检测性能

**关键词**：参考伪装物体检测, 多上下文特征融合, 重叠窗口交叉注意力, 显著图像特征, 局部信息匹配, 渐进式解码

## 3 点简述
- 核心问题：参考伪装物体检测需结合参考信息识别隐藏物体，现有方法将参考图像转为1D提示，但性能可提升。
- 方法要点：利用参考显著图像多编码阶段特征与伪装特征交互融合，并引入重叠窗口交叉注意力聚焦局部信息匹配。
- 实验或效果：在Ref-COD基准测试中实现最先进性能，验证方法有效性。

## 摘要（原文）

> Referring camouflaged object detection (Ref-COD) aims to identify hidden objects by incorporating reference information such as images and text descriptions. Previous research has transformed reference images with salient objects into one-dimensional prompts, yielding significant results. We explore ways to enhance performance through multi-context fusion of rich salient image features and camouflaged object features. Therefore, we propose RFMNet, which utilizes features from multiple encoding stages of the reference salient images and performs interactive fusion with the camouflage features at the corresponding encoding stages. Given that the features in salient object images contain abundant object-related detail information, performing feature fusion within local areas is more beneficial for detecting camouflaged objects. Therefore, we propose an Overlapped Windows Cross-attention mechanism to enable the model to focus more attention on the local information matching based on reference features. Besides, we propose the Referring Feature Aggregation (RFA) module to decode and segment the camouflaged objects progressively. Extensive experiments on the Ref-COD benchmark demonstrate that our method achieves state-of-the-art performance.

