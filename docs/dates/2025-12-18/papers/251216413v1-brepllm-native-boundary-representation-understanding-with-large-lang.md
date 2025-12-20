---
layout: default
title: BrepLLM: Native Boundary Representation Understanding with Large Language Models
---

# BrepLLM: Native Boundary Representation Understanding with Large Language Models
**arXiv**：[2512.16413v1](https://arxiv.org/abs/2512.16413) · [PDF](https://arxiv.org/pdf/2512.16413.pdf)  
**作者**：Liyuan Deng, Hao Guo, Yunpeng Bai, Yongkang Dai, Huaxi Huang, Yilei Shi  

**一句话要点**：提出BrepLLM框架，使大语言模型能直接解析三维边界表示数据，解决几何与语言模态不匹配问题。

**关键词**：三维边界表示理解, 跨模态对齐, 大语言模型微调, 几何拓扑编码, 自适应UV采样, 混合查询专家

## 3 点简述
- 核心问题：现有大语言模型基于文本序列，难以直接处理包含复杂几何拓扑信息的三维边界表示模型。
- 方法要点：采用两阶段训练，先通过自适应UV采样和分层编码器对齐几何与文本，再集成到大语言模型进行多阶段微调。
- 实验或效果：在三维物体分类和描述任务上达到最先进性能，并构建了包含26.9万对问答的数据集Brep2Text。

## 摘要（原文）

> Current token-sequence-based Large Language Models (LLMs) are not well-suited for directly processing 3D Boundary Representation (Brep) models that contain complex geometric and topological information. We propose BrepLLM, the first framework that enables LLMs to parse and reason over raw Brep data, bridging the modality gap between structured 3D geometry and natural language. BrepLLM employs a two-stage training pipeline: Cross-modal Alignment Pre-training and Multi-stage LLM Fine-tuning. In the first stage, an adaptive UV sampling strategy converts Breps into graphs representation with geometric and topological information. We then design a hierarchical BrepEncoder to extract features from geometry (i.e., faces and edges) and topology, producing both a single global token and a sequence of node tokens. Then we align the global token with text embeddings from a frozen CLIP text encoder (ViT-L/14) via contrastive learning. In the second stage, we integrate the pretrained BrepEncoder into an LLM. We then align its sequence of node tokens using a three-stage progressive training strategy: (1) training an MLP-based semantic mapping from Brep representation to 2D with 2D-LLM priors. (2) performing fine-tuning of the LLM. (3) designing a Mixture-of-Query Experts (MQE) to enhance geometric diversity modeling. We also construct Brep2Text, a dataset comprising 269,444 Brep-text question-answer pairs. Experiments show that BrepLLM achieves state-of-the-art (SOTA) results on 3D object classification and captioning tasks.

