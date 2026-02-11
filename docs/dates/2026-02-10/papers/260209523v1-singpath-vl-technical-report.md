---
layout: default
title: Singpath-VL Technical Report
---

# Singpath-VL Technical Report
**arXiv**：[2602.09523v1](https://arxiv.org/abs/2602.09523) · [PDF](https://arxiv.org/pdf/2602.09523.pdf)  
**作者**：Zhen Qiu, Kaiwen Xiao, Zhengwei Lu, Xiangyu Liu, Lei Zhao, Hao Zhang  

**一句话要点**：提出Singpath-VL以解决宫颈细胞学中AI助手缺失问题，通过合成数据集和微调模型实现细胞形态感知与诊断分类。

**关键词**：宫颈细胞学, 多模态大语言模型, 合成数据集, 细胞形态感知, 诊断分类, 开源基准

## 3 点简述
- 核心问题：宫颈细胞学领域缺乏大规模高质量标注数据集，限制了多模态大语言模型的应用。
- 方法要点：开发三阶段流程合成百万级图像-描述数据集，利用通用MLLMs作为弱标注器，结合共识融合和专家知识注入。
- 实验或效果：基于Qwen3-VL-4B模型微调，Singpath-VL在细粒度形态感知和细胞级诊断分类中表现优异，计划开源部分数据集和基准。

## 摘要（原文）

> We present Singpath-VL, a vision-language large model, to fill the vacancy of AI assistant in cervical cytology. Recent advances in multi-modal large language models (MLLMs) have significantly propelled the field of computational pathology. However, their application in cytopathology, particularly cervical cytology, remains underexplored, primarily due to the scarcity of large-scale, high-quality annotated datasets. To bridge this gap, we first develop a novel three-stage pipeline to synthesize a million-scale image-description dataset. The pipeline leverages multiple general-purpose MLLMs as weak annotators, refines their outputs through consensus fusion and expert knowledge injection, and produces high-fidelity descriptions of cell morphology. Using this dataset, we then fine-tune the Qwen3-VL-4B model via a multi-stage strategy to create a specialized cytopathology MLLM. The resulting model, named Singpath-VL, demonstrates superior performance in fine-grained morphological perception and cell-level diagnostic classification. To advance the field, we will open-source a portion of the synthetic dataset and benchmark.

