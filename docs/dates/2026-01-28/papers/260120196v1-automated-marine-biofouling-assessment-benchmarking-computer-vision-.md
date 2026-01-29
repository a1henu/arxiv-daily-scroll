---
layout: default
title: Automated Marine Biofouling Assessment: Benchmarking Computer Vision and Multimodal LLMs on the Level of Fouling Scale
---

# Automated Marine Biofouling Assessment: Benchmarking Computer Vision and Multimodal LLMs on the Level of Fouling Scale
**arXiv**：[2601.20196v1](https://arxiv.org/abs/2601.20196) · [PDF](https://arxiv.org/pdf/2601.20196.pdf)  
**作者**：Brayden Hamilton, Tim Cashmore, Peter Driscoll, Trevor Gee, Henry Williams  

**一句话要点**：提出基于计算机视觉和多模态大语言模型的自动化海洋生物污损评估方法，以解决传统潜水检查的局限。

**关键词**：海洋生物污损评估, 计算机视觉分类, 多模态大语言模型, 零样本学习, 船舶船体检查, 自动化监测

## 3 点简述
- 核心问题：船舶船体海洋生物污损带来生态、经济和生物安全风险，传统潜水检查危险且可扩展性差。
- 方法要点：结合卷积神经网络、基于Transformer的分割模型和零样本多模态大语言模型，用于污损严重程度分类。
- 实验或效果：在专家标注数据集上评估，计算机视觉模型在极端类别准确率高，多模态大语言模型无需训练即达到竞争性性能并提供可解释输出。

## 摘要（原文）

> Marine biofouling on vessel hulls poses major ecological, economic, and biosecurity risks. Traditional survey methods rely on diver inspections, which are hazardous and limited in scalability. This work investigates automated classification of biofouling severity on the Level of Fouling (LoF) scale using both custom computer vision models and large multimodal language models (LLMs). Convolutional neural networks, transformer-based segmentation, and zero-shot LLMs were evaluated on an expert-labelled dataset from the New Zealand Ministry for Primary Industries. Computer vision models showed high accuracy at extreme LoF categories but struggled with intermediate levels due to dataset imbalance and image framing. LLMs, guided by structured prompts and retrieval, achieved competitive performance without training and provided interpretable outputs. The results demonstrate complementary strengths across approaches and suggest that hybrid methods integrating segmentation coverage with LLM reasoning offer a promising pathway toward scalable and interpretable biofouling assessment.

