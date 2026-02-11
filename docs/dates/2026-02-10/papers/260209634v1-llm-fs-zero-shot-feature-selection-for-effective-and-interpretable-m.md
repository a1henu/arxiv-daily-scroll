---
layout: default
title: LLM-FS: Zero-Shot Feature Selection for Effective and Interpretable Malware Detection
---

# LLM-FS: Zero-Shot Feature Selection for Effective and Interpretable Malware Detection
**arXiv**：[2602.09634v1](https://arxiv.org/abs/2602.09634) · [PDF](https://arxiv.org/pdf/2602.09634.pdf)  
**作者**：Naveen Gill, Ajvad Haneef K, Madhu Kumar S D  

**一句话要点**：提出零样本LLM特征选择方法，用于高效可解释的恶意软件检测

**关键词**：特征选择, 恶意软件检测, 零样本学习, 大语言模型, 可解释性

## 3 点简述
- 传统特征选择方法依赖统计启发式，忽略特征语义上下文。
- 研究利用LLM基于特征名和任务描述进行零样本特征选择。
- 在恶意软件数据集上评估，LLM方法性能与传统方法相当，提升可解释性和稳定性。

## 摘要（原文）

> Feature selection (FS) remains essential for building accurate and interpretable detection models, particularly in high-dimensional malware datasets. Conventional FS methods such as Extra Trees, Variance Threshold, Tree-based models, Chi-Squared tests, ANOVA, Random Selection, and Sequential Attention rely primarily on statistical heuristics or model-driven importance scores, often overlooking the semantic context of features. Motivated by recent progress in LLM-driven FS, we investigate whether large language models (LLMs) can guide feature selection in a zero-shot setting, using only feature names and task descriptions, as a viable alternative to traditional approaches. We evaluate multiple LLMs (GPT-5.0, GPT-4.0, Gemini-2.5 etc.) on the EMBOD dataset (a fusion of EMBER and BODMAS benchmark datasets), comparing them against established FS methods across several classifiers, including Random Forest, Extra Trees, MLP, and KNN. Performance is assessed using accuracy, precision, recall, F1, AUC, MCC, and runtime. Our results demonstrate that LLM-guided zero-shot feature selection achieves competitive performance with traditional FS methods while offering additional advantages in interpretability, stability, and reduced dependence on labeled data. These findings position zero-shot LLM-based FS as a promising alternative strategy for effective and interpretable malware detection, paving the way for knowledge-guided feature selection in security-critical applications

