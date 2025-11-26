---
layout: default
title: Large Language Model Aided Birt-Hogg-Dube Syndrome Diagnosis with Multimodal Retrieval-Augmented Generation
---

# Large Language Model Aided Birt-Hogg-Dube Syndrome Diagnosis with Multimodal Retrieval-Augmented Generation
**arXiv**：[2511.19834v1](https://arxiv.org/abs/2511.19834) · [PDF](https://arxiv.org/pdf/2511.19834.pdf)  
**作者**：Haoqing Li, Jun Shi, Xianmeng Chen, Qiwei Jia, Rui Wang, Wei Wei, Hong An, Xiaowen Hu  

**一句话要点**：提出BHD-RAG框架以解决Birt-Hogg-Dube综合征诊断中的幻觉风险

**关键词**：多模态检索增强生成, Birt-Hogg-Dube综合征诊断, 计算机断层扫描, 余弦相似度检索, 多模态大语言模型, 罕见疾病诊断

## 3 点简述
- 核心问题：BHD诊断中临床样本少、类间差异低，且多模态大模型缺乏领域知识易产生幻觉。
- 方法要点：构建多模态病例库，基于余弦相似度检索相关图像-描述对，结合MLLM进行诊断。
- 实验或效果：在四种DCLDs数据集上验证，准确率高，生成描述与专家见解一致。

## 摘要（原文）

> Deep learning methods face dual challenges of limited clinical samples and low inter-class differentiation among Diffuse Cystic Lung Diseases (DCLDs) in advancing Birt-Hogg-Dube syndrome (BHD) diagnosis via Computed Tomography (CT) imaging. While Multimodal Large Language Models (MLLMs) demonstrate diagnostic potential fo such rare diseases, the absence of domain-specific knowledge and referable radiological features intensify hallucination risks. To address this problem, we propose BHD-RAG, a multimodal retrieval-augmented generation framework that integrates DCLD-specific expertise and clinical precedents with MLLMs to improve BHD diagnostic accuracy. BHDRAG employs: (1) a specialized agent generating imaging manifestation descriptions of CT images to construct a multimodal corpus of DCLDs cases. (2) a cosine similarity-based retriever pinpointing relevant imagedescription pairs for query images, and (3) an MLLM synthesizing retrieved evidence with imaging data for diagnosis. BHD-RAG is validated on the dataset involving four types of DCLDs, achieving superior accuracy and generating evidence-based descriptions closely aligned with expert insights.

