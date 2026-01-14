---
layout: default
title: An Under-Explored Application for Explainable Multimodal Misogyny Detection in code-mixed Hindi-English
---

# An Under-Explored Application for Explainable Multimodal Misogyny Detection in code-mixed Hindi-English
**arXiv**：[2601.08457v1](https://arxiv.org/abs/2601.08457) · [PDF](https://arxiv.org/pdf/2601.08457.pdf)  
**作者**：Sargam Yadav, Abhishek Kaushik, Kevin Mc Daid  

**一句话要点**：提出可解释多模态系统以检测印英混合语中的厌女内容，应用于网络平台安全。

**关键词**：可解释人工智能, 多模态检测, 混合语言处理, Transformer模型, 网络内容安全

## 3 点简述
- 核心问题：低资源混合语中厌女内容检测缺乏可解释性，影响模型透明度和应用可靠性。
- 方法要点：结合XLM-R、mBERT等Transformer模型处理文本和图像，集成SHAP和LIME提供特征重要性解释。
- 实验或效果：在约4193条评论和4218个表情包数据集上训练，通过CUQ和UEQ问卷评估用户体验和可用性。

## 摘要（原文）

> Digital platforms have an ever-expanding user base, and act as a hub for communication, business, and connectivity. However, this has also allowed for the spread of hate speech and misogyny. Artificial intelligence models have emerged as an effective solution for countering online hate speech but are under explored for low resource and code-mixed languages and suffer from a lack of interpretability. Explainable Artificial Intelligence (XAI) can enhance transparency in the decisions of deep learning models, which is crucial for a sensitive domain such as hate speech detection. In this paper, we present a multi-modal and explainable web application for detecting misogyny in text and memes in code-mixed Hindi and English. The system leverages state-of-the-art transformer-based models that support multilingual and multimodal settings. For text-based misogyny identification, the system utilizes XLM-RoBERTa (XLM-R) and multilingual Bidirectional Encoder Representations from Transformers (mBERT) on a dataset of approximately 4,193 comments. For multimodal misogyny identification from memes, the system utilizes mBERT + EfficientNet, and mBERT + ResNET trained on a dataset of approximately 4,218 memes. It also provides feature importance scores using explainability techniques including Shapley Additive Values (SHAP) and Local Interpretable Model Agnostic Explanations (LIME). The application aims to serve as a tool for both researchers and content moderators, to promote further research in the field, combat gender based digital violence, and ensure a safe digital space. The system has been evaluated using human evaluators who provided their responses on Chatbot Usability Questionnaire (CUQ) and User Experience Questionnaire (UEQ) to determine overall usability.

