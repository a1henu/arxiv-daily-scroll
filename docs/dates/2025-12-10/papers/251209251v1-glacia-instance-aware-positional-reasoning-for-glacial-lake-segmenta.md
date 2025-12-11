---
layout: default
title: GLACIA: Instance-Aware Positional Reasoning for Glacial Lake Segmentation via Multimodal Large Language Model
---

# GLACIA: Instance-Aware Positional Reasoning for Glacial Lake Segmentation via Multimodal Large Language Model
**arXiv**：[2512.09251v1](https://arxiv.org/abs/2512.09251) · [PDF](https://arxiv.org/pdf/2512.09251.pdf)  
**作者**：Lalit Maurya, Saurabh Kaushik, Beth Tellman  

**一句话要点**：提出GLACIA框架，通过多模态大语言模型实现冰川湖分割与实例感知位置推理，以支持灾害预防。

**关键词**：冰川湖分割, 多模态大语言模型, 实例感知推理, 遥感图像分析, 灾害监测

## 3 点简述
- 现有冰川湖分割方法缺乏高层语义和可解释推理，局限于像素级预测。
- GLACIA集成大语言模型，生成分割掩码和空间推理输出，提升准确性和可解释性。
- 在GLake-Pos数据集上评估，GLACIA在mIoU指标上超越CNN、ViT、地理基础模型和推理方法。

## 摘要（原文）

> Glacial lake monitoring bears great significance in mitigating the anticipated risk of Glacial Lake Outburst Floods. However, existing segmentation methods based on convolutional neural networks (CNNs) and Vision Transformers (ViTs), remain constrained to pixel-level predictions, lacking high-level global scene semantics and human-interpretable reasoning. To address this, we introduce GLACIA (\textbf{G}lacial \textbf{LA}ke segmentation with \textbf{C}ontextual \textbf{I}nstance \textbf{A}wareness), the first framework that integrates large language models with segmentation capabilities to produce both accurate segmentation masks and corresponding spatial reasoning outputs. We construct the Glacial Lake Position Reasoning (GLake-Pos) dataset pipeline, which provides diverse, spatially grounded question-answer pairs designed to overcome the lack of instance-aware positional reasoning data in remote sensing. Comparative evaluation demonstrate that GLACIA (mIoU: 87.30) surpasses state-of-the-art method based on CNNs (mIoU: 78.55 - 79.01), ViTs (mIoU: 69.27 - 81.75), Geo-foundation models (mIoU: 76.37 - 87.10), and reasoning based segmentation methods (mIoU: 60.12 - 75.66). Our approach enables intuitive disaster preparedness and informed policy-making in the context of rapidly changing glacial environments by facilitating natural language interaction, thereby supporting more efficient and interpretable decision-making. The code is released on https://github.com/lalitmaurya47/GLACIA

