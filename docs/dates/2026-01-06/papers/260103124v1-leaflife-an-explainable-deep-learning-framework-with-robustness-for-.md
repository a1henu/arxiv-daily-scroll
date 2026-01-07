---
layout: default
title: LeafLife: An Explainable Deep Learning Framework with Robustness for Grape Leaf Disease Recognition
---

# LeafLife: An Explainable Deep Learning Framework with Robustness for Grape Leaf Disease Recognition
**arXiv**：[2601.03124v1](https://arxiv.org/abs/2601.03124) · [PDF](https://arxiv.org/pdf/2601.03124.pdf)  
**作者**：B. M. Shahria Alam, Md. Nasim Ahmed  

**一句话要点**：提出LeafLife框架，结合可解释性与鲁棒性，用于葡萄叶病害识别。

**关键词**：葡萄叶病害识别, 可解释深度学习, 对抗训练, Grad-CAM, 预训练模型, 农业应用

## 3 点简述
- 核心问题：葡萄叶病害影响作物产量，需高效准确识别以支持农业管理。
- 方法要点：采用预训练模型Xception和InceptionV3，集成对抗训练和Grad-CAM增强鲁棒性与可解释性。
- 实验或效果：Xception模型在测试集上达到96.23%准确率，并部署Web应用提供热图可视化与置信度预测。

## 摘要（原文）

> Plant disease diagnosis is essential to farmers' management choices because plant diseases frequently lower crop yield and product quality. For harvests to flourish and agricultural productivity to boost, grape leaf disease detection is important. The plant disease dataset contains grape leaf diseases total of 9,032 images of four classes, among them three classes are leaf diseases, and the other one is healthy leaves. After rigorous pre-processing dataset was split (70% training, 20% validation, 10% testing), and two pre-trained models were deployed: InceptionV3 and Xception. Xception shows a promising result of 96.23% accuracy, which is remarkable than InceptionV3. Adversarial Training is used for robustness, along with more transparency. Grad-CAM is integrated to confirm the leaf disease. Finally deployed a web application using Streamlit with a heatmap visualization and prediction with confidence level for robust grape leaf disease classification.

