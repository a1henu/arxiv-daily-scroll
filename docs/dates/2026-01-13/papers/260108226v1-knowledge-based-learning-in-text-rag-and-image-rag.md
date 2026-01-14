---
layout: default
title: Knowledge-based learning in Text-RAG and Image-RAG
---

# Knowledge-based learning in Text-RAG and Image-RAG
**arXiv**：[2601.08226v1](https://arxiv.org/abs/2601.08226) · [PDF](https://arxiv.org/pdf/2601.08226.pdf)  
**作者**：Alexander Shim, Khalil Saieh, Samuel Clarke  

**一句话要点**：分析基于Vision Transformer和LLM的多模态RAG方法，以减少幻觉问题并检测胸部X光图像疾病。

**关键词**：多模态检索增强生成, 胸部X光图像分析, 幻觉问题减少, Vision Transformer, 大型语言模型, 预测校准

## 3 点简述
- 核心问题：针对胸部X光图像疾病检测中的幻觉问题，研究多模态检索增强生成方法。
- 方法要点：结合EVA-ViT图像编码器与LLM，比较文本RAG和图像RAG，使用KNN提升预测置信度。
- 实验或效果：文本RAG有效减少幻觉，图像RAG改善校准，GPT LLM性能优于Llama，但面临数据不平衡挑战。

## 摘要（原文）

> This research analyzed and compared the multi-modal approach in the Vision Transformer(EVA-ViT) based image encoder with the LlaMA or ChatGPT LLM to reduce the hallucination problem and detect diseases in chest x-ray images. In this research, we utilized the NIH Chest X-ray image to train the model and compared it in image-based RAG, text-based RAG, and baseline. [3] [5] In a result, the text-based RAG[2] e!ectively reduces the hallucination problem by using external knowledge information, and the image-based RAG improved the prediction con"dence and calibration by using the KNN methods. [4] Moreover, the GPT LLM showed better performance, a low hallucination rate, and better Expected Calibration Error(ECE) than Llama Llama-based model. This research shows the challenge of data imbalance, a complex multi-stage structure, but suggests a large experience environment and a balanced example of use.

