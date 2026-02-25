---
layout: default
title: Are Multimodal Large Language Models Good Annotators for Image Tagging?
---

# Are Multimodal Large Language Models Good Annotators for Image Tagging?
**arXiv**：[2602.20972v1](https://arxiv.org/abs/2602.20972) · [PDF](https://arxiv.org/pdf/2602.20972.pdf)  
**作者**：Ming-Kun Xie, Jia-Hao Xiao, Zhiqiang Kou, Zhongnian Li, Gang Niu, Masashi Sugiyama  

**一句话要点**：提出TagLLM框架以缩小多模态大语言模型与人类标注在图像标注任务中的差距

**关键词**：图像标注, 多模态大语言模型, 自动化标注, 标签消歧, 结构化提示

## 3 点简述
- 分析多模态大语言模型在图像标注中与人类标注的差距，发现其成本极低但质量约为50%至80%
- 提出TagLLM框架，包含候选生成和标签消歧组件，通过结构化提示和交互校准提升标注质量
- 实验显示TagLLM显著缩小差距，在下游训练性能上弥补约60%至80%的差异

## 摘要（原文）

> Image tagging, a fundamental vision task, traditionally relies on human-annotated datasets to train multi-label classifiers, which incurs significant labor and costs. While Multimodal Large Language Models (MLLMs) offer promising potential to automate annotation, their capability to replace human annotators remains underexplored. This paper aims to analyze the gap between MLLM-generated and human annotations and to propose an effective solution that enables MLLM-based annotation to replace manual labeling. Our analysis of MLLM annotations reveals that, under a conservative estimate, MLLMs can reduce annotation cost to as low as one-thousandth of the human cost, mainly accounting for GPU usage, which is nearly negligible compared to manual efforts. Their annotation quality reaches about 50\% to 80\% of human performance, while achieving over 90\% performance on downstream training tasks.Motivated by these findings, we propose TagLLM, a novel framework for image tagging, which aims to narrow the gap between MLLM-generated and human annotations. TagLLM comprises two components: Candidates generation, which employs structured group-wise prompting to efficiently produce a compact candidate set that covers as many true labels as possible while reducing subsequent annotation workload; and label disambiguation, which interactively calibrates the semantic concept of categories in the prompts and effectively refines the candidate labels. Extensive experiments show that TagLLM substantially narrows the gap between MLLM-generated and human annotations, especially in downstream training performance, where it closes about 60\% to 80\% of the difference.

